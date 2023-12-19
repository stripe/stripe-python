import stripe


class TestDeletableAPIResource(object):
    class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
        OBJECT_NAME = "mydeletable"

    def test_delete_class(self, http_client_mock):
        http_client_mock.stub_request(
            "delete",
            path="/v1/mydeletables/mid",
            rbody='{"id": "mid", "deleted": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.delete("mid")

        http_client_mock.assert_requested(
            "delete", path="/v1/mydeletables/mid", query_string=""
        )
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_class_with_object(self, http_client_mock):
        http_client_mock.stub_request(
            "delete",
            path="/v1/mydeletables/mid",
            rbody='{"id": "mid", "deleted": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        self.MyDeletable.delete(obj)

        http_client_mock.assert_requested(
            "delete", path="/v1/mydeletables/mid", query_string=""
        )
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_instance(self, http_client_mock):
        http_client_mock.stub_request(
            "delete",
            path="/v1/mydeletables/mid",
            rbody='{"id": "mid", "deleted": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        assert obj is obj.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/mydeletables/mid", query_string=""
        )
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_with_all_special_fields(self, http_client_mock):
        http_client_mock.stub_request(
            "delete",
            path="/v1/mydeletables/foo",
            query_string="bobble=new_scrobble",
            rbody='{"id": "foo", "bobble": "new_scrobble"}',
            rheaders={"Idempotency-Key": "IdempotencyKey"},
        )

        self.MyDeletable.delete(
            "foo",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
            bobble="new_scrobble",
        )

        http_client_mock.assert_requested(
            "delete",
            path="/v1/mydeletables/foo",
            query_string="bobble=new_scrobble",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
        )
