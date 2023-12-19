import stripe


class TestSearchableAPIResource(object):
    class MySearchable(stripe.api_resources.abstract.SearchableAPIResource):
        OBJECT_NAME = "mysearchable"

        @classmethod
        def search(cls, *args, **kwargs):
            return cls._search(
                search_url="/v1/mysearchables/search", *args, **kwargs
            )

    def test_search(self, http_client_mock):
        path = "/v1/mysearchables/search"
        query_string = "query=currency%3A%22CAD%22"
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"object": "search_result", "data": [{"object": "charge", "name": "jose"}, {"object": "charge", "name": "curly"}], "url": "/v1/charges", "has_more": false, "next_page": null}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MySearchable.search(query='currency:"CAD"')
        http_client_mock.assert_requested(
            "get", path=path, query_string=query_string
        )
        assert len(res.data) == 2
        assert all(isinstance(obj, stripe.Charge) for obj in res.data)
        assert res.data[0].name == "jose"
        assert res.data[1].name == "curly"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    def test_search_multiple_pages(self, http_client_mock):
        path = "/v1/mysearchables/search"
        query_string = 'query=currency:"CAD"'
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"object": "search_result", "data": [{"object": "charge", "name": "jose"}, {"object": "charge", "name": "curly"}], "url": "/v1/charges", "has_more": true, "next_page": "next-page-token"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MySearchable.search(query='currency:"CAD"')
        http_client_mock.assert_requested(
            "get", path=path, query_string=query_string
        )

        assert res.next_page == "next-page-token"

        query_string = 'page=next-page-token&query=currency:"CAD"'
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"object": "search_result", "data": [{"object": "charge", "name": "test"}], "url": "/v1/charges", "has_more": false, "next_page": null}',
            rheaders={"request-id": "req_id"},
        )
        res2 = self.MySearchable.search(
            query='currency:"CAD"', page=res.next_page
        )
        http_client_mock.assert_requested(
            "get",
            path=path,
            query_string=query_string,
        )

        assert len(res2.data) == 1
        assert all(isinstance(obj, stripe.Charge) for obj in res2.data)
        assert res2.data[0].name == "test"
