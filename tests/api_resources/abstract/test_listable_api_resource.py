import stripe


class TestListableAPIResource(object):
    class MyListable(stripe.api_resources.abstract.ListableAPIResource):
        OBJECT_NAME = "mylistable"

    def test_all(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/mylistables",
            rbody='{"object": "list", "data": [{"object": "charge", "name": "jose"}, {"object": "charge", "name": "curly"}], "url": "/v1/charges", "has_more": false}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MyListable.list()
        http_client_mock.assert_requested(
            "get", path="/v1/mylistables", query_string=""
        )
        assert len(res.data) == 2
        assert all(isinstance(obj, stripe.Charge) for obj in res.data)
        assert res.data[0].name == "jose"
        assert res.data[1].name == "curly"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"
