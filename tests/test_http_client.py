import io
import base64
import json
import sys
from typing import Any, Callable, Dict, List, Optional
from unittest.mock import MagicMock, Mock, call, patch

import pytest
from typing_extensions import Type

if sys.version_info >= (3, 8):
    from unittest.mock import AsyncMock
else:
    from mock import AsyncMock

from contextlib import contextmanager

import urllib3

import stripe
from stripe import APIConnectionError, _http_client
from stripe._encode import _api_encode
from stripe._http_client import (
    AIOHTTPClient,
    HTTPXClient,
    NoImportFoundAsyncClient,
    PycurlClient,
    RequestsClient,
)
from stripe._http_client import (
    UrlFetchClient as AppEngineClient,
)
from stripe._http_client import (
    UrllibClient as BuiltinClient,
)

VALID_API_METHODS = ("get", "post", "delete")


@pytest.fixture
def mocked_request_lib():
    return MagicMock()


SUPPORTED_LIBS = frozenset(
    ("google.appengine.api", "requests", "pycurl", "httpx", "aiohttp", "anyio")
)


@pytest.fixture
def mock_import():
    """
    A pytest fixture that simulates a specific set of libraries being available. Right now it hardcodes information about our `SUPPORTED_LIBS`, but we could make it more general.

    usage:
        with patch("builtins.__import__") as mocked_import_fn:
            mocked_import_fn.side_effect = mock_import(['a', 'b', 'c'])

            # assuming SUPPORTED_LIBS is a,b,c
            import a # works (MagicMock if `a` isn't installed for real)
            import d # importError
            import pytest # is a regular import, only works if pytest is actually installed
    """
    orig_import = __import__

    def create_mocked_import(available_libs: List[str]):
        def _mocked_import(name, *args):
            """
            emulate packages being missing by throwing early if they're not supposed to be here.
            """
            if name in SUPPORTED_LIBS and name not in available_libs:
                raise ImportError()

            try:
                # if it's not supposed to be missing, try and import it for real
                return orig_import(name, *args)
            except ImportError:
                # we don't have some of our 3rd party options (like the GAE module) available, but the import needs to succeed
                return MagicMock()

        return _mocked_import

    return create_mocked_import


class TestImports:
    @pytest.mark.parametrize(
        ["available_libs", "expected"],
        [
            [["google.appengine.api"], AppEngineClient],
            [["google.appengine.api", "requests"], AppEngineClient],
            [["requests"], RequestsClient],
            [["requests", "pycurl"], RequestsClient],
            [["pycurl"], PycurlClient],
            [[], BuiltinClient],
        ],
    )
    def test_default_httpclient_from_imports(
        self, available_libs, expected, mock_import
    ):
        with patch("builtins.__import__") as mocked_import_fn:
            mocked_import_fn.side_effect = mock_import(available_libs)

            client = _http_client.new_default_http_client()
            assert isinstance(client, expected)

    @pytest.mark.parametrize(
        ["available_libs", "expected"],
        [
            # needs both httpx and anyio
            [["httpx"], NoImportFoundAsyncClient],
            [["anyio"], NoImportFoundAsyncClient],
            [["httpx", "anyio"], HTTPXClient],
            # having only one required lib means we proceed
            [["anyio", "aiohttp"], AIOHTTPClient],
            [["aiohttp"], AIOHTTPClient],
            [[], NoImportFoundAsyncClient],
        ],
    )
    def test_default_async_httpclient_from_imports(
        self, available_libs, expected, mock_import
    ):
        with patch("builtins.__import__") as mocked_import_fn:
            mocked_import_fn.side_effect = mock_import(available_libs)

            client = _http_client.new_http_client_async_fallback()
            assert isinstance(client, expected)


MakeReqFunc = Callable[[str, str, Dict[str, str], Optional[str]], Any]


class TestRetrySleepTimeDefaultHttpClient:
    def assert_sleep_times(
        self, client: _http_client.HTTPClient, expected: List[float]
    ):
        # the sleep duration for a request after N retries
        actual = [
            client._sleep_time_seconds(i + 1) for i in range(len(expected))
        ]
        assert expected == actual

    @contextmanager
    def mock_max_delay(self, new_value):
        original_value = _http_client.HTTPClient.MAX_DELAY
        _http_client.HTTPClient.MAX_DELAY = new_value
        try:
            yield self
        finally:
            _http_client.HTTPClient.MAX_DELAY = original_value

    def test_sleep_time_exponential_back_off(self):
        client = _http_client.new_default_http_client()
        client._add_jitter_time = lambda sleep_seconds: sleep_seconds
        with self.mock_max_delay(10):
            self.assert_sleep_times(client, [])

    def test_initial_delay_as_minimum(self):
        client = _http_client.new_default_http_client()
        client._add_jitter_time = lambda sleep_seconds: sleep_seconds * 0.001
        initial_delay = _http_client.HTTPClient.INITIAL_DELAY
        self.assert_sleep_times(client, [initial_delay] * 5)

    def test_maximum_delay(self):
        client = _http_client.new_default_http_client()
        client._add_jitter_time = lambda sleep_seconds: sleep_seconds
        max_delay = _http_client.HTTPClient.MAX_DELAY
        expected = [0.5, 1.0, 2.0, 4.0, max_delay, max_delay, max_delay]
        self.assert_sleep_times(client, expected)

    def test_retry_after_header(self):
        client = _http_client.new_default_http_client()
        client._add_jitter_time = lambda sleep_seconds: sleep_seconds

        # Prefer retry-after if it's bigger
        assert 30 == client._sleep_time_seconds(
            2, (None, 409, {"retry-after": "30"})
        )
        # Prefer default if it's bigger
        assert 2 == client._sleep_time_seconds(
            3, (None, 409, {"retry-after": "1"})
        )
        # Ignore crazy-big values
        assert 1 == client._sleep_time_seconds(
            2, (None, 409, {"retry-after": "300"})
        )

    def test_randomness_added(self):
        client = _http_client.new_default_http_client()
        random_value = 0.8
        client._add_jitter_time = (
            lambda sleep_seconds: sleep_seconds * random_value
        )
        base_value = _http_client.HTTPClient.INITIAL_DELAY * random_value

        with self.mock_max_delay(10):
            expected = [
                _http_client.HTTPClient.INITIAL_DELAY,
                base_value * 2,
                base_value * 4,
                base_value * 8,
                base_value * 16,
            ]
            self.assert_sleep_times(client, expected)

    def test_jitter_has_randomness_but_within_range(self):
        client = _http_client.new_default_http_client()

        jittered_ones = set(
            map(lambda _: client._add_jitter_time(1), list(range(100)))
        )

        assert len(jittered_ones) > 1
        assert all(0.5 <= val <= 1 for val in jittered_ones)


