import pytest
import json

import stripe


class TestUpdateableAPIResource(object):
    class MyUpdateable(stripe.api_resources.abstract.UpdateableAPIResource):
        OBJECT_NAME = "myupdateable"

    @pytest.fixture
    def obj(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/myupdateables/myid",
            rbody=json.dumps({"id": "myid", "thats": "it"}),
            rheaders={"request-id": "req_id"},
        )

        return self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "foo": "bar",
                "baz": "boz",
                "metadata": {"size": "l", "score": 4, "height": 10},
                "object": "obj",
            },
            "mykey",
        )

    def checkSave(self, obj):
        assert obj is obj.save()

        assert obj.thats == "it"
        # TODO: Should we force id to be retained?
        # assert obj.id == 'myid'
        with pytest.raises(AttributeError):
            obj.baz

    def test_idempotent_save(self, http_client_mock, obj):
        obj.baz = "updated"
        obj.save(idempotency_key="foo")

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="baz=updated",
            idempotency_key="foo",
        )

    def test_save(self, http_client_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata.size = "m"
        obj.metadata.info = "a2"
        obj.metadata.height = None

        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="baz=updated&metadata[info]=a2&metadata[size]=m&other=newval",
        )

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

        # Saving again should not cause any request.
        http_client_mock.reset_mock()
        self.checkSave(obj)
        http_client_mock.assert_no_request()

        # Setting the same value should cause a request.
        http_client_mock.reset_mock()
        http_client_mock.stub_request(
            "post",
            path="/v1/myupdateables/myid",
            rbody=json.dumps({"id": "myid", "thats": "it"}),
        )

        obj.thats = "it"
        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post", path="/v1/myupdateables/myid", post_data="thats=it"
        )

        # Changing the value should cause a request.
        http_client_mock.reset_mock()
        http_client_mock.stub_request(
            "post",
            path="/v1/myupdateables/myid",
            rbody=json.dumps({"id": "myid", "thats": "it"}),
        )

        obj.id = "myid"
        obj.thats = "updated"
        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post", path="/v1/myupdateables/myid", post_data="thats=updated"
        )

    def test_add_key_to_nested_object(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"size": "l", "score": 4, "height": 10},
            },
            "mykey",
        )

        acct.legal_entity["first_name"] = "bob"

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="legal_entity[first_name]=bob",
        )

    def test_save_nothing(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "metadata": {"key": "value"}}, "mykey"
        )

        assert acct is acct.save()

        http_client_mock.assert_no_request()

    def test_replace_nested_object(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"last_name": "smith"}}, "mykey"
        )

        acct.legal_entity = {"first_name": "bob"}

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="legal_entity[first_name]=bob&legal_entity[last_name]=",
        )

    def test_array_setting(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {}}, "mykey"
        )

        acct.legal_entity.additional_owners = [{"first_name": "Bob"}]

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="legal_entity[additional_owners][0][first_name]=Bob",
        )

    def test_array_none(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": None}},
            "mykey",
        )

        acct.foo = "bar"

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post", path="/v1/myupdateables/myid", post_data="foo=bar"
        )

    def test_array_insertion(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": []}}, "mykey"
        )

        acct.legal_entity.additional_owners.append({"first_name": "Bob"})

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="legal_entity[additional_owners][0][first_name]=Bob",
        )

    def test_array_update(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {
                    "additional_owners": [
                        {"first_name": "Bob"},
                        {"first_name": "Jane"},
                    ]
                },
            },
            "mykey",
        )

        acct.legal_entity.additional_owners[1].first_name = "Janet"

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="legal_entity[additional_owners][1][first_name]=Janet",
        )

    def test_array_noop(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"additional_owners": [{"first_name": "Bob"}]},
                "currencies_supported": ["usd", "cad"],
            },
            "mykey",
        )

        assert acct is acct.save()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="",
        )

    def test_hash_noop(self, http_client_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"address": {"line1": "1 Two Three"}},
            },
            "mykey",
        )

        assert acct is acct.save()

        http_client_mock.assert_no_request()

    def test_save_replace_metadata_with_number(self, http_client_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata = 3

        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="baz=updated&metadata=3&other=newval",
        )

    def test_save_overwrite_metadata(self, http_client_mock, obj):
        obj.metadata = {}
        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="metadata[size]=&metadata[score]=&metadata[height]=",
        )

    def test_save_replace_metadata(self, http_client_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata = {"size": "m", "info": "a2", "score": 4}

        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="baz=updated&metadata[info]=a2&metadata[size]=m&metadata[score]=4&other=newval",
        )

    def test_save_update_metadata(self, http_client_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata.update({"size": "m", "info": "a2", "score": 4})

        self.checkSave(obj)

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/myid",
            post_data="baz=updated&metadata[info]=a2&metadata[size]=m&metadata[score]=4&other=newval",
        )

    def test_retrieve_and_update_with_stripe_version(
        self, http_client_mock, obj
    ):
        http_client_mock.stub_request(
            "get",
            path="/v1/myupdateables/foo",
            rbody=json.dumps({"id": "foo", "bobble": "scrobble"}),
        )

        res = self.MyUpdateable.retrieve("foo", stripe_version="2017-08-15")

        http_client_mock.assert_requested(stripe_version="2017-08-15")

        http_client_mock.stub_request(
            "post",
            path="/v1/myupdateables/foo",
            rbody=json.dumps({"id": "foo", "bobble": "new_scrobble"}),
        )

        res.bobble = "new_scrobble"
        res.save()

        http_client_mock.assert_requested(stripe_version="2017-08-15")

    def test_modify_with_all_special_fields(self, http_client_mock, obj):
        http_client_mock.stub_request(
            "post",
            path="/v1/myupdateables/foo",
            rbody=json.dumps({"id": "foo", "bobble": "new_scrobble"}),
            rheaders={"Idempotency-Key": "IdempotencyKey"},
        )

        self.MyUpdateable.modify(
            "foo",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
            bobble="new_scrobble",
            headers={"extra_header": "val"},
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/myupdateables/foo",
            post_data="bobble=new_scrobble",
            stripe_version="2017-08-15",
            idempotency_key="IdempotencyKey",
            extra_headers={"extra_header": "val"},
        )
