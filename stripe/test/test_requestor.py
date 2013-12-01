import datetime
import unittest

from mock import Mock

# Python 3 compatibility
try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl

import stripe

from stripe import APIRequestor, APIError, APIConnectionError
from stripe.test.helper import StripeUnitTestCase

VALID_API_METHODS = ('get', 'post', 'delete')


class GMT1(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Europe/Prague"


class APIRequestorClassTests(unittest.TestCase):
    ENCODE_INPUTS = {
        'dict': {
            'astring': 'bar',
            'anint': 5,
            'anull': None,
            'adatetime': datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            # 'atuple': (1, 2, 3), TODO: Handle tuples properly
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
        ],
        'list': [
            ('%s[]', 1),
            ('%s[]', 'foo'),
            ('%s[]', 'baz'),
        ],
        'string': [('%s', 'boo')],
        'unicode': [('%s', (u'\u1234').encode('utf-8'))],
        'datetime': [('%s', 1356994801)],
        'none': [],
    }

    def encoder_check(self, key):
        stk_key = "my%s" % key

        value = self.ENCODE_INPUTS[key]
        expectation = [(k % stk_key, v) for k, v in
                       self.ENCODE_EXPECTATIONS[key]]

        stk = []
        getattr(APIRequestor, "encode_%s" % key)(stk, stk_key, value)

        if(isinstance(value, dict)):
            expectation.sort()
            stk.sort()

        self.assertEqual(expectation, stk)

    def test_encode_dict(self):
        self.encoder_check('dict')

    def test_encode_list(self):
        self.encoder_check('list')

    def test_encode_datetime(self):
        self.encoder_check('datetime')

    def test_encode_none(self):
        self.encoder_check('none')

    def test_encode(self):
        expectation = []
        for type_, values in self.ENCODE_EXPECTATIONS.iteritems():
            expectation.extend([(k % type_, str(v)) for k, v in values])

        result = APIRequestor.encode(self.ENCODE_INPUTS)
        decoded = parse_qsl(result)

        # List ordering is checked elsewhere
        self.assertEqual(sorted(expectation),
                         sorted(decoded))

    def test_build_url(self):
        CASES = (
            ('stripe.com?foo=bar', 'stripe.com', {'foo': 'bar'}),
            ('stripe.com?foo=bar', 'stripe.com?', {'foo': 'bar'}),
            ('stripe.com', 'stripe.com', {}),
            (
                'https://stripe.com/%20spaced?foo=bar%24&baz=5',
                'https://stripe.com/%20spaced?foo=bar%24',
                {'baz': '5'}
            ),
            (
                'http://foo.com?foo=bar&foo=bar',
                'http://foo.com?foo=bar',
                {'foo': 'bar'}
            ),
        )

        for expected, url, params in CASES:
            self.assertEqual(expected, APIRequestor.build_url(url, params))


class APIHeaderMatcher(object):
    EXP_KEYS = ['X-Stripe-Client-User-Agent', 'User-Agent', 'Authorization']

    def __init__(self, api_key=None, extra={}):
        self.api_key = api_key or stripe.api_key
        self.extra = extra

    def __eq__(self, other):
        return (self._keys_match(other) and
                self._auth_match(other) and
                self._extra_match(other))

    def _keys_match(self, other):
        expected_keys = self.EXP_KEYS + self.extra.keys()
        return (sorted(other.keys()) == sorted(expected_keys))

    def _auth_match(self, other):
        return other['Authorization'] == "Bearer %s" % self.api_key

    def _extra_match(self, other):
        for k, v in self.extra.iteritems():
            if other[k] != v:
                return False

        return True


class APIRequestorRequestTests(StripeUnitTestCase):

    def setUp(self):
        super(APIRequestorRequestTests, self).setUp()

        self.http_client = Mock(stripe.http_client.HTTPClient)
        self.http_client._verify_ssl_certs = True
        self.http_client.name = 'mockclient'

        self.requestor = APIRequestor(client=self.http_client)

    def mock_response(self, return_body, return_code, requestor=None):
        if not requestor:
            requestor = self.requestor

        self.http_client.request = Mock(
            return_value=(return_body, return_code))

    def check_call(self, meth, abs_url=None, headers={},
                   post_data=None, requestor=None):
        if not abs_url:
            abs_url = 'https://api.stripe.com%s' % self.valid_path
        if not requestor:
            requestor = self.requestor
        if not headers:
            headers = APIHeaderMatcher()

        self.http_client.request.assert_called_with(
            meth, abs_url, headers, post_data)

    @property
    def valid_path(self):
        return '/foo'

    # TODO: Test that we fallback on request libraries in the right order

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
                'adatetime': datetime.datetime(2013, 1, 1)
            }
            encoded = ('alist%5B%5D=1&alist%5B%5D=2&alist%5B%5D=3&'
                       'adatetime=1356994800&adict%5Bfrobble%5D=bits')

            body, key = self.requestor.request(meth, self.valid_path,
                                               params)
            self.assertEqual({'foo': 'bar', 'baz': 6}, body)

            if meth == 'post':
                self.check_call(meth, post_data=encoded)
            else:
                abs_url = "https://api.stripe.com%s?%s" % (
                    self.valid_path, encoded)
                self.check_call(meth, abs_url=abs_url)

    def test_uses_instance_key(self):
        key = 'fookey'
        requestor = APIRequestor(key, client=self.http_client)

        self.mock_response('{}', 200, requestor=requestor)

        body, used_key = requestor.request('get', self.valid_path, {})

        self.check_call('get', headers=APIHeaderMatcher(key),
                        requestor=requestor)
        self.assertEqual(key, used_key)

    def test_passes_api_version(self):
        stripe.api_version = 'fooversion'

        self.mock_response('{}', 200)

        body, key = self.requestor.request('get', self.valid_path, {})

        self.check_call('get', headers=APIHeaderMatcher(
            extra={'Stripe-Version': 'fooversion'}))

    def test_fails_without_api_key(self):
        stripe.api_key = None

        with self.assertRaises(stripe.AuthenticationError):
            self.requestor.request('get', self.valid_path, {})

    def test_not_found(self):
        self.mock_response('{"error": {}}', 404)

        with self.assertRaises(stripe.InvalidRequestError):
            self.requestor.request('get', self.valid_path, {})

    def test_authentication_error(self):
        self.mock_response('{"error": {}}', 401)

        with self.assertRaises(stripe.AuthenticationError):
            self.requestor.request('get', self.valid_path, {})

    def test_card_error(self):
        self.mock_response('{"error": {}}', 402)

        with self.assertRaises(stripe.CardError):
            self.requestor.request('get', self.valid_path, {})

    def test_server_error(self):
        self.mock_response('{"error": {}}', 500)

        with self.assertRaises(APIError):
            self.requestor.request('get', self.valid_path, {})

    def test_invalid_json(self):
        self.mock_response('{', 200)

        with self.assertRaises(APIError):
            self.requestor.request('get', self.valid_path, {})