class TestRetryConditionsDefaultHttpClient:
    def test_should_retry_on_codes(self):
        one_xx = list(range(100, 104))
        two_xx = list(range(200, 209))
        three_xx = list(range(300, 308))
        four_xx = list(range(400, 431))

        client = _http_client.new_default_http_client()
        codes = one_xx + two_xx + three_xx + four_xx
        codes.remove(409)

        # These status codes should not be retried by default.
        for code in codes:
            assert (
                client._should_retry(
                    (None, code, None), None, 0, max_network_retries=1
                )
                is False
            )

        # These status codes should be retried by default.
        assert (
            client._should_retry(
                (None, 409, None), None, 0, max_network_retries=1
            )
            is True
        )
        assert (
            client._should_retry(
                (None, 500, None), None, 0, max_network_retries=1
            )
            is True
        )
        assert (
            client._should_retry(
                (None, 503, None), None, 0, max_network_retries=1
            )
            is True
        )

    def test_should_retry_on_error(self, mocker):
        client = _http_client.new_default_http_client()
        api_connection_error = Mock()

        api_connection_error.should_retry = True
        assert (
            client._should_retry(
                None, api_connection_error, 0, max_network_retries=1
            )
            is True
        )

        api_connection_error.should_retry = False
        assert (
            client._should_retry(
                None, api_connection_error, 0, max_network_retries=1
            )
            is False
        )

    def test_should_retry_on_stripe_should_retry_true(self, mocker):
        client = _http_client.new_default_http_client()
        headers = {"stripe-should-retry": "true"}

        # Ordinarily, we would not retry a 400, but with the header as true, we would.
        assert (
            client._should_retry(
                (None, 400, {}), None, 0, max_network_retries=1
            )
            is False
        )
        assert (
            client._should_retry(
                (None, 400, headers), None, 0, max_network_retries=1
            )
            is True
        )

    def test_should_retry_on_stripe_should_retry_false(self, mocker):
        client = _http_client.new_default_http_client()
        headers = {"stripe-should-retry": "false"}

        # Ordinarily, we would retry a 500, but with the header as false, we would not.
        assert (
            client._should_retry(
                (None, 500, {}), None, 0, max_network_retries=1
            )
            is True
        )
        assert (
            client._should_retry(
                (None, 500, headers), None, 0, max_network_retries=1
            )
            is False
        )

    def test_should_retry_on_num_retries(self, mocker):
        client = _http_client.new_default_http_client()
        max_test_retries = 10
        api_connection_error = Mock()
        api_connection_error.should_retry = True

        assert (
            client._should_retry(
                None,
                api_connection_error,
                max_test_retries + 1,
                max_network_retries=max_test_retries,
            )
            is False
        )
        assert (
            client._should_retry(
                (None, 409, None),
                None,
                max_test_retries + 1,
                max_network_retries=max_test_retries,
            )
            is False
        )


class TestHTTPClient:
    @pytest.fixture(autouse=True)
    def setup_stripe(self):
        orig_attrs = {"enable_telemetry": stripe.enable_telemetry}
        stripe.enable_telemetry = False
        yield
        stripe.enable_telemetry = orig_attrs["enable_telemetry"]

    def test_sends_telemetry_on_second_request(self, mocker):
        class TestClient(_http_client.HTTPClient):
            pass

        stripe.enable_telemetry = True

        url = "http://fake.url"

        client = TestClient()

        client.request = mocker.MagicMock(
            return_value=["", 200, {"Request-Id": "req_123"}]
        )
        _, code, _ = client.request_with_retries("get", url, {}, None)
        assert code == 200
        client.request.assert_called_with("get", url, {}, None)

        client.request = mocker.MagicMock(
            return_value=["", 200, {"Request-Id": "req_234"}]
        )
        _, code, _ = client.request_with_retries("get", url, {}, None)
        assert code == 200
        args, _ = client.request.call_args
        assert "X-Stripe-Client-Telemetry" in args[2]

        telemetry = json.loads(args[2]["X-Stripe-Client-Telemetry"])
        assert telemetry["last_request_metrics"]["request_id"] == "req_123"


