import base64
from typing import Any, List
from typing_extensions import Type
from unittest.mock import call
import pytest
import json
import sys

if sys.version_info >= (3, 8):
    from unittest.mock import AsyncMock
else:
    from mock import AsyncMock

import stripe
from stripe import _http_client
from stripe._encode import _api_encode
from stripe import APIConnectionError
import urllib3
from stripe import _util

VALID_API_METHODS = ("get", "post", "delete")


class StripeClientTestCase(object):
    REQUEST_LIBRARIES = [
        ("urlfetch", "stripe._http_client.urlfetch"),
        ("requests", "stripe._http_client.requests"),
        ("pycurl", "stripe._http_client.pycurl"),
        ("urllib.request", "stripe._http_client.urllibrequest"),
        ("httpx", "stripe._http_client.httpx"),
        ("aiohttp", "stripe._http_client.aiohttp"),
    ]

    @pytest.fixture
    def request_mocks(self, mocker):
        request_mocks = {}
        for lib, mockpath in self.REQUEST_LIBRARIES:
            request_mocks[lib] = mocker.patch(mockpath)
        return request_mocks


class TestNewDefaultHttpClient(StripeClientTestCase):
    def check_default(self, none_libs, expected):
        for lib in none_libs:
            setattr(_http_client, lib, None)

        inst = _http_client.new_default_http_client()

        assert isinstance(inst, expected)

    def test_new_default_http_client_urlfetch(self, request_mocks):
        self.check_default((), _http_client.UrlFetchClient)

    def test_new_default_http_client_requests(self, request_mocks):
        self.check_default(("urlfetch",), _http_client.RequestsClient)

    def test_new_default_http_client_pycurl(self, request_mocks):
        self.check_default(("urlfetch", "requests"), _http_client.PycurlClient)

    def test_new_default_http_client_urllib2(self, request_mocks):
        self.check_default(
            ("urlfetch", "requests", "pycurl"),
            _http_client.Urllib2Client,
        )


class TestNewHttpClientAsyncFallback(StripeClientTestCase):
    def check_default(self, none_libs, expected):
        for lib in none_libs:
            setattr(_http_client, lib, None)

        inst = _http_client.new_http_client_async_fallback()

        assert isinstance(inst, expected)

    def test_new_http_client_async_fallback_httpx(self, request_mocks):
        self.check_default((), _http_client.HTTPXClient)

    def test_new_http_client_async_fallback_aiohttp(self, request_mocks):
        self.check_default(
            (("httpx"),),
            _http_client.AIOHTTPClient,
        )

    def test_new_http_client_async_fallback_no_import_found(
        self, request_mocks
    ):
        self.check_default(
            (
                ("httpx"),
                ("aiohttp"),
            ),
            _http_client.NoImportFoundAsyncClient,
        )


class TestRetrySleepTimeDefaultHttpClient(StripeClientTestCase):
    from contextlib import contextmanager

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


class TestRetryConditionsDefaultHttpClient(StripeClientTestCase):
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
        api_connection_error = mocker.Mock()

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
        api_connection_error = mocker.Mock()
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


class TestHTTPClient(object):
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


