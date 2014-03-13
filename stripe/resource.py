import urllib
import warnings
import sys

from stripe import api_requestor, error, util


def convert_to_stripe_object(resp, api_key):
    types = {'charge': Charge, 'customer': Customer,
             'invoice': Invoice, 'invoiceitem': InvoiceItem,
             'plan': Plan, 'coupon': Coupon, 'token': Token, 'event': Event,
             'transfer': Transfer, 'list': ListObject, 'recipient': Recipient,
             'card': Card, 'application_fee': ApplicationFee,
             'subscription': Subscription}

    if isinstance(resp, list):
        return [convert_to_stripe_object(i, api_key) for i in resp]
    elif isinstance(resp, dict) and not isinstance(resp, StripeObject):
        resp = resp.copy()
        klass_name = resp.get('object')
        if isinstance(klass_name, basestring):
            klass = types.get(klass_name, StripeObject)
        else:
            klass = StripeObject
        return klass.construct_from(resp, api_key)
    else:
        return resp


class StripeObject(dict):
    def __init__(self, id=None, api_key=None, **params):
        super(StripeObject, self).__init__()

        self._unsaved_values = set()
        self._transient_values = set()

        self._retrieve_params = params
        self._previous_metadata = None

        object.__setattr__(self, 'api_key', api_key)

        if id:
            self['id'] = id

    def __setattr__(self, k, v):
        if k[0] == '_' or k in self.__dict__:
            return super(StripeObject, self).__setattr__(k, v)
        else:
            self[k] = v

    def __getattr__(self, k):
        if k[0] == '_':
            raise AttributeError(k)

        try:
            return self[k]
        except KeyError, err:
            raise AttributeError(*err.args)

    def __setitem__(self, k, v):
        if v == "":
            raise ValueError(
                "You cannot set %s to an empty string. "
                "We interpret empty strings as None in requests."
                "You may set %s.%s = None to delete the property" % (
                    k, str(self), k))

        super(StripeObject, self).__setitem__(k, v)

        # Allows for unpickling in Python 3.x
        if not hasattr(self, '_unsaved_values'):
            self._unsaved_values = set()

        self._unsaved_values.add(k)

    def __getitem__(self, k):
        try:
            return super(StripeObject, self).__getitem__(k)
        except KeyError, err:
            if k in self._transient_values:
                raise KeyError(
                    "%r.  HINT: The %r attribute was set in the past."
                    "It was then wiped when refreshing the object with "
                    "the result returned by Stripe's API, probably as a "
                    "result of a save().  The attributes currently "
                    "available on this object are: %s" %
                    (k, k, ', '.join(self.keys())))
            else:
                raise err

    def __delitem__(self, k):
        raise TypeError(
            "You cannot delete attributes on a StripeObject. "
            "To unset a property, set it to None.")

    @classmethod
    def construct_from(cls, values, api_key):
        instance = cls(values.get('id'), api_key)
        instance.refresh_from(values, api_key)
        return instance

    def refresh_from(self, values, api_key=None, partial=False):
        self.api_key = api_key or getattr(values, 'api_key', None)

        # Wipe old state before setting new.  This is useful for e.g.
        # updating a customer, where there is no persistent card
        # parameter.  Mark those values which don't persist as transient
        if partial:
            self._unsaved_values = (self._unsaved_values - set(values))
        else:
            removed = set(self.keys()) - set(values)
            self._transient_values = self._transient_values | removed
            self._unsaved_values = set()

            self.clear()

        self._transient_values = self._transient_values - set(values)

        for k, v in values.iteritems():
            super(StripeObject, self).__setitem__(
                k, convert_to_stripe_object(v, api_key))

        self._previous_metadata = values.get('metadata')

    def request(self, method, url, params=None):
        if params is None:
            params = self._retrieve_params

        requestor = api_requestor.APIRequestor(self.api_key)
        response, api_key = requestor.request(method, url, params)

        return convert_to_stripe_object(response, api_key)

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), basestring):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), basestring):
            ident_parts.append('id=%s' % (self.get('id'),))

        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts), hex(id(self)), str(self))

        if sys.version_info[0] < 3:
            return unicode_repr.encode('utf-8')
        else:
            return unicode_repr

    def __str__(self):
        return util.json.dumps(self, sort_keys=True, indent=2)

    def to_dict(self):
        warnings.warn(
            'The `to_dict` method is deprecated and will be removed in '
            'version 2.0 of the Stripe bindings. The StripeObject is '
            'itself now a subclass of `dict`.',
            DeprecationWarning)

        return dict(self)

    @property
    def stripe_id(self):
        return self.id


