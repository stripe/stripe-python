from __future__ import absolute_import, division, print_function

import datetime
import json
import tempfile
import uuid
from collections import OrderedDict

import pytest

import stripe
from stripe import six, util
from stripe.stripe_response import StripeResponse, StripeStreamResponse

from stripe.six.moves.urllib.parse import urlsplit

import urllib3

VALID_API_METHODS = ("get", "post", "delete")


class GMT1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Europe/Prague"


class APIHeaderMatcher(object):
    EXP_KEYS = [
        "Authorization",
        "Stripe-Version",
        "User-Agent",
        "X-Stripe-Client-User-Agent",
    ]
    METHOD_EXTRA_KEYS = {"post": ["Content-Type", "Idempotency-Key"]}

    def __init__(
        self,
        api_key=None,
        extra={},
        request_method=None,
        user_agent=None,
        app_info=None,
        idempotency_key=None,
        fail_platform_call=False,
    ):
        self.request_method = request_method
        self.api_key = api_key or stripe.api_key
        self.extra = extra
        self.user_agent = user_agent
        self.app_info = app_info
        self.idempotency_key = idempotency_key
        self.fail_platform_call = fail_platform_call

    def __eq__(self, other):
        return (
            self._keys_match(other)
            and self._auth_match(other)
            and self._user_agent_match(other)
            and self._x_stripe_ua_contains_app_info(other)
            and self._x_stripe_ua_handles_failed_platform_function(other)
            and self._idempotency_key_match(other)
            and self._extra_match(other)
        )

    def __repr__(self):
        return "APIHeaderMatcher(request_method=%s, api_key=%s, extra=%s, " "user_agent=%s, app_info=%s, idempotency_key=%s, fail_platform_call=%s)" % (
            repr(self.request_method),
            repr(self.api_key),
            repr(self.extra),
            repr(self.user_agent),
            repr(self.app_info),
            repr(self.idempotency_key),
            repr(self.fail_platform_call),
        )

    def _keys_match(self, other):
        expected_keys = list(set(self.EXP_KEYS + list(self.extra.keys())))
        if (
            self.request_method is not None
            and self.request_method in self.METHOD_EXTRA_KEYS
        ):
            expected_keys.extend(self.METHOD_EXTRA_KEYS[self.request_method])
        return sorted(other.keys()) == sorted(expected_keys)

    def _auth_match(self, other):
        return other["Authorization"] == "Bearer %s" % (self.api_key,)

    def _user_agent_match(self, other):
        if self.user_agent is not None:
            return other["User-Agent"] == self.user_agent

        return True

    def _idempotency_key_match(self, other):
        if self.idempotency_key is not None:
            return other["Idempotency-Key"] == self.idempotency_key
        return True

    def _x_stripe_ua_contains_app_info(self, other):
        if self.app_info:
            ua = json.loads(other["X-Stripe-Client-User-Agent"])
            if "application" not in ua:
                return False
            return ua["application"] == self.app_info

        return True

    def _x_stripe_ua_handles_failed_platform_function(self, other):
        if self.fail_platform_call:
            ua = json.loads(other["X-Stripe-Client-User-Agent"])
            return ua["platform"] == "(disabled)"
        return True

    def _extra_match(self, other):
        for k, v in six.iteritems(self.extra):
            if other[k] != v:
                return False

        return True


class QueryMatcher(object):
    def __init__(self, expected):
        self.expected = sorted(expected)

    def __eq__(self, other):
        query = urlsplit(other).query or other

        parsed = stripe.util.parse_qsl(query)
        return self.expected == sorted(parsed)

    def __repr__(self):
        return "QueryMatcher(expected=%s)" % (repr(self.expected))


