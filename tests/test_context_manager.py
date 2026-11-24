import pytest
from stripe import StripeClient, RequestsClient, AIOHTTPClient, HTTPXClient


class TestContextManager:
    def test_stripe_client_sync_context_manager(self):
        client = StripeClient("sk_test_123")
        with client as c:
            assert c is client
        # Should close without raising any exceptions

    @pytest.mark.anyio
    async def test_stripe_client_async_context_manager(self):
        client = StripeClient("sk_test_123")
        async with client as c:
            assert c is client
        # Should close async without raising any exceptions

    def test_http_client_sync_context_manager(self):
        http_client = RequestsClient()
        with http_client as c:
            assert c is http_client

    @pytest.mark.anyio
    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    async def test_aiohttp_client_async_context_manager(self, anyio_backend):
        http_client = AIOHTTPClient()
        async with http_client as c:
            assert c is http_client

    @pytest.mark.anyio
    async def test_httpx_client_async_context_manager(self):
        http_client = HTTPXClient()
        async with http_client as c:
            assert c is http_client

    def test_with_stripe_context_does_not_close_parent_client(self, mocker):
        parent = StripeClient("sk_test_123")
        child = parent.with_stripe_context("ctx_test")
        assert child._owns_http_client is False
        assert parent._owns_http_client is True

        spy_close = mocker.spy(parent._requestor._client, "close")
        with child as c:
            assert c is child
        # Child closing should NOT close the parent HTTP client
        spy_close.assert_not_called()

        # But parent closing SHOULD close it
        parent.close()
        spy_close.assert_called_once()

    @pytest.mark.anyio
    async def test_with_stripe_context_async_does_not_close_parent_client(
        self, mocker
    ):
        parent = StripeClient("sk_test_123")
        child = parent.with_stripe_context("ctx_test")
        assert child._owns_http_client is False
        assert parent._owns_http_client is True

        spy_close_async = mocker.spy(parent._requestor._client, "close_async")
        async with child as c:
            assert c is child
        # Child async exit should NOT close the parent HTTP client
        spy_close_async.assert_not_called()

        # But parent async close SHOULD close it
        await parent.close_async()
        spy_close_async.assert_called_once()

    def test_custom_user_http_client_not_closed_by_stripe_client(self, mocker):
        custom_http = RequestsClient()
        client = StripeClient("sk_test_123", http_client=custom_http)
        assert client._owns_http_client is False
        spy_close = mocker.spy(custom_http, "close")
        with client:
            pass
        spy_close.assert_not_called()

        # User closes it explicitly
        custom_http.close()
        spy_close.assert_called_once()

    @pytest.mark.anyio
    async def test_aexit_closes_both_sync_and_async_pools(self, mocker):
        client = StripeClient("sk_test_123")
        http_client = client._requestor._client
        spy_sync_close = mocker.spy(http_client, "close")
        spy_async_close = mocker.spy(http_client, "close_async")

        async with client:
            pass

        spy_sync_close.assert_called()
        spy_async_close.assert_called()

    @pytest.mark.anyio
    async def test_httpx_client_dual_pool_cleanup(self, mocker):
        httpx_client = HTTPXClient(allow_sync_methods=True)
        assert httpx_client._client is not None
        spy_sync = mocker.spy(httpx_client._client, "close")
        spy_async = mocker.spy(httpx_client._client_async, "aclose")

        async with httpx_client:
            pass

        spy_sync.assert_called_once()
        spy_async.assert_called_once()
