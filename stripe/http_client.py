import sys
import textwrap
import warnings
import email
import time
import random
import threading
import json

import stripe
from stripe import error, util
from stripe.request_metrics import RequestMetrics

from typing import Optional
from typing_extensions import NoReturn, TypedDict

# - Requests is the preferred HTTP library
# - Google App Engine has urlfetch
# - Use Pycurl if it's there (at least it verifies SSL certs)
# - Fall back to urllib2 with a warning if needed
try:
    import urllib.request as urllibrequest
    import urllib.error as urlliberror
except ImportError:
    # Try to load in urllib2, but don't sweat it if it's not available.
    pass

try:
    import pycurl  # pyright: ignore
except ImportError:
    pycurl = None

try:
    import requests  # pyright: ignore
except ImportError:
    requests = None
else:
    try:
        # Require version 0.8.8, but don't want to depend on distutils
        version = requests.__version__
        major, minor, patch = [int(i) for i in version.split(".")]
    except Exception:
        # Probably some new-fangled version, so it should support verify
        pass
    else:
        if (major, minor, patch) < (0, 8, 8):
            sys.stderr.write(
                "Warning: the Stripe library requires that your Python "
                '"requests" library be newer than version 0.8.8, but your '
                '"requests" library is version %s. Stripe will fall back to '
                "an alternate HTTP library so everything should work. We "
                'recommend upgrading your "requests" library. If you have any '
                "questions, please contact support@stripe.com. (HINT: running "
                '"pip install -U requests" should upgrade your requests '
                "library to the latest version.)" % (version,)
            )
            requests = None

try:
    from google.appengine.api import urlfetch  # type: ignore
except ImportError:
    urlfetch = None

# proxy support for the pycurl client
from urllib.parse import urlparse, ParseResult


def _now_ms():
    return int(round(time.time() * 1000))


def new_default_http_client(*args, **kwargs):
    if urlfetch:
        impl = UrlFetchClient
    elif requests:
        impl = RequestsClient
    elif pycurl:
        impl = PycurlClient
    else:
        impl = Urllib2Client
        if sys.version_info < (2, 7, 9):
            warnings.warn(
                "Warning: the Stripe library is falling back to urllib2 "
                "because neither requests nor pycurl are installed. "
                "urllib2's SSL implementation doesn't verify server "
                "certificates. For improved security, we suggest installing "
                "requests."
            )

    return impl(*args, **kwargs)


