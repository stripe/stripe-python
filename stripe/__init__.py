# Stripe Python bindings
# API spec at http://stripe.com/api/spec
# Authors: Patrick Collison <patrick@stripe.com> and Greg Brockman <gdb@stripe.com>

import cStringIO as StringIO
import logging
import platform
import pycurl
import sys
import urllib # need urlencode
import textwrap

# Python 2.5 and below do not ship with json
__loaded = None
try:
  import json
  __loaded = hasattr(json, 'loads')
except ImportError:
  pass

if not __loaded:
  try:
    import simplejson as json
  except ImportError:
    if __loaded is None:
      raise ImportError("Stripe requires a JSON library, which you do not appear to have.  Please install the simplejson library.  HINT: Try installing the python simplejson library via 'easy_install simplejson', or contact support@stripe.com with questions.")
    else:
      raise ImportError("Stripe requires a JSON library with the same interface as the Python 2.6 'json' library.  You appear to have a 'json' library with a different interface.  Please install the simplejson library.  HINT: Try installing the python simplejson library via 'easy_install simplejson', or contact support@stripe.com with questions.")

## Configuration variables
VERSION = '1.5.0'
logger = logging.getLogger('stripe')
logger.addHandler(logging.StreamHandler(sys.stderr))
logger.setLevel(logging.ERROR)

api_key = None
api_base = 'https://api.stripe.com/v1'

## Exceptions
class StripeError(Exception):
  pass

class APIError(StripeError):
  pass

class APIConnectionError(StripeError):
  pass

class CardError(StripeError):
  def __init__(self, message, param, code):
    super(CardError, self).__init__(message)
    self.param = param
    self.code = code

class InvalidRequestError(StripeError):
  def __init__(self, message, param):
    super(InvalidRequestError, self).__init__(message)
    self.param = param

class AuthenticationError(StripeError):
  pass


def convertToStripeObject(resp, api_key):
  types = { 'charge' : Charge, 'customer' : Customer,
            'invoice' : Invoice, 'invoice_item' : InvoiceItem }
  if isinstance(resp, list):
    return [convertToStripeObject(i, api_key) for i in resp]
  elif isinstance(resp, dict):
    resp = resp.copy()
    klass_name = resp.get('object')
    klass = types.get(klass_name, StripeObject)
    return klass.constructFrom(resp, api_key)
  else:
    return resp

class APIRequestor(object):
  def __init__(self, key=None):
    self.api_key = key

  @classmethod
  def apiUrl(cls, url=''):
    return '%s%s' % (api_base, url)

  @classmethod
  def _utf8(cls, value):
    if isinstance(value, unicode):
      return value.encode('utf-8')
    else:
      return value

  @classmethod
  def _encodeInner(cls, d):
    """
    We want post vars of form:
    {'foo': 'bar', 'nested': {'a': 'b', 'c': 'd'}}
    to become:
    foo=bar&nested[a]=b&nested[c]=d
    """
    stk = []
    for key, value in d.iteritems():
      key = cls._utf8(key)
      if value is None:
        stk.append((key, ''))
      elif isinstance(value, dict):
        n = {}
        for k, v in value.iteritems():
          k = cls._utf8(k)
          v = cls._utf8(v)
          n["%s[%s]" % (key, k)] = v
        stk.extend(cls._encodeInner(n))
      else:
        value = cls._utf8(value)
        stk.append((key, value))
    return stk

  @classmethod
  def _objects_to_ids(cls, d):
    if isinstance(d, APIResource):
      return d.id
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
    return urllib.urlencode(cls._encodeInner(d))

  def handleCurlError(self, e):
    if e[0] in [pycurl.E_COULDNT_CONNECT,
                pycurl.E_COULDNT_RESOLVE_HOST,
                pycurl.E_OPERATION_TIMEOUTED]:
      msg = "Could not connect to Stripe (%s).  Please check your internet connection and try again.  If this problem persists, you should check Stripe's service status at https://twitter.com/stripe, or let us know at support@stripe.com." % api_base
    elif e[0] == pycurl.E_SSL_CACERT:
      msg = "Could not verify Stripe's SSL certificate.  Please make sure that your network is not intercepting certificates.  (Try going to https://api.stripe.com in your browser.)  If this problem persists, let us know at support@stripe.com."
    else:
      msg = "Unexpected error communicating with Stripe.  If this problem persists, let us know at support@stripe.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + e[1] + ")"
    raise APIConnectionError(msg)

  def handleApiError(self, rcode, resp):
    try:
      error = resp['error']
    except (KeyError, TypeError):
      raise APIError("Invalid response object from API: %r (HTTP response code was %d)" % (rcode, resp))

    if rcode in [400, 404]:
      raise InvalidRequestError(error.get('message'), error.get('param'))
    elif rcode == 401:
      raise AuthenticationError(error.get('message'))
    elif rcode == 402:
      raise CardError(error.get('message'), error.get('param'), error.get('code'))
    else:
      raise APIError(error.get('message'))

  def request(self, meth, url, params={}):
    """
    Mechanism for issuing an API call
    """
    my_api_key = self.api_key or api_key
    if my_api_key is None:
      raise AuthenticationError('No API key provided.  (HINT: set your API key using "stripe.api_key = <API-KEY>".  You can generate API keys from the Stripe web interface.  See https://stripe.com/api for details, or email support@stripe.com if you have any questions.')

    abs_url = self.apiUrl(url)
    params = params.copy()
    self._objects_to_ids(params)

    s = StringIO.StringIO()
    curl = pycurl.Curl()
    ua = {
      'bindings_version' : VERSION,
      'lang' : 'python',
      'lang_version' : platform.python_version(),
      'platform' : platform.platform(),
      'publisher' : 'stripe',
      'uname' : ' '.join(platform.uname())
      }
    headers = ['X-Stripe-Client-User-Agent: %s' % (json.dumps(ua), ),
               'User-Agent: Stripe/v1 PythonBindings/%s' % (VERSION, )]

    meth = meth.lower()
    if meth == 'get':
      curl.setopt(pycurl.HTTPGET, 1)
      # TODO: maybe be a bit less manual here
      abs_url = '%s?%s' % (abs_url, self.encode(params))
    elif meth == 'post':
      curl.setopt(pycurl.POST, 1)
      curl.setopt(pycurl.POSTFIELDS, self.encode(params))
    elif meth == 'delete':
      curl.setopt(pycurl.CUSTOMREQUEST, 'DELETE')
    else:
      raise APIError('Unrecognized method %r' % (meth, ))

    # pycurl doesn't like unicode URLs
    abs_url = self._utf8(abs_url)
    curl.setopt(pycurl.URL, abs_url)
    curl.setopt(pycurl.WRITEFUNCTION, s.write)
    curl.setopt(pycurl.NOSIGNAL, 1)
    curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
    curl.setopt(pycurl.USERPWD, '%s:' % (my_api_key, ))
    curl.setopt(pycurl.CONNECTTIMEOUT, 30)
    curl.setopt(pycurl.TIMEOUT, 80)
    curl.setopt(pycurl.HTTPHEADER, headers)

    try:
      curl.perform()
    except pycurl.error, e:
      self.handleCurlError(e)
    rcode = curl.getinfo(pycurl.RESPONSE_CODE)
    rbody = s.getvalue()

    try:
      resp = json.loads(rbody)
    except Exception:
      raise APIError("Invalid response body from API: %s (HTTP response code was %d)" % (rbody, rcode))

    if not (200 <= rcode < 300):
      self.handleApiError(rcode, resp)

    logger.info('API request to %s returned (response code, response object) of (%d, %r)' % (abs_url, rcode, resp))
    return resp, my_api_key

