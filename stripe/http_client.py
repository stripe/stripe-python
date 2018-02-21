from __future__ import absolute_import, division, print_function

import os
import sys
import textwrap
import warnings
import email

from stripe import error, util, six

# - Requests is the preferred HTTP library
# - Google App Engine has urlfetch
# - Use Pycurl if it's there (at least it verifies SSL certs)
# - Fall back to urllib2 with a warning if needed
try:
    from stripe.six.moves import urllib
except ImportError:
    # Try to load in urllib2, but don't sweat it if it's not available.
    pass

try:
    import pycurl
except ImportError:
    pycurl = None

try:
    import requests
except ImportError:
    requests = None
else:
    try:
        # Require version 0.8.8, but don't want to depend on distutils
        version = requests.__version__
        major, minor, patch = [int(i) for i in version.split('.')]
    except Exception:
        # Probably some new-fangled version, so it should support verify
        pass
    else:
        if (major, minor, patch) < (0, 8, 8):
            sys.stderr.write(
                'Warning: the Stripe library requires that your Python '
                '"requests" library be newer than version 0.8.8, but your '
                '"requests" library is version %s. Stripe will fall back to '
                'an alternate HTTP library so everything should work. We '
                'recommend upgrading your "requests" library. If you have any '
                'questions, please contact support@stripe.com. (HINT: running '
                '"pip install -U requests" should upgrade your requests '
                'library to the latest version.)' % (version,))
            requests = None

try:
    from google.appengine.api import urlfetch
except ImportError:
    urlfetch = None

# proxy support for the pycurl client
from stripe.six.moves.urllib.parse import urlparse


def new_default_http_client(*args, **kwargs):
    if urlfetch:
        impl = UrlFetchClient
    elif requests:
        impl = RequestsClient
    elif pycurl:
        impl = PycurlClient
    else:
        impl = Urllib2Client
        warnings.warn(
            "Warning: the Stripe library is falling back to urllib2/urllib "
            "because neither requests nor pycurl are installed. "
            "urllib2's SSL implementation doesn't verify server "
            "certificates. For improved security, we suggest installing "
            "requests.")

    return impl(*args, **kwargs)


