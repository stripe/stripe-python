from __future__ import absolute_import, division, print_function

import atexit
import os
import sys
from distutils.version import StrictVersion

import pytest

import stripe
from stripe.six.moves.urllib.request import urlopen
from stripe.six.moves.urllib.error import HTTPError

from tests.test_api_requestor import APIHeaderMatcher
from tests.request_mock import RequestMock
from tests.stripe_mock import StripeMock

MOCK_MINIMUM_VERSION = "0.109.0"

# Starts stripe-mock if an OpenAPI spec override is found in `openapi/`, and
# otherwise fall back to `STRIPE_MOCK_PORT` or 12111.
if StripeMock.start():
    MOCK_PORT = StripeMock.port()
else:
    MOCK_PORT = os.environ.get("STRIPE_MOCK_PORT", 12111)


@atexit.register
def stop_stripe_mock():
    StripeMock.stop()


def pytest_configure(config):
    if not config.getoption("--nomock"):
        try:
            resp = urlopen("http://localhost:%s/" % MOCK_PORT)
            info = resp.info()
            version = info.get("Stripe-Mock-Version")
            if version != "master" and StrictVersion(version) < StrictVersion(
                MOCK_MINIMUM_VERSION
            ):
                sys.exit(
                    "Your version of stripe-mock (%s) is too old. The minimum "
                    "version to run this test suite is %s. Please "
                    "see its repository for upgrade instructions."
                    % (version, MOCK_MINIMUM_VERSION)
                )

        except HTTPError as e:
            info = e.info()
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
    if "request_mock" in item.fixturenames and item.config.getoption(
        "--nomock"
    ):
        pytest.skip(
            "run stripe-mock locally and remove --nomock flag to run skipped tests"
        )


@pytest.fixture(autouse=True)
def setup_stripe():
    orig_attrs = {
        "api_base": stripe.api_base,
        "api_key": stripe.api_key,
        "client_id": stripe.client_id,
        "default_http_client": stripe.default_http_client,
    }
    http_client = stripe.http_client.new_default_http_client()
    stripe.api_base = "http://localhost:%s" % MOCK_PORT
    stripe.api_key = "sk_test_123"
    stripe.client_id = "ca_123"
    stripe.default_http_client = http_client
    yield
    http_client.close()
    stripe.api_base = orig_attrs["api_base"]
    stripe.api_key = orig_attrs["api_key"]
    stripe.client_id = orig_attrs["client_id"]
    stripe.default_http_client = orig_attrs["default_http_client"]


@pytest.fixture
def request_mock(mocker):
    return RequestMock(mocker)


@pytest.fixture
def http_client(mocker):
    http_client = mocker.Mock(stripe.http_client.HTTPClient)
    http_client._verify_ssl_certs = True
    http_client.name = "mockclient"
    return http_client


@pytest.fixture
def mock_response(mocker, http_client):
    def mock_response(return_body, return_code, headers=None):
        http_client.request_with_retries = mocker.Mock(
            return_value=(return_body, return_code, headers or {})
        )

    return mock_response


@pytest.fixture
def mock_streaming_response(mocker, http_client):
    def mock_streaming_response(return_body, return_code, headers=None):
        http_client.request_stream_with_retries = mocker.Mock(
            return_value=(return_body, return_code, headers or {})
        )

    return mock_streaming_response


@pytest.fixture
def check_call(http_client):
    def check_call(
        method,
        abs_url=None,
        headers=None,
        post_data=None,
        is_streaming=False,
    ):
        if not abs_url:
            abs_url = "%s%s" % (stripe.api_base, "/foo")
        if not headers:
            headers = APIHeaderMatcher(request_method=method)

        if is_streaming:
            http_client.request_stream_with_retries.assert_called_with(
                method, abs_url, headers, post_data
            )
        else:
            http_client.request_with_retries.assert_called_with(
                method, abs_url, headers, post_data
            )

    return check_call