class StripeObjectEncoder(util.json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        warnings.warn(
            '`StripeObjectEncoder` is deprecated and will be removed in '
            'version 2.0 of the Stripe bindings.  StripeObject is now a '
            'subclass of `dict` and is handled natively by the built-in '
            'json library.',
            DeprecationWarning)
        super(StripeObjectEncoder, self).__init__(*args, **kwargs)


class APIResource(StripeObject):

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    def refresh(self):
        self.refresh_from(self.request('get', self.instance_url()))
        return self

    @classmethod
    def class_name(cls):
        if cls == APIResource:
            raise NotImplementedError(
                'APIResource is an abstract class.  You should perform '
                'actions on its subclasses (e.g. Charge, Customer)')
        return str(urllib.quote_plus(cls.__name__.lower()))

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%ss" % (cls_name,)

    def instance_url(self):
        id = self.get('id')
        if not id:
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r' % (type(self).__name__, id), 'id')
        id = util.utf8(id)
        base = self.class_url()
        extn = urllib.quote_plus(id)
        return "%s/%s" % (base, extn)


class ListObject(StripeObject):

    def all(self, **params):
        return self.request('get', self['url'], params)

    def create(self, **params):
        return self.request('post', self['url'], params)

    def retrieve(self, id, **params):
        base = self.get('url')
        id = util.utf8(id)
        extn = urllib.quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request('get', url, params)


class SingletonAPIResource(APIResource):

    @classmethod
    def retrieve(cls, api_key=None):
        return super(SingletonAPIResource, cls).retrieve(None,
                                                         api_key=api_key)

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()


# Classes of API operations


class ListableAPIResource(APIResource):

    @classmethod
    def all(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        return convert_to_stripe_object(response, api_key)


class CreateableAPIResource(APIResource):

    @classmethod
    def create(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('post', url, params)
        return convert_to_stripe_object(response, api_key)


class UpdateableAPIResource(APIResource):

    def save(self):
        updated_params = self.serialize(self)

        if getattr(self, 'metadata', None):
            updated_params['metadata'] = self.serialize_metadata()

        if updated_params:
            self.refresh_from(self.request('post', self.instance_url(),
                                           updated_params))
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self

    def serialize_metadata(self):
        if 'metadata' in self._unsaved_values:
            # the metadata object has been reassigned
            # i.e. as object.metadata = {key: val}
            metadata_update = self.metadata
            keys_to_unset = set(self._previous_metadata.keys()) - \
                set(self.metadata.keys())
            for key in keys_to_unset:
                metadata_update[key] = ""

            return metadata_update
        else:
            return self.serialize(self.metadata)

    def serialize(self, obj):
        params = {}
        if obj._unsaved_values:
            for k in obj._unsaved_values:
                if k == 'id' or k == '_previous_metadata':
                    continue
                v = getattr(obj, k)
                params[k] = v if v is not None else ""
        return params


class DeletableAPIResource(APIResource):

    def delete(self, **params):
        self.refresh_from(self.request('delete', self.instance_url(), params))
        return self

# API objects


class Account(SingletonAPIResource):
    pass


class Balance(SingletonAPIResource):
    pass


class BalanceTransaction(ListableAPIResource):

    @classmethod
    def class_url(cls):
        return '/v1/balance/history'


class Card(UpdateableAPIResource, DeletableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.customer = util.utf8(self.customer)

        base = Customer.class_url()
        cust_extn = urllib.quote_plus(self.customer)
        extn = urllib.quote_plus(self.id)

        return "%s/%s/cards/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a card without a customer ID. Use "
            "customer.cards.retrieve('card_id') instead.")


class Charge(CreateableAPIResource, ListableAPIResource,
             UpdateableAPIResource):

    def refund(self, **params):
        url = self.instance_url() + '/refund'
        self.refresh_from(self.request('post', url, params))
        return self

    def capture(self, **params):
        url = self.instance_url() + '/capture'
        self.refresh_from(self.request('post', url, params))
        return self

    def update_dispute(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/dispute'
        response, api_key = requestor.request('post', url, params)
        self.refresh_from({'dispute': response}, api_key, True)
        return self.dispute

    def close_dispute(self):
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/dispute/close'
        response, api_key = requestor.request('post', url, {})
        self.refresh_from({'dispute': response}, api_key, True)
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
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/subscription'
        response, api_key = requestor.request('post', url, params)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    def cancel_subscription(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/subscription'
        response, api_key = requestor.request('delete', url, params)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)


class Invoice(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource):

    def pay(self):
        return self.request('post', self.instance_url() + '/pay', {})

    @classmethod
    def upcoming(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url() + '/upcoming'
        response, api_key = requestor.request('get', url, params)
        return convert_to_stripe_object(response, api_key)


class InvoiceItem(CreateableAPIResource, UpdateableAPIResource,
                  ListableAPIResource, DeletableAPIResource):
    pass


class Plan(CreateableAPIResource, DeletableAPIResource,
           UpdateableAPIResource, ListableAPIResource):
    pass


class Subscription(UpdateableAPIResource, DeletableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.customer = util.utf8(self.customer)

        base = Customer.class_url()
        cust_extn = urllib.quote_plus(self.customer)
        extn = urllib.quote_plus(self.id)

        return "%s/%s/subscriptions/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a subscription without a customer ID. "
            "Use customer.subscriptions.retrieve('subscription_id') instead.")

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)


class Token(CreateableAPIResource):
    pass


class Coupon(CreateableAPIResource, DeletableAPIResource,
             ListableAPIResource):
    pass


class Event(ListableAPIResource):
    pass


class Transfer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource):
    pass


class Recipient(CreateableAPIResource, UpdateableAPIResource,
                ListableAPIResource, DeletableAPIResource):

    def transfers(self, **params):
        params['recipient'] = self.id
        transfers = Transfer.all(self.api_key, **params)
        return transfers


class ApplicationFee(ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'application_fee'

    def refund(self, **params):
        url = self.instance_url() + '/refund'
        self.refresh_from(self.request('post', url, params))
        return self
