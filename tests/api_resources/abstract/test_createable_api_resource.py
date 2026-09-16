from stripe._createable_api_resource import CreateableAPIResource
from stripe._charge import Charge


class TestCreateableAPIResource(object):
    class MyCreatable(CreateableAPIResource):
        OBJECT_NAME = "mycreatable"

    def test_create(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/mycreatables",
            rbody='{"object": "charge", "foo": "bar"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MyCreatable.create()

        http_client_mock.assert_requested(
            "post", path="/v1/mycreatables", post_data=""
        )
        assert isinstance(res, Charge)
        assert res.foo == "bar"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    def test_idempotent_create(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/mycreatables",
            rbody='{"object": "charge", "foo": "bar"}',
            rheaders={"idempotency-key": "foo"},
        )

        res = self.MyCreatable.create(idempotency_key="foo")

        http_client_mock.assert_requested(
            "post",
            path="/v1/mycreatables",
            post_data="",
            idempotency_key="foo",
        )
        assert isinstance(res, Charge)
        assert res.foo == "bar"
