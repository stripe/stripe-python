import os
import sys
import StringIO
import textwrap
import urlparse

from . import encoders
from . import exceptions as stripe_exceptions

verify_ssl_certs = True
api_base = 'https://api.stripe.com'
protocol = None
_default_protocols = [
    "urlfetch",
    "requests",
    "pycurl",
    "urllib2"
]
_requestors = {}
_configured = False


def build_url(url, params):
    base_query = urlparse.urlparse(url).query
    if base_query:
        return '%s&%s' % (url, encoders.encode(params))
    else:
        return '%s?%s' % (url, encoders.encode(params))


def handle_requests_error(e):
    import requests
    if isinstance(e, requests.exceptions.RequestException):
      msg = "Unexpected error communicating with Stripe.  If this problem persists, let us know at support@stripe.com."
      err = "%s: %s" % (type(e).__name__, str(e))
    else:
      msg = "Unexpected error communicating with Stripe.  It looks like there's probably a configuration issue locally.  If this problem persists, let us know at support@stripe.com."
      err = "A %s was raised" % (type(e).__name__, )
      if str(e):
        err += " with error message %s" % (str(e), )
      else:
        err += " with no error message"
    msg = textwrap.fill(msg) + "\n\n(Network error: " + err + ")"
    raise stripe_exceptions.APIConnectionError(msg)


def requests_request(meth, abs_url, headers, params):
    import requests
    meth = meth.lower()
    if meth == 'get' or meth == 'delete':
        if params:
            abs_url = build_url(abs_url, params)
        data = None
    elif meth == 'post':
        data = encoders.encode(params)
    else:
        raise stripe_exceptions.APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Stripe bindings.  Please contact support@stripe.com for assistance.' % (meth, ))

    kwargs = {}
    if verify_ssl_certs:
        kwargs['verify'] = os.path.join(os.path.dirname(__file__), 'data/ca-certificates.crt')
    else:
        kwargs['verify'] = False

    try:
        try:
            result = requests.request(
                meth,
                abs_url,
                headers=headers,
                data=data,
                timeout=80,
                **kwargs
            )
        except TypeError, e:
            raise TypeError('Warning: It looks like your installed version of the "requests" library is not compatible with Stripe\'s usage thereof. (HINT: The most likely cause is that your "requests" library is out of date. You can fix that by running "pip install -U requests".) The underlying error was: %s' %(e, ))

        # This causes the content to actually be read, which could cause
        # e.g. a socket timeout. TODO: The other fetch methods probably
        # are succeptible to the same and should be updated.
        content = result.content
        status_code = result.status_code
        return content, status_code
    except Exception, e:
        # Would catch just requests.exceptions.RequestException, but can
        # also raise ValueError, RuntimeError, etc.
        handle_requests_error(e)


def handle_pycurl_error(e):
    import pycurl
    if e[0] in [pycurl.E_COULDNT_CONNECT,
                pycurl.E_COULDNT_RESOLVE_HOST,
                pycurl.E_OPERATION_TIMEOUTED]:
      msg = "Could not connect to Stripe (%s).  Please check your internet connection and try again.  If this problem persists, you should check Stripe's service status at https://twitter.com/stripestatus, or let us know at support@stripe.com." % (api_base, )
    elif e[0] == pycurl.E_SSL_CACERT or e[0] == pycurl.E_SSL_PEER_CERTIFICATE:
      msg = "Could not verify Stripe's SSL certificate.  Please make sure that your network is not intercepting certificates.  (Try going to %s in your browser.)  If this problem persists, let us know at support@stripe.com." % (api_base, )
    else:
      msg = "Unexpected error communicating with Stripe.  If this problem persists, let us know at support@stripe.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + e[1] + ")"
    raise stripe_exceptions.APIConnectionError(msg)


