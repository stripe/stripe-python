from __future__ import absolute_import, division, print_function

import platform
import sys
from threading import Thread, Lock
import json
import warnings
import time

import stripe
import pytest

if platform.python_implementation() == "PyPy":
    pytest.skip("skip integration tests with PyPy", allow_module_level=True)

if sys.version_info[0] < 3:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
else:
    from http.server import BaseHTTPRequestHandler, HTTPServer


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
            "api_key": stripe.api_key,
            "default_http_client": stripe.default_http_client,
            "enable_telemetry": stripe.enable_telemetry,
            "max_network_retries": stripe.max_network_retries,
            "proxy": stripe.proxy,
        }
        stripe.api_base = "http://localhost:12111"  # stripe-mock
        stripe.api_key = "sk_test_123"
        stripe.default_http_client = None
        stripe.enable_telemetry = False
        stripe.max_network_retries = 3
        stripe.proxy = None
        yield
        stripe.api_base = orig_attrs["api_base"]
        stripe.api_key = orig_attrs["api_key"]
        stripe.default_http_client = orig_attrs["default_http_client"]
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
        class MockServerRequestHandler(BaseHTTPRequestHandler):
            num_requests = 0

            def do_GET(self):
                self.__class__.num_requests += 1

                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(json.dumps({}).encode("utf-8"))
                return

        self.setup_mock_server(MockServerRequestHandler)

        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.Balance.retrieve()
        assert MockServerRequestHandler.num_requests == 1

    def test_hits_proxy_through_default_http_client(self):
        class MockServerRequestHandler(BaseHTTPRequestHandler):
            num_requests = 0

            def do_GET(self):
                self.__class__.num_requests += 1

                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(json.dumps({}).encode("utf-8"))
                return

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
        class MockServerRequestHandler(BaseHTTPRequestHandler):
            num_requests = 0

            def do_GET(self):
                self.__class__.num_requests += 1

                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(json.dumps({}).encode("utf-8"))
                return

        self.setup_mock_server(MockServerRequestHandler)

        stripe.default_http_client = (
            stripe.http_client.new_default_http_client(
                proxy="http://localhost:%s" % self.mock_server_port
            )
        )
        stripe.Balance.retrieve()
        assert MockServerRequestHandler.num_requests == 1

    def test_passes_client_telemetry_when_enabled(self):
        class MockServerRequestHandler(BaseHTTPRequestHandler):
            num_requests = 0

            def do_GET(self):
                try:
                    self.__class__.num_requests += 1
                    req_num = self.__class__.num_requests
                    if req_num == 1:
                        time.sleep(31 / 1000)  # 31 ms
                        assert not self.headers.get(
                            "X-Stripe-Client-Telemetry"
                        )
                    elif req_num == 2:
                        assert self.headers.get("X-Stripe-Client-Telemetry")
                        telemetry = json.loads(
                            self.headers.get("x-stripe-client-telemetry")
                        )
                        assert "last_request_metrics" in telemetry
                        req_id = telemetry["last_request_metrics"][
                            "request_id"
                        ]
                        duration_ms = telemetry["last_request_metrics"][
                            "request_duration_ms"
                        ]
                        assert req_id == "req_1"
                        # The first request took 31 ms, so the client perceived
                        # latency shouldn't be outside this range.
                        assert 30 < duration_ms < 300
                    else:
                        assert False, (
                            "Should not have reached request %d" % req_num
                        )

                    self.send_response(200)
                    self.send_header(
                        "Content-Type", "application/json; charset=utf-8"
                    )
                    self.send_header("Request-Id", "req_%d" % req_num)
                    self.end_headers()
                    self.wfile.write(json.dumps({}).encode("utf-8"))
                except AssertionError as ex:
                    # Throwing assertions on the server side causes a
                    # connection error to be logged instead of an assertion
                    # failure. Instead, we return the assertion failure as
                    # json so it can be logged as a StripeError.
                    self.send_response(400)
                    self.send_header(
                        "Content-Type", "application/json; charset=utf-8"
                    )
                    self.end_headers()
                    self.wfile.write(
                        json.dumps(
                            {
                                "error": {
                                    "type": "invalid_request_error",
                                    "message": str(ex),
                                }
                            }
                        ).encode("utf-8")
                    )

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.enable_telemetry = True

        stripe.Balance.retrieve()
        stripe.Balance.retrieve()
        assert MockServerRequestHandler.num_requests == 2

    def test_uses_thread_local_client_telemetry(self):
        class MockServerRequestHandler(BaseHTTPRequestHandler):
            num_requests = 0
            seen_metrics = set()
            stats_lock = Lock()

            def do_GET(self):
                with self.__class__.stats_lock:
                    self.__class__.num_requests += 1
                    req_num = self.__class__.num_requests

                if self.headers.get("X-Stripe-Client-Telemetry"):
                    telemetry = json.loads(
                        self.headers.get("X-Stripe-Client-Telemetry")
                    )
                    req_id = telemetry["last_request_metrics"]["request_id"]
                    with self.__class__.stats_lock:
                        self.__class__.seen_metrics.add(req_id)

                self.send_response(200)
                self.send_header(
                    "Content-Type", "application/json; charset=utf-8"
                )
                self.send_header("Request-Id", "req_%d" % req_num)
                self.end_headers()
                self.wfile.write(json.dumps({}).encode("utf-8"))

        self.setup_mock_server(MockServerRequestHandler)
        stripe.api_base = "http://localhost:%s" % self.mock_server_port
        stripe.enable_telemetry = True
        stripe.default_http_client = stripe.http_client.RequestsClient()

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
