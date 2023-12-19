import stripe


class TestSingletonAPIResource(object):
    class MySingleton(stripe.api_resources.abstract.SingletonAPIResource):
        OBJECT_NAME = "mysingleton"

    def test_retrieve(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/mysingleton",
            rbody='{"single": "ton"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MySingleton.retrieve()

        http_client_mock.assert_requested("get", path="/v1/mysingleton")
        assert res.single == "ton"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"
