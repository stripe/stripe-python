import atexit
import os
import sys
import pytest

import stripe
from stripe import StripeClient
import requests

from tests.stripe_mock import StripeMock
from tests.http_client_mock import HTTPClientMock


pytest_plugins = ("anyio",)


MOCK_MINIMUM_VERSION = "0.109.0"

# Starts stripe-mock if an OpenAPI spec override is found in `openapi/`, and
# otherwise fall back to `STRIPE_MOCK_PORT` or 12111.
if StripeMock.start():
    MOCK_PORT = StripeMock.port()
else:
    MOCK_PORT = os.environ.get("STRIPE_MOCK_PORT", 12111)

MOCK_API_BASE = "http://localhost:%s" % MOCK_PORT
MOCK_API_KEY = "sk_test_123"


@atexit.register
def stop_stripe_mock():
    StripeMock.stop()


def pytest_configure(config):
    if not config.getoption("--nomock"):
        try:
            requests.get("http://localhost:%s/" % MOCK_PORT)
        except Exception:
            sys.exit(
                "Couldn't reach stripe-mock at `localhost:%s`. Is "
                "it running? Please see README for setup instructions."
                % MOCK_PORT
            )


def pytest_addoption(parser):
    parser.addoption(
        "--nomock",
        action="store_true",
        help="only run tests that don't need stripe-mock",
    )


def pytest_runtest_setup(item):
    if "http_client_mock" in item.fixturenames and item.config.getoption(
        "--nomock"
    ):
        pytest.skip(
            "run stripe-mock locally and remove --nomock flag to run skipped tests"
        )


@pytest.fixture(autouse=True)
def setup_stripe():
    orig_attrs = {
        "api_base": stripe.api_base,
        "upload_api_base": stripe.upload_api_base,
        "api_key": stripe.api_key,
        "client_id": stripe.client_id,
        "default_http_client": stripe.default_http_client,
        "default_http_client_async": stripe.default_http_client_async,
    }
    http_client = stripe.http_client.new_default_http_client()
    http_client_async = stripe.http_client.new_default_http_client_async()
    stripe.api_base = MOCK_API_BASE
    stripe.upload_api_base = MOCK_API_BASE
    stripe.api_key = MOCK_API_KEY
    stripe.client_id = "ca_123"
    stripe.default_http_client = http_client
    stripe.default_http_client_async = http_client_async
    yield
    http_client.close()
    stripe.api_base = orig_attrs["api_base"]
    stripe.upload_api_base = orig_attrs["upload_api_base"]
    stripe.api_key = orig_attrs["api_key"]
    stripe.client_id = orig_attrs["client_id"]
    stripe.default_http_client = orig_attrs["default_http_client"]
    stripe.default_http_client_async = orig_attrs["default_http_client_async"]


@pytest.fixture
def http_client_mock(mocker):
    mock_client = HTTPClientMock(mocker)
    old_client = stripe.default_http_client
    stripe.default_http_client = mock_client.get_mock_http_client()
    yield mock_client
    stripe.default_http_client = old_client


@pytest.fixture
def http_client_mock_streaming(mocker):
    mock_client = HTTPClientMock(mocker, is_streaming=True)
    old_client = stripe.default_http_client
    stripe.default_http_client = mock_client.get_mock_http_client()
    yield mock_client
    stripe.default_http_client = old_client


@pytest.fixture
def http_client_mock_async(mocker):
    mock_client = HTTPClientMock(mocker, is_async=True)
    old_client = stripe.default_http_client_async
    stripe.default_http_client_async = mock_client.get_mock_http_client()
    yield mock_client
    stripe.default_http_client_async = old_client


@pytest.fixture
def http_client_mock_streaming_async(mocker):
    mock_client = HTTPClientMock(mocker, is_streaming=True, is_async=True)
    old_client = stripe.default_http_client_async
    stripe.default_http_client_async = mock_client.get_mock_http_client()
    yield mock_client
    stripe.default_http_client_async = old_client


@pytest.fixture
def stripe_mock_stripe_client(http_client_mock):
    return StripeClient(
        MOCK_API_KEY,
        base_addresses={"api": MOCK_API_BASE},
        http_client=http_client_mock.get_mock_http_client(),
    )


@pytest.fixture
def file_stripe_mock_stripe_client(http_client_mock):
    return StripeClient(
        MOCK_API_KEY,
        base_addresses={"files": MOCK_API_BASE},
        http_client=http_client_mock.get_mock_http_client(),
    )


@pytest.fixture
def stripe_mock_stripe_client_streaming(http_client_mock_streaming):
    return StripeClient(
        MOCK_API_KEY,
        base_addresses={"api": MOCK_API_BASE},
        http_client=http_client_mock_streaming.get_mock_http_client(),
    )


@pytest.fixture
def file_stripe_mock_stripe_client_streaming(http_client_mock_streaming):
    return StripeClient(
        MOCK_API_KEY,
        base_addresses={"files": MOCK_API_BASE},
        http_client=http_client_mock_streaming.get_mock_http_client(),
    )
