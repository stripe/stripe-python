from __future__ import absolute_import, division, print_function

import calendar
import datetime
import platform
import time
import warnings

import stripe
from stripe import error, oauth_error, http_client, version, util, six
from stripe.multipart_data_generator import MultipartDataGenerator
from stripe.six.moves.urllib.parse import urlencode, urlsplit, urlunsplit
from stripe.stripe_response import StripeResponse


def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt='%s[%s]'):
    d = {}
    for subkey, subvalue in six.iteritems(data):
        d[fmt % (key, subkey)] = subvalue
    return d


def _api_encode(data):
    for key, value in six.iteritems(data):
        key = util.utf8(key)
        if value is None:
            continue
        elif hasattr(value, 'stripe_id'):
            yield (key, value.stripe_id)
        elif isinstance(value, list) or isinstance(value, tuple):
            for sv in value:
                if isinstance(sv, dict):
                    subdict = _encode_nested_dict(key, sv, fmt='%s[][%s]')
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield ("%s[]" % (key,), util.utf8(sv))
        elif isinstance(value, dict):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, util.utf8(value))


def _build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlunsplit((scheme, netloc, path, query, fragment))


class APIRequestor(object):

    def __init__(self, key=None, client=None, api_base=None, api_version=None,
                 account=None):
        self.api_base = api_base or stripe.api_base
        self.api_key = key
        self.api_version = api_version or stripe.api_version
        self.stripe_account = account

        from stripe import verify_ssl_certs as verify
        from stripe import proxy

        self._client = client or stripe.default_http_client or \
            http_client.new_default_http_client(
                verify_ssl_certs=verify, proxy=proxy)

    @classmethod
    def api_url(cls, url=''):
        warnings.warn(
            'The `api_url` class method of APIRequestor is '
            'deprecated and will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning)
        return '%s%s' % (stripe.api_base, url)

    @classmethod
    def _deprecated_encode(cls, stk, key, value):
        warnings.warn(
            'The encode_* class methods of APIRequestor are deprecated and '
            'will be removed in version 2.0. '
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning, stacklevel=2)
        stk.extend(_api_encode({key: value}))

    @classmethod
    def encode_dict(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_list(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_datetime(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_none(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode(cls, d):
        """
        Internal: encode a string for url representation
        """
        warnings.warn(
            'The `encode` class method of APIRequestor is deprecated and '
            'will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning)
        return urlencode(list(_api_encode(d)))

    @classmethod
    def build_url(cls, url, params):
        warnings.warn(
            'The `build_url` class method of APIRequestor is deprecated and '
            'will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning)
        return _build_api_url(url, cls.encode(params))

    @classmethod
    def format_app_info(cls, info):
        str = info['name']
        if info['version']:
            str += "/%s" % (info['version'],)
        if info['url']:
            str += " (%s)" % (info['url'],)
        return str

    def request(self, method, url, params=None, headers=None):
        rbody, rcode, rheaders, my_api_key = self.request_raw(
            method.lower(), url, params, headers)
        resp = self.interpret_response(rbody, rcode, rheaders)
        return resp, my_api_key

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_data = resp['error']
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        err = None

        # OAuth errors are a JSON object where `error` is a string. In
        # contrast, in API errors, `error` is a hash with sub-keys. We use
        # this property to distinguish between OAuth and API errors.
        if isinstance(error_data, six.string_types):
            err = self.specific_oauth_error(
                rbody, rcode, resp, rheaders, error_data)

        if err is None:
            err = self.specific_api_error(
                rbody, rcode, resp, rheaders, error_data)

        raise err

    def specific_api_error(self, rbody, rcode, resp, rheaders, error_data):
        util.log_info(
            'Stripe API error received',
            error_code=error_data.get('code'),
            error_type=error_data.get('type'),
            error_message=error_data.get('message'),
            error_param=error_data.get('param'),
        )

        # Rate limits were previously coded as 400's with code 'rate_limit'
        if rcode == 429 or (rcode == 400 and
                            error_data.get('code') == 'rate_limit'):
            return error.RateLimitError(
                error_data.get('message'), rbody, rcode, resp, rheaders)
        elif rcode in [400, 404]:
            if error_data.get('type') == "idempotency_error":
                return error.IdempotencyError(
                    error_data.get('message'), rbody, rcode, resp, rheaders)
            else:
                return error.InvalidRequestError(
                    error_data.get('message'), error_data.get('param'),
                    error_data.get('code'), rbody, rcode, resp, rheaders)
        elif rcode == 401:
            return error.AuthenticationError(
                error_data.get('message'), rbody, rcode, resp, rheaders)
        elif rcode == 402:
            return error.CardError(
                error_data.get('message'), error_data.get('param'),
                error_data.get('code'), rbody, rcode, resp, rheaders)
        elif rcode == 403:
            return error.PermissionError(
                error_data.get('message'), rbody, rcode, resp, rheaders)
        else:
            return error.APIError(
                error_data.get('message'), rbody, rcode, resp, rheaders)

    def specific_oauth_error(self, rbody, rcode, resp, rheaders, error_code):
        description = resp.get('error_description', error_code)

        util.log_info(
            'Stripe OAuth error received',
            error_code=error_code,
            error_description=description,
        )

        args = [
            error_code,
            description,
            rbody,
            rcode,
            resp,
            rheaders
        ]

        if error_code == 'invalid_client':
            return oauth_error.InvalidClientError(*args)
        elif error_code == 'invalid_grant':
            return oauth_error.InvalidGrantError(*args)
        elif error_code == 'invalid_request':
            return oauth_error.InvalidRequestError(*args)
        elif error_code == 'invalid_scope':
            return oauth_error.InvalidScopeError(*args)
        elif error_code == 'unsupported_grant_type':
            return oauth_error.UnsupportedGrantTypError(*args)
        elif error_code == 'unsupported_response_type':
            return oauth_error.UnsupportedResponseTypError(*args)

        return None

    def request_headers(self, api_key, method):
        user_agent = 'Stripe/v1 PythonBindings/%s' % (version.VERSION,)
        if stripe.app_info:
            user_agent += " " + self.format_app_info(stripe.app_info)

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
            except Exception as e:
                val = "!! %s" % (e,)
            ua[attr] = val
        if stripe.app_info:
            ua['application'] = stripe.app_info

        headers = {
            'X-Stripe-Client-User-Agent': util.json.dumps(ua),
            'User-Agent': user_agent,
            'Authorization': 'Bearer %s' % (api_key,),
        }

        if self.stripe_account:
            headers['Stripe-Account'] = self.stripe_account

        if method == 'post':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if self.api_version is not None:
            headers['Stripe-Version'] = self.api_version

        return headers

    def request_raw(self, method, url, params=None, supplied_headers=None):
        """
        Mechanism for issuing an API call
        """

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

        abs_url = '%s%s' % (self.api_base, url)

        encoded_params = urlencode(list(_api_encode(params or {})))

        if method == 'get' or method == 'delete':
            if params:
                abs_url = _build_api_url(abs_url, encoded_params)
            post_data = None
        elif method == 'post':
            if supplied_headers is not None and \
                    supplied_headers.get("Content-Type") == \
                    "multipart/form-data":
                generator = MultipartDataGenerator()
                generator.add_params(params or {})
                post_data = generator.get_post_data()
                supplied_headers["Content-Type"] = \
                    "multipart/form-data; boundary=%s" % (generator.boundary,)
            else:
                post_data = encoded_params
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Stripe bindings.  Please contact support@stripe.com for '
                'assistance.' % (method,))

        headers = self.request_headers(my_api_key, method)

        if supplied_headers is not None:
            for key, value in six.iteritems(supplied_headers):
                headers[key] = value

        util.log_info('Request to Stripe api', method=method, path=abs_url)
        util.log_debug(
            'Post details',
            post_data=encoded_params, api_version=self.api_version)

        rbody, rcode, rheaders = self._client.request(
            method, abs_url, headers, post_data)

        util.log_info(
            'Stripe API response', path=abs_url, response_code=rcode)
        util.log_debug('API response body', body=rbody)
        if 'Request-Id' in rheaders:
            util.log_debug('Dashboard link for request',
                           link=util.dashboard_link(rheaders['Request-Id']))
        return rbody, rcode, rheaders, my_api_key

    def interpret_response(self, rbody, rcode, rheaders):
        try:
            if hasattr(rbody, 'decode'):
                rbody = rbody.decode('utf-8')
            resp = StripeResponse(rbody, rcode, rheaders)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody, rcode, rheaders)
        if not (200 <= rcode < 300):
            self.handle_error_response(rbody, rcode, resp.data, rheaders)

        return resp

    # Deprecated request handling.  Will all be removed in 2.0
    def _deprecated_request(self, impl, method, url, headers, params):
        warnings.warn(
            'The *_request functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead',
            DeprecationWarning, stacklevel=2)

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
            'The handle_*_error functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead',
            DeprecationWarning, stacklevel=2)

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
        return self._deprecated_handle_error(Urllib2Client, err, abs_url)
