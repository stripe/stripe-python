import datetime
import unittest2
import urlparse

from mock import Mock, ANY

import stripe

from stripe.test.helper import StripeUnitTestCase

VALID_API_METHODS = ('get', 'post', 'delete')


class GMT1(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Europe/Prague"


class APIHeaderMatcher(object):
    EXP_KEYS = ['X-Stripe-Client-User-Agent', 'User-Agent', 'Authorization']
    METHOD_EXTRA_KEYS = {"post": ["Content-Type"]}

    def __init__(self, api_key=None, extra={}, request_method=None):
        self.request_method = request_method
        self.api_key = api_key or stripe.api_key
        self.extra = extra

    def __eq__(self, other):
        return (self._keys_match(other) and
                self._auth_match(other) and
                self._extra_match(other))

    def _keys_match(self, other):
        expected_keys = self.EXP_KEYS + self.extra.keys()
        if self.request_method is not None and self.request_method in \
                self.METHOD_EXTRA_KEYS:
            expected_keys.extend(self.METHOD_EXTRA_KEYS[self.request_method])

        return (sorted(other.keys()) == sorted(expected_keys))

    def _auth_match(self, other):
        return other['Authorization'] == "Bearer %s" % (self.api_key,)

    def _extra_match(self, other):
        for k, v in self.extra.iteritems():
            if other[k] != v:
                return False

        return True


class QueryMatcher(object):

    def __init__(self, expected):
        self.expected = sorted(expected)

    def __eq__(self, other):
        query = urlparse.urlsplit(other).query or other

        parsed = stripe.util.parse_qsl(query)
        return self.expected == sorted(parsed)


class UrlMatcher(object):

    def __init__(self, expected):
        self.exp_parts = urlparse.urlsplit(expected)

    def __eq__(self, other):
        other_parts = urlparse.urlsplit(other)

        for part in ('scheme', 'netloc', 'path', 'fragment'):
            expected = getattr(self.exp_parts, part)
            actual = getattr(other_parts, part)
            if expected != actual:
                print 'Expected %s "%s" but got "%s"' % (
                    part, expected, actual)
                return False

        q_matcher = QueryMatcher(stripe.util.parse_qsl(self.exp_parts.query))
        return q_matcher == other


class APIRequestorRequestTests(StripeUnitTestCase):
    ENCODE_INPUTS = {
        'dict': {
            'astring': 'bar',
            'anint': 5,
            'anull': None,
            'adatetime': datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            'atuple': (1, 2),
            'adict': {'foo': 'bar', 'boz': 5},
            'alist': ['foo', 'bar'],
        },
        'list': [1, 'foo', 'baz'],
        'string': 'boo',
        'unicode': u'\u1234',
        'datetime': datetime.datetime(2013, 1, 1, second=1, tzinfo=GMT1()),
        'none': None,
    }

    ENCODE_EXPECTATIONS = {
        'dict': [
            ('%s[astring]', 'bar'),
            ('%s[anint]', 5),
            ('%s[adatetime]', 1356994800),
            ('%s[adict][foo]', 'bar'),
            ('%s[adict][boz]', 5),
            ('%s[alist][]', 'foo'),
            ('%s[alist][]', 'bar'),
            ('%s[atuple][]', 1),
            ('%s[atuple][]', 2),
        ],
        'list': [
            ('%s[]', 1),
            ('%s[]', 'foo'),
            ('%s[]', 'baz'),
        ],
        'string': [('%s', 'boo')],
        'unicode': [('%s', stripe.util.utf8(u'\u1234'))],
        'datetime': [('%s', 1356994801)],
        'none': [],
    }

    def setUp(self):
        super(APIRequestorRequestTests, self).setUp()

        self.http_client = Mock(stripe.http_client.HTTPClient)
        self.http_client._verify_ssl_certs = True
        self.http_client.name = 'mockclient'

        self.requestor = stripe.api_requestor.APIRequestor(
            client=self.http_client)

    def mock_response(self, return_body, return_code, requestor=None,
                      headers=None):
        if not requestor:
            requestor = self.requestor

        self.http_client.request = Mock(
            return_value=(return_body, return_code, headers or {}))

    def check_call(self, meth, abs_url=None, headers=None,
                   post_data=None, requestor=None):
        if not abs_url:
            abs_url = 'https://api.stripe.com%s' % (self.valid_path,)
        if not requestor:
            requestor = self.requestor
        if not headers:
            headers = APIHeaderMatcher(request_method=meth)

        self.http_client.request.assert_called_with(
            meth, abs_url, headers, post_data)

    @property
    def valid_path(self):
        return '/foo'

    def encoder_check(self, key):
        stk_key = "my%s" % (key,)

        value = self.ENCODE_INPUTS[key]
        expectation = [(k % (stk_key,), v) for k, v in
                       self.ENCODE_EXPECTATIONS[key]]

        stk = []
        fn = getattr(stripe.api_requestor.APIRequestor, "encode_%s" % (key,))
        fn(stk, stk_key, value)

        if isinstance(value, dict):
            expectation.sort()
            stk.sort()

        self.assertEqual(expectation, stk)

    def _test_encode_naive_datetime(self):
        stk = []

        stripe.api_requestor.APIRequestor.encode_datetime(
            stk, 'test', datetime.datetime(2013, 1, 1))

        # Naive datetimes will encode differently depending on your system
        # local time.  Since we don't know the local time of your system,
        # we just check that naive encodings are within 24 hours of correct.
        self.assertTrue(60 * 60 * 24 > abs(stk[0][1] - 1356994800))

    def test_param_encoding(self):
        self.mock_response('{}', 200)

        self.requestor.request('get', '', self.ENCODE_INPUTS)

        expectation = []
        for type_, values in self.ENCODE_EXPECTATIONS.iteritems():
            expectation.extend([(k % (type_,), str(v)) for k, v in values])

        self.check_call('get', QueryMatcher(expectation))

    def test_dictionary_list_encoding(self):
        params = {
            'foo': {
                '0': {
                    'bar': 'bat',
                }
            }
        }
        encoded = list(stripe.api_requestor._api_encode(params))
        key, value = encoded[0]

        self.assertEqual('foo[0][bar]', key)
        self.assertEqual('bat', value)

    def test_url_construction(self):
        CASES = (
            ('https://api.stripe.com?foo=bar', '', {'foo': 'bar'}),
            ('https://api.stripe.com?foo=bar', '?', {'foo': 'bar'}),
            ('https://api.stripe.com', '', {}),
            (
                'https://api.stripe.com/%20spaced?foo=bar%24&baz=5',
                '/%20spaced?foo=bar%24',
                {'baz': '5'}
            ),
            (
                'https://api.stripe.com?foo=bar&foo=bar',
                '?foo=bar',
                {'foo': 'bar'}
            ),
        )

        for expected, url, params in CASES:
            self.mock_response('{}', 200)

            self.requestor.request('get', url, params)

            self.check_call('get', expected)

    def test_empty_methods(self):
        for meth in VALID_API_METHODS:
            self.mock_response('{}', 200)

            body, key = self.requestor.request(meth, self.valid_path, {})

            if meth == 'post':
                post_data = ''
            else:
                post_data = None

            self.check_call(meth, post_data=post_data)
            self.assertEqual({}, body)

    def test_methods_with_params_and_response(self):
        for meth in VALID_API_METHODS:
            self.mock_response('{"foo": "bar", "baz": 6}', 200)

            params = {
                'alist': [1, 2, 3],
                'adict': {'frobble': 'bits'},
                'adatetime': datetime.datetime(2013, 1, 1, tzinfo=GMT1())
            }
            encoded = ('adict%5Bfrobble%5D=bits&adatetime=1356994800&'
                       'alist%5B%5D=1&alist%5B%5D=2&alist%5B%5D=3')

            body, key = self.requestor.request(meth, self.valid_path,
                                               params)
            self.assertEqual({'foo': 'bar', 'baz': 6}, body)

            if meth == 'post':
                self.check_call(
                    meth,
                    post_data=QueryMatcher(stripe.util.parse_qsl(encoded)))
            else:
                abs_url = "https://api.stripe.com%s?%s" % (
                    self.valid_path, encoded)
                self.check_call(meth, abs_url=UrlMatcher(abs_url))

    def test_uses_headers(self):
        self.mock_response('{}', 200)
        self.requestor.request('get', self.valid_path, {}, {'foo': 'bar'})
        self.check_call('get', headers=APIHeaderMatcher(extra={'foo': 'bar'}))

    def test_uses_instance_key(self):
        key = 'fookey'
        requestor = stripe.api_requestor.APIRequestor(key,
                                                      client=self.http_client)

        self.mock_response('{}', 200, requestor=requestor)

        body, used_key = requestor.request('get', self.valid_path, {})

        self.check_call('get', headers=APIHeaderMatcher(
            key, request_method='get'), requestor=requestor)
        self.assertEqual(key, used_key)

    def test_passes_api_version(self):
        stripe.api_version = 'fooversion'

        self.mock_response('{}', 200)

        body, key = self.requestor.request('get', self.valid_path, {})

        self.check_call('get', headers=APIHeaderMatcher(
            extra={'Stripe-Version': 'fooversion'}, request_method='get'))

    def test_uses_instance_account(self):
        account = 'acct_foo'
        requestor = stripe.api_requestor.APIRequestor(account=account,
                                                      client=self.http_client)

        self.mock_response('{}', 200, requestor=requestor)

        requestor.request('get', self.valid_path, {})

        self.check_call(
            'get',
            requestor=requestor,
            headers=APIHeaderMatcher(
                extra={'Stripe-Account': account},
                request_method='get'
            ),
        )

    def test_fails_without_api_key(self):
        stripe.api_key = None

        self.assertRaises(stripe.error.AuthenticationError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_not_found(self):
        self.mock_response('{"error": {}}', 404)

        self.assertRaises(stripe.error.InvalidRequestError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_authentication_error(self):
        self.mock_response('{"error": {}}', 401)

        self.assertRaises(stripe.error.AuthenticationError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_card_error(self):
        self.mock_response('{"error": {}}', 402)

        self.assertRaises(stripe.error.CardError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_rate_limit_error(self):
        self.mock_response('{"error": {}}', 429)

        self.assertRaises(stripe.error.RateLimitError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_old_rate_limit_error(self):
        """
        Tests legacy rate limit error pre-2015-09-18
        """
        self.mock_response('{"error": {"code":"rate_limit"}}', 400)

        self.assertRaises(stripe.error.RateLimitError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_server_error(self):
        self.mock_response('{"error": {}}', 500)

        self.assertRaises(stripe.error.APIError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_invalid_json(self):
        self.mock_response('{', 200)

        self.assertRaises(stripe.error.APIError,
                          self.requestor.request,
                          'get', self.valid_path, {})

    def test_invalid_method(self):
        self.assertRaises(stripe.error.APIConnectionError,
                          self.requestor.request,
                          'foo', 'bar')


class DefaultClientTests(unittest2.TestCase):

    def setUp(self):
        stripe.default_http_client = None
        stripe.api_key = 'foo'

    def test_default_http_client_called(self):
        hc = Mock(stripe.http_client.HTTPClient)
        hc._verify_ssl_certs = True
        hc.name = 'mockclient'
        hc.request = Mock(return_value=("{}", 200, {}))

        stripe.default_http_client = hc
        stripe.Charge.list(limit=3)

        hc.request.assert_called_with(
            'get', 'https://api.stripe.com/v1/charges?limit=3', ANY, None)

    def tearDown(self):
        stripe.api_key = None
        stripe.default_http_client = None


if __name__ == '__main__':
    unittest2.main()