class ClientTestBase():

    @property
    def request_mock(self):
        return self.request_mocks[self.request_client.name]

    @property
    def valid_url(self, path='/foo'):
        return 'https://api.stripe.com%s' % path

    def make_request(self, meth, abs_url, headers, params):
        requestor = APIRequestor()
        request_method = getattr(requestor,
                                 "%s_request" % self.request_client.name)

        return request_method(meth, abs_url, headers, params)

    def mock_response(self, body, code):
        raise NotImplementedError(
            'You must implement this in your test subclass')

    def mock_error(self, error):
        raise NotImplementedError(
            'You must implement this in your test subclass')

    def check_call(self, meth, abs_url, headers, params):
        raise NotImplementedError(
            'You must implement this in your test subclass')

    def test_request(self):
        self.mock_response(self.request_mock, '{"foo": "baz"}', 200)

        for meth in VALID_API_METHODS:
            abs_url = self.valid_url
            params = {'myparam': 5, 'otherparam[]': 'foo'}
            headers = {'my-header': 'header val'}

            body, code = self.make_request(meth, abs_url, headers, params)

            self.assertEqual(200, code)
            self.assertEqual('{"foo": "baz"}', body)

            encoded = APIRequestor.encode(params)

            if meth != 'post':
                url = "%s?%s" % (abs_url, encoded)
                post_data = None
            else:
                url = abs_url
                post_data = encoded

            self.check_call(self.request_mock, meth, url, post_data, headers)

    def test_invalid_method(self):
        with self.assertRaises(APIConnectionError):
            self.make_request('put', self.valid_url, {}, {})

    def test_exception(self):
        with self.assertRaises(APIConnectionError):
            self.mock_error(self.request_mock)

            self.make_request('get', self.valid_url, {}, {})


class RequestsVerify(object):

    def __eq__(self, other):
        return other and other.endswith('stripe/data/ca-certificates.crt')


class RequestsClientTests(StripeUnitTestCase, ClientTestBase):
    request_client = stripe.http_client.RequestsClient

    def mock_response(self, mock, body, code):
        result = Mock()
        result.content = body
        result.status_code = code

        mock.request = Mock(return_value=result)

    def mock_error(self, mock):
        mock.exceptions.RequestException = Exception
        mock.request.side_effect = mock.exceptions.RequestException()

    def check_call(self, mock, meth, url, post_data, headers):
        mock.request.assert_called_with(meth, url,
                                        headers=headers,
                                        data=post_data,
                                        verify=RequestsVerify(),
                                        timeout=80)


class UrlFetchClientTests(StripeUnitTestCase, ClientTestBase):
    request_client = stripe.http_client.UrlFetchClient

    def mock_response(self, mock, body, code):
        result = Mock()
        result.content = body
        result.status_code = code

        mock.fetch = Mock(return_value=result)

    def mock_error(self, mock):
        mock.Error = mock.InvalidURLError = Exception
        mock.fetch.side_effect = mock.InvalidURLError()

    def check_call(self, mock, meth, url, post_data, headers):
        mock.fetch.assert_called_with(
            url=url,
            method=meth,
            headers=headers,
            validate_certificate=True,
            deadline=55,
            payload=post_data
        )


class Urllib2ClientTests(StripeUnitTestCase, ClientTestBase):
    request_client = stripe.http_client.Urllib2Client

    def mock_response(self, mock, body, code):
        response = Mock
        response.read = Mock(return_value=body)
        response.code = code

        self.request_object = Mock()
        mock.Request = Mock(return_value=self.request_object)

        mock.urlopen = Mock(return_value=response)

    def mock_error(self, mock):
        mock.URLError = Exception
        mock.urlopen.side_effect = mock.URLError()

    def check_call(self, mock, meth, url, post_data, headers):
        mock.Request.assert_called_with(url, post_data, headers)
        mock.urlopen.assert_called_with(self.request_object)


# TODO: We don't currently unittest pycurl because it's a pain
# integration tests will have to suffice for now

if __name__ == '__main__':
    unittest.main()
