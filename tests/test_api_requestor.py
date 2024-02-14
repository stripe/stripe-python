import datetime
import json
import tempfile
import uuid
from collections import OrderedDict

import pytest

import stripe
from stripe import util
from stripe._encode import _json_encode_date_callback
from stripe._stripe_response import (
    StripeStreamResponse,
    StripeStreamResponseAsync,
)
from stripe._api_requestor import _APIRequestor, _api_encode
from stripe._stripe_object import StripeObject
from stripe._requestor_options import (
    _GlobalRequestorOptions,
)
from stripe._request_options import RequestOptions

from urllib.parse import urlencode, urlsplit

import urllib3

VALID_API_METHODS = ("get", "post", "delete")


class GMT1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Europe/Prague"


class AnyUUID4Matcher(object):
    def __eq__(self, other):
        try:
            uuid.UUID(other, version=4)
        except ValueError:
            return False
        return True

    def __repr__(self):
        return "AnyUUID4Matcher()"


class TestAPIRequestor(object):
    ENCODE_INPUTS = {
        "dict": {
            "astring": "bar",
            "anint": 5,
            "anull": None,
            "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            "atuple": (1, 2),
            "adict": {"foo": "bar", "boz": 5},
            "alist": ["foo", "bar"],
        },
        "list": [1, "foo", "baz"],
        "string": "boo",
        "unicode": "\u1234",
        "datetime": datetime.datetime(2013, 1, 1, second=1, tzinfo=GMT1()),
        "none": None,
    }

    ENCODE_EXPECTATIONS = {
        "dict": [
            ("%s[astring]", "bar"),
            ("%s[anint]", 5),
            ("%s[adatetime]", 1356994800),
            ("%s[adict][foo]", "bar"),
            ("%s[adict][boz]", 5),
            ("%s[alist][0]", "foo"),
            ("%s[alist][1]", "bar"),
            ("%s[atuple][0]", 1),
            ("%s[atuple][1]", 2),
        ],
        "list": [("%s[0]", 1), ("%s[1]", "foo"), ("%s[2]", "baz")],
        "string": [("%s", "boo")],
        "unicode": [("%s", "\u1234")],
        "datetime": [("%s", 1356994801)],
        "none": [],
    }

    @pytest.fixture(autouse=True)
    def setup_stripe(self):
        orig_attrs = {
            "api_key": stripe.api_key,
            "api_version": stripe.api_version,
            "default_http_client": stripe.default_http_client,
            "enable_telemetry": stripe.enable_telemetry,
        }
        stripe.api_key = "sk_test_123"
        stripe.api_version = "2017-12-14"
        stripe.default_http_client = None
        stripe.enable_telemetry = False
        yield
        stripe.api_key = orig_attrs["api_key"]
        stripe.api_version = orig_attrs["api_version"]
        stripe.default_http_client = orig_attrs["default_http_client"]
        stripe.enable_telemetry = orig_attrs["enable_telemetry"]

    @pytest.fixture
    def requestor(self, http_client_mock):
        requestor = _APIRequestor(
            client=http_client_mock.get_mock_http_client(),
            options=_GlobalRequestorOptions(),
        )
        return requestor

    @pytest.fixture
    def requestor_streaming(self, http_client_mock_streaming):
        requestor_streaming = _APIRequestor(
            client=http_client_mock_streaming.get_mock_http_client(),
            options=_GlobalRequestorOptions(),
        )
        return requestor_streaming

    @property
    def valid_path(self):
        return "/foo"

    def encoder_check(self, key):
        stk_key = "my%s" % (key,)

        value = self.ENCODE_INPUTS[key]
        expectation = [
            (k % (stk_key,), v) for k, v in self.ENCODE_EXPECTATIONS[key]
        ]

        stk = []
        fn = getattr(_APIRequestor, "encode_%s" % (key,))
        fn(stk, stk_key, value)

        if isinstance(value, dict):
            expectation.sort()
            stk.sort()

        assert stk == expectation, stk

    def _test_encode_naive_datetime(self):
        stk = []

        _APIRequestor.encode_datetime(
            stk, "test", datetime.datetime(2013, 1, 1)
        )

        # Naive datetimes will encode differently depending on your system
        # local time.  Since we don't know the local time of your system,
        # we just check that naive encodings are within 24 hours of correct.
        assert abs(stk[0][1] - 1356994800) <= 60 * 60 * 24

    def test_param_encoding(self, requestor, http_client_mock):
        expectation = []
        for type_, values in iter(self.ENCODE_EXPECTATIONS.items()):
            expectation.extend([(k % (type_,), str(v)) for k, v in values])

        query_string = (
            urlencode(expectation).replace("%5B", "[").replace("%5D", "]")
        )
        http_client_mock.stub_request(
            "get", query_string=query_string, rbody="{}", rcode=200
        )

        requestor.request(
            "get", "", self.ENCODE_INPUTS, base_address="api", api_mode="V1"
        )

        http_client_mock.assert_requested("get", query_string=query_string)

    def test_param_api_mode_preview(self, requestor, http_client_mock):
        http_client_mock.stub_request("post", path=self.valid_path)

        requestor.request(
            "post",
            self.valid_path,
            self.ENCODE_INPUTS,
            base_address="api",
            api_mode="preview",
        )

        expectation = json.dumps(
            self.ENCODE_INPUTS, default=_json_encode_date_callback
        )

        http_client_mock.assert_requested(
            "post",
            content_type="application/json",
            post_data=expectation,
            is_json=True,
        )

    def test_dictionary_list_encoding(self):
        params = {"foo": {"0": {"bar": "bat"}}}
        encoded = list(_api_encode(params))
        key, value = encoded[0]

        assert key == "foo[0][bar]"
        assert value == "bat"

    def test_ordereddict_encoding(self):
        params = {
            "ordered": OrderedDict(
                [
                    ("one", 1),
                    ("two", 2),
                    ("three", 3),
                    ("nested", OrderedDict([("a", "a"), ("b", "b")])),
                ]
            )
        }
        encoded = list(_api_encode(params))

        assert encoded[0][0] == "ordered[one]"
        assert encoded[1][0] == "ordered[two]"
        assert encoded[2][0] == "ordered[three]"
        assert encoded[3][0] == "ordered[nested][a]"
        assert encoded[4][0] == "ordered[nested][b]"

    def test_url_construction(self, requestor, http_client_mock):
        CASES = (
            ("%s?foo=bar" % stripe.api_base, "", {"foo": "bar"}),
            ("%s?foo=bar" % stripe.api_base, "?", {"foo": "bar"}),
            (stripe.api_base, "", {}),
            (
                "%s/%%20spaced?foo=bar%%24&baz=5" % stripe.api_base,
                "/%20spaced?foo=bar%24",
                {"baz": "5"},
            ),
            (
                "%s?foo=bar&foo=bar" % stripe.api_base,
                "?foo=bar",
                {"foo": "bar"},
            ),
        )

        for expected, url, params in CASES:
            path = urlsplit(expected).path
            query_string = urlsplit(expected).query
            http_client_mock.stub_request(
                "get",
                path=path,
                query_string=query_string,
                rbody="{}",
                rcode=200,
            )

            requestor.request(
                "get", url, params, base_address="api", api_mode="V1"
            )

            http_client_mock.assert_requested("get", abs_url=expected)

    def test_empty_methods(self, requestor, http_client_mock):
        for meth in VALID_API_METHODS:
            http_client_mock.stub_request(
                meth, path=self.valid_path, rbody="{}", rcode=200
            )

            resp = requestor.request(
                meth, self.valid_path, {}, base_address="api", api_mode="V1"
            )

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            http_client_mock.assert_requested(meth, post_data=post_data)
            assert isinstance(resp, StripeObject)

            assert resp == {}

    @pytest.mark.anyio
    async def test_empty_methods_async(
        self, requestor, http_client_mock_async
    ):
        for meth in VALID_API_METHODS:
            http_client_mock_async.stub_request(
                meth, path=self.valid_path, rbody="{}", rcode=200
            )

            resp = await requestor.request_async(
                meth, self.valid_path, {}, base_address="api", api_mode="V1"
            )

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            http_client_mock_async.assert_requested(meth, post_data=post_data)
            assert isinstance(resp, StripeObject)

            assert resp == {}

    @pytest.mark.anyio
    async def test_empty_methods_streaming_response_async(
        self, requestor_streaming, http_client_mock_streaming_async
    ):
        async def async_iter():
            yield b"this"
            yield b"is"
            yield b"data"

        for meth in VALID_API_METHODS:
            http_client_mock_streaming_async.stub_request(
                meth,
                path=self.valid_path,
                rbody=async_iter(),
                rcode=200,
            )

            resp = await requestor_streaming.request_stream_async(
                meth,
                self.valid_path,
                {},
                base_address="api",
                api_mode="V1",
            )

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            http_client_mock_streaming_async.assert_requested(
                meth, post_data=post_data
            )
            assert isinstance(resp, StripeStreamResponseAsync)

            assert b"".join([x async for x in resp.stream()]) == b"thisisdata"

    def test_empty_methods_streaming_response(
        self, requestor_streaming, http_client_mock_streaming
    ):
        for meth in VALID_API_METHODS:
            http_client_mock_streaming.stub_request(
                meth,
                path=self.valid_path,
                rbody=util.io.BytesIO(b"thisisdata"),
                rcode=200,
            )

            resp = requestor_streaming.request_stream(
                meth,
                self.valid_path,
                {},
                base_address="api",
                api_mode="V1",
            )

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            http_client_mock_streaming.assert_requested(
                meth, post_data=post_data
            )
            assert isinstance(resp, StripeStreamResponse)

            assert resp.io.getvalue() == b"thisisdata"

    def test_methods_with_params_and_response(
        self, requestor, http_client_mock
    ):
        for method in VALID_API_METHODS:
            encoded = (
                "adict[frobble]=bits&adatetime=1356994800&"
                "alist[0]=1&alist[1]=2&alist[2]=3"
            )

            http_client_mock.stub_request(
                method,
                path=self.valid_path,
                query_string=encoded if method != "post" else "",
                rbody='{"foo": "bar", "baz": 6}',
                rcode=200,
            )

            params = {
                "alist": [1, 2, 3],
                "adict": {"frobble": "bits"},
                "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            }

            resp = requestor.request(
                method,
                self.valid_path,
                params,
                base_address="api",
                api_mode="V1",
            )
            assert isinstance(resp, StripeObject)

            assert resp == {"foo": "bar", "baz": 6}

            if method == "post":
                http_client_mock.assert_requested(
                    method,
                    post_data=encoded,
                )
            else:
                abs_url = "%s%s?%s" % (
                    stripe.api_base,
                    self.valid_path,
                    encoded,
                )
                http_client_mock.assert_requested(method, abs_url=abs_url)

    def test_methods_with_params_and_streaming_response(
        self, requestor_streaming, http_client_mock_streaming
    ):
        for method in VALID_API_METHODS:
            encoded = (
                "adict[frobble]=bits&adatetime=1356994800&"
                "alist[0]=1&alist[1]=2&alist[2]=3"
            )

            http_client_mock_streaming.stub_request(
                method,
                path=self.valid_path,
                query_string=encoded if method != "post" else "",
                rbody=util.io.BytesIO(b'{"foo": "bar", "baz": 6}'),
                rcode=200,
            )

            params = {
                "alist": [1, 2, 3],
                "adict": {"frobble": "bits"},
                "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            }

            resp = requestor_streaming.request_stream(
                method,
                self.valid_path,
                params,
                base_address="api",
                api_mode="V1",
            )
            assert isinstance(resp, StripeStreamResponse)

            assert resp.io.getvalue() == b'{"foo": "bar", "baz": 6}'

            if method == "post":
                http_client_mock_streaming.assert_requested(
                    method, post_data=encoded
                )
            else:
                abs_url = "%s%s?%s" % (
                    stripe.api_base,
                    self.valid_path,
                    encoded,
                )
                http_client_mock_streaming.assert_requested(
                    method, abs_url=abs_url
                )

    def test_uses_headers(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )
        request_options: RequestOptions = {"headers": {"foo": "bar"}}
        requestor.request(
            "get",
            self.valid_path,
            {},
            options=request_options,
            base_address="api",
            api_mode="V1",
        )
        http_client_mock.assert_requested("get", extra_headers={"foo": "bar"})

    def test_uses_api_version(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )
        request_options: RequestOptions = {"stripe_version": "fooversion"}
        requestor.request(
            "get",
            self.valid_path,
            options=request_options,
            base_address="api",
            api_mode="V1",
        )
        http_client_mock.assert_requested(
            "get",
            stripe_version="fooversion",
        )

    def test_prefers_headers_api_version(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )
        request_options: RequestOptions = {
            "stripe_version": "fooversion",
            "headers": {"Stripe-Version": "barversion"},
        }
        requestor.request(
            "get",
            self.valid_path,
            {},
            options=request_options,
            base_address="api",
            api_mode="V1",
        )
        http_client_mock.assert_requested(
            "get",
            stripe_version="barversion",
        )

    def test_uses_instance_key(self, requestor, http_client_mock):
        key = "fookey"
        requestor = requestor._replace_options(RequestOptions(api_key=key))

        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )

        requestor.request(
            "get", self.valid_path, {}, base_address="api", api_mode="V1"
        )

        http_client_mock.assert_requested("get", api_key=key)
        assert requestor.api_key == key

    def test_uses_instance_account(self, requestor, http_client_mock):
        account = "acct_foo"
        requestor = requestor._replace_options(
            RequestOptions(stripe_account=account)
        )

        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )

        requestor.request(
            "get", self.valid_path, {}, base_address="api", api_mode="V1"
        )

        http_client_mock.assert_requested(
            "get",
            stripe_account=account,
        )

    def test_sets_default_http_client(self, mocker):
        assert not stripe.default_http_client

        _APIRequestor(
            client=mocker.Mock(stripe.http_client.HTTPClient)
        )._get_http_client()

        # default_http_client is not populated if a client is provided
        assert not stripe.default_http_client

        _APIRequestor()._get_http_client()

        # default_http_client is set when no client is specified
        assert stripe.default_http_client

        new_default_client = stripe.default_http_client
        _APIRequestor()

        # the newly created client is reused
        assert stripe.default_http_client == new_default_client

    def test_uses_app_info(self, requestor, http_client_mock):
        try:
            old = stripe.app_info
            stripe.set_app_info(
                "MyAwesomePlugin",
                url="https://myawesomeplugin.info",
                version="1.2.34",
                partner_id="partner_12345",
            )

            http_client_mock.stub_request(
                "get", path=self.valid_path, rbody="{}", rcode=200
            )
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

            ua = "Stripe/v1 PythonBindings/%s" % (stripe.VERSION,)
            ua += " MyAwesomePlugin/1.2.34 (https://myawesomeplugin.info)"
            expected_app_info = {
                "name": "MyAwesomePlugin",
                "url": "https://myawesomeplugin.info",
                "version": "1.2.34",
                "partner_id": "partner_12345",
            }

            last_call = http_client_mock.get_last_call()
            last_call.assert_method("get")
            last_call.assert_header("User-Agent", ua)
            assert (
                json.loads(
                    last_call.get_raw_header("X-Stripe-Client-User-Agent")
                )["application"]
                == expected_app_info
            )
        finally:
            stripe.app_info = old

    def test_handles_failed_platform_call(
        self, requestor, mocker, http_client_mock
    ):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{}", rcode=200
        )

        def fail():
            raise RuntimeError

        mocker.patch("platform.platform", side_effect=fail)

        requestor.request(
            "get", self.valid_path, {}, {}, base_address="api", api_mode="V1"
        )

        last_call = http_client_mock.get_last_call()
        last_call.assert_method("get")
        assert (
            json.loads(last_call.get_raw_header("X-Stripe-Client-User-Agent"))[
                "platform"
            ]
            == "(disabled)"
        )

    def test_uses_given_idempotency_key(self, requestor, http_client_mock):
        meth = "post"
        http_client_mock.stub_request(
            meth, path=self.valid_path, rbody="{}", rcode=200
        )
        request_options: RequestOptions = {"idempotency_key": "123abc"}
        requestor.request(
            meth,
            self.valid_path,
            {},
            options=request_options,
            base_address="api",
            api_mode="V1",
        )

        http_client_mock.assert_requested(
            meth, idempotency_key="123abc", post_data=""
        )

    def test_uuid4_idempotency_key_when_not_given(
        self, requestor, http_client_mock
    ):
        meth = "post"
        http_client_mock.stub_request(
            meth, path=self.valid_path, rbody="{}", rcode=200
        )
        requestor.request(
            meth, self.valid_path, {}, base_address="api", api_mode="V1"
        )

        http_client_mock.assert_requested(
            meth, idempotency_key=AnyUUID4Matcher(), post_data=""
        )

    def test_fails_without_api_key(self, requestor):
        stripe.api_key = None

        with pytest.raises(stripe.error.AuthenticationError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_request_error_404(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=404
        )

        with pytest.raises(stripe.error.InvalidRequestError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_request_error_400(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=400
        )

        with pytest.raises(stripe.error.InvalidRequestError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_idempotency_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": {"type": "idempotency_error"}}',
            rcode=400,
        )

        with pytest.raises(stripe.error.IdempotencyError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_authentication_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=401
        )

        with pytest.raises(stripe.error.AuthenticationError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_permissions_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=403
        )

        with pytest.raises(stripe.error.PermissionError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_card_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": {"code": "invalid_expiry_year"}}',
            rcode=402,
        )

        with pytest.raises(stripe.error.CardError) as excinfo:
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )
        assert excinfo.value.code == "invalid_expiry_year"

    def test_rate_limit_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=429
        )

        with pytest.raises(stripe.error.RateLimitError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_old_rate_limit_error(self, requestor, http_client_mock):
        """
        Tests legacy rate limit error pre-2015-09-18
        """
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": {"code":"rate_limit"}}',
            rcode=400,
        )

        with pytest.raises(stripe.error.RateLimitError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_server_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody='{"error": {}}', rcode=500
        )

        with pytest.raises(stripe.error.APIError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_json(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get", path=self.valid_path, rbody="{", rcode=200
        )

        with pytest.raises(stripe.error.APIError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_method(self, requestor):
        with pytest.raises(stripe.error.APIConnectionError):
            requestor.request("foo", "bar", base_address="api", api_mode="V1")

    def test_oauth_invalid_requestor_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": "invalid_request"}',
            rcode=400,
        )

        with pytest.raises(stripe.oauth_error.InvalidRequestError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_client_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": "invalid_client"}',
            rcode=401,
        )

        with pytest.raises(stripe.oauth_error.InvalidClientError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_invalid_grant_error(self, requestor, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.valid_path,
            rbody='{"error": "invalid_grant"}',
            rcode=400,
        )

        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor.request(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_extract_error_from_stream_request_for_bytes(
        self, requestor_streaming, http_client_mock_streaming
    ):
        http_client_mock_streaming.stub_request(
            "get",
            path=self.valid_path,
            rbody=util.io.BytesIO(b'{"error": "invalid_grant"}'),
            rcode=400,
        )

        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor_streaming.request_stream(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_extract_error_from_stream_request_for_response(
        self, requestor_streaming, http_client_mock_streaming
    ):
        # Responses don't have getvalue, they only have a read method.
        http_client_mock_streaming.stub_request(
            "get",
            path=self.valid_path,
            rbody=urllib3.response.HTTPResponse(
                body=util.io.BytesIO(b'{"error": "invalid_grant"}'),
                preload_content=False,
            ),
            rcode=400,
        )
        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor_streaming.request_stream(
                "get", self.valid_path, {}, base_address="api", api_mode="V1"
            )

    def test_raw_request_with_file_param(self, requestor, http_client_mock):
        test_file = tempfile.NamedTemporaryFile()
        test_file.write("\u263A".encode("utf-16"))
        test_file.seek(0)
        meth = "post"
        path = "/v1/files"
        params = {"file": test_file, "purpose": "dispute_evidence"}
        supplied_headers = {"Content-Type": "multipart/form-data"}
        http_client_mock.stub_request(meth, path=path, rbody="{}", rcode=200)
        requestor.request(
            meth,
            path,
            params,
            supplied_headers,
            base_address="api",
            api_mode="V1",
        )
        assert supplied_headers["Content-Type"] == "multipart/form-data"


class TestDefaultClient(object):
    @pytest.fixture(autouse=True)
    def setup_stripe(self):
        orig_attrs = {
            "api_key": stripe.api_key,
            "default_http_client": stripe.default_http_client,
        }
        stripe.api_key = "sk_test_123"
        yield
        stripe.api_key = orig_attrs["api_key"]
        stripe.default_http_client = orig_attrs["default_http_client"]

    def test_default_http_client_called(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            query_string="limit=3",
            rbody='{"object": "list", "data": []}',
            rcode=200,
            rheaders={},
        )

        stripe.Charge.list(limit=3)

        last_call = http_client_mock.get_last_call()

        last_call.assert_method("get")
        last_call.assert_abs_url("https://api.stripe.com/v1/charges?limit=3")
        last_call.assert_post_data(None)
