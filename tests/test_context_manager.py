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
