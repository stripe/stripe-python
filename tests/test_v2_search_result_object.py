import pytest

from stripe.v2 import SearchResultObject


class TestSearchResult(SearchResultObject):
    requests = []
    pages = []

    def _request(self, method, url, params=None, **kwargs):
        self.requests.append((method, url, params, kwargs))
        return self.pages.pop(0)

    async def _request_async(self, method, url, params=None, **kwargs):
        return self._request(method, url, params=params, **kwargs)


def make_result(data, next_page_url):
    result = TestSearchResult._construct_from(
        values={
            "object": "v2.search_result",
            "data": data,
            "next_page_url": next_page_url,
            "previous_page_url": None,
            "total_count": 2,
        },
        last_response=None,
        requestor=None,
        api_mode="V2",
    )
    return result


def test_auto_paging_replays_original_post_body():
    params = {
        "query": 'status:"active"',
        "sort": ["name", "-created"],
        "limit": 2,
        "future_field": {"enabled": True},
    }
    first = make_result(["one"], "/v2/widgets/search?page=2")
    first._retrieve_params = params
    TestSearchResult.requests = []
    TestSearchResult.pages = [
        make_result([], "/v2/widgets/search?page=3"),
        make_result(["two"], None),
    ]

    assert list(first.auto_paging_iter()) == ["one", "two"]
    assert [
        (method, url, body) for method, url, body, _ in TestSearchResult.requests
    ] == [
        ("post", "/v2/widgets/search?page=2", params),
        ("post", "/v2/widgets/search?page=3", params),
    ]


@pytest.mark.asyncio
async def test_async_auto_paging_replays_original_post_body():
    first = make_result(["one"], "/v2/widgets/search?page=2")
    first._retrieve_params = {"query": "widgets"}
    TestSearchResult.requests = []
    TestSearchResult.pages = [make_result(["two"], None)]

    results = [item async for item in first.auto_paging_iter()]
    assert results == ["one", "two"]
    assert TestSearchResult.requests[0][:3] == (
        "post",
        "/v2/widgets/search?page=2",
        {"query": "widgets"},
    )
