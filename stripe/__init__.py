# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors: Patrick Collison <patrick@stripe.com> and Greg Brockman <gdb@stripe.com>

## Imports
import logging
import platform
import urllib

from . import protocols
from . import encoders
from . import exceptions as stripe_exceptions

# Use cStringIO if it's available.  Otherwise, StringIO is fine.
try:
  import cStringIO as StringIO
except ImportError:
  import StringIO




from version import VERSION
import importer
json = importer.import_json()

logger = logging.getLogger('stripe')

## Configuration variables

api_key = None
api_base = 'https://api.stripe.com'
api_version = None


def convert_to_stripe_object(resp, api_key):
  types = { 'charge' : Charge, 'customer' : Customer,
            'invoice' : Invoice, 'invoiceitem' : InvoiceItem,
            'plan' : Plan, 'coupon': Coupon, 'token' : Token, 'event': Event,
            'transfer': Transfer, 'list': ListObject, 'recipient': Recipient,
            'card': Card }

  if isinstance(resp, list):
    return [convert_to_stripe_object(i, api_key) for i in resp]
  elif isinstance(resp, dict):
    resp = resp.copy()
    klass_name = resp.get('object')
    if isinstance(klass_name, basestring):
      klass = types.get(klass_name, StripeObject)
    else:
      klass = StripeObject
    return klass.construct_from(resp, api_key)
  else:
    return resp

## Network transport
class APIRequestor(object):
  def __init__(self, key=None):
    self.api_key = key

  @classmethod
  def api_url(cls, url=''):
    return '%s%s' % (api_base, url)

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


  def request(self, meth, url, params={}):
    rbody, rcode, my_api_key = self.request_raw(meth, url, params)
    resp = self.interpret_response(rbody, rcode)
    return resp, my_api_key

  def handle_api_error(self, rbody, rcode, resp):
    try:
      error = resp['error']
    except (KeyError, TypeError):
      raise stripe_exceptions.APIError("Invalid response object from API: %r (HTTP response code was %d)" % (rbody, rcode), rbody, rcode, resp)

    if rcode in [400, 404]:
      raise stripe_exceptions.InvalidRequestError(error.get('message'), error.get('param'), rbody, rcode, resp)
    elif rcode == 401:
      raise stripe_exceptions.AuthenticationError(error.get('message'), rbody, rcode, resp)
    elif rcode == 402:
      raise stripe_exceptions.CardError(error.get('message'), error.get('param'), error.get('code'), rbody, rcode, resp)
    else:
      raise stripe_exceptions.APIError(error.get('message'), rbody, rcode, resp)

  def request_raw(self, meth, url, params={}):
    """
    Mechanism for issuing an API call
    """
    my_api_key = self.api_key or api_key
    if my_api_key is None:
      raise stripe_exceptions.AuthenticationError('No API key provided. (HINT: set your API key using "stripe.api_key = <API-KEY>"). You can generate API keys from the Stripe web interface.  See https://stripe.com/api for details, or email support@stripe.com if you have any questions.')

    abs_url = self.api_url(url)
    params = params.copy()
    self._objects_to_ids(params)

    ua = {
      'bindings_version' : VERSION,
      'lang' : 'python',
      'publisher' : 'stripe',
      'httplib': protocols.protocol,
      }
    for attr, func in [['lang_version', platform.python_version],
                       ['platform', platform.platform],
                       ['uname', lambda: ' '.join(platform.uname())]]:
      try:
        val = func()
      except Exception, e:
        val = "!! %s" % e
      ua[attr] = val

    headers = {
      'X-Stripe-Client-User-Agent' : json.dumps(ua),
      'User-Agent' : 'Stripe/v1 PythonBindings/%s' % (VERSION, ),
      'Authorization' : 'Bearer %s' % (my_api_key, )
      }
    if api_version is not None:
      headers['Stripe-Version'] = api_version
    requestor = protocols.get_requestor()
    if requestor is None:
        raise stripe_exceptions.StripeError("Stripe Python library bug discovered: invalid httplib %s.  Please report to support@stripe.com" % (protocols.protocol, ))
    rbody, rcode = requestor(meth, abs_url, headers, params)

    logger.info('API request to %s returned (response code, response body) of (%d, %r)' % (abs_url, rcode, rbody))
    return rbody, rcode, my_api_key

  def interpret_response(self, rbody, rcode):
    try:
      resp = json.loads(rbody.decode('utf-8'))
    except Exception:
      raise stripe_exceptions.APIError("Invalid response body from API: %s (HTTP response code was %d)" % (rbody, rcode), rbody, rcode)
    if not (200 <= rcode < 300):
      self.handle_api_error(rbody, rcode, resp)
    return resp