class HTTPClient(object):
    class _Proxy(TypedDict):
        http: Optional[str]
        https: Optional[str]

    MAX_DELAY = 2
    INITIAL_DELAY = 0.5
    MAX_RETRY_AFTER = 60
    proxy: _Proxy

    def __init__(self, verify_ssl_certs=True, proxy=None):
        self._verify_ssl_certs = verify_ssl_certs
        if proxy:
            if isinstance(proxy, str):
                proxy = {"http": proxy, "https": proxy}
            if not isinstance(proxy, dict):
                raise ValueError(
                    "Proxy(ies) must be specified as either a string "
                    "URL or a dict() with string URL under the"
                    " "
                    "https"
                    " and/or "
                    "http"
                    " keys."
                )
        self._proxy = proxy.copy() if proxy else None

        self._thread_local = threading.local()

    def request_with_retries(self, method, url, headers, post_data=None):
        return self._request_with_retries_internal(
            method, url, headers, post_data, is_streaming=False
        )

    def request_stream_with_retries(
        self, method, url, headers, post_data=None
    ):
        return self._request_with_retries_internal(
            method, url, headers, post_data, is_streaming=True
        )

    def _request_with_retries_internal(
        self, method, url, headers, post_data, is_streaming
    ):
        self._add_telemetry_header(headers)

        num_retries = 0

        while True:
            request_start = _now_ms()

            try:
                if is_streaming:
                    response = self.request_stream(
                        method, url, headers, post_data
                    )
                else:
                    response = self.request(method, url, headers, post_data)
                connection_error = None
            except error.APIConnectionError as e:
                connection_error = e
                response = None

            if self._should_retry(response, connection_error, num_retries):
                if connection_error:
                    util.log_info(
                        "Encountered a retryable error %s"
                        % connection_error.user_message
                    )
                num_retries += 1
                sleep_time = self._sleep_time_seconds(num_retries, response)
                util.log_info(
                    (
                        "Initiating retry %i for request %s %s after "
                        "sleeping %.2f seconds."
                        % (num_retries, method, url, sleep_time)
                    )
                )
                time.sleep(sleep_time)
            else:
                if response is not None:
                    self._record_request_metrics(response, request_start)

                    return response
                else:
                    assert connection_error is not None
                    raise connection_error

    def request(self, method, url, headers, post_data=None):
        raise NotImplementedError(
            "HTTPClient subclasses must implement `request`"
        )

    def request_stream(self, method, url, headers, post_data=None):
        raise NotImplementedError(
            "HTTPClient subclasses must implement `request_stream`"
        )

    def _should_retry(self, response, api_connection_error, num_retries):
        if num_retries >= self._max_network_retries():
            return False

        if response is None:
            # We generally want to retry on timeout and connection
            # exceptions, but defer this decision to underlying subclass
            # implementations. They should evaluate the driver-specific
            # errors worthy of retries, and set flag on the error returned.
            return api_connection_error.should_retry

        _, status_code, rheaders = response

        # The API may ask us not to retry (eg; if doing so would be a no-op)
        # or advise us to retry (eg; in cases of lock timeouts); we defer to that.
        #
        # Note that we expect the headers object to be a CaseInsensitiveDict, as is the case with the requests library.
        if rheaders is not None and "stripe-should-retry" in rheaders:
            if rheaders["stripe-should-retry"] == "false":
                return False
            if rheaders["stripe-should-retry"] == "true":
                return True

        # Retry on conflict errors.
        if status_code == 409:
            return True

        # Retry on 500, 503, and other internal errors.
        #
        # Note that we expect the stripe-should-retry header to be false
        # in most cases when a 500 is returned, since our idempotency framework
        # would typically replay it anyway.
        if status_code >= 500:
            return True

        return False

    def _max_network_retries(self):
        from stripe import max_network_retries

        # Configured retries, isolated here for tests
        return max_network_retries

    def _retry_after_header(self, response=None):
        if response is None:
            return None
        _, _, rheaders = response

        try:
            return int(rheaders["retry-after"])
        except (KeyError, ValueError):
            return None

    def _sleep_time_seconds(self, num_retries, response=None):
        # Apply exponential backoff with initial_network_retry_delay on the
        # number of num_retries so far as inputs.
        # Do not allow the number to exceed max_network_retry_delay.
        sleep_seconds = min(
            HTTPClient.INITIAL_DELAY * (2 ** (num_retries - 1)),
            HTTPClient.MAX_DELAY,
        )

        sleep_seconds = self._add_jitter_time(sleep_seconds)

        # But never sleep less than the base sleep seconds.
        sleep_seconds = max(HTTPClient.INITIAL_DELAY, sleep_seconds)

        # And never sleep less than the time the API asks us to wait, assuming it's a reasonable ask.
        retry_after = self._retry_after_header(response) or 0
        if retry_after <= HTTPClient.MAX_RETRY_AFTER:
            sleep_seconds = max(retry_after, sleep_seconds)

        return sleep_seconds

    def _add_jitter_time(self, sleep_seconds):
        # Randomize the value in [(sleep_seconds/ 2) to (sleep_seconds)]
        # Also separated method here to isolate randomness for tests
        sleep_seconds *= 0.5 * (1 + random.uniform(0, 1))
        return sleep_seconds

    def _add_telemetry_header(self, headers):
        last_request_metrics = getattr(
            self._thread_local, "last_request_metrics", None
        )
        if stripe.enable_telemetry and last_request_metrics:
            telemetry = {
                "last_request_metrics": last_request_metrics.payload()
            }
            headers["X-Stripe-Client-Telemetry"] = json.dumps(telemetry)

    def _record_request_metrics(self, response, request_start):
        _, _, rheaders = response
        if "Request-Id" in rheaders and stripe.enable_telemetry:
            request_id = rheaders["Request-Id"]
            request_duration_ms = _now_ms() - request_start
            self._thread_local.last_request_metrics = RequestMetrics(
                request_id, request_duration_ms
            )

    def close(self):
        raise NotImplementedError(
            "HTTPClient subclasses must implement `close`"
        )