class ClientTestBase:
    REQUEST_CLIENT: Type[_http_client.HTTPClient]
    valid_url = "https://api.stripe.com/foo"
    # only some clients support proxies
    PROXY = None
    # certain test classes depend on re-initializing the client because they've modified the mocked lib before it goes in
    ALWAYS_INIT_CLIENT = False
    # allow customizing client creation
    CLIENT_KWARGS = None

    @pytest.fixture
    def make_client(self, mocked_request_lib):
        def _make_client(**kwargs):
            client = self.REQUEST_CLIENT(
                verify_ssl_certs=True,
                proxy=self.PROXY,
                _lib=mocked_request_lib,
                **kwargs,
            )
            # speed up all retries
            client._sleep_time_seconds = (
                lambda num_retries, response=None: 0.0001
            )
            return client

        return _make_client

    @pytest.fixture
    def client(self, make_client):
        return make_client()

    @pytest.fixture
    def make_request(self, make_client, client) -> MakeReqFunc:
        def _make_request(
            method,
            url,
            headers,
            post_data,
            client_kwargs=None,
            max_retries=None,
        ):
            # reuse the fixture client, if possible
            if client_kwargs or self.CLIENT_KWARGS or self.ALWAYS_INIT_CLIENT:
                local_client = make_client(
                    **{
                        **(self.CLIENT_KWARGS or {}),
                        **(client_kwargs or {}),
                    }
                )
            else:
                local_client = client

            return local_client.request_with_retries(
                method,
                url,
                headers,
                post_data,
                max_network_retries=max_retries,
            )

        return _make_request

    @pytest.fixture
    def make_streamed_request(self, make_client, client) -> MakeReqFunc:
        def _make_request_stream(
            method,
            url,
            headers,
            post_data,
            client_kwargs=None,
            max_retries=None,
        ):
            if client_kwargs or self.CLIENT_KWARGS or self.ALWAYS_INIT_CLIENT:
                local_client = make_client(
                    **(client_kwargs or self.CLIENT_KWARGS or {})
                )
            else:
                local_client = client

            return local_client.request_stream_with_retries(
                method,
                url,
                headers,
                post_data,
                max_network_retries=max_retries,
            )

        return _make_request_stream

    @pytest.fixture
    def make_async_request(self, make_client, client) -> MakeReqFunc:
        def _make_request_async(
            method,
            url,
            headers,
            post_data,
            client_kwargs=None,
            max_retries=None,
        ):
            if client_kwargs or self.CLIENT_KWARGS or self.ALWAYS_INIT_CLIENT:
                local_client = make_client(
                    **(client_kwargs or {}),
                    **(self.CLIENT_KWARGS or {}),
                )
            else:
                local_client = client

            return local_client.request_with_retries_async(
                method,
                url,
                headers,
                post_data,
                max_network_retries=max_retries,
            )

        return _make_request_async

    @pytest.fixture
    def make_async_stream_request(self, make_client, client) -> MakeReqFunc:
        async def _make_request_stream_async(
            method,
            url,
            headers,
            post_data,
            client_kwargs=None,
            max_retries=None,
        ):
            if client_kwargs or self.CLIENT_KWARGS or self.ALWAYS_INIT_CLIENT:
                local_client = make_client(
                    **(client_kwargs or {}),
                    **(self.CLIENT_KWARGS or {}),
                )
            else:
                local_client = client

            return await local_client.request_stream_with_retries_async(
                method,
                url,
                headers,
                post_data,
                max_network_retries=max_retries,
            )

        return _make_request_stream_async

    @pytest.fixture
    def mock_response(self):
        def mock_response(mock, body, code):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock, error):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(
            mock, method, abs_url, headers, params, is_streaming=False
        ):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return check_call

    def test_request(
        self,
        mocked_request_lib,
        make_request: MakeReqFunc,
        mock_response,
        check_call,
    ):
        mock_response(mocked_request_lib, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = f"{abs_url}?{data}"
                data = None

            headers = {"my-header": "header val"}

            body, code, _ = make_request(method, abs_url, headers, data)

            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call(mocked_request_lib, method, abs_url, data, headers)

    def test_request_stream(
        self, mocked_request_lib, make_streamed_request, mock_response
    ):
        for method in VALID_API_METHODS:
            mock_response(mocked_request_lib, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = make_streamed_request(
                method, abs_url, headers, data
            )

            assert code == 200

            body_content = None
            # Here we need to convert and align all content on one type (string)
            # as some clients return a string stream others a byte stream.
            if hasattr(stream, "read"):
                body_content = stream.read()
                if hasattr(body_content, "decode"):
                    body_content = body_content.decode("utf-8")
            elif hasattr(stream, "__iter__"):
                body_content = "".join(
                    [chunk.decode("utf-8") for chunk in stream]
                )

            assert body_content == "some streamed content"

    def test_exception(self, mocked_request_lib, mock_error, make_request):
        mock_error(mocked_request_lib)
        with pytest.raises(APIConnectionError):
            make_request("get", self.valid_url, {}, None, mocked_request_lib)


class RequestsVerify(object):
    def __eq__(self, other):
        return other and other.endswith("stripe/data/ca-certificates.crt")


class TestRequestsClient(ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.RequestsClient] = (
        _http_client.RequestsClient
    )
    PROXY = "http://slap/"

    @pytest.fixture
    def session(self):
        return MagicMock()

    @pytest.fixture
    def mock_response(self, session):
        def _mock_response(mock, body, code):
            result = Mock()
            result.content = body
            result.status_code = code
            result.headers = {}
            result.raw = urllib3.response.HTTPResponse(
                body=io.BytesIO(str.encode(body)),
                preload_content=False,
                status=code,
            )

            session.request = MagicMock(return_value=result)
            mock.Session = MagicMock(return_value=session)

        return _mock_response

    @pytest.fixture
    def mock_error(self, session):
        def _mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            session.request.side_effect = mock.exceptions.SSLError()
            mock.Session = MagicMock(return_value=session)

        return _mock_error

    @pytest.fixture
    def check_call(self, session):
        def _check_call(
            _,
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
            timeout=80,
            times=None,
        ):
            times = times or 1
            pargs = (method, url)
            kwargs = {
                "headers": headers,
                "data": post_data,
                "verify": RequestsVerify(),
                "proxies": {"http": "http://slap/", "https": "http://slap/"},
                "timeout": timeout,
            }

            if is_streaming:
                kwargs["stream"] = True

            calls = [call(*pargs, **kwargs) for _ in range(times)]
            session.request.assert_has_calls(calls)

        return _check_call

    def test_timeout(
        self, mocked_request_lib, mock_response, check_call, make_request
    ):
        headers = {"my-header": "header val"}
        data = ""
        mock_response(mocked_request_lib, '{"foo": "baz"}', 200)
        make_request(
            "POST", self.valid_url, headers, data, client_kwargs={"timeout": 5}
        )

        check_call(None, "POST", self.valid_url, data, headers, timeout=5)

    def test_request_stream_forwards_stream_param(
        self,
        mocked_request_lib,
        mock_response,
        check_call,
        make_streamed_request: MakeReqFunc,
    ):
        mock_response(mocked_request_lib, "some streamed content", 200)
        make_streamed_request("GET", self.valid_url, {}, None)

        check_call(None, "GET", self.valid_url, None, {}, is_streaming=True)


class TestRequestClientRetryBehavior(TestRequestsClient):
    PROXY = "http://slap/"
    max_retries = 3

    @pytest.fixture
    def response(self):
        def response(code=200, headers=None):
            result = Mock()
            result.content = "{}"
            result.status_code = code
            result.headers = headers or {}
            result.raw = urllib3.response.HTTPResponse(
                body=io.BytesIO(str.encode(result.content)),
                preload_content=False,
                status=code,
            )

            return result

        return response

    @pytest.fixture
    def mock_retry(self, session, mocked_request_lib):
        def _mock_retry(
            retry_error_num=0, no_retry_error_num=0, responses=None
        ):
            if responses is None:
                responses = []
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            mocked_request_lib.exceptions.RequestException = (
                request_root_error_class
            )

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            mocked_request_lib.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            mocked_request_lib.exceptions.Timeout = retry_parent_class
            mocked_request_lib.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num

            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions
            session.request.side_effect = (
                retry_errors + no_retry_errors + responses
            )

            mocked_request_lib.Session = MagicMock(return_value=session)
            return mocked_request_lib

        return _mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call):
        valid_url = self.valid_url

        def _check_call_numbers(times, is_streaming=False):
            check_call(
                None,
                "GET",
                valid_url,
                None,
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return _check_call_numbers

    def test_retry_error_until_response(
        self, mock_retry, response, check_call_numbers, make_request
    ):
        mock_retry(retry_error_num=1, responses=[response(code=202)])
        _, code, _ = make_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 202
        check_call_numbers(2)

    def test_retry_error_until_exceeded(
        self, mock_retry, check_call_numbers, make_request
    ):
        mock_retry(retry_error_num=self.max_retries)
        with pytest.raises(APIConnectionError):
            make_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )

        check_call_numbers(self.max_retries)

    def test_no_retry_error(
        self, mock_retry, check_call_numbers, make_request
    ):
        mock_retry(no_retry_error_num=self.max_retries)
        with pytest.raises(APIConnectionError):
            make_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )
        check_call_numbers(1)

    def test_retry_codes(
        self, mock_retry, response, check_call_numbers, make_request
    ):
        mock_retry(responses=[response(code=409), response(code=202)])
        _, code, _ = make_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 202
        check_call_numbers(2)

    def test_retry_codes_until_exceeded(
        self, mock_retry, response, check_call_numbers, make_request
    ):
        mock_retry(responses=[response(code=409)] * (self.max_retries + 1))
        _, code, _ = make_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 409
        check_call_numbers(self.max_retries + 1)

    def test_retry_request_stream_error_until_response(
        self,
        mock_retry,
        response,
        check_call_numbers,
        make_streamed_request,
    ):
        mock_retry(retry_error_num=1, responses=[response(code=202)])
        _, code, _ = make_streamed_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 202
        check_call_numbers(2, is_streaming=True)

    def test_retry_request_stream_error_until_exceeded(
        self,
        mock_retry,
        check_call_numbers,
        make_streamed_request,
    ):
        mock_retry(retry_error_num=self.max_retries)
        with pytest.raises(APIConnectionError):
            make_streamed_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )

        check_call_numbers(self.max_retries, is_streaming=True)

    def test_no_retry_request_stream_error(
        self,
        mock_retry,
        check_call_numbers,
        make_streamed_request,
    ):
        mock_retry(no_retry_error_num=self.max_retries)
        with pytest.raises(APIConnectionError):
            make_streamed_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )
        check_call_numbers(1, is_streaming=True)

    def test_retry_request_stream_codes(
        self,
        mock_retry,
        response,
        check_call_numbers,
        make_streamed_request,
    ):
        mock_retry(responses=[response(code=409), response(code=202)])
        _, code, _ = make_streamed_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 202
        check_call_numbers(2, is_streaming=True)

    def test_retry_request_stream_codes_until_exceeded(
        self,
        mock_retry,
        response,
        check_call_numbers,
        make_streamed_request,
    ):
        mock_retry(responses=[response(code=409)] * (self.max_retries + 1))
        _, code, _ = make_streamed_request(
            "GET", self.valid_url, {}, None, max_retries=self.max_retries
        )
        assert code == 409
        check_call_numbers(self.max_retries + 1, is_streaming=True)

    @pytest.fixture
    def connection_error(self, client):
        def connection_error(given_exception):
            with pytest.raises(APIConnectionError) as error:
                client._handle_request_error(given_exception)
            return error.value

        return connection_error

    def test_handle_request_error_should_retry(
        self, connection_error, mock_retry
    ):
        mocked_lib = mock_retry()

        error = connection_error(mocked_lib.exceptions.Timeout())
        assert error.should_retry

        error = connection_error(mocked_lib.exceptions.ConnectionError())
        assert error.should_retry

    def test_handle_request_error_should_not_retry(
        self, connection_error, mock_retry
    ):
        request_mock = mock_retry()

        error = connection_error(request_mock.exceptions.SSLError())
        assert error.should_retry is False
        assert "not verify Stripe's SSL certificate" in error.user_message

        error = connection_error(request_mock.exceptions.RequestException())
        assert error.should_retry is False

        # Mimic non-requests exception as not being children of Exception,
        # See mock_retry for the exceptions setup
        error = connection_error(BaseException(""))
        assert error.should_retry is False
        assert "configuration issue locally" in error.user_message

    # Skip inherited basic requests client tests
    def test_request(self):
        pass

    def test_exception(self):
        pass

    def test_timeout(self):
        pass