def pycurl_request(meth, abs_url, headers, params):
    import pycurl
    s = StringIO.StringIO()
    curl = pycurl.Curl()

    meth = meth.lower()
    if meth == 'get':
        curl.setopt(pycurl.HTTPGET, 1)
        # TODO: maybe be a bit less manual here
        if params:
            abs_url = build_url(abs_url, params)
    elif meth == 'post':
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, encoders.encode(params))
    elif meth == 'delete':
        curl.setopt(pycurl.CUSTOMREQUEST, 'DELETE')
        if params:
            abs_url = build_url(abs_url, params)
    else:
        raise stripe_exceptions.APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Stripe bindings.  Please contact support@stripe.com for assistance.' % (meth, ))

    # pycurl doesn't like unicode URLs
    abs_url = encoders.utf8(abs_url)
    curl.setopt(pycurl.URL, abs_url)
    curl.setopt(pycurl.WRITEFUNCTION, s.write)
    curl.setopt(pycurl.NOSIGNAL, 1)
    curl.setopt(pycurl.CONNECTTIMEOUT, 30)
    curl.setopt(pycurl.TIMEOUT, 80)
    curl.setopt(pycurl.HTTPHEADER, ['%s: %s' % (k, v) for k, v in headers.iteritems()])
    if verify_ssl_certs:
        curl.setopt(pycurl.CAINFO, os.path.join(os.path.dirname(__file__), 'data/ca-certificates.crt'))
    else:
        curl.setopt(pycurl.SSL_VERIFYHOST, False)

    try:
        curl.perform()
        rbody = s.getvalue()
        rcode = curl.getinfo(pycurl.RESPONSE_CODE)
        return rbody, rcode
    except pycurl.error, e:
        handle_pycurl_error(e)


def handle_urlfetch_error(e, abs_url):
    from google.appengine.api import urlfetch
    if isinstance(e, urlfetch.InvalidURLError):
      msg = "The Stripe library attempted to fetch an invalid URL (%r).  This is likely due to a bug in the Stripe Python bindings.  Please let us know at support@stripe.com." % (abs_url, )
    elif isinstance(e, urlfetch.DownloadError):
      msg = "There were a problem retrieving data from Stripe."
    elif isinstance(e, urlfetch.ResponseTooLargeError):
      msg = "There was a problem receiving all of your data from Stripe.  This is likely due to a bug in Stripe.  Please let us know at support@stripe.com."
    else:
      msg = "Unexpected error communicating with Stripe.  If this problem persists, let us know at support@stripe.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
    raise stripe_exceptions.APIConnectionError(msg)


def urlfetch_request(meth, abs_url, headers, params):
    from google.appengine.api import urlfetch
    args = {}
    if meth == 'post':
        args['payload'] = encoders.encode(params)
    elif meth == 'get' or meth == 'delete':
        abs_url = build_url(abs_url, params)
    else:
        raise stripe_exceptions.APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Stripe bindings.  Please contact support@stripe.com for assistance.' % (meth, ))
    args['url'] = abs_url
    args['method'] = meth
    args['headers'] = headers
    # Google App Engine doesn't let us specify our own cert bundle.
    # However, that's ok because the CA bundle they use recognizes
    # api.stripe.com.
    args['validate_certificate'] = verify_ssl_certs
    # GAE requests time out after 60 seconds, so make sure we leave
    # some time for the application to handle a slow Stripe
    args['deadline'] = 55

    try:
        result = urlfetch.fetch(**args)
        return result.content, result.status_code
    except urlfetch.Error, e:
        handle_urlfetch_error(e, abs_url)


def handle_urllib2_error(e, abs_url):
    msg = "Unexpected error communicating with Stripe.  If this problem persists, let us know at support@stripe.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
    raise stripe_exceptions.APIConnectionError(msg)