class HTTPClient(object):
    def __init__(self, verify_ssl_certs=True, proxy=None):
        self._verify_ssl_certs = verify_ssl_certs
        if proxy:
            if type(proxy) is str:
                proxy = {"http": proxy, "https": proxy}
            if not (type(proxy) is dict):
                raise ValueError(
                    "Proxy(ies) must be specified as either a string "
                    "URL or a dict() with string URL under the"
                    " ""https"" and/or ""http"" keys.")
        self._proxy = proxy.copy() if proxy else None

    def request(self, method, url, headers, post_data=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`')


class RequestsClient(HTTPClient):
    name = 'requests'

    def __init__(self, timeout=80, session=None, **kwargs):
        super(RequestsClient, self).__init__(**kwargs)
        self._timeout = timeout
        self._session = session or requests.Session()

    def __del__(self):
        if self._session:
            self._session.close()

    def request(self, method, url, headers, post_data=None):
        kwargs = {}
        if self._verify_ssl_certs:
            kwargs['verify'] = os.path.join(
                os.path.dirname(__file__), 'data/ca-certificates.crt')
        else:
            kwargs['verify'] = False

        if self._proxy:
            kwargs['proxies'] = self._proxy

        try:
            try:
                result = self._session.request(method,
                                               url,
                                               headers=headers,
                                               data=post_data,
                                               timeout=self._timeout,
                                               **kwargs)
            except TypeError as e:
                raise TypeError(
                    'Warning: It looks like your installed version of the '
                    '"requests" library is not compatible with Stripe\'s '
                    'usage thereof. (HINT: The most likely cause is that '
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    'underlying error was: %s' % (e,))

            # This causes the content to actually be read, which could cause
            # e.g. a socket timeout. TODO: The other fetch methods probably
            # are susceptible to the same and should be updated.
            content = result.content
            status_code = result.status_code
        except Exception as e:
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return content, status_code, result.headers

    def _handle_request_error(self, e):
        if isinstance(e, requests.exceptions.RequestException):
            msg = ("Unexpected error communicating with Stripe.  "
                   "If this problem persists, let us know at "
                   "support@stripe.com.")
            err = "%s: %s" % (type(e).__name__, str(e))
        else:
            msg = ("Unexpected error communicating with Stripe. "
                   "It looks like there's probably a configuration "
                   "issue locally.  If this problem persists, let us "
                   "know at support@stripe.com.")
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise error.APIConnectionError(msg)


class UrlFetchClient(HTTPClient):
    name = 'urlfetch'

    def __init__(self, verify_ssl_certs=True, proxy=None, deadline=55):
        super(UrlFetchClient, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy)

        # no proxy support in urlfetch. for a patch, see:
        # https://code.google.com/p/googleappengine/issues/detail?id=544
        if proxy:
            raise ValueError(
                "No proxy support in urlfetch library. "
                "Set stripe.default_http_client to either RequestsClient, "
                "PycurlClient, or Urllib2Client instance to use a proxy.")

        self._verify_ssl_certs = verify_ssl_certs
        # GAE requests time out after 60 seconds, so make sure to default
        # to 55 seconds to allow for a slow Stripe
        self._deadline = deadline

    def request(self, method, url, headers, post_data=None):
        try:
            result = urlfetch.fetch(
                url=url,
                method=method,
                headers=headers,
                # Google App Engine doesn't let us specify our own cert bundle.
                # However, that's ok because the CA bundle they use recognizes
                # api.stripe.com.
                validate_certificate=self._verify_ssl_certs,
                deadline=self._deadline,
                payload=post_data
            )
        except urlfetch.Error as e:
            self._handle_request_error(e, url)

        return result.content, result.status_code, result.headers

    def _handle_request_error(self, e, url):
        if isinstance(e, urlfetch.InvalidURLError):
            msg = ("The Stripe library attempted to fetch an "
                   "invalid URL (%r). This is likely due to a bug "
                   "in the Stripe Python bindings. Please let us know "
                   "at support@stripe.com." % (url,))
        elif isinstance(e, urlfetch.DownloadError):
            msg = "There was a problem retrieving data from Stripe."
        elif isinstance(e, urlfetch.ResponseTooLargeError):
            msg = ("There was a problem receiving all of your data from "
                   "Stripe.  This is likely due to a bug in Stripe. "
                   "Please let us know at support@stripe.com.")
        else:
            msg = ("Unexpected error communicating with Stripe. If this "
                   "problem persists, let us know at support@stripe.com.")

        msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
        raise error.APIConnectionError(msg)


class PycurlClient(HTTPClient):
    name = 'pycurl'

    def __init__(self, verify_ssl_certs=True, proxy=None):
        super(PycurlClient, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy)

        # Initialize this within the object so that we can reuse connections.
        self._curl = pycurl.Curl()

        # need to urlparse the proxy, since PyCurl
        # consumes the proxy url in small pieces
        if self._proxy:
            # now that we have the parser, get the proxy url pieces
            proxy = self._proxy
            for scheme in proxy:
                proxy[scheme] = urlparse(proxy[scheme])

    def parse_headers(self, data):
        if '\r\n' not in data:
            return {}
        raw_headers = data.split('\r\n', 1)[1]
        headers = email.message_from_string(raw_headers)
        return dict((k.lower(), v) for k, v in six.iteritems(dict(headers)))

    def request(self, method, url, headers, post_data=None):
        b = util.io.BytesIO()
        rheaders = util.io.BytesIO()

        # Pycurl's design is a little weird: although we set per-request
        # options on this object, it's also capable of maintaining established
        # connections. Here we call reset() between uses to make sure it's in a
        # pristine state, but notably reset() doesn't reset connections, so we
        # still get to take advantage of those by virtue of re-using the same
        # object.
        self._curl.reset()

        proxy = self._get_proxy(url)
        if proxy:
            if proxy.hostname:
                self._curl.setopt(pycurl.PROXY, proxy.hostname)
            if proxy.port:
                self._curl.setopt(pycurl.PROXYPORT, proxy.port)
            if proxy.username or proxy.password:
                self._curl.setopt(
                    pycurl.PROXYUSERPWD,
                    "%s:%s" % (proxy.username, proxy.password))

        if method == 'get':
            self._curl.setopt(pycurl.HTTPGET, 1)
        elif method == 'post':
            self._curl.setopt(pycurl.POST, 1)
            self._curl.setopt(pycurl.POSTFIELDS, post_data)
        else:
            self._curl.setopt(pycurl.CUSTOMREQUEST, method.upper())

        # pycurl doesn't like unicode URLs
        self._curl.setopt(pycurl.URL, util.utf8(url))

        self._curl.setopt(pycurl.WRITEFUNCTION, b.write)
        self._curl.setopt(pycurl.HEADERFUNCTION, rheaders.write)
        self._curl.setopt(pycurl.NOSIGNAL, 1)
        self._curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        self._curl.setopt(pycurl.TIMEOUT, 80)
        self._curl.setopt(
            pycurl.HTTPHEADER,
            ['%s: %s' % (k, v) for k, v in six.iteritems(dict(headers))]
        )
        if self._verify_ssl_certs:
            self._curl.setopt(pycurl.CAINFO, os.path.join(
                os.path.dirname(__file__), 'data/ca-certificates.crt'))
        else:
            self._curl.setopt(pycurl.SSL_VERIFYHOST, False)

        try:
            self._curl.perform()
        except pycurl.error as e:
            self._handle_request_error(e)
        rbody = b.getvalue().decode('utf-8')
        rcode = self._curl.getinfo(pycurl.RESPONSE_CODE)
        headers = self.parse_headers(rheaders.getvalue().decode('utf-8'))

        return rbody, rcode, headers

    def _handle_request_error(self, e):
        if e.args[0] in [pycurl.E_COULDNT_CONNECT,
                         pycurl.E_COULDNT_RESOLVE_HOST,
                         pycurl.E_OPERATION_TIMEOUTED]:
            msg = ("Could not connect to Stripe.  Please check your "
                   "internet connection and try again.  If this problem "
                   "persists, you should check Stripe's service status at "
                   "https://twitter.com/stripestatus, or let us know at "
                   "support@stripe.com.")
        elif e.args[0] in [pycurl.E_SSL_CACERT,
                           pycurl.E_SSL_PEER_CERTIFICATE]:
            msg = ("Could not verify Stripe's SSL certificate.  Please make "
                   "sure that your network is not intercepting certificates.  "
                   "If this problem persists, let us know at "
                   "support@stripe.com.")
        else:
            msg = ("Unexpected error communicating with Stripe. If this "
                   "problem persists, let us know at support@stripe.com.")

        msg = textwrap.fill(msg) + "\n\n(Network error: " + e.args[1] + ")"
        raise error.APIConnectionError(msg)

    def _get_proxy(self, url):
        if self._proxy:
            proxy = self._proxy
            scheme = url.split(":")[0] if url else None
            if scheme:
                if scheme in proxy:
                    return proxy[scheme]
                scheme = scheme[0:-1]
                if scheme in proxy:
                    return proxy[scheme]
        return None


class Urllib2Client(HTTPClient):
    name = 'urllib.request'

    def __init__(self, verify_ssl_certs=True, proxy=None):
        super(Urllib2Client, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy)
        # prepare and cache proxy tied opener here
        self._opener = None
        if self._proxy:
            proxy = urllib.request.ProxyHandler(self._proxy)
            self._opener = urllib.request.build_opener(proxy)

    def request(self, method, url, headers, post_data=None):
        if six.PY3 and isinstance(post_data, six.string_types):
            post_data = post_data.encode('utf-8')

        req = urllib.request.Request(url, post_data, headers)

        if method not in ('get', 'post'):
            req.get_method = lambda: method.upper()

        try:
            # use the custom proxy tied opener, if any.
            # otherwise, fall to the default urllib opener.
            response = self._opener.open(req) \
                if self._opener \
                else urllib.request.urlopen(req)
            rbody = response.read()
            rcode = response.code
            headers = dict(response.info())
        except urllib.error.HTTPError as e:
            rcode = e.code
            rbody = e.read()
            headers = dict(e.info())
        except (urllib.error.URLError, ValueError) as e:
            self._handle_request_error(e)
        lh = dict((k.lower(), v) for k, v in six.iteritems(dict(headers)))
        return rbody, rcode, lh

    def _handle_request_error(self, e):
        msg = ("Unexpected error communicating with Stripe. "
               "If this problem persists, let us know at support@stripe.com.")
        msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
        raise error.APIConnectionError(msg)
