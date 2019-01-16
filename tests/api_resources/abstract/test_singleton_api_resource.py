from __future__ import absolute_import, division, print_function

import stripe


class TestSingletonAPIResource(object):
    class MySingleton(stripe.api_resources.abstract.SingletonAPIResource):
        OBJECT_NAME = "mysingleton"

    def test_retrieve(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/mysingleton",
            {"single": "ton"},
            rheaders={"request-id": "req_id"},
        )

        res = self.MySingleton.retrieve()

        request_mock.assert_requested("get", "/v1/mysingleton", {})
        assert res.single == "ton"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"
