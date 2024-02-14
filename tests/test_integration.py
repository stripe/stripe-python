import platform
from threading import Thread, Lock
import json
import warnings
import time

import httpx

import stripe
import pytest
from queue import Queue
from collections import defaultdict
from typing import List, Dict, Tuple, Optional

if platform.python_implementation() == "PyPy":
    pytest.skip("skip integration tests with PyPy", allow_module_level=True)

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyTestHandler(BaseHTTPRequestHandler):
    num_requests = 0

    requests = defaultdict(Queue)

    @classmethod
    def _add_request(cls, req):
        q = cls.requests[id(cls)]
        q.put(req)

    @classmethod
    def get_requests(cls, n) -> List[BaseHTTPRequestHandler]:
        reqs = []
        for _ in range(n):
            reqs.append(cls.requests[id(cls)].get(False))

        assert cls.requests[id(cls)].empty()
        return reqs

    def do_GET(self):
        return self._do_request()

    def do_POST(self):
        return self._do_request()

    def _do_request(self):
        n = self.__class__.num_requests
        self.__class__.num_requests += 1
        self._add_request(self)

        provided_status, provided_headers, provided_body = self.do_request(n)
        status = provided_status or self.default_status
        headers = provided_headers or self.default_headers
        body = provided_body or self.default_body
        content_length = len(body)
        self.send_response(status)
        for header_name, header_value in headers.items():
            self.send_header(header_name, header_value)
        self.send_header("Content-Length", str(content_length))
        self.end_headers()
        self.wfile.write(body)
        return

    default_status = 200
    default_headers = {"Content-Type": "application/json; charset=utf-8"}
    default_body = json.dumps({}).encode("utf-8")

    def do_request(
        self, n: int
    ) -> Tuple[Optional[int], Optional[Dict[str, str]], Optional[bytes]]:
        return (self.default_status, self.default_headers, self.default_body)