class TestUrlFetchClient(ClientTestBase):
    REQUEST_CLIENT = _http_client.UrlFetchClient

    @pytest.fixture
    def mock_response(self):
        def mock_response(mocked_lib, body, code):
            result = Mock()
            result.content = body
            result.status_code = code
            result.headers = {}

            mocked_lib.fetch = Mock(return_value=result)
            return result

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            mock.Error = mock.InvalidURLError = Exception
            mock.fetch.side_effect = mock.InvalidURLError()

        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(
            mock, method, url, post_data, headers, is_streaming=False
        ):
            mock.fetch.assert_called_with(
                url=url,
                method=method,
                headers=headers,
                validate_certificate=True,
                deadline=55,
                payload=post_data,
            )

        return check_call


class TestUrllibClient(ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.UrllibClient] = _http_client.UrllibClient
    USE_PROXY = False

    request_object: Any

    @pytest.fixture
    def mock_response(self):
        def mock_response(mocked_lib, body, code):
            response = Mock()
            response.read = MagicMock(return_value=body)
            response.code = code
            response.info = Mock(return_value={})

            self.request_object = Mock()
            mocked_lib.Request = Mock(return_value=self.request_object)

            opener = Mock()
            opener.open = Mock(return_value=response)
            mocked_lib.build_opener = Mock(return_value=opener)
            mocked_lib.build_opener.open = opener.open
            mocked_lib.ProxyHandler = Mock(return_value=opener)

            mocked_lib.urlopen = Mock(return_value=response)

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            mock.urlopen.side_effect = ValueError
            mock.build_opener().open.side_effect = ValueError
            mock.build_opener.reset_mock()

        return mock_error

    @pytest.fixture
    def check_call(self, client):
        def _check_call(
            mocked_lib,
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
        ):
            if isinstance(post_data, str):
                post_data = post_data.encode("utf-8")

            mocked_lib.Request.assert_called_with(url, post_data, headers)

            if client._proxy:
                assert isinstance(client._proxy, dict)
                mocked_lib.ProxyHandler.assert_called_with(client._proxy)
                mocked_lib.build_opener.open.assert_called_with(
                    self.request_object
                )
                assert not mocked_lib.urlopen.called
            else:
                mocked_lib.urlopen.assert_called_with(self.request_object)
                assert not mocked_lib.build_opener.called
                assert not mocked_lib.build_opener.open.called

        return _check_call