class UrlMatcher(object):
    def __init__(self, expected):
        self.exp_parts = urlsplit(expected)

    def __eq__(self, other):
        other_parts = urlsplit(other)

        for part in ("scheme", "netloc", "path", "fragment"):
            expected = getattr(self.exp_parts, part)
            actual = getattr(other_parts, part)
            if expected != actual:
                print(
                    'Expected %s "%s" but got "%s"' % (part, expected, actual)
                )
                return False

        q_matcher = QueryMatcher(stripe.util.parse_qsl(self.exp_parts.query))
        return q_matcher == other

    def __repr__(self):
        return "UrlMatcher(exp_parts=%s)" % (repr(self.exp_parts))


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
        "unicode": u"\u1234",
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
        "unicode": [("%s", stripe.util.utf8(u"\u1234"))],
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
    def http_client(self, mocker):
        http_client = mocker.Mock(stripe.http_client.HTTPClient)
        http_client._verify_ssl_certs = True
        http_client.name = "mockclient"
        return http_client

    @pytest.fixture
    def requestor(self, http_client):
        requestor = stripe.api_requestor.APIRequestor(client=http_client)
        return requestor

    @pytest.fixture
    def mock_response(self, mocker, http_client):
        def mock_response(return_body, return_code, headers=None):
            http_client.request_with_retries = mocker.Mock(
                return_value=(return_body, return_code, headers or {})
            )

        return mock_response

    @pytest.fixture
    def mock_streaming_response(self, mocker, http_client):
        def mock_streaming_response(return_body, return_code, headers=None):
            http_client.request_stream_with_retries = mocker.Mock(
                return_value=(return_body, return_code, headers or {})
            )

        return mock_streaming_response

    @pytest.fixture
    def check_call(self, http_client):
        def check_call(
            method,
            abs_url=None,
            headers=None,
            post_data=None,
            is_streaming=False,
        ):
            if not abs_url:
                abs_url = "%s%s" % (stripe.api_base, self.valid_path)
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
        fn = getattr(stripe.api_requestor.APIRequestor, "encode_%s" % (key,))
        fn(stk, stk_key, value)

        if isinstance(value, dict):
            expectation.sort()
            stk.sort()

        assert stk == expectation, stk

    def _test_encode_naive_datetime(self):
        stk = []

        stripe.api_requestor.APIRequestor.encode_datetime(
            stk, "test", datetime.datetime(2013, 1, 1)
        )

        # Naive datetimes will encode differently depending on your system
        # local time.  Since we don't know the local time of your system,
        # we just check that naive encodings are within 24 hours of correct.
        assert abs(stk[0][1] - 1356994800) <= 60 * 60 * 24

    def test_param_encoding(self, requestor, mock_response, check_call):
        mock_response("{}", 200)

        requestor.request("get", "", self.ENCODE_INPUTS)

        expectation = []
        for type_, values in six.iteritems(self.ENCODE_EXPECTATIONS):
            expectation.extend([(k % (type_,), str(v)) for k, v in values])

        check_call("get", QueryMatcher(expectation))

    def test_dictionary_list_encoding(self):
        params = {"foo": {"0": {"bar": "bat"}}}
        encoded = list(stripe.api_requestor._api_encode(params))
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
        encoded = list(stripe.api_requestor._api_encode(params))

        assert encoded[0][0] == "ordered[one]"
        assert encoded[1][0] == "ordered[two]"
        assert encoded[2][0] == "ordered[three]"
        assert encoded[3][0] == "ordered[nested][a]"
        assert encoded[4][0] == "ordered[nested][b]"

    def test_url_construction(self, requestor, mock_response, check_call):
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
            mock_response("{}", 200)

            requestor.request("get", url, params)

            check_call("get", expected)

    def test_empty_methods(self, requestor, mock_response, check_call):
        for meth in VALID_API_METHODS:
            mock_response("{}", 200)

            resp, key = requestor.request(meth, self.valid_path, {})

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            check_call(meth, post_data=post_data)
            assert isinstance(resp, StripeResponse)

            assert resp.data == {}
            assert resp.data == json.loads(resp.body)

    def test_empty_methods_streaming_response(
        self, requestor, mock_streaming_response, check_call
    ):
        for meth in VALID_API_METHODS:
            mock_streaming_response(util.io.BytesIO(b"thisisdata"), 200)

            resp, key = requestor.request_stream(
                meth,
                self.valid_path,
                {},
            )

            if meth == "post":
                post_data = ""
            else:
                post_data = None

            check_call(meth, post_data=post_data, is_streaming=True)
            assert isinstance(resp, StripeStreamResponse)

            assert resp.io.getvalue() == b"thisisdata"

    def test_methods_with_params_and_response(
        self, requestor, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response('{"foo": "bar", "baz": 6}', 200)

            params = {
                "alist": [1, 2, 3],
                "adict": {"frobble": "bits"},
                "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            }
            encoded = (
                "adict[frobble]=bits&adatetime=1356994800&"
                "alist[0]=1&alist[1]=2&alist[2]=3"
            )

            resp, key = requestor.request(method, self.valid_path, params)
            assert isinstance(resp, StripeResponse)

            assert resp.data == {"foo": "bar", "baz": 6}
            assert resp.data == json.loads(resp.body)

            if method == "post":
                check_call(
                    method,
                    post_data=QueryMatcher(stripe.util.parse_qsl(encoded)),
                )
            else:
                abs_url = "%s%s?%s" % (
                    stripe.api_base,
                    self.valid_path,
                    encoded,
                )
                check_call(method, abs_url=UrlMatcher(abs_url))

    def test_methods_with_params_and_streaming_response(
        self, requestor, mock_streaming_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_streaming_response(
                util.io.BytesIO(b'{"foo": "bar", "baz": 6}'), 200
            )

            params = {
                "alist": [1, 2, 3],
                "adict": {"frobble": "bits"},
                "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            }
            encoded = (
                "adict[frobble]=bits&adatetime=1356994800&"
                "alist[0]=1&alist[1]=2&alist[2]=3"
            )

            resp, key = requestor.request_stream(
                method,
                self.valid_path,
                params,
            )
            assert isinstance(resp, StripeStreamResponse)

            assert resp.io.getvalue() == b'{"foo": "bar", "baz": 6}'

            if method == "post":
                check_call(
                    method,
                    post_data=QueryMatcher(stripe.util.parse_qsl(encoded)),
                    is_streaming=True,
                )
            else:
                abs_url = "%s%s?%s" % (
                    stripe.api_base,
                    self.valid_path,
                    encoded,
                )
                check_call(
                    method, abs_url=UrlMatcher(abs_url), is_streaming=True
                )

    def test_uses_headers(self, requestor, mock_response, check_call):
        mock_response("{}", 200)
        requestor.request("get", self.valid_path, {}, {"foo": "bar"})
        check_call("get", headers=APIHeaderMatcher(extra={"foo": "bar"}))

    def test_uses_instance_key(self, http_client, mock_response, check_call):
        key = "fookey"
        requestor = stripe.api_requestor.APIRequestor(key, client=http_client)

        mock_response("{}", 200)

        resp, used_key = requestor.request("get", self.valid_path, {})

        check_call("get", headers=APIHeaderMatcher(key, request_method="get"))
        assert used_key == key

    def test_uses_instance_api_version(
        self, http_client, mock_response, check_call
    ):
        api_version = "fooversion"
        requestor = stripe.api_requestor.APIRequestor(
            api_version=api_version, client=http_client
        )

        mock_response("{}", 200)

        requestor.request("get", self.valid_path, {})

        check_call(
            "get",
            headers=APIHeaderMatcher(
                extra={"Stripe-Version": "fooversion"}, request_method="get"
            ),
        )

    def test_uses_instance_account(
        self, http_client, mock_response, check_call
    ):
        account = "acct_foo"
        requestor = stripe.api_requestor.APIRequestor(
            account=account, client=http_client
        )

        mock_response("{}", 200)

        requestor.request("get", self.valid_path, {})

        check_call(
            "get",
            headers=APIHeaderMatcher(
                extra={"Stripe-Account": account}, request_method="get"
            ),
        )

    def test_sets_default_http_client(self, http_client):
        assert not stripe.default_http_client

        stripe.api_requestor.APIRequestor(client=http_client)

        # default_http_client is not populated if a client is provided
        assert not stripe.default_http_client

        stripe.api_requestor.APIRequestor()

        # default_http_client is set when no client is specified
        assert stripe.default_http_client

        new_default_client = stripe.default_http_client
        stripe.api_requestor.APIRequestor()

        # the newly created client is reused
        assert stripe.default_http_client == new_default_client

    def test_uses_app_info(self, requestor, mock_response, check_call):
        try:
            old = stripe.app_info
            stripe.set_app_info(
                "MyAwesomePlugin",
                url="https://myawesomeplugin.info",
                version="1.2.34",
                partner_id="partner_12345",
            )

            mock_response("{}", 200)
            requestor.request("get", self.valid_path, {})

            ua = "Stripe/v1 PythonBindings/%s" % (stripe.version.VERSION,)
            ua += " MyAwesomePlugin/1.2.34 (https://myawesomeplugin.info)"
            header_matcher = APIHeaderMatcher(
                user_agent=ua,
                app_info={
                    "name": "MyAwesomePlugin",
                    "url": "https://myawesomeplugin.info",
                    "version": "1.2.34",
                    "partner_id": "partner_12345",
                },
            )
            check_call("get", headers=header_matcher)
        finally:
            stripe.app_info = old

    def test_handles_failed_platform_call(
        self, requestor, mocker, mock_response, check_call
    ):
        mock_response("{}", 200)

        def fail():
            raise RuntimeError

        mocker.patch("platform.platform", side_effect=fail)

        requestor.request("get", self.valid_path, {}, {})

        check_call("get", headers=APIHeaderMatcher(fail_platform_call=True))

    def test_uses_given_idempotency_key(
        self, requestor, mock_response, check_call
    ):
        mock_response("{}", 200)
        meth = "post"
        requestor.request(
            meth, self.valid_path, {}, {"Idempotency-Key": "123abc"}
        )

        header_matcher = APIHeaderMatcher(
            request_method=meth, idempotency_key="123abc"
        )
        check_call(meth, headers=header_matcher, post_data="")

    def test_uuid4_idempotency_key_when_not_given(
        self, requestor, mock_response, check_call
    ):
        mock_response("{}", 200)
        meth = "post"
        requestor.request(meth, self.valid_path, {})

        header_matcher = APIHeaderMatcher(
            request_method=meth, idempotency_key=AnyUUID4Matcher()
        )
        check_call(meth, headers=header_matcher, post_data="")

    def test_fails_without_api_key(self, requestor):
        stripe.api_key = None

        with pytest.raises(stripe.error.AuthenticationError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_request_error_404(self, requestor, mock_response):
        mock_response('{"error": {}}', 404)

        with pytest.raises(stripe.error.InvalidRequestError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_request_error_400(self, requestor, mock_response):
        mock_response('{"error": {}}', 400)

        with pytest.raises(stripe.error.InvalidRequestError):
            requestor.request("get", self.valid_path, {})

    def test_idempotency_error(self, requestor, mock_response):
        mock_response('{"error": {"type": "idempotency_error"}}', 400)

        with pytest.raises(stripe.error.IdempotencyError):
            requestor.request("get", self.valid_path, {})

    def test_authentication_error(self, requestor, mock_response):
        mock_response('{"error": {}}', 401)

        with pytest.raises(stripe.error.AuthenticationError):
            requestor.request("get", self.valid_path, {})

    def test_permissions_error(self, requestor, mock_response):
        mock_response('{"error": {}}', 403)

        with pytest.raises(stripe.error.PermissionError):
            requestor.request("get", self.valid_path, {})

    def test_card_error(self, requestor, mock_response):
        mock_response('{"error": {"code": "invalid_expiry_year"}}', 402)

        with pytest.raises(stripe.error.CardError) as excinfo:
            requestor.request("get", self.valid_path, {})
        assert excinfo.value.code == "invalid_expiry_year"

    def test_rate_limit_error(self, requestor, mock_response):
        mock_response('{"error": {}}', 429)

        with pytest.raises(stripe.error.RateLimitError):
            requestor.request("get", self.valid_path, {})

    def test_old_rate_limit_error(self, requestor, mock_response):
        """
        Tests legacy rate limit error pre-2015-09-18
        """
        mock_response('{"error": {"code":"rate_limit"}}', 400)

        with pytest.raises(stripe.error.RateLimitError):
            requestor.request("get", self.valid_path, {})

    def test_server_error(self, requestor, mock_response):
        mock_response('{"error": {}}', 500)

        with pytest.raises(stripe.error.APIError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_json(self, requestor, mock_response):
        mock_response("{", 200)

        with pytest.raises(stripe.error.APIError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_method(self, requestor):
        with pytest.raises(stripe.error.APIConnectionError):
            requestor.request("foo", "bar")

    def test_oauth_invalid_requestor_error(self, requestor, mock_response):
        mock_response('{"error": "invalid_request"}', 400)

        with pytest.raises(stripe.oauth_error.InvalidRequestError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_client_error(self, requestor, mock_response):
        mock_response('{"error": "invalid_client"}', 401)

        with pytest.raises(stripe.oauth_error.InvalidClientError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_grant_error(self, requestor, mock_response):
        mock_response('{"error": "invalid_grant"}', 400)

        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor.request("get", self.valid_path, {})

    def test_extract_error_from_stream_request_for_bytes(
        self, requestor, mock_streaming_response
    ):
        mock_streaming_response(
            util.io.BytesIO(b'{"error": "invalid_grant"}'), 400
        )

        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor.request_stream("get", self.valid_path, {})

    def test_extract_error_from_stream_request_for_response(
        self, requestor, mock_streaming_response
    ):
        # Responses don't have getvalue, they only have a read method.
        mock_streaming_response(
            urllib3.response.HTTPResponse(
                body=util.io.BytesIO(b'{"error": "invalid_grant"}'),
                preload_content=False,
            ),
            400,
        )

        with pytest.raises(stripe.oauth_error.InvalidGrantError):
            requestor.request_stream("get", self.valid_path, {})

    def test_raw_request_with_file_param(self, requestor, mock_response):
        test_file = tempfile.NamedTemporaryFile()
        test_file.write("\u263A".encode("utf-16"))
        test_file.seek(0)
        params = {"file": test_file, "purpose": "dispute_evidence"}
        supplied_headers = {"Content-Type": "multipart/form-data"}
        mock_response("{}", 200)
        requestor.request("post", "/v1/files", params, supplied_headers)


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

    def test_default_http_client_called(self, mocker):
        hc = mocker.Mock(stripe.http_client.HTTPClient)
        hc._verify_ssl_certs = True
        hc.name = "mockclient"
        hc.request_with_retries = mocker.Mock(return_value=("{}", 200, {}))

        stripe.default_http_client = hc
        stripe.Charge.list(limit=3)

        hc.request_with_retries.assert_called_with(
            "get",
            "https://api.stripe.com/v1/charges?limit=3",
            mocker.ANY,
            None,
        )
