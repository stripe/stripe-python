import pytest
from unittest.mock import AsyncMock, Mock

from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService

from stripe.v2._search_result_object import SearchResultObject


@pytest.mark.parametrize(
    "url,params,expected_url,body",
    [
        (
            "/v2/widgets/search",
            {"limit": 2, "query": "widgets"},
            "/v2/widgets/search?limit=2",
            {"query": "widgets"},
        ),
        (
            "/v2/widgets/search?page=2&limit=2",
            {"limit": 9, "query": "widgets"},
            "/v2/widgets/search?page=2&limit=2",
            {"query": "widgets"},
        ),
        (
            "/v2/widgets/search?page=2",
            {"limit": 9, "query": "widgets"},
            "/v2/widgets/search?page=2",
            {"query": "widgets"},
        ),
        (
            "/v2/widgets/search",
            {"query": "widgets"},
            "/v2/widgets/search",
            {"query": "widgets"},
        ),
        ("/v2/widgets/search", None, "/v2/widgets/search", None),
    ],
)
@pytest.mark.anyio
async def test_search_helper_delegates_once(url, params, expected_url, body):
    service = StripeService(Mock())
    options = {"stripe_account": "acct_123"}
    encodings = {"count": "int64_string"}
    original = dict(params) if params is not None else None
    service._request = Mock()
    service._request_async = AsyncMock()
    service._request_v2_search(
        "post",
        url,
        params,
        options,
        base_address="api",
        _param_encodings=encodings,
    )
    service._request.assert_called_once_with(
        "post",
        expected_url,
        body,
        options,
        base_address="api",
        _param_encodings=encodings,
    )
    await service._request_v2_search_async(
        "post",
        url,
        params,
        options,
        base_address="api",
        _param_encodings=encodings,
    )
    service._request_async.assert_awaited_once_with(
        "post",
        expected_url,
        body,
        options,
        base_address="api",
        _param_encodings=encodings,
    )
    assert params == original


@pytest.mark.anyio
async def test_ordinary_custom_search_keeps_limit_in_body():
    requestor = Mock()
    requestor.request_async = AsyncMock()
    service = StripeService(requestor)
    params = {"limit": 2, "query": "widgets"}
    options = {"stripe_account": "acct_123"}
    url = "/v2/data/operations/search"
    service._request("post", url, params, options, base_address="api")
    requestor.request.assert_called_once_with(
        "post",
        url,
        params,
        options,
        base_address="api",
        usage=["stripe_client"],
    )
    await service._request_async(
        "post", url, params, options, base_address="api"
    )
    requestor.request_async.assert_awaited_once_with(
        "post",
        url,
        params,
        options,
        base_address="api",
        usage=["stripe_client"],
    )
    assert params == {"limit": 2, "query": "widgets"}


@pytest.mark.anyio
async def test_search_helper_preserves_encoding_options_and_usage(mocker):
    coerce = mocker.patch(
        "stripe._stripe_service._coerce_v2_params", wraps=_coerce_v2_params
    )
    requestor = Mock()
    requestor.request_async = AsyncMock()
    service = StripeService(requestor)
    params = {"limit": 2, "count": 123}
    options = {"stripe_account": "acct_123"}
    encodings = {"count": "int64_string"}
    service._request_v2_search(
        "post",
        "/v2/widgets/search",
        params,
        options,
        base_address="meter_events",
        _param_encodings=encodings,
    )
    coerce.assert_called_once_with({"count": 123}, encodings)
    requestor.request.assert_called_once_with(
        "post",
        "/v2/widgets/search?limit=2",
        {"count": "123"},
        options,
        base_address="meter_events",
        usage=["stripe_client"],
    )
    coerce.reset_mock()
    await service._request_v2_search_async(
        "post",
        "/v2/widgets/search",
        params,
        options,
        base_address="meter_events",
        _param_encodings=encodings,
    )
    coerce.assert_called_once_with({"count": 123}, encodings)
    requestor.request_async.assert_awaited_once_with(
        "post",
        "/v2/widgets/search?limit=2",
        {"count": "123"},
        options,
        base_address="meter_events",
        usage=["stripe_client"],
    )
    assert params == {"limit": 2, "count": 123}


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
    first = make_result(["one"], "/v2/widgets/search?page=2&limit=2")
    first._retrieve_params = params
    TestSearchResult.requests = []
    TestSearchResult.pages = [
        make_result([], "/v2/widgets/search?page=3&limit=2"),
        make_result(["two"], None),
    ]

    assert list(first.auto_paging_iter()) == ["one", "two"]
    assert [
        (method, url, body)
        for method, url, body, _ in TestSearchResult.requests
    ] == [
        (
            "post",
            "/v2/widgets/search?page=2&limit=2",
            {
                "query": 'status:"active"',
                "sort": ["name", "-created"],
                "future_field": {"enabled": True},
            },
        ),
        (
            "post",
            "/v2/widgets/search?page=3&limit=2",
            {
                "query": 'status:"active"',
                "sort": ["name", "-created"],
                "future_field": {"enabled": True},
            },
        ),
    ]


@pytest.mark.anyio
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