class TestIntegration(object):
    @pytest.fixture(autouse=True)
    def close_mock_server(self):
        yield
        if self.mock_server:
            self.mock_server.shutdown()
            self.mock_server.server_close()
            self.mock_server_thread.join()

    @pytest.fixture(autouse=True)
    def setup_stripe(self):
        orig_attrs = {
            "api_base": stripe.api_base,
            "upload_api_base": stripe.upload_api_base,
            "api_key": stripe.api_key,
            "default_http_client": stripe.default_http_client,
            "default_http_client_async": stripe.default_http_client_async,
            "enable_telemetry": stripe.enable_telemetry,
            "max_network_retries": stripe.max_network_retries,
            "proxy": stripe.proxy,
        }
        stripe.api_base = "http://localhost:12111"  # stripe-mock
        stripe.upload_api_base = "http://localhost:12111"  # stripe-mock
        stripe.api_key = "sk_test_123"
        stripe.default_http_client = None
        stripe._default_proxy = None
        stripe.enable_telemetry = False
        stripe.max_network_retries = 3
        stripe.proxy = None
        yield
        stripe.api_base = orig_attrs["api_base"]
        stripe.upload_api_base = orig_attrs["api_base"]
        stripe.api_key = orig_attrs["api_key"]
        stripe.default_http_client_async = orig_attrs[
            "default_http_client_async"
        ]
        stripe.enable_telemetry = orig_attrs["enable_telemetry"]
        stripe.max_network_retries = orig_attrs["max_network_retries"]
        stripe.proxy = orig_attrs["proxy"]

    def setup_mock_server(self, handler):
        # Configure mock server.
        # Passing 0 as the port will cause a random free port to be chosen.
        self.mock_server = HTTPServer(("localhost", 0), handler)
        _, self.mock_server_port = self.mock_server.server_address

        # Start running mock server in a separate thread.
        # Daemon threads automatically shut down when the main process exits.
        self.mock_server_thread = Thread(target=self.mock_server.serve_forever)
        self.mock_server_thread.daemon = True
        self.mock_server_thread.start()

    def test_hits_api_base(self):
        class MockServerRequestHandler(MyTestHandler):
            pass

        self.setup_mock_server(MockServerRequestHandler)

        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.Balance.retrieve()
        reqs = MockServerRequestHandler.get_requests(1)
        assert reqs[0].path == "/v1/balance"

    def test_hits_proxy_through_default_http_client(self):
        class MockServerRequestHandler(MyTestHandler):
            pass

        self.setup_mock_server(MockServerRequestHandler)

        stripe.proxy = "http://localhost:%s" % self.mock_server_port
        stripe.Balance.retrieve()
        assert MockServerRequestHandler.num_requests == 1

        stripe.proxy = "http://bad-url"

        with warnings.catch_warnings(record=True) as w:
            stripe.Balance.retrieve()
            assert len(w) == 1
            assert "stripe.proxy was updated after sending a request" in str(
                w[0].message
            )

        assert MockServerRequestHandler.num_requests == 2

    def test_hits_proxy_through_custom_client(self):
        class MockServerRequestHandler(MyTestHandler):
            pass

        self.setup_mock_server(MockServerRequestHandler)

        stripe.default_http_client = stripe.new_default_http_client(
            proxy="http://localhost:%s" % self.mock_server_port
        )
        stripe.Balance.retrieve()
        assert MockServerRequestHandler.num_requests == 1

    def test_hits_proxy_through_stripe_client_proxy(self):
        class MockServerRequestHandler(MyTestHandler):
            pass

        self.setup_mock_server(MockServerRequestHandler)

        client = stripe.StripeClient(
            "sk_test_123",
            proxy="http://localhost:%s" % self.mock_server_port,
            base_addresses={"api": "http://localhost:12111"},
        )
        client.balance.retrieve()

        assert MockServerRequestHandler.num_requests == 1

    def test_hits_proxy_through_stripe_client_http_client(self):
        class MockServerRequestHandler(MyTestHandler):
            pass

        self.setup_mock_server(MockServerRequestHandler)

        client = stripe.StripeClient(
            "sk_test_123",
            http_client=stripe.http_client.new_default_http_client(
                proxy="http://localhost:%s" % self.mock_server_port
            ),
            base_addresses={"api": "http://localhost:12111"},
        )
        client.balance.retrieve()

        assert MockServerRequestHandler.num_requests == 1

    def test_passes_client_telemetry_when_enabled(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, req_num):
                if req_num == 0:
                    time.sleep(31 / 1000)  # 31 ms

                return [
                    200,
                    {
                        "Content-Type": "application/json; charset=utf-8",
                        "Request-Id": "req_%s" % (req_num + 1),
                    },
                    None,
                ]

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.enable_telemetry = True

        cus = stripe.Customer("cus_xyz")
        cus.description = "hello"
        cus.save()

        stripe.Customer.retrieve("cus_xyz")
        stripe.Customer.retrieve("cus_xyz")

        reqs = MockServerRequestHandler.get_requests(3)

        # req 1
        assert not reqs[0].headers.get("x-stripe-client-telemetry")
        # req 2
        telemetry_raw = reqs[1].headers.get("x-stripe-client-telemetry")

        assert telemetry_raw is not None
        telemetry = json.loads(telemetry_raw)
        assert "last_request_metrics" in telemetry

        duration_ms = telemetry["last_request_metrics"]["request_duration_ms"]
        # The first request took 31 ms, so the client perceived
        # latency shouldn't be outside this range.
        assert 30 < duration_ms < 300

        usage = telemetry["last_request_metrics"]["usage"]
        assert usage == ["save"]

        # req 3
        telemetry_raw = reqs[2].headers.get("x-stripe-client-telemetry")
        assert telemetry_raw is not None
        metrics = json.loads(telemetry_raw)["last_request_metrics"]
        assert metrics["request_id"] == "req_2"
        assert "usage" not in metrics

    def test_uses_thread_local_client_telemetry(self):
        class MockServerRequestHandler(MyTestHandler):
            local_num_requests = 0
            seen_metrics = set()
            stats_lock = Lock()

            def do_request(self, _n):
                with self.__class__.stats_lock:
                    self.__class__.local_num_requests += 1
                    req_num = self.__class__.local_num_requests

                raw_telemetry = self.headers.get("X-Stripe-Client-Telemetry")
                if raw_telemetry:
                    telemetry = json.loads(raw_telemetry)
                    req_id = telemetry["last_request_metrics"]["request_id"]
                    with self.__class__.stats_lock:
                        self.__class__.seen_metrics.add(req_id)

                return [
                    200,
                    {
                        "Content-Type": "application/json; charset=utf-8",
                        "Request-Id": "req_%s" % (req_num),
                    },
                    None,
                ]

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.enable_telemetry = True
        stripe.default_http_client = stripe.RequestsClient()

        def work():
            stripe.Balance.retrieve()
            stripe.Balance.retrieve()

        threads = [Thread(target=work) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert MockServerRequestHandler.num_requests == 20
        assert len(MockServerRequestHandler.seen_metrics) == 10

    def test_measures_stripe_client_telemetry(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, req_num):
                return [
                    200,
                    {
                        "Content-Type": "application/json; charset=utf-8",
                        "Request-Id": "req_%s" % (req_num + 1),
                    },
                    None,
                ]

        self.setup_mock_server(MockServerRequestHandler)
        stripe.enable_telemetry = True

        client = stripe.StripeClient(
            "sk_test_123",
            base_addresses={
                "api": "http://localhost:%s" % self.mock_server_port
            },
        )
        client.customers.create()
        client.customers.create()

        reqs = MockServerRequestHandler.get_requests(2)

        telemetry_raw = reqs[1].headers.get("x-stripe-client-telemetry")

        assert telemetry_raw is not None
        telemetry = json.loads(telemetry_raw)
        assert "last_request_metrics" in telemetry

        usage = telemetry["last_request_metrics"]["usage"]
        assert usage == ["stripe_client"]

    @pytest.mark.anyio
    async def test_async_raw_request_success(self):
        class MockServerRequestHandler(MyTestHandler):
            default_body = '{"id": "cus_123", "object": "customer"}'.encode(
                "utf-8"
            )
            pass

        self.setup_mock_server(MockServerRequestHandler)

        stripe.api_base = "http://localhost:%s" % self.mock_server_port

        resp = await stripe.raw_request_async(
            "post", "/v1/customers", description="My test customer"
        )
        cus = stripe.deserialize(resp.data)

        reqs = MockServerRequestHandler.get_requests(1)
        req = reqs[0]

        assert req.path == "/v1/customers"
        assert req.command == "POST"
        assert isinstance(cus, stripe.Customer)

    @pytest.mark.anyio
    async def test_async_raw_request_timeout(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, n):
                time.sleep(0.02)
                return super().do_request(n)

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.default_http_client_async = stripe.HTTPXClient()
        # If we set HTTPX's generic timeout the test is flaky (sometimes it's a ReadTimeout, sometimes its a ConnectTimeout)
        # so we set only the read timeout specifically.
        stripe.default_http_client_async._timeout = httpx.Timeout(
            None, read=0.01
        )
        stripe.max_network_retries = 0

        exception = None
        try:
            await stripe.raw_request_async(
                "post", "/v1/customers", description="My test customer"
            )
        except stripe.APIConnectionError as e:
            exception = e

        assert exception is not None

        assert "A ReadTimeout was raised" in str(exception.user_message)

    @pytest.mark.anyio
    async def test_async_httpx_raw_request_retries(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, n):
                if n == 0:
                    return (
                        500,
                        {"Request-Id": "req_1"},
                        b'{"error": {"message": "Internal server error"}}',
                    )
                return (200, None, None)

            pass

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port

        await stripe.raw_request_async(
            "post", "/v1/customers", description="My test customer"
        )

        reqs = MockServerRequestHandler.get_requests(2)
        req = reqs[0]

        assert req.path == "/v1/customers"

    @pytest.mark.anyio
    async def test_async_httpx_raw_request_unretryable(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, n):
                return (
                    401,
                    {"Request-Id": "req_1"},
                    b'{"error": {"message": "Unauthorized"}}',
                )

            pass

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port

        exception = None
        try:
            await stripe.raw_request_async(
                "post", "/v1/customers", description="My test customer"
            )
        except stripe.AuthenticationError as e:
            exception = e

        MockServerRequestHandler.get_requests(1)
        assert exception is not None
        assert "Unauthorized" in str(exception.user_message)

    @pytest.mark.anyio
    async def test_async_httpx_stream(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, n):
                return (200, None, b"hello")

        self.setup_mock_server(MockServerRequestHandler)
        stripe.upload_api_base = "http://localhost:%s" % self.mock_server_port

        result = await stripe.Quote.pdf_async("qt_123")
        assert str(await result.read(), "utf-8") == "hello"

    @pytest.mark.anyio
    async def test_async_httpx_stream_error(self):
        class MockServerRequestHandler(MyTestHandler):
            def do_request(self, n):
                return (400, None, b'{"error": {"message": "bad request"}}')

        self.setup_mock_server(MockServerRequestHandler)
        stripe.upload_api_base = "http://localhost:%s" % self.mock_server_port

        try:
            await stripe.Quote.pdf_async("qt_123")
        except stripe.InvalidRequestError as e:
            assert "bad request" in str(e.user_message)
