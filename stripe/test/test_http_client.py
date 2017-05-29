import sys
import unittest2

from mock import MagicMock, Mock, patch

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

    def setUp(self):
        super(RequestsClientTests, self).setUp()
        self.session = MagicMock()

    def test_timeout(self):
        headers = {'my-header': 'header val'}
        data = ''
        self.mock_response(self.request_mock, '{"foo": "baz"}', 200)
        self.make_request('POST', self.valid_url,
                          headers, data, timeout=5)

        self.check_call(None, 'POST', self.valid_url,
                        data, headers, timeout=5)

    def make_request(self, method, url, headers, post_data, timeout=80):
        client = self.request_client(verify_ssl_certs=True,
                                     timeout=timeout,
                                     proxy='http://slap/')

        return client.request(method, url, headers, post_data)

    def mock_response(self, mock, body, code):
        result = Mock()
        result.content = body
        result.status_code = code

        self.session.request = MagicMock(return_value=result)
        mock.Session = MagicMock(return_value=self.session)

    def mock_error(self, mock):
        mock.exceptions.RequestException = Exception
        self.session.request.side_effect = mock.exceptions.RequestException()
        mock.Session = MagicMock(return_value=self.session)

    # Note that unlike other modules, we don't use the "mock" argument here
    # because we need to run the request call against the internal mock
    # session.
    def check_call(self, mock, meth, url, post_data, headers, timeout=80):
        self.session.request. \
            assert_called_with(meth, url,
                               headers=headers,
                               data=post_data,
                               verify=RequestsVerify(),
                               proxies={"http": "http://slap/",
                                        "https": "http://slap/"},
                               timeout=timeout)


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

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.client = self.request_client(verify_ssl_certs=True,
                                          proxy=proxy)
        self.proxy = proxy
        return self.client.request(method, url, headers, post_data)

    def mock_response(self, mock, body, code):
        response = Mock
        response.read = Mock(return_value=body)
        response.code = code
        response.info = Mock(return_value={})

        self.request_object = Mock()
        mock.Request = Mock(return_value=self.request_object)

        mock.urlopen = Mock(return_value=response)

        opener = Mock
        opener.open = Mock(return_value=response)
        mock.build_opener = Mock(return_value=opener)
        mock.build_opener.open = opener.open
        mock.ProxyHandler = Mock(return_value=opener)

        mock.urlopen = Mock(return_value=response)

    def mock_error(self, mock):
        mock.urlopen.side_effect = ValueError
        mock.build_opener().open.side_effect = ValueError
        mock.build_opener.reset_mock()

    def check_call(self, mock, meth, url, post_data, headers):
        if sys.version_info >= (3, 0) and isinstance(post_data, basestring):
            post_data = post_data.encode('utf-8')

        mock.Request.assert_called_with(url, post_data, headers)

        if (self.client._proxy):
            self.assertTrue(type(self.client._proxy) is dict)
            mock.ProxyHandler.assert_called_with(self.client._proxy)
            mock.build_opener.open.assert_called_with(self.request_object)
            self.assertTrue(not mock.urlopen.called)

        if (not self.client._proxy):
            mock.urlopen.assert_called_with(self.request_object)
            self.assertTrue(not mock.build_opener.called)
            self.assertTrue(not mock.build_opener.open.called)


class Urllib2ClientHttpsProxyTests(Urllib2ClientTests):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(Urllib2ClientHttpsProxyTests, self).make_request(
                    method, url, headers, post_data,
                    {"http": "http://slap/",
                     "https": "http://slap/"})


class Urllib2ClientHttpProxyTests(Urllib2ClientTests):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(Urllib2ClientHttpProxyTests, self).make_request(
                    method, url, headers, post_data,
                    "http://slap/")


class PycurlClientTests(StripeUnitTestCase, ClientTestBase):
    request_client = stripe.http_client.PycurlClient

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.client = self.request_client(verify_ssl_certs=True,
                                          proxy=proxy)
        self.proxy = proxy
        return self.client.request(method, url, headers, post_data)

    @property
    def request_mock(self):
        if not hasattr(self, 'curl_mock'):
            lib_mock = self.request_mocks[self.request_client.name]

            self.curl_mock = Mock()

            lib_mock.Curl = Mock(return_value=self.curl_mock)

        return self.curl_mock

    def setUp(self):
        super(PycurlClientTests, self).setUp()

        self.bio_patcher = patch('stripe.util.io.BytesIO')

        bio_mock = Mock()
        self.bio_patcher.start().return_value = bio_mock
        self.bio_getvalue = bio_mock.getvalue

    def tearDown(self):
        super(PycurlClientTests, self).tearDown()

        self.bio_patcher.stop()

    def mock_response(self, mock, body, code):
        self.bio_getvalue.return_value = body.encode('utf-8')

        mock.getinfo.return_value = code

    def mock_error(self, mock):
        class FakeException(BaseException):
            @property
            def args(self):
                return ('foo', 'bar')

        stripe.http_client.pycurl.error = FakeException
        mock.perform.side_effect = stripe.http_client.pycurl.error

    def check_call(self, mock, meth, url, post_data, headers):
        lib_mock = self.request_mocks[self.request_client.name]

        # A note on methodology here: we don't necessarily need to verify
        # _every_ call to setopt, but check a few of them to make sure the
        # right thing is happening. Keep an eye specifically on conditional
        # statements where things are more likely to go wrong.

        self.curl_mock.setopt.assert_any_call(lib_mock.NOSIGNAL, 1)
        self.curl_mock.setopt.assert_any_call(lib_mock.URL,
                                              stripe.util.utf8(url))

        if meth == 'get':
            self.curl_mock.setopt.assert_any_call(lib_mock.HTTPGET, 1)
        elif meth == 'post':
            self.curl_mock.setopt.assert_any_call(lib_mock.POST, 1)
        else:
            self.curl_mock.setopt.assert_any_call(lib_mock.CUSTOMREQUEST,
                                                  meth.upper())

        self.curl_mock.perform.assert_any_call()


class PycurlClientHttpProxyTests(PycurlClientTests):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(PycurlClientHttpProxyTests, self).make_request(
                    method, url, headers, post_data,
                    "http://user:withPwd@slap:8888/")

    def check_call(self, mock, meth, url, post_data, headers):
        lib_mock = self.request_mocks[self.request_client.name]

        self.curl_mock.setopt.assert_any_call(lib_mock.PROXY, "slap")
        self.curl_mock.setopt.assert_any_call(lib_mock.PROXYPORT, 8888)
        self.curl_mock.setopt.assert_any_call(lib_mock.PROXYUSERPWD,
                                              "user:withPwd")

        super(PycurlClientHttpProxyTests, self).check_call(
                mock, meth, url, post_data, headers)


class PycurlClientHttpsProxyTests(PycurlClientTests):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(PycurlClientHttpsProxyTests, self).make_request(
                    method, url, headers, post_data,
                    {"http": "http://slap:8888/",
                     "https": "http://slap2:444/"})

    def check_call(self, mock, meth, url, post_data, headers):
        lib_mock = self.request_mocks[self.request_client.name]

        self.curl_mock.setopt.assert_any_call(lib_mock.PROXY, "slap2")
        self.curl_mock.setopt.assert_any_call(lib_mock.PROXYPORT, 444)

        super(PycurlClientHttpsProxyTests, self).check_call(
                mock, meth, url, post_data, headers)


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