class StripeObject(object):
  _permanent_attributes = set(['api_key'])

  def __init__(self, id=None, api_key=None, **params):
    self.__dict__['_values'] = set()
    self.__dict__['_unsaved_values'] = set()
    self.__dict__['_transient_values'] = set()
    self.__dict__['_retrieve_params'] = params

    self.__dict__['api_key'] = api_key

    if id:
      self.id = id

  def __setattr__(self, k, v):
    self.__dict__[k] = v
    self._values.add(k)
    if k not in self._permanent_attributes:
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
    return self.to_dict().keys()

  def values(self):
    return self.to_dict().values()

  @classmethod
  def construct_from(cls, values, api_key):
    instance = cls(values.get('id'), api_key)
    instance.refresh_from(values, api_key)
    return instance

  def refresh_from(self, values, api_key, partial=False):
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
      self.__dict__[k] = convert_to_stripe_object(v, api_key)
      self._values.add(k)
      self._transient_values.discard(k)
      self._unsaved_values.discard(k)

  def __repr__(self):
    type_string = ''
    if isinstance(self.get('object'), basestring):
      type_string = ' %s' % self.get('object').encode('utf8')

    id_string = ''
    if isinstance(self.get('id'), basestring):
      id_string = ' id=%s' % self.get('id').encode('utf8')

    return '<%s%s%s at %s> JSON: %s' % (type(self).__name__, type_string, id_string, hex(id(self)), json.dumps(self.to_dict(), sort_keys=True, indent=2, cls=StripeObjectEncoder))

  def __str__(self):
    return json.dumps(self.to_dict(), sort_keys=True, indent=2, cls=StripeObjectEncoder)

  def to_dict(self):
    def _serialize(o):
      if isinstance(o, StripeObject):
        return o.to_dict()
      if isinstance(o, list):
        return [_serialize(i) for i in o]
      return o

    d = dict()
    for k in sorted(self._values):
      if k in self._permanent_attributes:
        continue
      v = getattr(self, k)
      v = _serialize(v)
      d[k] = v
    return d

class StripeObjectEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, StripeObject):
      return obj.to_dict()
    else:
      return json.JSONEncoder.default(self, obj)

class APIResource(StripeObject):
  def _ident(self):
    return [self.get('id')]

  @classmethod
  def retrieve(cls, id, api_key=None, **params):
    instance = cls(id, api_key, **params)
    instance.refresh()
    return instance

  def refresh(self):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url()
    response, api_key = requestor.request('get', url, self._retrieve_params)
    self.refresh_from(response, api_key)
    return self

  @classmethod
  def class_name(cls):
    if cls == APIResource:
      raise NotImplementedError('APIResource is an abstract class.  You should perform actions on its subclasses (Charge, Customer, etc.)')
    return "%s" % urllib.quote_plus(cls.__name__.lower())

  @classmethod
  def class_url(cls):
    cls_name = cls.class_name()
    return "/v1/%ss" % cls_name

  def instance_url(self):
    id = self.get('id')
    if not id:
      raise stripe_exceptions.InvalidRequestError('Could not determine which URL to request: %s instance has invalid ID: %r' % (type(self).__name__, id), 'id')
    id = encoders.utf8(id)
    base = self.class_url()
    extn = urllib.quote_plus(id)
    return "%s/%s" % (base, extn)