class TestUrllibClientHttpsProxy(TestUrllibClient):
    USE_PROXY = True
    ALWAYS_INIT_CLIENT = True


class TestPycurlClient(ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.PycurlClient] = _http_client.PycurlClient
    ALWAYS_INIT_CLIENT = True

    @pytest.fixture
    def curl_mock(self):
        return Mock()

    @pytest.fixture
    def request_mock(self, mocker, mocked_request_lib, curl_mock):
        mocked_request_lib.Curl = Mock(return_value=curl_mock)
        return curl_mock

    @pytest.fixture
    def bio_mock(self, mocker):
        bio_patcher = mocker.patch("stripe._http_client.BytesIO")
        bio_mock = Mock()
        bio_patcher.return_value = bio_mock
        return bio_mock

    @pytest.fixture
    def mock_response(self, mocker, bio_mock):
        def mock_response(mock, body, code):
            bio_mock.getvalue = mocker.MagicMock(
                return_value=body.encode("utf-8")
            )
            bio_mock.read = mocker.MagicMock(return_value=body.encode("utf-8"))
            # Set up the getinfo method on the curl instance
            curl_instance = mock.Curl()
            curl_instance.getinfo = mocker.MagicMock(return_value=code)

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def _mock_error(mock):
            class FakeException(BaseException):
                @property
                def args(self):
                    return ("foo", "bar")

            # Set the pycurl.error class on the mocked lib
            mock.error = FakeException
            # Create a curl mock that will raise the exception on perform()
            curl_instance = MagicMock()
            curl_instance.perform.side_effect = FakeException()
            mock.Curl.return_value = curl_instance

        return _mock_error

    @pytest.fixture
    def check_call(self, client):
        def _check_call(
            mocked_lib, method, url, post_data, headers, is_streaming=False
        ):
            # The mock parameter should be the curl instance, but it's being passed the mocked_request_lib
            # Get the actual curl mock instance
            curl_mock = mocked_lib.Curl()

            if client._proxy:
                proxy = client._get_proxy(url)
                assert proxy is not None
                if proxy.hostname:
                    curl_mock.setopt.assert_any_call(
                        mocked_lib.PROXY, proxy.hostname
                    )
                if proxy.port:
                    curl_mock.setopt.assert_any_call(
                        mocked_lib.PROXYPORT, proxy.port
                    )
                if proxy.username or proxy.password:
                    curl_mock.setopt.assert_any_call(
                        mocked_lib.PROXYUSERPWD,
                        "%s:%s" % (proxy.username, proxy.password),
                    )

            # A note on methodology here: we don't necessarily need to verify
            # _every_ call to setopt, but check a few of them to make sure the
            # right thing is happening. Keep an eye specifically on conditional
            # statements where things are more likely to go wrong.
            curl_mock.setopt.assert_any_call(mocked_lib.NOSIGNAL, 1)
            curl_mock.setopt.assert_any_call(mocked_lib.URL, url)

            if method == "get":
                curl_mock.setopt.assert_any_call(mocked_lib.HTTPGET, 1)
            elif method == "post":
                curl_mock.setopt.assert_any_call(mocked_lib.POST, 1)
            else:
                curl_mock.setopt.assert_any_call(
                    mocked_lib.CUSTOMREQUEST, method.upper()
                )

            curl_mock.perform.assert_any_call()

        return _check_call


class TestPycurlClientHttpProxy(TestPycurlClient):
    PROXY = "http://user:withPwd@slap:8888/"


class TestPycurlClientHttpsProxy(TestPycurlClient):
    PROXY = {"http": "http://slap:8888/", "https": "http://slap2:444/"}