class RequestsClient(HTTPClient):
    name = "requests"

    def __init__(self, timeout=80, session=None, **kwargs):
        super(RequestsClient, self).__init__(**kwargs)
        self._session = session
        self._timeout = timeout

        assert requests is not None
        self.requests = requests

    def request(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=False
        )

    def request_stream(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=True
        )

    def _request_internal(self, method, url, headers, post_data, is_streaming):
        kwargs = {}
        if self._verify_ssl_certs:
            kwargs["verify"] = stripe.ca_bundle_path
        else:
            kwargs["verify"] = False

        if self._proxy:
            kwargs["proxies"] = self._proxy

        if is_streaming:
            kwargs["stream"] = True

        if getattr(self._thread_local, "session", None) is None:
            self._thread_local.session = (
                self._session or self.requests.Session()
            )

        try:
            try:
                result = self._thread_local.session.request(
                    method,
                    url,
                    headers=headers,
                    data=post_data,
                    timeout=self._timeout,
                    **kwargs
                )
            except TypeError as e:
                raise TypeError(
                    "Warning: It looks like your installed version of the "
                    '"requests" library is not compatible with Stripe\'s '
                    "usage thereof. (HINT: The most likely cause is that "
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    "underlying error was: %s" % (e,)
                )

            if is_streaming:
                content = result.raw
            else:
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

    def _handle_request_error(self, e) -> NoReturn:

        # Catch SSL error first as it belongs to ConnectionError,
        # but we don't want to retry
        if isinstance(e, self.requests.exceptions.SSLError):
            msg = (
                "Could not verify Stripe's SSL certificate.  Please make "
                "sure that your network is not intercepting certificates.  "
                "If this problem persists, let us know at "
                "support@stripe.com."
            )
            err = "%s: %s" % (type(e).__name__, str(e))
            should_retry = False
        # Retry only timeout and connect errors; similar to urllib3 Retry
        elif isinstance(
            e,
            (
                self.requests.exceptions.Timeout,
                self.requests.exceptions.ConnectionError,
            ),
        ):
            msg = (
                "Unexpected error communicating with Stripe.  "
                "If this problem persists, let us know at "
                "support@stripe.com."
            )
            err = "%s: %s" % (type(e).__name__, str(e))
            should_retry = True
        # Catch remaining request exceptions
        elif isinstance(e, self.requests.exceptions.RequestException):
            msg = (
                "Unexpected error communicating with Stripe.  "
                "If this problem persists, let us know at "
                "support@stripe.com."
            )
            err = "%s: %s" % (type(e).__name__, str(e))
            should_retry = False
        else:
            msg = (
                "Unexpected error communicating with Stripe. "
                "It looks like there's probably a configuration "
                "issue locally.  If this problem persists, let us "
                "know at support@stripe.com."
            )
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
            should_retry = False

        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise error.APIConnectionError(msg, should_retry=should_retry)

    def close(self):
        if getattr(self._thread_local, "session", None) is not None:
            self._thread_local.session.close()


