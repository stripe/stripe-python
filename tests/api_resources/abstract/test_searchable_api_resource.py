from __future__ import absolute_import, division, print_function

import stripe


class TestSearchableAPIResource(object):
    class MySearchable(stripe.api_resources.abstract.SearchableAPIResource):
        OBJECT_NAME = "mysearchable"

        @classmethod
        def search(cls, *args, **kwargs):
            return cls._search(
                search_url="/v1/mysearchables/search", *args, **kwargs
            )

    def test_search(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/mysearchables/search",
            {
                "object": "search_result",
                "data": [
                    {"object": "charge", "name": "jose"},
                    {"object": "charge", "name": "curly"},
                ],
                "url": "/v1/charges",
                "has_more": False,
                "next_page": None,
            },
            rheaders={"request-id": "req_id"},
        )

        res = self.MySearchable.search(query='currency:"CAD"')
        request_mock.assert_requested("get", "/v1/mysearchables/search", {})
        assert len(res.data) == 2
        assert all(isinstance(obj, stripe.Charge) for obj in res.data)
        assert res.data[0].name == "jose"
        assert res.data[1].name == "curly"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    def test_search_multiple_pages(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/mysearchables/search",
            {
                "object": "search_result",
                "data": [
                    {"object": "charge", "name": "jose"},
                    {"object": "charge", "name": "curly"},
                ],
                "url": "/v1/charges",
                "has_more": True,
                "next_page": "next-page-token",
            },
            rheaders={"request-id": "req_id"},
        )

        res = self.MySearchable.search(query='currency:"CAD"')
        request_mock.assert_requested(
            "get", "/v1/mysearchables/search", {"query": 'currency:"CAD"'}
        )

        assert res.next_page == "next-page-token"

        request_mock.stub_request(
            "get",
            "/v1/mysearchables/search",
            {
                "object": "list",
                "data": [
                    {"object": "charge", "name": "test"},
                ],
                "url": "/v1/charges",
                "has_more": False,
                "next_page": None,
            },
            rheaders={"request-id": "req_id"},
        )
        res2 = self.MySearchable.search(
            query='currency:"CAD"', page=res.next_page
        )
        request_mock.assert_requested(
            "get",
            "/v1/mysearchables/search",
            {"page": "next-page-token", "query": 'currency:"CAD"'},
        )

        assert len(res2.data) == 1
        assert all(isinstance(obj, stripe.Charge) for obj in res2.data)
        assert res2.data[0].name == "test"
