import calendar
import datetime
import platform
import time
import types
import urllib
import urlparse
import warnings

# TODO: replace api_base import somehow
import stripe
from stripe import error, http_client, version, util


class APIRequestor(object):

    def __init__(self, key=None, client=None):
        self.api_key = key

        # TODO: This should be handled by passing a custom http_client,
        # not setting a global variable
        from stripe import verify_ssl_certs

        self._client = client or http_client.new_default_http_client(
            verify_ssl_certs=verify_ssl_certs)

    @classmethod
    def api_url(cls, url=''):
        return '%s%s' % (stripe.api_base, url)

    @classmethod
    def encode_dict(cls, stk, key, dictvalue):
        n = {}
        for k, v in dictvalue.iteritems():
            k = util.utf8(k)
            v = util.utf8(v)
            n["%s[%s]" % (key, k)] = v
        stk.extend(cls._encode_inner(n))

    @classmethod
    def encode_list(cls, stk, key, listvalue):
        for v in listvalue:
            v = util.utf8(v)
            stk.append(("%s[]" % (key,), v))

    @classmethod
    def encode_datetime(cls, stk, key, dttime):
        if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
            utc_timestamp = calendar.timegm(dttime.utctimetuple())
        else:
            utc_timestamp = time.mktime(dttime.timetuple())

        stk.append((key, int(utc_timestamp)))

    @classmethod
    def encode_none(cls, stk, k, v):
        pass  # do not include None-valued params in request

    @classmethod
    def _encode_inner(cls, d):
        """
        We want post vars of form:
        {'foo': 'bar', 'nested': {'a': 'b', 'c': 'd'}}
        to become:
        foo=bar&nested[a]=b&nested[c]=d
        """
        # special case value encoding
        ENCODERS = {
            list: cls.encode_list,
            dict: cls.encode_dict,
            datetime.datetime: cls.encode_datetime,
            types.NoneType: cls.encode_none,
        }

        stk = []
        for key, value in d.iteritems():
            key = util.utf8(key)
            try:
                encoder = ENCODERS[value.__class__]
                encoder(stk, key, value)
            except KeyError:
                # don't need special encoding
                value = util.utf8(value)
                stk.append((key, value))
        return stk

    @classmethod
    def _objects_to_ids(cls, d):
        if hasattr(d, 'stripe_id'):
            return d.stripe_id
        elif isinstance(d, dict):
            res = {}
            for k, v in d.iteritems():
                res[k] = cls._objects_to_ids(v)
            return res
        else:
            return d

    @classmethod
    def encode(cls, d):
        """
        Internal: encode a string for url representation
        """
        return urllib.urlencode(cls._encode_inner(d))

    @classmethod
    def build_url(cls, url, params):
        scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)

        query = cls.encode(params)

        if base_query:
            query = '%s&%s' % (base_query, query)

        return urlparse.urlunsplit((scheme, netloc, path, query, fragment))

    def request(self, method, url, params=None):
        rbody, rcode, my_api_key = self.request_raw(
            method.lower(), url, params)
        resp = self.interpret_response(rbody, rcode)
        return resp, my_api_key

    def handle_api_error(self, rbody, rcode, resp):
        try:
            err = resp['error']
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r (HTTP response code"
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        if rcode in [400, 404]:
            raise error.InvalidRequestError(
                err.get('message'), err.get('param'), rbody, rcode, resp)
        elif rcode == 401:
            raise error.AuthenticationError(
                err.get('message'), rbody, rcode, resp)
        elif rcode == 402:
            raise error.CardError(err.get('message'), err.get('param'),
                                  err.get('code'), rbody, rcode, resp)
        else:
            raise error.APIError(err.get('message'), rbody, rcode, resp)

    def request_raw(self, method, url, params=None):
        """
        Mechanism for issuing an API call
        """
        from stripe import api_version

        if self.api_key:
            my_api_key = self.api_key
        else:
            from stripe import api_key
            my_api_key = api_key

        if my_api_key is None:
            raise error.AuthenticationError(
                'No API key provided. (HINT: set your API key using '
                '"stripe.api_key = <API-KEY>"). You can generate API keys '
                'from the Stripe web interface.  See https://stripe.com/api '
                'for details, or email support@stripe.com if you have any '
                'questions.')

        abs_url = self.api_url(url)

        params = (params or {}).copy()
        self._objects_to_ids(params)

        if method == 'get' or method == 'delete':
            if params:
                abs_url = self.build_url(abs_url, params)
            post_data = None
        elif method == 'post':
            post_data = self.encode(params)
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Stripe bindings.  Please contact support@stripe.com for '
                'assistance.' % (method,))

        ua = {
            'bindings_version': version.VERSION,
            'lang': 'python',
            'publisher': 'stripe',
            'httplib': self._client.name,
        }
        for attr, func in [['lang_version', platform.python_version],
                           ['platform', platform.platform],
                           ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception, e:
                val = "!! %s" % (e,)
            ua[attr] = val

        headers = {
            'X-Stripe-Client-User-Agent': util.json.dumps(ua),
            'User-Agent': 'Stripe/v1 PythonBindings/%s' % (version.VERSION,),
            'Authorization': 'Bearer %s' % (my_api_key,)
        }

        if api_version is not None:
            headers['Stripe-Version'] = api_version

        rbody, rcode = self._client.request(
            method, abs_url, headers, post_data)

        util.logger.info(
            'API request to %s returned (response code, response body) of '
            '(%d, %r)',
            abs_url, rcode, rbody)
        return rbody, rcode, my_api_key

    def interpret_response(self, rbody, rcode):
        try:
            resp = util.json.loads(rbody.decode('utf-8'))
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody, rcode)
        if not (200 <= rcode < 300):
            self.handle_api_error(rbody, rcode, resp)
        return resp

    # Deprecated request handling.  Will all be removed in 2.0
    def _deprecated_request(self, impl, method, url, headers, params):
        warnings.warn(
            'the *_request functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead', DeprecationWarning)

        method = method.lower()

        if method == 'get' or method == 'delete':
            if params:
                url = self.build_url(url, params)
            post_data = None
        elif method == 'post':
            post_data = self.encode(params)
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Stripe bindings.  Please contact support@stripe.com for '
                'assistance.' % (method,))

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client.request(method, url, headers, post_data)

    def _deprecated_handle_error(self, impl, *args):
        warnings.warn(
            'the handle_*_error functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead', DeprecationWarning)

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client._handle_request_error(*args)

    def requests_request(self, meth, abs_url, headers, params):
        from stripe.http_client import RequestsClient
        return self._deprecated_request(RequestsClient, meth, abs_url,
                                        headers, params)

    def handle_requests_error(self, err):
        from stripe.http_client import RequestsClient
        return self._deprecated_handle_error(RequestsClient, err)

    def pycurl_request(self, meth, abs_url, headers, params):
        from stripe.http_client import PycurlClient
        return self._deprecated_request(PycurlClient, meth, abs_url,
                                        headers, params)

    def handle_pycurl_error(self, err):
        from stripe.http_client import PycurlClient
        return self._deprecated_handle_error(PycurlClient, err)

    def urlfetch_request(self, meth, abs_url, headers, params):
        from stripe.http_client import UrlFetchClient
        return self._deprecated_request(UrlFetchClient, meth, abs_url,
                                        headers, params)

    def handle_urlfetch_error(self, err, abs_url):
        from stripe.http_client import UrlFetchClient
        return self._deprecated_handle_error(UrlFetchClient, err, abs_url)

    def urllib2_request(self, meth, abs_url, headers, params):
        from stripe.http_client import Urllib2Client
        return self._deprecated_request(Urllib2Client, meth, abs_url,
                                        headers, params)

    def handle_urllib2_error(self, err, abs_url):
        from stripe.http_client import Urllib2Client
        return self._deprecated_handle_error(Urllib2Client, err)