class UrlFetchClient(HTTPClient):
    name = "urlfetch"

    def __init__(self, verify_ssl_certs=True, proxy=None, deadline=55):
        super(UrlFetchClient, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy
        )

        # no proxy support in urlfetch. for a patch, see:
        # https://code.google.com/p/googleappengine/issues/detail?id=544
        if proxy:
            raise ValueError(
                "No proxy support in urlfetch library. "
                "Set stripe.default_http_client to either RequestsClient, "
                "PycurlClient, or Urllib2Client instance to use a proxy."
            )

        self._verify_ssl_certs = verify_ssl_certs
        # GAE requests time out after 60 seconds, so make sure to default
        # to 55 seconds to allow for a slow Stripe
        self._deadline = deadline

        assert urlfetch is not None
        self.urlfetch = urlfetch

    def request(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=False
        )

    def request_stream(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=True
        )

    def _request_internal(self, method, url, headers, post_data, is_streaming):
        try:
            result = self.urlfetch.fetch(
                url=url,
                method=method,
                headers=headers,
                # Google App Engine doesn't let us specify our own cert bundle.
                # However, that's ok because the CA bundle they use recognizes
                # api.stripe.com.
                validate_certificate=self._verify_ssl_certs,
                deadline=self._deadline,
                payload=post_data,
            )
        except self.urlfetch.Error as e:
            self._handle_request_error(e, url)

        if is_streaming:
            content = util.io.BytesIO(str.encode(result.content))
        else:
            content = result.content

        return content, result.status_code, result.headers

    def _handle_request_error(self, e, url) -> NoReturn:
        if isinstance(e, self.urlfetch.InvalidURLError):
            msg = (
                "The Stripe library attempted to fetch an "
                "invalid URL (%r). This is likely due to a bug "
                "in the Stripe Python bindings. Please let us know "
                "at support@stripe.com." % (url,)
            )
        elif isinstance(e, self.urlfetch.DownloadError):
            msg = "There was a problem retrieving data from Stripe."
        elif isinstance(e, self.urlfetch.ResponseTooLargeError):
            msg = (
                "There was a problem receiving all of your data from "
                "Stripe.  This is likely due to a bug in Stripe. "
                "Please let us know at support@stripe.com."
            )
        else:
            msg = (
                "Unexpected error communicating with Stripe. If this "
                "problem persists, let us know at support@stripe.com."
            )

        msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
        raise error.APIConnectionError(msg)

    def close(self):
        pass


class PycurlClient(HTTPClient):
    class _ParsedProxy(TypedDict, total=False):
        http: Optional[ParseResult]
        https: Optional[ParseResult]

    name = "pycurl"
    _parsed_proxy: Optional[_ParsedProxy]

    def __init__(self, verify_ssl_certs=True, proxy=None):
        super(PycurlClient, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy
        )

        assert pycurl is not None
        self.pycurl = pycurl
        # Initialize this within the object so that we can reuse connections.
        self._curl = pycurl.Curl()

        self._parsed_proxy = {}
        # need to urlparse the proxy, since PyCurl
        # consumes the proxy url in small pieces
        if self._proxy:
            # now that we have the parser, get the proxy url pieces
            # Note: self._proxy is actually dict[str, str] because this is the
            # type on the superclass. Here, we reassign self._proxy into
            # dict[str, ParseResult]
            proxy_ = self._proxy
            for scheme, value in proxy_.items():
                self._parsed_proxy[scheme] = urlparse(value)

    def parse_headers(self, data):
        if "\r\n" not in data:
            return {}
        raw_headers = data.split("\r\n", 1)[1]
        headers = email.message_from_string(raw_headers)
        return dict((k.lower(), v) for k, v in dict(headers).items())

    def request(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=False
        )

    def request_stream(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=True
        )

    def _request_internal(self, method, url, headers, post_data, is_streaming):
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
                self._curl.setopt(self.pycurl.PROXY, proxy.hostname)
            if proxy.port:
                self._curl.setopt(self.pycurl.PROXYPORT, proxy.port)
            if proxy.username or proxy.password:
                self._curl.setopt(
                    self.pycurl.PROXYUSERPWD,
                    "%s:%s" % (proxy.username, proxy.password),
                )

        if method == "get":
            self._curl.setopt(self.pycurl.HTTPGET, 1)
        elif method == "post":
            self._curl.setopt(self.pycurl.POST, 1)
            self._curl.setopt(self.pycurl.POSTFIELDS, post_data)
        else:
            self._curl.setopt(self.pycurl.CUSTOMREQUEST, method.upper())

        # pycurl doesn't like unicode URLs
        self._curl.setopt(self.pycurl.URL, url)

        self._curl.setopt(self.pycurl.WRITEFUNCTION, b.write)
        self._curl.setopt(self.pycurl.HEADERFUNCTION, rheaders.write)
        self._curl.setopt(self.pycurl.NOSIGNAL, 1)
        self._curl.setopt(self.pycurl.CONNECTTIMEOUT, 30)
        self._curl.setopt(self.pycurl.TIMEOUT, 80)
        self._curl.setopt(
            self.pycurl.HTTPHEADER,
            ["%s: %s" % (k, v) for k, v in iter(dict(headers).items())],
        )
        if self._verify_ssl_certs:
            self._curl.setopt(self.pycurl.CAINFO, stripe.ca_bundle_path)
        else:
            self._curl.setopt(self.pycurl.SSL_VERIFYHOST, False)

        try:
            self._curl.perform()
        except self.pycurl.error as e:
            self._handle_request_error(e)

        if is_streaming:
            b.seek(0)
            rcontent = b
        else:
            rcontent = b.getvalue().decode("utf-8")

        rcode = self._curl.getinfo(self.pycurl.RESPONSE_CODE)
        headers = self.parse_headers(rheaders.getvalue().decode("utf-8"))

        return rcontent, rcode, headers

    def _handle_request_error(self, e) -> NoReturn:
        if e.args[0] in [
            self.pycurl.E_COULDNT_CONNECT,
            self.pycurl.E_COULDNT_RESOLVE_HOST,
            self.pycurl.E_OPERATION_TIMEOUTED,
        ]:
            msg = (
                "Could not connect to Stripe.  Please check your "
                "internet connection and try again.  If this problem "
                "persists, you should check Stripe's service status at "
                "https://twitter.com/stripestatus, or let us know at "
                "support@stripe.com."
            )
            should_retry = True
        elif e.args[0] in [
            self.pycurl.E_SSL_CACERT,
            self.pycurl.E_SSL_PEER_CERTIFICATE,
        ]:
            msg = (
                "Could not verify Stripe's SSL certificate.  Please make "
                "sure that your network is not intercepting certificates.  "
                "If this problem persists, let us know at "
                "support@stripe.com."
            )
            should_retry = False
        else:
            msg = (
                "Unexpected error communicating with Stripe. If this "
                "problem persists, let us know at support@stripe.com."
            )
            should_retry = False

        msg = textwrap.fill(msg) + "\n\n(Network error: " + e.args[1] + ")"
        raise error.APIConnectionError(msg, should_retry=should_retry)

    def _get_proxy(self, url) -> Optional[ParseResult]:
        if self._parsed_proxy:
            proxy = self._parsed_proxy
            scheme = url.split(":")[0] if url else None
            if scheme:
                return proxy.get(scheme, proxy.get(scheme[0:-1]))
        return None

    def close(self):
        pass


