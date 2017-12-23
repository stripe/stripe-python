from __future__ import absolute_import, division, print_function

import pytest

import stripe
from stripe import six

VALID_API_METHODS = ('get', 'post', 'delete')


class StripeClientTestCase(object):
    REQUEST_LIBRARIES = ['urlfetch', 'requests', 'pycurl', 'urllib.request']

    @pytest.fixture
    def request_mocks(self, mocker):
        request_mocks = {}
        for lib in self.REQUEST_LIBRARIES:
            request_mocks[lib] = mocker.patch("stripe.http_client.%s" % (lib,))
        return request_mocks


class TestNewDefaultHttpClient(StripeClientTestCase):
    @pytest.fixture(autouse=True)
    def setup_warnings(self, request_mocks):
        original_filters = stripe.http_client.warnings.filters[:]
        stripe.http_client.warnings.simplefilter('ignore')
        yield
        stripe.http_client.warnings.filters = original_filters

    def check_default(self, none_libs, expected):
        for lib in none_libs:
            setattr(stripe.http_client, lib, None)

        inst = stripe.http_client.new_default_http_client()

        assert isinstance(inst, expected)

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


class ClientTestBase(object):
    @pytest.fixture
    def request_mock(self, request_mocks):
        return request_mocks[self.REQUEST_CLIENT.name]

    @property
    def valid_url(self, path='/foo'):
        return 'https://api.stripe.com%s' % (path,)

    def make_request(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return client.request(method, url, headers, post_data)

    @pytest.fixture
    def mock_response(self):
        def mock_response(mock, body, code):
            raise NotImplementedError(
                'You must implement this in your test subclass')
        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock, error):
            raise NotImplementedError(
                'You must implement this in your test subclass')
        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(mock, method, abs_url, headers, params):
            raise NotImplementedError(
                'You must implement this in your test subclass')
        return check_call

    def test_request(self, request_mock, mock_response, check_call):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = ''

            if method != 'post':
                abs_url = '%s?%s' % (abs_url, data)
                data = None

            headers = {'my-header': 'header val'}

            body, code, _ = self.make_request(
                method, abs_url, headers, data)

            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call(request_mock, method, abs_url, data, headers)

    def test_exception(self, request_mock, mock_error):
        mock_error(request_mock)
        with pytest.raises(stripe.error.APIConnectionError):
            self.make_request('get', self.valid_url, {}, None)


class RequestsVerify(object):
    def __eq__(self, other):
        return other and other.endswith('stripe/data/ca-certificates.crt')


class TestRequestsClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT = stripe.http_client.RequestsClient

    @pytest.fixture
    def session(self, mocker, request_mocks):
        return mocker.MagicMock()

    @pytest.fixture
    def mock_response(self, mocker, session):
        def mock_response(mock, body, code):
            result = mocker.Mock()
            result.content = body
            result.status_code = code

            session.request = mocker.MagicMock(return_value=result)
            mock.Session = mocker.MagicMock(return_value=session)
        return mock_response

    @pytest.fixture
    def mock_error(self, mocker, session):
        def mock_error(mock):
            mock.exceptions.RequestException = Exception
            session.request.side_effect = mock.exceptions.RequestException()
            mock.Session = mocker.MagicMock(return_value=session)
        return mock_error

    # Note that unlike other modules, we don't use the "mock" argument here
    # because we need to run the request call against the internal mock
    # session.
    @pytest.fixture
    def check_call(self, session):
        def check_call(mock, method, url, post_data, headers, timeout=80):
            session.request. \
                assert_called_with(method, url,
                                   headers=headers,
                                   data=post_data,
                                   verify=RequestsVerify(),
                                   proxies={"http": "http://slap/",
                                            "https": "http://slap/"},
                                   timeout=timeout)
        return check_call

    def make_request(self, method, url, headers, post_data, timeout=80):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True,
                                     timeout=timeout,
                                     proxy='http://slap/')
        return client.request(method, url, headers, post_data)

    def test_timeout(self, request_mock, mock_response, check_call):
        headers = {'my-header': 'header val'}
        data = ''
        mock_response(request_mock, '{"foo": "baz"}', 200)
        self.make_request('POST', self.valid_url,
                          headers, data, timeout=5)

        check_call(None, 'POST', self.valid_url, data, headers, timeout=5)


class TestUrlFetchClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT = stripe.http_client.UrlFetchClient

    @pytest.fixture
    def mock_response(self, mocker):
        def mock_response(mock, body, code):
            result = mocker.Mock()
            result.content = body
            result.status_code = code

            mock.fetch = mocker.Mock(return_value=result)
        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            mock.Error = mock.InvalidURLError = Exception
            mock.fetch.side_effect = mock.InvalidURLError()
        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(mock, method, url, post_data, headers):
            mock.fetch.assert_called_with(
                url=url,
                method=method,
                headers=headers,
                validate_certificate=True,
                deadline=55,
                payload=post_data
            )
        return check_call