class ListObject(StripeObject):
  def all(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.get('url')
    response, api_key = requestor.request('get', url, params)
    return convert_to_stripe_object(response, api_key)

  def create(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.get('url')
    response, api_key = requestor.request('post', url, params)
    return convert_to_stripe_object(response, api_key)

  def retrieve(self, id, **params):
    requestor = APIRequestor(self.api_key)
    base = self.get('url')
    id = encoders.utf8(id)
    extn = urllib.quote_plus(id)
    url =  "%s/%s" % (base, extn)
    response, api_key = requestor.request('get', url, params)
    return convert_to_stripe_object(response, api_key)

class SingletonAPIResource(APIResource):
  def _ident(self):
    return [self.get('id')]

  @classmethod
  def retrieve(cls, api_key=None):
    instance = cls(None, api_key)
    instance.refresh()
    return instance

  @classmethod
  def class_url(cls):
    cls_name = cls.class_name()
    return "/v1/%s" % cls_name

  def instance_url(self):
    return self.class_url()

# Classes of API operations
class ListableAPIResource(APIResource):
  @classmethod
  def all(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.class_url()
    response, api_key = requestor.request('get', url, params)
    return convert_to_stripe_object(response, api_key)

class CreateableAPIResource(APIResource):
  @classmethod
  def create(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.class_url()
    response, api_key = requestor.request('post', url, params)
    return convert_to_stripe_object(response, api_key)

class UpdateableAPIResource(APIResource):
  def save(self):
    if self._unsaved_values:
      requestor = APIRequestor(self.api_key)

      params = {}
      for k in self._unsaved_values:
        if k == 'id':
          continue
        params[k] = getattr(self, k)

      url = self.instance_url()
      response, api_key = requestor.request('post', url, params)
      self.refresh_from(response, api_key)
    else:
      logger.debug("Trying to save already saved object %r" % (self, ))
    return self

class DeletableAPIResource(APIResource):
  def delete(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url()
    response, api_key = requestor.request('delete', url, params)
    self.refresh_from(response, api_key)
    return self

# API objects
class Account(SingletonAPIResource):
  pass

class Card(UpdateableAPIResource, DeletableAPIResource):
  def instance_url(self):
    self.id = APIRequestor._utf8(self.id)
    self.customer = APIRequestor._utf8(self.customer)

    base = Customer.class_url()
    cust_extn = urllib.quote_plus(self.customer)
    extn = urllib.quote_plus(self.id)

    return "%s/%s/cards/%s" % (base, cust_extn, extn)

  @classmethod
  def retrieve(cls, id, api_key=None, **params):
    raise NotImplementedError("Can't retrieve a card without a customer ID. Use customer.cards.retrieve('card_id') instead.")

class Charge(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
  def refund(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/refund'
    response, api_key = requestor.request('post', url, params)
    self.refresh_from(response, api_key)
    return self

  def capture(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/capture'
    response, api_key = requestor.request('post', url, params)
    self.refresh_from(response, api_key)
    return self

  def update_dispute(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/dispute'
    response, api_key = requestor.request('post', url, params)
    self.refresh_from({ 'dispute' : response }, api_key, True)
    return self.dispute

class Customer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):
  def add_invoice_item(self, **params):
    params['customer'] = self.id
    ii = InvoiceItem.create(self.api_key, **params)
    return ii

  def invoices(self, **params):
    params['customer'] = self.id
    invoices = Invoice.all(self.api_key, **params)
    return invoices

  def invoice_items(self, **params):
    params['customer'] = self.id
    iis = InvoiceItem.all(self.api_key, **params)
    return iis

  def charges(self, **params):
    params['customer'] = self.id
    charges = Charge.all(self.api_key, **params)
    return charges

  def update_subscription(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/subscription'
    response, api_key = requestor.request('post', url, params)
    self.refresh_from({ 'subscription' : response }, api_key, True)
    return self.subscription

  def cancel_subscription(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/subscription'
    response, api_key = requestor.request('delete', url, params)
    self.refresh_from({ 'subscription' : response }, api_key, True)
    return self.subscription

  def delete_discount(self, **params):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/discount'
    response, api_key = requestor.request('delete', url)
    self.refresh_from({ 'discount' : None }, api_key, True)

class Invoice(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
  def pay(self):
    requestor = APIRequestor(self.api_key)
    url = self.instance_url() + '/pay'
    response, api_key = requestor.request('post', url, {})
    return convert_to_stripe_object(response, api_key)

  @classmethod
  def upcoming(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.class_url() + '/upcoming'
    response, api_key = requestor.request('get', url, params)
    return convert_to_stripe_object(response, api_key)

class InvoiceItem(CreateableAPIResource, UpdateableAPIResource,
                  ListableAPIResource, DeletableAPIResource):
  pass

class Plan(CreateableAPIResource, DeletableAPIResource, UpdateableAPIResource, ListableAPIResource):
  pass

class Token(CreateableAPIResource):
  pass

class Coupon(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
  pass

class Event(ListableAPIResource):
  pass

class Transfer(CreateableAPIResource, ListableAPIResource):
  pass

class Recipient(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):
  def transfers(self, **params):
    params['recipient'] = self.id
    transfers = Transfer.all(self.api_key, **params)
    return transfers
