from __future__ import absolute_import, division, print_function

import stripe


class TestDeletableAPIResource(object):
    class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
        OBJECT_NAME = "mydeletable"

    def test_delete_class(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.delete("mid")

        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_class_with_object(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        self.MyDeletable.delete(obj)

        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_instance(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        assert obj is obj.delete()
        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    def test_delete_with_all_special_fields(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/foo",
            {"id": "foo", "bobble": "new_scrobble"},
            {"Idempotency-Key": "IdempotencyKey"},
        )

        self.MyDeletable.delete(
            "foo",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
            bobble="new_scrobble",
        )

        request_mock.assert_requested(
            "delete",
            "/v1/mydeletables/foo",
            {"bobble": "new_scrobble"},
            {"Idempotency-Key": "IdempotencyKey"},
        )
        request_mock.assert_api_version("2017-08-15")