class TestAPIEncode:
    def test_encode_dict(self):
        body = {"foo": {"dob": {"month": 1}, "name": "bat"}}

        values = [t for t in _api_encode(body)]

        assert ("foo[dob][month]", 1) in values
        assert ("foo[name]", "bat") in values

    def test_encode_array(self):
        body = {"foo": [{"dob": {"month": 1}, "name": "bat"}]}

        values = [t for t in _api_encode(body)]

        assert ("foo[0][dob][month]", 1) in values
        assert ("foo[0][name]", "bat") in values

    def test_encode_v2_array(self):
        body = {"foo": [{"dob": {"month": 1}, "name": "bat"}]}

        values = [t for t in _api_encode(body)]

        assert ("foo[0][dob][month]", 1) in values
        assert ("foo[0][name]", "bat") in values


class TestHTTPXClient(ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.HTTPXClient] = _http_client.HTTPXClient
    PROXY = "http://slap/"
    # ALWAYS_INIT_CLIENT= True
    CLIENT_KWARGS = {"allow_sync_methods": True}

    @pytest.fixture
    def request_mock(self, mocked_request_lib):
        # Set up the httpx library mock structure
        async_client_instance = Mock()
        sync_client_instance = Mock()

        mocked_request_lib.AsyncClient = Mock(
            return_value=async_client_instance
        )
        mocked_request_lib.Client = Mock(return_value=sync_client_instance)

        return mocked_request_lib

    @pytest.fixture
    def mock_response(self, request_mock):
        def _mock_response(mock, body="", code=200):
            result = Mock()
            result.content = body

            async def aiter_bytes():
                yield bytes(body, "utf-8")

            def iter_bytes():
                yield bytes(body, "utf-8")

            result.aiter_bytes = aiter_bytes
            result.iter_bytes = iter_bytes
            result.status_code = code
            result.headers = {}

            async def do_buffered(*args, **kwargs):
                return result

            async def do_stream(*args, **kwargs):
                return result

            async_mock = AsyncMock(side_effect=do_buffered)
            async_mock_stream = AsyncMock(side_effect=do_stream)

            request_mock.Client().send = Mock(return_value=result)
            request_mock.Client().request = Mock(return_value=result)
            request_mock.AsyncClient().send = async_mock_stream
            request_mock.AsyncClient().request = async_mock
            return result

        return _mock_response

    @pytest.fixture
    def mock_error(self, mocker, request_mock):
        def _mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            request_mock.AsyncClient().request.side_effect = (
                mock.exceptions.SSLError()
            )

        return _mock_error

    @pytest.fixture
    def check_call(self, request_mock, mocker):
        def _check_call(
            mock,
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
            timeout=80,
            times=None,
        ):
            times = times or 1
            args = (method, url)
            kwargs = {
                "headers": headers,
                "data": post_data or {},
                "timeout": timeout,
                "proxies": {"http": "http://slap/", "https": "http://slap/"},
            }

            if is_streaming:
                kwargs["stream"] = True

            calls = [mocker.call(*args, **kwargs) for _ in range(times)]
            request_mock.Client().request.assert_has_calls(calls)

        return _check_call

    @pytest.fixture
    def check_call_async(self, request_mock, mocker):
        def _check_call_async(
            mock,
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
            timeout=80,
            times=None,
        ):
            times = times or 1
            args = (method, url)
            kwargs = {
                "headers": headers,
                "data": post_data,
                "timeout": timeout,
                "proxies": {"http": "http://slap/", "https": "http://slap/"},
            }

            if is_streaming:
                kwargs["stream"] = True

            calls = [mocker.call(*args, **kwargs) for _ in range(times)]
            request_mock.AsyncClient().request.assert_has_calls(calls)

        return _check_call_async

    @pytest.mark.anyio
    async def test_request_async(
        self, request_mock, mock_response, check_call_async, make_async_request
    ):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = {}

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = {}

            headers = {"my-header": "header val"}
            body, code, _ = await make_async_request(
                method, abs_url, headers, data
            )
            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call_async(request_mock, method, abs_url, data, headers)

    @pytest.mark.anyio
    async def test_request_stream_async(
        self,
        mocker,
        request_mock,
        mock_response,
        check_call,
        make_async_stream_request,
    ):
        for method in VALID_API_METHODS:
            mock_response(request_mock, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = await make_async_stream_request(
                method, abs_url, headers, data
            )

            assert code == 200

            # Here we need to convert and align all content on one type (string)
            # as some clients return a string stream others a byte stream.
            body_content = b"".join([x async for x in stream])
            if hasattr(body_content, "decode"):
                body_content = body_content.decode("utf-8")

            assert body_content == "some streamed content"

            mocker.resetall()

    @pytest.mark.anyio
    async def test_exception(
        self, request_mock, mock_error, make_async_request
    ):
        mock_error(request_mock)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request("get", self.valid_url, {}, None)

    @pytest.mark.anyio
    def test_timeout(
        self, request_mock, mock_response, check_call, make_request
    ):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(request_mock, '{"foo": "baz"}', 200)
        make_request("POST", self.valid_url, headers, data, {"timeout": 5})

        check_call(
            request_mock, "POST", self.valid_url, data, headers, timeout=5
        )

    @pytest.mark.anyio
    async def test_timeout_async(
        self, request_mock, mock_response, check_call_async, make_async_request
    ):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(request_mock, '{"foo": "baz"}', 200)
        await make_async_request(
            "POST", self.valid_url, headers, data, {"timeout": 5}
        )

        check_call_async(
            request_mock, "POST", self.valid_url, data, headers, timeout=5
        )

    @pytest.mark.anyio
    async def test_request_stream_forwards_stream_param(self):
        # TODO
        pass

    def test_allow_sync_methods(self, request_mock, mock_response):
        client = self.REQUEST_CLIENT(_lib=request_mock)
        assert client._client is None
        with pytest.raises(RuntimeError):
            client.request("GET", "http://foo", {})
        with pytest.raises(RuntimeError):
            client.request_stream("GET", "http://foo", {})
        client = self.REQUEST_CLIENT(
            allow_sync_methods=True, _lib=request_mock
        )
        assert client._client is not None
        mock_response(request_mock, '{"foo": "baz"}', 200)
        client.request("GET", "http://foo", {})
        mock_response(request_mock, '{"foo": "baz"}', 200)
        client.request_stream("GET", "http://foo", {})


class TestHTTPXClientRetryBehavior(TestHTTPXClient):
    responses = None
    max_retries = 3
    ALWAYS_INIT_CLIENT = True

    @pytest.fixture
    def mock_retry(self, mocked_request_lib):
        def _mock_retry(
            retry_error_num=0, no_retry_error_num=0, responses=None
        ):
            # Store the mocked request lib for use in make_client

            if responses is None:
                responses = []
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            mocked_request_lib.exceptions.RequestException = (
                request_root_error_class
            )

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            mocked_request_lib.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            mocked_request_lib.exceptions.Timeout = retry_parent_class
            mocked_request_lib.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num
            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions

            results = retry_errors + no_retry_errors + responses

            mocked_request_lib.AsyncClient().request = AsyncMock(
                side_effect=results
            )
            self.responses = results

            return mocked_request_lib

        return _mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call_async):
        valid_url = self.valid_url

        def _check_call_numbers(times, is_streaming=False):
            check_call_async(
                None,
                "GET",
                valid_url,
                {},
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return _check_call_numbers

    @pytest.fixture
    def make_async_request_with_args(self, make_async_request):
        async def _make_async_request():
            return await make_async_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )

        return _make_async_request

    @pytest.mark.anyio
    async def test_retry_error_until_response(
        self,
        mock_retry,
        mock_response,
        check_call_numbers,
        request_mock,
        make_async_request_with_args,
    ):
        mock_retry(
            retry_error_num=1,
            responses=[mock_response(request_mock, code=202)],
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.anyio
    async def test_retry_error_until_exceeded(
        self, mock_retry, make_async_request_with_args, check_call_numbers
    ):
        mock_retry(retry_error_num=3)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request_with_args()
        check_call_numbers(self.max_retries)

    @pytest.mark.anyio
    async def test_no_retry_error(
        self, mock_retry, make_async_request_with_args, check_call_numbers
    ):
        mock_retry(no_retry_error_num=self.max_retries)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request_with_args()
        check_call_numbers(1)

    @pytest.mark.anyio
    async def test_retry_codes(
        self,
        mock_retry,
        mock_response,
        make_async_request_with_args,
        request_mock,
        check_call_numbers,
    ):
        mock_retry(
            responses=[
                mock_response(request_mock, code=409),
                mock_response(request_mock, code=202),
            ]
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.anyio
    async def test_retry_codes_until_exceeded(
        self,
        mock_retry,
        mock_response,
        make_async_request_with_args,
        request_mock,
        check_call_numbers,
    ):
        mock_retry(
            responses=[mock_response(request_mock, code=409)]
            * (self.max_retries + 1)
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 409
        check_call_numbers(self.max_retries + 1)

    @pytest.fixture
    def connection_error(self, client):
        def _connection_error(given_exception):
            with pytest.raises(stripe.APIConnectionError) as error:
                client._handle_request_error(given_exception)
            return error.value

        return _connection_error

    def test_handle_request_error_should_retry(
        self, connection_error, mock_retry
    ):
        request_mock = mock_retry()

        error = connection_error(request_mock.exceptions.Timeout())
        assert error.should_retry

        error = connection_error(request_mock.exceptions.ConnectionError())
        assert error.should_retry

    # Skip inherited basic client tests
    def test_request(self):
        pass

    def test_request_async(self):
        pass

    def test_timeout(self):
        pass

    def test_timeout_async(self):
        pass


class TestAIOHTTPClient(ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.AIOHTTPClient] = (
        _http_client.AIOHTTPClient
    )
    PROXY = "http://slap/"

    @pytest.fixture
    def mock_response(self, mocker, mocked_request_lib):
        def mock_response(mock, body=None, code=200):
            if body is None:
                body = {}

            class Content:
                def __aiter__(self):
                    async def chunk():
                        yield (
                            bytes(body, "utf-8")
                            if isinstance(body, str)
                            else body
                        )

                    return chunk()

                async def read(self):
                    return body

            class Result:
                def __init__(self):
                    self.content = Content()
                    self.status = code
                    self.headers = {}

            result = Result()

            mocked_request_lib.ClientSession().request = AsyncMock(
                return_value=result
            )
            return result

        return mock_response

    @pytest.fixture
    def mock_error(self, mocker, mocked_request_lib):
        def mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            mocked_request_lib.ClientSession().request.side_effect = (
                mock.exceptions.SSLError()
            )

        return mock_error

    @pytest.fixture
    def check_call(self, mocked_request_lib, mocker):
        def check_call(
            mock,
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
            timeout=80,
            times=None,
        ):
            times = times or 1
            args = (method, url)
            kwargs = {
                "headers": headers,
                "data": post_data or {},
                "timeout": timeout,
                "proxies": {"http": "http://slap/", "https": "http://slap/"},
            }

            if is_streaming:
                kwargs["stream"] = True

            calls = [mocker.call(*args, **kwargs) for _ in range(times)]
            mocked_request_lib.ClientSession().request.assert_has_calls(calls)

        return check_call

    @pytest.fixture
    def check_call_async(self, mocked_request_lib, mocker):
        def check_call_async(
            method,
            url,
            post_data,
            headers,
            is_streaming=False,
            timeout=80,
            times=None,
        ):
            times = times or 1
            args = (method, url)
            kwargs = {
                "headers": headers,
                "data": post_data,
                "timeout": timeout,
                "proxy": "http://slap/",
            }

            calls = [mocker.call(*args, **kwargs) for _ in range(times)]
            mocked_request_lib.ClientSession().request.assert_has_calls(calls)

        return check_call_async

    def test_request(self):
        pass

    def test_request_stream(self):
        pass

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_async(
        self,
        mocked_request_lib,
        mock_response,
        check_call_async,
        make_async_request,
    ):
        mock_response(mocked_request_lib, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = {}

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = {}

            headers = {"my-header": "header val"}
            body, code, _ = await make_async_request(
                method, abs_url, headers, data
            )
            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call_async(method, abs_url, data, headers)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_stream_async(
        self,
        mocked_request_lib,
        mock_response,
        make_async_stream_request,
    ):
        for method in VALID_API_METHODS:
            mock_response(mocked_request_lib, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = await make_async_stream_request(
                method, abs_url, headers, data
            )

            assert code == 200

            # Here we need to convert and align all content on one type (string)
            # as some clients return a string stream others a byte stream.
            body_content = b"".join([x async for x in stream])
            if hasattr(body_content, "decode"):
                body_content = body_content.decode("utf-8")

            assert body_content == "some streamed content"

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_exception(
        self, mocked_request_lib, mock_error, make_async_request
    ):
        mock_error(mocked_request_lib)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request("get", self.valid_url, {}, None)

    def test_timeout(self):
        pass

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_timeout_async(
        self,
        mocked_request_lib,
        mock_response,
        check_call_async,
        make_async_request,
    ):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(mocked_request_lib, '{"foo": "baz"}', 200)
        await make_async_request(
            "POST", self.valid_url, headers, data, client_kwargs={"timeout": 5}
        )

        check_call_async(
            "POST",
            self.valid_url,
            data,
            headers,
            timeout=5,
        )

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_stream_forwards_stream_param(self):
        # TODO
        pass


class TestAIOHTTPClientRetryBehavior(TestAIOHTTPClient):
    responses = None
    _mocked_request_lib = None
    max_retries = 3

    @pytest.fixture
    def mock_retry(self, mocked_request_lib):
        def mock_retry(
            retry_error_num=0, no_retry_error_num=0, responses=None
        ):
            # Store the mocked request lib for use in make_client
            self._mocked_request_lib = mocked_request_lib

            if responses is None:
                responses = []
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            mocked_request_lib.exceptions.RequestException = (
                request_root_error_class
            )

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            mocked_request_lib.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            mocked_request_lib.exceptions.Timeout = retry_parent_class
            mocked_request_lib.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num
            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions

            results = retry_errors + no_retry_errors + responses

            mocked_request_lib.ClientSession().request = AsyncMock(
                side_effect=results
            )
            self.responses = results

            return mocked_request_lib

        return mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call_async):
        valid_url = self.valid_url

        def check_call_numbers(times, is_streaming=False):
            check_call_async(
                "GET",
                valid_url,
                None,
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return check_call_numbers

    @pytest.fixture
    def make_async_request_with_args(self, make_async_request):
        async def _make_async_request():
            return await make_async_request(
                "GET", self.valid_url, {}, None, max_retries=self.max_retries
            )

        return _make_async_request

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_error_until_response(
        self,
        mock_retry,
        mock_response,
        check_call_numbers,
        mocked_request_lib,
        make_async_request_with_args,
    ):
        mock_retry(
            retry_error_num=1,
            responses=[mock_response(mocked_request_lib, code=202)],
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_error_until_exceeded(
        self, mock_retry, check_call_numbers, make_async_request_with_args
    ):
        mock_retry(retry_error_num=self.max_retries)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request_with_args()

        check_call_numbers(self.max_retries)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_no_retry_error(
        self, mock_retry, check_call_numbers, make_async_request_with_args
    ):
        mock_retry(no_retry_error_num=self.max_retries)
        with pytest.raises(stripe.APIConnectionError):
            await make_async_request_with_args()
        check_call_numbers(1)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_codes(
        self,
        mock_retry,
        mock_response,
        mocked_request_lib,
        check_call_numbers,
        make_async_request_with_args,
    ):
        mock_retry(
            responses=[
                mock_response(mocked_request_lib, code=409),
                mock_response(mocked_request_lib, code=202),
            ]
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_codes_until_exceeded(
        self,
        mock_retry,
        mock_response,
        mocked_request_lib,
        check_call_numbers,
        make_async_request_with_args,
    ):
        mock_retry(
            responses=[mock_response(mocked_request_lib, code=409)]
            * (self.max_retries + 1)
        )
        _, code, _ = await make_async_request_with_args()
        assert code == 409
        check_call_numbers(self.max_retries + 1)

    def connection_error(self, client, given_exception):
        with pytest.raises(stripe.APIConnectionError) as error:
            client._handle_request_error(given_exception)
        return error.value

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_handle_request_error_should_retry(
        self, mock_retry, anyio_backend
    ):
        client = self.REQUEST_CLIENT()
        mocked_request_lib = mock_retry()

        error = self.connection_error(
            client, mocked_request_lib.exceptions.Timeout()
        )
        assert error.should_retry

        error = self.connection_error(
            client, mocked_request_lib.exceptions.ConnectionError()
        )
        assert error.should_retry

    # Skip inherited basic client tests
    def test_request(self):
        pass

    def test_request_async(self):
        pass

    def test_timeout(self):
        pass

    def test_timeout_async(self):
        pass


class TestLiveHTTPClients:
    """
    Tests that actually make HTTP requests in order to test functionality (like https)
    end to end.
    """

    @pytest.mark.anyio
    async def test_httpx_request_async_https(self):
        """
        Test to ensure that httpx https calls succeed by making a live test call
        to the public stripe API.
        """
        method = "get"
        abs_url = "https://api.stripe.com/v1/balance"
        data = {}

        client = _http_client.HTTPXClient(verify_ssl_certs=True)
        # the public test secret key, as found on https://docs.stripe.com/keys#obtain-api-keys
        test_api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
        basic_auth = base64.b64encode(
            (test_api_key + ":").encode("utf-8")
        ).decode("utf-8")
        headers = {"Authorization": "Basic " + basic_auth}

        _, code, _ = await client.request_with_retries_async(
            method, abs_url, headers, data
        )
        assert code >= 200 and code < 400