class ClientTestBase(object):
    REQUEST_CLIENT: Type[_http_client.HTTPClient]

    @pytest.fixture
    def request_mock(self, request_mocks):
        return request_mocks[self.REQUEST_CLIENT.name]

    @property
    def valid_url(self, path="/foo"):
        return "https://api.stripe.com%s" % (path,)

    def make_request(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return client.request_with_retries(method, url, headers, post_data)

    def make_request_stream(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return client.request_stream_with_retries(
            method, url, headers, post_data
        )

    def make_request_async(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return client.request_with_retries_async(
            method, url, headers, post_data
        )

    async def make_request_stream_async(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return await client.request_stream_with_retries_async(
            method, url, headers, post_data
        )

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

    def test_request(self, request_mock, mock_response, check_call):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            body, code, _ = self.make_request(method, abs_url, headers, data)

            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call(request_mock, method, abs_url, data, headers)

    def test_request_stream(
        self, mocker, request_mock, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response(request_mock, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = self.make_request_stream(
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

            mocker.resetall()

    def test_exception(self, request_mock, mock_error):
        mock_error(request_mock)
        with pytest.raises(APIConnectionError):
            self.make_request("get", self.valid_url, {}, None)


class RequestsVerify(object):
    def __eq__(self, other):
        return other and other.endswith("stripe/data/ca-certificates.crt")


class TestRequestsClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.RequestsClient] = (
        _http_client.RequestsClient
    )

    @pytest.fixture
    def session(self, mocker, request_mocks):
        return mocker.MagicMock()

    @pytest.fixture
    def mock_response(self, mocker, session):
        def mock_response(mock, body, code):
            result = mocker.Mock()
            result.content = body
            result.status_code = code
            result.headers = {}
            result.raw = urllib3.response.HTTPResponse(
                body=_util.io.BytesIO(str.encode(body)),
                preload_content=False,
                status=code,
            )

            session.request = mocker.MagicMock(return_value=result)
            mock.Session = mocker.MagicMock(return_value=session)

        return mock_response

    @pytest.fixture
    def mock_error(self, mocker, session):
        def mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            session.request.side_effect = mock.exceptions.SSLError()
            mock.Session = mocker.MagicMock(return_value=session)

        return mock_error

    # Note that unlike other modules, we don't use the "mock" argument here
    # because we need to run the request call against the internal mock
    # session.
    @pytest.fixture
    def check_call(self, session):
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

        return check_call

    def make_request(self, method, url, headers, post_data, timeout=80):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, timeout=timeout, proxy="http://slap/"
        )
        return client.request_with_retries(method, url, headers, post_data)

    def make_request_stream(self, method, url, headers, post_data, timeout=80):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, timeout=timeout, proxy="http://slap/"
        )
        return client.request_stream_with_retries(
            method, url, headers, post_data
        )

    def test_timeout(self, request_mock, mock_response, check_call):
        headers = {"my-header": "header val"}
        data = ""
        mock_response(request_mock, '{"foo": "baz"}', 200)
        self.make_request("POST", self.valid_url, headers, data, timeout=5)

        check_call(None, "POST", self.valid_url, data, headers, timeout=5)

    def test_request_stream_forwards_stream_param(
        self, mocker, request_mock, mock_response, check_call
    ):
        mock_response(request_mock, "some streamed content", 200)
        self.make_request_stream("GET", self.valid_url, {}, None)

        check_call(
            None,
            "GET",
            self.valid_url,
            None,
            {},
            is_streaming=True,
        )


class TestRequestClientRetryBehavior(TestRequestsClient):
    @pytest.fixture
    def response(self, mocker):
        def response(code=200, headers={}):
            result = mocker.Mock()
            result.content = "{}"
            result.status_code = code
            result.headers = headers
            result.raw = urllib3.response.HTTPResponse(
                body=_util.io.BytesIO(str.encode(result.content)),
                preload_content=False,
                status=code,
            )

            return result

        return response

    @pytest.fixture
    def mock_retry(self, mocker, session, request_mock):
        def mock_retry(retry_error_num=0, no_retry_error_num=0, responses=[]):
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            request_mock.exceptions.RequestException = request_root_error_class

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            request_mock.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            request_mock.exceptions.Timeout = retry_parent_class
            request_mock.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num

            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions
            session.request.side_effect = (
                retry_errors + no_retry_errors + responses
            )

            request_mock.Session = mocker.MagicMock(return_value=session)
            return request_mock

        return mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call):
        valid_url = self.valid_url

        def check_call_numbers(times, is_streaming=False):
            check_call(
                None,
                "GET",
                valid_url,
                None,
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return check_call_numbers

    def max_retries(self):
        return 3

    def make_client(self):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, timeout=80, proxy="http://slap/"
        )
        # Override sleep time to speed up tests
        client._sleep_time_seconds = lambda num_retries, response=None: 0.0001
        # Override configured max retries
        return client

    def make_request(self, *args, **kwargs):
        client = self.make_client()
        return client.request_with_retries(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    def make_request_stream(self, *args, **kwargs):
        client = self.make_client()
        return client.request_stream_with_retries(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    def test_retry_error_until_response(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(retry_error_num=1, responses=[response(code=202)])
        _, code, _ = self.make_request()
        assert code == 202
        check_call_numbers(2)

    def test_retry_error_until_exceeded(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(retry_error_num=self.max_retries())
        with pytest.raises(APIConnectionError):
            self.make_request()

        check_call_numbers(self.max_retries())

    def test_no_retry_error(self, mock_retry, response, check_call_numbers):
        mock_retry(no_retry_error_num=self.max_retries())
        with pytest.raises(APIConnectionError):
            self.make_request()
        check_call_numbers(1)

    def test_retry_codes(self, mock_retry, response, check_call_numbers):
        mock_retry(responses=[response(code=409), response(code=202)])
        _, code, _ = self.make_request()
        assert code == 202
        check_call_numbers(2)

    def test_retry_codes_until_exceeded(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(responses=[response(code=409)] * (self.max_retries() + 1))
        _, code, _ = self.make_request()
        assert code == 409
        check_call_numbers(self.max_retries() + 1)

    def test_retry_request_stream_error_until_response(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(retry_error_num=1, responses=[response(code=202)])
        _, code, _ = self.make_request_stream()
        assert code == 202
        check_call_numbers(2, is_streaming=True)

    def test_retry_request_stream_error_until_exceeded(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(retry_error_num=self.max_retries())
        with pytest.raises(APIConnectionError):
            self.make_request_stream()

        check_call_numbers(self.max_retries(), is_streaming=True)

    def test_no_retry_request_stream_error(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(no_retry_error_num=self.max_retries())
        with pytest.raises(APIConnectionError):
            self.make_request_stream()
        check_call_numbers(1, is_streaming=True)

    def test_retry_request_stream_codes(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(responses=[response(code=409), response(code=202)])
        _, code, _ = self.make_request_stream()
        assert code == 202
        check_call_numbers(2, is_streaming=True)

    def test_retry_request_stream_codes_until_exceeded(
        self, mock_retry, response, check_call_numbers
    ):
        mock_retry(responses=[response(code=409)] * (self.max_retries() + 1))
        _, code, _ = self.make_request_stream()
        assert code == 409
        check_call_numbers(self.max_retries() + 1, is_streaming=True)

    @pytest.fixture
    def connection_error(self, session):
        client = self.REQUEST_CLIENT()

        def connection_error(given_exception):
            with pytest.raises(APIConnectionError) as error:
                client._handle_request_error(given_exception)
            return error.value

        return connection_error

    def test_handle_request_error_should_retry(
        self, connection_error, mock_retry
    ):
        request_mock = mock_retry()

        error = connection_error(request_mock.exceptions.Timeout())
        assert error.should_retry

        error = connection_error(request_mock.exceptions.ConnectionError())
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
    def test_request(self, request_mock, mock_response, check_call):
        pass

    def test_exception(self, request_mock, mock_error):
        pass

    def test_timeout(self, request_mock, mock_response, check_call):
        pass


class TestUrlFetchClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT = _http_client.UrlFetchClient

    @pytest.fixture
    def mock_response(self, mocker):
        def mock_response(mock, body, code):
            result = mocker.Mock()
            result.content = body
            result.status_code = code
            result.headers = {}

            mock.fetch = mocker.Mock(return_value=result)
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


class TestUrllib2Client(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.Urllib2Client] = (
        _http_client.Urllib2Client
    )

    request_object: Any

    def make_client(self, proxy):
        self.client = self.REQUEST_CLIENT(verify_ssl_certs=True, proxy=proxy)
        self.proxy = proxy

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.make_client(proxy)
        return self.client.request_with_retries(
            method, url, headers, post_data
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        self.make_client(proxy)
        return self.client.request_stream_with_retries(
            method, url, headers, post_data
        )

    @pytest.fixture
    def mock_response(self, mocker):
        def mock_response(mock, body, code):
            response = mocker.Mock()
            response.read = mocker.MagicMock(return_value=body)
            response.code = code
            response.info = mocker.Mock(return_value={})

            self.request_object = mocker.Mock()
            mock.Request = mocker.Mock(return_value=self.request_object)

            mock.urlopen = mocker.Mock(return_value=response)

            opener = mocker.Mock()
            opener.open = mocker.Mock(return_value=response)
            mock.build_opener = mocker.Mock(return_value=opener)
            mock.build_opener.open = opener.open
            mock.ProxyHandler = mocker.Mock(return_value=opener)

            mock.urlopen = mocker.Mock(return_value=response)

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            mock.urlopen.side_effect = ValueError
            mock.build_opener().open.side_effect = ValueError
            mock.build_opener.reset_mock()

        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(
            mock, method, url, post_data, headers, is_streaming=False
        ):
            if isinstance(post_data, str):
                post_data = post_data.encode("utf-8")

            mock.Request.assert_called_with(url, post_data, headers)

            if self.client._proxy:
                assert isinstance(self.client._proxy, dict)
                mock.ProxyHandler.assert_called_with(self.client._proxy)
                mock.build_opener.open.assert_called_with(self.request_object)
                assert not mock.urlopen.called

            if not self.client._proxy:
                mock.urlopen.assert_called_with(self.request_object)
                assert not mock.build_opener.called
                assert not mock.build_opener.open.called

        return check_call


class TestUrllib2ClientHttpsProxy(TestUrllib2Client):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestUrllib2ClientHttpsProxy, self).make_request(
            method,
            url,
            headers,
            post_data,
            {"http": "http://slap/", "https": "http://slap/"},
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        return super(TestUrllib2ClientHttpsProxy, self).make_request_stream(
            method,
            url,
            headers,
            post_data,
            {"http": "http://slap/", "https": "http://slap/"},
        )


class TestUrllib2ClientHttpProxy(TestUrllib2Client):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestUrllib2ClientHttpProxy, self).make_request(
            method, url, headers, post_data, "http://slap/"
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        return super(TestUrllib2ClientHttpProxy, self).make_request_stream(
            method, url, headers, post_data, "http://slap/"
        )


class TestPycurlClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.PycurlClient] = _http_client.PycurlClient

    def make_client(self, proxy):
        self.client = self.REQUEST_CLIENT(verify_ssl_certs=True, proxy=proxy)
        self.proxy = proxy

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.make_client(proxy)
        return self.client.request_with_retries(
            method, url, headers, post_data
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        self.make_client(proxy)
        return self.client.request_stream_with_retries(
            method, url, headers, post_data
        )

    @pytest.fixture
    def curl_mock(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def request_mock(self, mocker, request_mocks, curl_mock):
        lib_mock = request_mocks[self.REQUEST_CLIENT.name]
        lib_mock.Curl = mocker.Mock(return_value=curl_mock)
        return curl_mock

    @pytest.fixture
    def bio_mock(self, mocker):
        bio_patcher = mocker.patch("stripe.util.io.BytesIO")
        bio_mock = mocker.Mock()
        bio_patcher.return_value = bio_mock
        return bio_mock

    @pytest.fixture
    def mock_response(self, mocker, bio_mock):
        def mock_response(mock, body, code):
            bio_mock.getvalue = mocker.MagicMock(
                return_value=body.encode("utf-8")
            )
            bio_mock.read = mocker.MagicMock(return_value=body.encode("utf-8"))
            mock.getinfo.return_value = code

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            class FakeException(BaseException):
                @property
                def args(self):
                    return ("foo", "bar")

            _http_client.pycurl.error = FakeException
            mock.perform.side_effect = _http_client.pycurl.error

        return mock_error

    @pytest.fixture
    def check_call(self, request_mocks):
        def check_call(
            mock, method, url, post_data, headers, is_streaming=False
        ):
            lib_mock = request_mocks[self.REQUEST_CLIENT.name]

            if self.client._proxy:
                proxy = self.client._get_proxy(url)
                assert proxy is not None
                if proxy.hostname:
                    mock.setopt.assert_any_call(lib_mock.PROXY, proxy.hostname)
                if proxy.port:
                    mock.setopt.assert_any_call(lib_mock.PROXYPORT, proxy.port)
                if proxy.username or proxy.password:
                    mock.setopt.assert_any_call(
                        lib_mock.PROXYUSERPWD,
                        "%s:%s" % (proxy.username, proxy.password),
                    )

            # A note on methodology here: we don't necessarily need to verify
            # _every_ call to setopt, but check a few of them to make sure the
            # right thing is happening. Keep an eye specifically on conditional
            # statements where things are more likely to go wrong.

            mock.setopt.assert_any_call(lib_mock.NOSIGNAL, 1)
            mock.setopt.assert_any_call(lib_mock.URL, url)

            if method == "get":
                mock.setopt.assert_any_call(lib_mock.HTTPGET, 1)
            elif method == "post":
                mock.setopt.assert_any_call(lib_mock.POST, 1)
            else:
                mock.setopt.assert_any_call(
                    lib_mock.CUSTOMREQUEST, method.upper()
                )

            mock.perform.assert_any_call()

        return check_call


class TestPycurlClientHttpProxy(TestPycurlClient):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpProxy, self).make_request(
            method,
            url,
            headers,
            post_data,
            "http://user:withPwd@slap:8888/",
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpProxy, self).make_request_stream(
            method,
            url,
            headers,
            post_data,
            "http://user:withPwd@slap:8888/",
        )


class TestPycurlClientHttpsProxy(TestPycurlClient):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpsProxy, self).make_request(
            method,
            url,
            headers,
            post_data,
            {"http": "http://slap:8888/", "https": "http://slap2:444/"},
        )

    def make_request_stream(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpsProxy, self).make_request_stream(
            method,
            url,
            headers,
            post_data,
            {"http": "http://slap:8888/", "https": "http://slap2:444/"},
        )


class TestAPIEncode(StripeClientTestCase):
    def test_encode_dict(self):
        body = {"foo": {"dob": {"month": 1}, "name": "bat"}}

        values = [t for t in _api_encode(body, "V1")]

        assert ("foo[dob][month]", 1) in values
        assert ("foo[name]", "bat") in values

    def test_encode_array(self):
        body = {"foo": [{"dob": {"month": 1}, "name": "bat"}]}

        values = [t for t in _api_encode(body, "V1")]

        assert ("foo[0][dob][month]", 1) in values
        assert ("foo[0][name]", "bat") in values

    def test_encode_v2_array(self):
        body = {"foo": [{"dob": {"month": 1}, "name": "bat"}]}

        values = [t for t in _api_encode(body, "V2")]

        assert ("foo[dob][month]", 1) in values
        assert ("foo[name]", "bat") in values


class TestHTTPXClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.HTTPXClient] = _http_client.HTTPXClient

    @pytest.fixture
    def mock_response(self, mocker, request_mock):
        def mock_response(mock, body={}, code=200):
            result = mocker.Mock()
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

            request_mock.Client().send = mocker.Mock(return_value=result)
            request_mock.Client().request = mocker.Mock(return_value=result)
            request_mock.AsyncClient().send = async_mock_stream
            request_mock.AsyncClient().request = async_mock
            return result

        return mock_response

    @pytest.fixture
    def mock_error(self, mocker, request_mock):
        def mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            request_mock.AsyncClient().request.side_effect = (
                mock.exceptions.SSLError()
            )

        return mock_error

    @pytest.fixture
    def check_call(self, request_mock, mocker):
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
            request_mock.Client().request.assert_has_calls(calls)

        return check_call

    @pytest.fixture
    def check_call_async(self, request_mock, mocker):
        def check_call_async(
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

        return check_call_async

    def make_request(self, method, url, headers, post_data, timeout=80):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True,
            proxy="http://slap/",
            timeout=timeout,
            allow_sync_methods=True,
        )
        return client.request_with_retries(method, url, headers, post_data)

    def make_request_stream(self, method, url, headers, post_data, timeout=80):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True,
            proxy="http://slap/",
            timeout=timeout,
            allow_sync_methods=True,
        )
        return client.request_stream_with_retries(
            method, url, headers, post_data
        )

    async def make_request_async(
        self, method, url, headers, post_data, timeout=80
    ):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, proxy="http://slap/", timeout=timeout
        )
        return await client.request_with_retries_async(
            method, url, headers, post_data
        )

    async def make_request_stream_async(
        self, method, url, headers, post_data, timeout=80
    ):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, proxy="http://slap/"
        )
        return await client.request_stream_with_retries_async(
            method, url, headers, post_data
        )

    @pytest.mark.anyio
    async def test_request_async(
        self, request_mock, mock_response, check_call_async
    ):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = {}

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = {}

            headers = {"my-header": "header val"}
            body, code, _ = await self.make_request_async(
                method, abs_url, headers, data
            )
            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call_async(request_mock, method, abs_url, data, headers)

    @pytest.mark.anyio
    async def test_request_stream_async(
        self, mocker, request_mock, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response(request_mock, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = await self.make_request_stream_async(
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
    async def test_exception(self, request_mock, mock_error):
        mock_error(request_mock)
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async("get", self.valid_url, {}, None)

    @pytest.mark.anyio
    def test_timeout(self, request_mock, mock_response, check_call):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(request_mock, '{"foo": "baz"}', 200)
        self.make_request("POST", self.valid_url, headers, data, timeout=5)

        check_call(
            request_mock, "POST", self.valid_url, data, headers, timeout=5
        )

    @pytest.mark.anyio
    async def test_timeout_async(
        self, request_mock, mock_response, check_call_async
    ):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(request_mock, '{"foo": "baz"}', 200)
        await self.make_request_async(
            "POST", self.valid_url, headers, data, timeout=5
        )

        check_call_async(
            request_mock, "POST", self.valid_url, data, headers, timeout=5
        )

    @pytest.mark.anyio
    async def test_request_stream_forwards_stream_param(
        self, mocker, request_mock, mock_response, check_call
    ):
        # TODO
        pass

    def test_allow_sync_methods(self, request_mock, mock_response):
        client = self.REQUEST_CLIENT()
        assert client._client is None
        with pytest.raises(RuntimeError):
            client.request("GET", "http://foo", {})
        with pytest.raises(RuntimeError):
            client.request_stream("GET", "http://foo", {})
        client = self.REQUEST_CLIENT(allow_sync_methods=True)
        assert client._client is not None
        mock_response(request_mock, '{"foo": "baz"}', 200)
        client.request("GET", "http://foo", {})
        mock_response(request_mock, '{"foo": "baz"}', 200)
        client.request_stream("GET", "http://foo", {})


class TestHTTPXClientRetryBehavior(TestHTTPXClient):
    responses = None

    @pytest.fixture
    def mock_retry(self, mocker, request_mock):
        def mock_retry(
            retry_error_num=0, no_retry_error_num=0, responses=None
        ):
            if responses is None:
                responses = []
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            request_mock.exceptions.RequestException = request_root_error_class

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            request_mock.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            request_mock.exceptions.Timeout = retry_parent_class
            request_mock.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num
            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions

            results = retry_errors + no_retry_errors + responses

            request_mock.AsyncClient().request = AsyncMock(side_effect=results)
            self.responses = results

            return request_mock

        return mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call_async):
        valid_url = self.valid_url

        def check_call_numbers(times, is_streaming=False):
            check_call_async(
                None,
                "GET",
                valid_url,
                {},
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return check_call_numbers

    def max_retries(self):
        return 3

    def make_client(self, **kwargs):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, timeout=80, proxy="http://slap/", **kwargs
        )
        # Override sleep time to speed up tests
        client._sleep_time_seconds = lambda num_retries, response=None: 0.0001
        # Override configured max retries
        return client

    def make_request(self, *args, **kwargs):
        client = self.make_client(allow_sync_methods=True)
        return client.request_with_retries(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    def make_request_stream(self, *args, **kwargs):
        client = self.make_client(allow_sync_methods=True)
        return client.request_stream_with_retries(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    async def make_request_async(self, *args, **kwargs):
        client = self.make_client()
        return await client.request_with_retries_async(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    async def make_request_stream_async(self, *args, **kwargs):
        client = self.make_client()
        return await client.request_stream_with_retries_async(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    @pytest.mark.anyio
    async def test_retry_error_until_response(
        self,
        mock_retry,
        mock_response,
        check_call_numbers,
        request_mock,
        mocker,
    ):
        mock_retry(
            retry_error_num=1,
            responses=[mock_response(request_mock, code=202)],
        )
        _, code, _ = await self.make_request_async()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.anyio
    async def test_retry_error_until_exceeded(
        self, mock_retry, mock_response, check_call_numbers
    ):
        mock_retry(retry_error_num=self.max_retries())
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async()

        check_call_numbers(self.max_retries())

    @pytest.mark.anyio
    async def test_no_retry_error(
        self, mock_retry, mock_response, check_call_numbers
    ):
        mock_retry(no_retry_error_num=self.max_retries())
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async()
        check_call_numbers(1)

    @pytest.mark.anyio
    async def test_retry_codes(
        self, mock_retry, mock_response, request_mock, check_call_numbers
    ):
        mock_retry(
            responses=[
                mock_response(request_mock, code=409),
                mock_response(request_mock, code=202),
            ]
        )
        _, code, _ = await self.make_request_async()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.anyio
    async def test_retry_codes_until_exceeded(
        self, mock_retry, mock_response, request_mock, check_call_numbers
    ):
        mock_retry(
            responses=[mock_response(request_mock, code=409)]
            * (self.max_retries() + 1)
        )
        _, code, _ = await self.make_request_async()
        assert code == 409
        check_call_numbers(self.max_retries() + 1)

    @pytest.fixture
    def connection_error(self):
        client = self.REQUEST_CLIENT()

        def connection_error(given_exception):
            with pytest.raises(stripe.APIConnectionError) as error:
                client._handle_request_error(given_exception)
            return error.value

        return connection_error

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


class TestAIOHTTPClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT: Type[_http_client.AIOHTTPClient] = (
        _http_client.AIOHTTPClient
    )

    @pytest.fixture
    def mock_response(self, mocker, request_mock):
        def mock_response(mock, body={}, code=200):
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

            request_mock.ClientSession().request = AsyncMock(
                return_value=result
            )
            return result

        return mock_response

    @pytest.fixture
    def mock_error(self, mocker, request_mock):
        def mock_error(mock):
            # The first kind of request exceptions we catch
            mock.exceptions.SSLError = Exception
            request_mock.ClientSession().request.side_effect = (
                mock.exceptions.SSLError()
            )

        return mock_error

    @pytest.fixture
    def check_call(self, request_mock, mocker):
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
            request_mock.ClientSession().request.assert_has_calls(calls)

        return check_call

    @pytest.fixture
    def check_call_async(self, request_mock, mocker):
        def check_call_async(
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
                "proxy": "http://slap/",
            }

            calls = [mocker.call(*args, **kwargs) for _ in range(times)]
            request_mock.ClientSession().request.assert_has_calls(calls)

        return check_call_async

    def make_request(self, method, url, headers, post_data, timeout=80):
        pass

    async def make_request_async(
        self, method, url, headers, post_data, timeout=80
    ):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, proxy="http://slap/", timeout=timeout
        )
        return await client.request_with_retries_async(
            method, url, headers, post_data
        )

    async def make_request_stream_async(
        self, method, url, headers, post_data, timeout=80
    ):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, proxy="http://slap/"
        )
        return await client.request_stream_with_retries_async(
            method, url, headers, post_data
        )

    def test_request(self):
        pass

    def test_request_stream(self):
        pass

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_async(
        self, request_mock, mock_response, check_call_async
    ):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = {}

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = {}

            headers = {"my-header": "header val"}
            body, code, _ = await self.make_request_async(
                method, abs_url, headers, data
            )
            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call_async(request_mock, method, abs_url, data, headers)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_stream_async(
        self, mocker, request_mock, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response(request_mock, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            stream, code, _ = await self.make_request_stream_async(
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

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_exception(self, request_mock, mock_error):
        mock_error(request_mock)
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async("get", self.valid_url, {}, None)

    def test_timeout(
        self, request_mock, mock_response, check_call, anyio_backend
    ):
        pass

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_timeout_async(
        self, request_mock, mock_response, check_call_async
    ):
        headers = {"my-header": "header val"}
        data = {}
        mock_response(request_mock, '{"foo": "baz"}', 200)
        await self.make_request_async(
            "POST", self.valid_url, headers, data, timeout=5
        )

        check_call_async(
            request_mock, "POST", self.valid_url, data, headers, timeout=5
        )

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_request_stream_forwards_stream_param(
        self, mocker, request_mock, mock_response, check_call
    ):
        # TODO
        pass


class TestAIOHTTPClientRetryBehavior(TestAIOHTTPClient):
    responses = None

    @pytest.fixture
    def mock_retry(self, mocker, request_mock):
        def mock_retry(
            retry_error_num=0, no_retry_error_num=0, responses=None
        ):
            if responses is None:
                responses = []
            # Mocking classes of exception we catch. Any group of exceptions
            # with the same inheritance pattern will work
            request_root_error_class = Exception
            request_mock.exceptions.RequestException = request_root_error_class

            no_retry_parent_class = LookupError
            no_retry_child_class = KeyError
            request_mock.exceptions.SSLError = no_retry_parent_class
            no_retry_errors = [no_retry_child_class()] * no_retry_error_num

            retry_parent_class = EnvironmentError
            retry_child_class = IOError
            request_mock.exceptions.Timeout = retry_parent_class
            request_mock.exceptions.ConnectionError = retry_parent_class
            retry_errors = [retry_child_class()] * retry_error_num
            # Include mock responses as possible side-effects
            # to simulate returning proper results after some exceptions

            results = retry_errors + no_retry_errors + responses

            request_mock.ClientSession().request = AsyncMock(
                side_effect=results
            )
            self.responses = results

            return request_mock

        return mock_retry

    @pytest.fixture
    def check_call_numbers(self, check_call_async):
        valid_url = self.valid_url

        def check_call_numbers(times, is_streaming=False):
            check_call_async(
                None,
                "GET",
                valid_url,
                None,
                {},
                times=times,
                is_streaming=is_streaming,
            )

        return check_call_numbers

    def max_retries(self):
        return 3

    def make_client(self):
        client = self.REQUEST_CLIENT(
            verify_ssl_certs=True, timeout=80, proxy="http://slap/"
        )
        # Override sleep time to speed up tests
        client._sleep_time_seconds = lambda num_retries, response=None: 0.0001
        # Override configured max retries
        return client

    def make_request(self, *args, **kwargs):
        pass

    def make_request_stream(self, *args, **kwargs):
        pass

    async def make_request_async(self, *args, **kwargs):
        client = self.make_client()
        return await client.request_with_retries_async(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    async def make_request_stream_async(self, *args, **kwargs):
        client = self.make_client()
        return await client.request_stream_with_retries_async(
            "GET", self.valid_url, {}, None, self.max_retries()
        )

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_error_until_response(
        self,
        mock_retry,
        mock_response,
        check_call_numbers,
        request_mock,
        mocker,
    ):
        mock_retry(
            retry_error_num=1,
            responses=[mock_response(request_mock, code=202)],
        )
        _, code, _ = await self.make_request_async()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_error_until_exceeded(
        self, mock_retry, mock_response, check_call_numbers
    ):
        mock_retry(retry_error_num=self.max_retries())
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async()

        check_call_numbers(self.max_retries())

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_no_retry_error(
        self, mock_retry, mock_response, check_call_numbers
    ):
        mock_retry(no_retry_error_num=self.max_retries())
        with pytest.raises(stripe.APIConnectionError):
            await self.make_request_async()
        check_call_numbers(1)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_codes(
        self, mock_retry, mock_response, request_mock, check_call_numbers
    ):
        mock_retry(
            responses=[
                mock_response(request_mock, code=409),
                mock_response(request_mock, code=202),
            ]
        )
        _, code, _ = await self.make_request_async()
        assert code == 202
        check_call_numbers(2)

    @pytest.mark.parametrize("anyio_backend", ["asyncio"])
    @pytest.mark.anyio
    async def test_retry_codes_until_exceeded(
        self, mock_retry, mock_response, request_mock, check_call_numbers
    ):
        mock_retry(
            responses=[mock_response(request_mock, code=409)]
            * (self.max_retries() + 1)
        )
        _, code, _ = await self.make_request_async()
        assert code == 409
        check_call_numbers(self.max_retries() + 1)

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
        request_mock = mock_retry()

        error = self.connection_error(
            client, request_mock.exceptions.Timeout()
        )
        assert error.should_retry

        error = self.connection_error(
            client, request_mock.exceptions.ConnectionError()
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
