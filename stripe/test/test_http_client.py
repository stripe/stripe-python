import sys
import unittest2

from mock import Mock, patch

import stripe

from stripe.test.helper import StripeUnitTestCase

VALID_API_METHODS = ('get', 'post', 'delete')


class HttpClientTests(StripeUnitTestCase):

    def setUp(self):
        super(HttpClientTests, self).setUp()

        self.original_filters = stripe.http_client.warnings.filters[:]
        stripe.http_client.warnings.simplefilter('ignore')

    def tearDown(self):
        stripe.http_client.warnings.filters = self.original_filters

        super(HttpClientTests, self).tearDown()

    def check_default(self, none_libs, expected):
        for lib in none_libs:
            setattr(stripe.http_client, lib, None)

        inst = stripe.http_client.new_default_http_client()

        self.assertTrue(isinstance(inst, expected))

    def test_new_default_http_client_urlfetch(self):
        self.check_default((),
                           stripe.http_client.UrlFetchClient)

    def test_new_default_http_client_requests(self):
        self.check_default(('urlfetch',),
                           stripe.http_client.RequestsClient)

    def test_new_default_http_client_pycurl(self):
        self.check_default(('urlfetch', 'requests',),
                           stripe.http_client.PycurlClient)

    def test_new_default_http_client_urllib2(self):
        self.check_default(('urlfetch', 'requests', 'pycurl'),
                           stripe.http_client.Urllib2Client)


class ClientTestBase():

    @property
    def request_mock(self):
        return self.request_mocks[self.request_client.name]

    @property
    def valid_url(self, path='/foo'):
        return 'https://api.stripe.com%s' % (path,)

    def make_request(self, method, url, headers, post_data):
        client = self.request_client(verify_ssl_certs=True)
        return client.request(method, url, headers, post_data)

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
            data = ''

            if meth != 'post':
                abs_url = '%s?%s' % (abs_url, data)
                data = None

            headers = {'my-header': 'header val'}

            body, code, _ = self.make_request(
                meth, abs_url, headers, data)

            self.assertEqual(200, code)
            self.assertEqual('{"foo": "baz"}', body)

            self.check_call(self.request_mock, meth, abs_url,
                            data, headers)

    def test_exception(self):
        self.mock_error(self.request_mock)
        self.assertRaises(stripe.error.APIConnectionError,
                          self.make_request,
                          'get', self.valid_url, {}, None)


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
        response.info = Mock(return_value={})

        self.request_object = Mock()
        mock.Request = Mock(return_value=self.request_object)

        mock.urlopen = Mock(return_value=response)

    def mock_error(self, mock):
        mock.urlopen.side_effect = ValueError

    def check_call(self, mock, meth, url, post_data, headers):
        if sys.version_info >= (3, 0) and isinstance(post_data, basestring):
            post_data = post_data.encode('utf-8')

        mock.Request.assert_called_with(url, post_data, headers)
        mock.urlopen.assert_called_with(self.request_object)


class PycurlClientTests(StripeUnitTestCase, ClientTestBase):
    request_client = stripe.http_client.PycurlClient

    @property
    def request_mock(self):
        if not hasattr(self, 'curl_mock'):
            lib_mock = self.request_mocks[self.request_client.name]

            self.curl_mock = Mock()

            lib_mock.Curl = Mock(return_value=self.curl_mock)

        return self.curl_mock

    def setUp(self):
        super(PycurlClientTests, self).setUp()

        self.sio_patcher = patch('stripe.util.StringIO.StringIO')

        sio_mock = Mock()
        self.sio_patcher.start().return_value = sio_mock
        self.sio_getvalue = sio_mock.getvalue

    def tearDown(self):
        super(PycurlClientTests, self).tearDown()

        self.sio_patcher.stop()

    def mock_response(self, mock, body, code):
        self.sio_getvalue.return_value = body

        mock.getinfo.return_value = code

    def mock_error(self, mock):
        class FakeException(BaseException):

            def __getitem__(self, i):
                return 'foo'

        stripe.http_client.pycurl.error = FakeException
        mock.perform.side_effect = stripe.http_client.pycurl.error

    def check_call(self, mock, meth, url, post_data, headers):
        # TODO: Check the setopt calls
        pass


class APIEncodeTest(StripeUnitTestCase):

    def test_encode_dict(self):
        body = {
            'foo': {
                'dob': {
                    'month': 1,
                },
                'name': 'bat'
            },
        }

        values = [t for t in stripe.api_requestor._api_encode(body)]

        self.assertTrue(('foo[dob][month]', 1) in values)
        self.assertTrue(('foo[name]', 'bat') in values)

    def test_encode_array(self):
        body = {
            'foo': [{
                'dob': {
                    'month': 1,
                },
                'name': 'bat'
            }],
        }

        values = [t for t in stripe.api_requestor._api_encode(body)]

        self.assertTrue(('foo[][dob][month]', 1) in values)
        self.assertTrue(('foo[][name]', 'bat') in values)

if __name__ == '__main__':
    unittest2.main()