class Urllib2Client(HTTPClient):
    name = "urllib.request"

    def __init__(self, verify_ssl_certs=True, proxy=None):
        super(Urllib2Client, self).__init__(
            verify_ssl_certs=verify_ssl_certs, proxy=proxy
        )
        # prepare and cache proxy tied opener here
        self._opener = None
        if self._proxy:
            proxy = urllibrequest.ProxyHandler(self._proxy)
            self._opener = urllibrequest.build_opener(proxy)

    def request(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=False
        )

    def request_stream(self, method, url, headers, post_data=None):
        return self._request_internal(
            method, url, headers, post_data, is_streaming=True
        )

    def _request_internal(self, method, url, headers, post_data, is_streaming):
        if isinstance(post_data, str):
            post_data = post_data.encode("utf-8")

        req = urllibrequest.Request(url, post_data, headers)

        if method not in ("get", "post"):
            req.get_method = lambda: method.upper()

        try:
            # use the custom proxy tied opener, if any.
            # otherwise, fall to the default urllib opener.
            response = (
                self._opener.open(req)
                if self._opener
                else urllibrequest.urlopen(req)
            )

            if is_streaming:
                rcontent = response
            else:
                rcontent = response.read()

            rcode = response.code
            headers = dict(response.info())
        except urlliberror.HTTPError as e:
            rcode = e.code
            rcontent = e.read()
            headers = dict(e.info())
        except (urlliberror.URLError, ValueError) as e:
            self._handle_request_error(e)
        lh = dict((k.lower(), v) for k, v in iter(dict(headers).items()))
        return rcontent, rcode, lh

    def _handle_request_error(self, e) -> NoReturn:
        msg = (
            "Unexpected error communicating with Stripe. "
            "If this problem persists, let us know at support@stripe.com."
        )
        msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
        raise error.APIConnectionError(msg)

    def close(self):
        pass