class TestUrllib2Client(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT = stripe.http_client.Urllib2Client

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.client = self.REQUEST_CLIENT(verify_ssl_certs=True,
                                          proxy=proxy)
        self.proxy = proxy
        return self.client.request(method, url, headers, post_data)

    @pytest.fixture
    def mock_response(self, mocker):
        def mock_response(mock, body, code):
            response = mocker.Mock()
            response.read = mocker.Mock(return_value=body)
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
        def check_call(mock, method, url, post_data, headers):
            if six.PY3 and isinstance(post_data, six.string_types):
                post_data = post_data.encode('utf-8')

            mock.Request.assert_called_with(url, post_data, headers)

            if self.client._proxy:
                assert type(self.client._proxy) is dict
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
                    method, url, headers, post_data,
                    {"http": "http://slap/",
                     "https": "http://slap/"})


class TestUrllib2ClientHttpProxy(TestUrllib2Client):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestUrllib2ClientHttpProxy, self).make_request(
                    method, url, headers, post_data,
                    "http://slap/")


class TestPycurlClient(StripeClientTestCase, ClientTestBase):
    REQUEST_CLIENT = stripe.http_client.PycurlClient

    def make_request(self, method, url, headers, post_data, proxy=None):
        self.client = self.REQUEST_CLIENT(verify_ssl_certs=True,
                                          proxy=proxy)
        self.proxy = proxy
        return self.client.request(method, url, headers, post_data)

    @pytest.fixture
    def curl_mock(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def request_mock(self, mocker, request_mocks, curl_mock):
        lib_mock = request_mocks[self.REQUEST_CLIENT.name]
        lib_mock.Curl = mocker.Mock(return_value=curl_mock)
        return curl_mock

    @pytest.fixture
    def bio_getvalue(self, mocker):
        bio_patcher = mocker.patch('stripe.util.io.BytesIO')
        bio_mock = mocker.Mock()
        bio_patcher.return_value = bio_mock
        bio_getvalue = bio_mock.getvalue
        return bio_getvalue

    @pytest.fixture
    def mock_response(self, bio_getvalue):
        def mock_response(mock, body, code):
            bio_getvalue.return_value = body.encode('utf-8')
            mock.getinfo.return_value = code
        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock):
            class FakeException(BaseException):
                @property
                def args(self):
                    return ('foo', 'bar')

            stripe.http_client.pycurl.error = FakeException
            mock.perform.side_effect = stripe.http_client.pycurl.error
        return mock_error

    @pytest.fixture
    def check_call(self, request_mocks):
        def check_call(mock, method, url, post_data, headers):
            lib_mock = request_mocks[self.REQUEST_CLIENT.name]

            # A note on methodology here: we don't necessarily need to verify
            # _every_ call to setopt, but check a few of them to make sure the
            # right thing is happening. Keep an eye specifically on conditional
            # statements where things are more likely to go wrong.

            mock.setopt.assert_any_call(lib_mock.NOSIGNAL, 1)
            mock.setopt.assert_any_call(lib_mock.URL, stripe.util.utf8(url))

            if method == 'get':
                mock.setopt.assert_any_call(lib_mock.HTTPGET, 1)
            elif method == 'post':
                mock.setopt.assert_any_call(lib_mock.POST, 1)
            else:
                mock.setopt.assert_any_call(lib_mock.CUSTOMREQUEST,
                                            method.upper())

            mock.perform.assert_any_call()
        return check_call


class TestPycurlClientHttpProxy(TestPycurlClient):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpProxy, self).make_request(
                    method, url, headers, post_data,
                    "http://user:withPwd@slap:8888/")

    @pytest.fixture
    def check_call(self, request_mocks, curl_mock):
        def check_call(mock, meth, url, post_data, headers):
            lib_mock = request_mocks[self.REQUEST_CLIENT.name]

            curl_mock.setopt.assert_any_call(lib_mock.PROXY, "slap")
            curl_mock.setopt.assert_any_call(lib_mock.PROXYPORT, 8888)
            curl_mock.setopt.assert_any_call(lib_mock.PROXYUSERPWD,
                                             "user:withPwd")

            super(TestPycurlClientHttpProxy, self).check_call(request_mocks)(
                mock, meth, url, post_data, headers)
        return check_call


class TestPycurlClientHttpsProxy(TestPycurlClient):
    def make_request(self, method, url, headers, post_data, proxy=None):
        return super(TestPycurlClientHttpsProxy, self).make_request(
                    method, url, headers, post_data,
                    {"http": "http://slap:8888/",
                     "https": "http://slap2:444/"})

    @pytest.fixture
    def check_call(self, request_mocks, curl_mock):
        def check_call(mock, meth, url, post_data, headers):
            lib_mock = request_mocks[self.REQUEST_CLIENT.name]

            curl_mock.setopt.assert_any_call(lib_mock.PROXY, "slap2")
            curl_mock.setopt.assert_any_call(lib_mock.PROXYPORT, 444)

            super(TestPycurlClientHttpsProxy, self).check_call(request_mocks)(
                mock, meth, url, post_data, headers)
        return check_call


class TestAPIEncode(StripeClientTestCase):

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

        assert ('foo[dob][month]', 1) in values
        assert ('foo[name]', 'bat') in values

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

        assert ('foo[][dob][month]', 1) in values
        assert ('foo[][name]', 'bat') in values