class StripeObject(object):
  _permanent_attributes = set(['api_key'])
  _ignored_attributes = set(['id', 'api_key', 'object'])

  def __init__(self, id=None, api_key=None):
    self.__dict__['_values'] = set()
    self.__dict__['_unsaved_values'] = set()
    self.__dict__['_transient_values'] = set()
    self.__dict__['api_key'] = api_key

    if id:
      self.id = id

  def __setattr__(self, k, v):
    # TODO: may want to make ignored attributes immutable
    self.__dict__[k] = v
    self._values.add(k)
    if k not in self._ignored_attributes:
      self._unsaved_values.add(k)

  def __getattr__(self, k):
    try:
      return self.__dict__[k]
    except KeyError:
      pass
    if k in self._transient_values:
      raise AttributeError("%r object has no attribute %r.  HINT: The %r attribute was set in the past, however.  It was then wiped when refreshing the object with the result returned by Stripe's API, probably as a result of a save().  The attributes currently available on this object are: %s" %
                           (type(self).__name__, k, k, ', '.join(self._values)))
    else:
      raise AttributeError("%r object has no attribute %r" % (type(self).__name__, k))

  def __getitem__(self, k):
    if k in self._values:
      return self.__dict__[k]
    elif k in self._transient_values:
      raise KeyError("%r.  HINT: The %r attribute was set in the past, however.  It was then wiped when refreshing the object with the result returned by Stripe's API, probably as a result of a save().  The attributes currently available on this object are: %s" % (k, k, ', '.join(self._values)))
    else:
      raise KeyError(k)

  def get(self, k, default=None):
    try:
      return self[k]
    except KeyError:
      return default

  def setdefault(self, k, default=None):
    try:
      return self[k]
    except KeyError:
      self[k] = default
      return default

  def __setitem__(self, k, v):
    setattr(self, k, v)

  def keys(self):
    return self._values.keys()

  def values(self):
    return self._values.keys()

  @classmethod
  def constructFrom(cls, values, api_key):
    instance = cls(values.get('id'), api_key)
    instance.refreshFrom(values, api_key)
    return instance

  def refreshFrom(self, values, api_key, partial=False):
    self.api_key = api_key

    # Wipe old state before setting new.  This is useful for e.g. updating a
    # customer, where there is no persistent card parameter.  Mark those values
    # which don't persist as transient
    if partial:
      removed = set()
    else:
      removed = self._values - set(values)

    for k in removed:
      if k in self._permanent_attributes:
        continue
      del self.__dict__[k]
      self._values.discard(k)
      self._transient_values.add(k)
      self._unsaved_values.discard(k)

    for k, v in values.iteritems():
      if k in self._permanent_attributes:
        continue
      self.__dict__[k] = convertToStripeObject(v, api_key)
      self._values.add(k)
      self._transient_values.discard(k)
      self._unsaved_values.discard(k)

  def _ident(self):
    return [self.get('object'), self.get('id')]

  def __repr__(self, nested=False):
    ident = [i for i in self._ident() if i]
    if ident:
      ident = '[%s]' % (', '.join(ident), )
    else:
      ident = ''

    if nested:
      return '<stripe.%s%s ...>' % (type(self).__name__, ident)

    values_str = []
    for k in sorted(self._values):
      if k in self._ignored_attributes:
        continue
      v = getattr(self, k)
      if isinstance(v, StripeObject):
        v = v.__repr__(True)
      elif isinstance(v, unicode):
        v = repr(v)
        if v[0] == 'u':
          v = v[1:]
      else:
        v = repr(v)
      if k in self._unsaved_values:
        values_str.append('%s=%s (unsaved)' % (k, v))
      else:
        values_str.append('%s=%s' % (k, v))
    if not values_str:
      values_str.append('(no attributes)')
    return '<stripe.%s%s %s>' % (type(self).__name__, ident, ', '.join(values_str))

  def __str__(self):
    return repr(self)