def urllib2_request(meth, abs_url, headers, params):
    import urllib2
    if meth == 'get':
        abs_url = build_url(abs_url, params)
        req = urllib2.Request(abs_url, None, headers)
    elif meth == 'post':
        body = encoders.encode(params).encode('utf-8')
        req = urllib2.Request(abs_url, body, headers)
    elif meth == 'delete':
        abs_url = build_url(abs_url, params)
        req = urllib2.Request(abs_url, None, headers)
        req.get_method = lambda: 'DELETE'
    else:
        raise stripe_exceptions.APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Stripe bindings.  Please contact support@stripe.com for assistance.' % (meth, ))

    try:
        response = urllib2.urlopen(req)
        rbody = response.read()
        rcode = response.code
    except urllib2.HTTPError, e:
        rcode = e.code
        rbody = e.read()
    except (urllib2.URLError, ValueError), e:
        handle_urllib2_error(e, abs_url)
    return rbody, rcode


def _import_defaults():
    """
    # - Requests is the preferred HTTP library
    # - Google App Engine has urlfetch
    # - Use Pycurl if it's there (at least it verifies SSL certs)
    # - Fall back to urllib2 with a warning if needed
    """
    global protocol, _configured, _requestors
    try:
        from google.appengine.api import urlfetch
        protocol = 'urlfetch'
        _requestors[protocol] = urlfetch_request
    except ImportError:
        pass

    if not protocol:
        try:
            import requests
            protocol = 'requests'
            _requestors[protocol] = requests_request
        except ImportError:
            pass
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
                    print >>sys.stderr, 'Warning: the Stripe library requires that your Python "requests" library has a version no older than 0.8.8, but your "requests" library has version %s. Stripe will fall back to an alternate HTTP library, so everything should work, though we recommend upgrading your "requests" library. If you have any questions, please contact support@stripe.com. (HINT: running "pip install -U requests" should upgrade your requests library to the latest version.)' % (version, )
                    protocol = None

    if not protocol:
        try:
            import pycurl
            protocol = 'pycurl'
            _requestors[protocol] = pycurl_request
        except ImportError:
            pass

    if not protocol:
        try:
            import urllib2
            protocol = 'urllib2'
            _requestors[protocol] = urllib2_request
            print >>sys.stderr, "Warning: the Stripe library is falling back to urllib2 because neither requests nor pycurl are installed. urllib2's SSL implementation doesn't verify server certificates. For improved security, we suggest installing requests."
        except ImportError:
            pass

    if not protocol:
        raise ImportError("Stripe requires one of requests, pycurl, Google App Engine's urlfetch, or urllib2.  If you are on a platform where none of these libraries are available, please let us know at support@stripe.com.")
    _configured = True


def get_requestor():
    """
    Grabs a cached requestor function to make a network request.

    If the protocol has not yet been configured, the default protocol
    implementations are configured.

    :return: the current configured request function.
    """
    global protocol
    if not _configured:
        _import_defaults()

    return _requestors.get(protocol)


def add_protocol(protocol_name, request_fn):
    """
    Adds a protocol to the _requestors dict using request_fn for requests.

    If a protocol has not yet been configured, the default protocol
    implementations are configured.

    :param protocol_name: the request protocol name.
    :param request_fn: the request function to be used when get_requestor() is called.
    """
    global protocol, _requestors
    if protocol_name in _default_protocols and not _configured:
        _import_defaults()
    else:
        _requestors[protocol_name] = request_fn


def unset_protocol(protocol_name):
    """
    Unsets a protocol from the _requestors dict with the name protocol_name.
    :param protocol_name: the name of the request protocol to remove.
    :return:
    """
    global protocol, _requestors, _configured
    if _configured:
        if protocol_name in _requestors.keys():
            del _requestors[protocol]
        if protocol_name == protocol:
            protocol = None
        _configured = False


def set_protocol(protocol_name):
    """
    Sets the current request protocol to the protocol identified by protocol_name.
    :param protocol_name: the protocol to set.
    """
    global protocol, _configured
    if protocol_name in _default_protocols:
        _import_defaults()
    elif protocol_name in _requestors.keys():
        protocol = protocol_name
    else:
        raise Exception("Invalid protocol: %s. You must add_protocol before you set, or use defaults." % protocol_name)
    _configured = True