class APIResource(StripeObject):
  def _ident(self):
    return [self.get('id')]

  @classmethod
  def retrieve(cls, id, api_key=None):
    instance = cls(id, api_key)
    instance.refresh()
    return instance

  def refresh(self):
    requestor = APIRequestor(self.api_key)
    url = self.instanceUrl()
    response, api_key = requestor.request('get', url)
    self.refreshFrom(response, api_key)
    return self

  @classmethod
  def classUrl(cls):
    if cls == APIResource:
      raise NotImplementedError('APIResource is an abstract class.  You should perform actions on its subclasses (Charge, Customer, etc.)')
    return "/%ss" % urllib.quote_plus(cls.__name__.lower())

  def instanceUrl(self):
    id = APIRequestor._utf8(self.id)
    base = type(self).classUrl()
    extn = urllib.quote_plus(id)
    return "%s/%s" % (base, extn)

# Classes of API operations
class ListableAPIResource(APIResource):
  @classmethod
  def all(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.classUrl()
    response, api_key = requestor.request('get', url, params)
    return convertToStripeObject(response, api_key)

class CreateableAPIResource(APIResource):
  @classmethod
  def create(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.classUrl()
    response, api_key = requestor.request('post', url, params)
    return convertToStripeObject(response, api_key)

class UpdateableAPIResource(APIResource):
  def save(self):
    if self._unsaved_values:
      requestor = APIRequestor(self.api_key)
      params = {}
      for k in self._unsaved_values:
        params[k] = getattr(self, k)
      url = self.instanceUrl()
      response, api_key = requestor.request('post', url, params)
      self.refreshFrom(response, api_key)
    else:
      logger.debug("Trying to save already saved object %r" % (self, ))
    return self

class DeletableAPIResource(APIResource):
  def delete(self):
    requestor = APIRequestor(self.api_key)
    url = self.instanceUrl()
    response, api_key = requestor.request('delete', url)
    self.refreshFrom(response, api_key)
    return self

# API objects
class Charge(CreateableAPIResource, ListableAPIResource):
  def refund(self):
    requestor = APIRequestor(self.api_key)
    url = self.instanceUrl() + '/refund'
    response, api_key = requestor.request('post', url)
    self.refreshFrom(response, api_key)
    return self

class Customer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):
  def add_invoice_item(self, **params):
    params['customer_id'] = self.id
    ii = InvoiceItem.create(self.api_key, **params)
    return ii

  def invoices(self, **params):
    params['customer_id'] = self.id
    invoices = Invoice.all(self.api_key, **params)
    return invoices

  def invoice_items(self, **params):
    params['customer_id'] = self.id
    iis = InvoiceItem.all(self.api_key, **params)
    return iis

  def charges(self, **params):
    params['customer_id'] = self.id
    charges = Charge.all(self.api_key, **params)
    return charges

  def update_subscription(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instanceUrl() + '/subscription'
    response, api_key = requestor.request('post', url, params)
    self.refreshFrom({ 'subscription' : response }, api_key, True)
    return self.subscription

  def cancel_subscription(self):
    requestor = APIRequestor(self.api_key)
    url = self.instanceUrl() + '/subscription'
    response, api_key = requestor.request('delete', url)
    self.refreshFrom({ 'subscription' : response }, api_key, True)
    return self.subscription

class Invoice(ListableAPIResource):
  @classmethod
  def upcoming(cls, **params):
    requestor = APIRequestor(self.api_key)
    url = self.classUrl() + '/upcoming'
    response, api_key = requestor.request('get', url, params)
    return convertToStripeObject(response, api_key)

class InvoiceItem(CreateableAPIResource, UpdateableAPIResource,
                  ListableAPIResource, DeletableAPIResource):
  pass
