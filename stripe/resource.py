import urllib
import warnings
import sys

from stripe import api_requestor, error, util, upload_api_base


def convert_to_stripe_object(resp, api_key, account):
    types = {'charge': Charge, 'customer': Customer,
             'invoice': Invoice, 'invoiceitem': InvoiceItem,
             'plan': Plan, 'coupon': Coupon, 'token': Token, 'event': Event,
             'transfer': Transfer, 'list': ListObject, 'recipient': Recipient,
             'card': Card, 'application_fee': ApplicationFee,
             'subscription': Subscription, 'refund': Refund,
             'file_upload': FileUpload,
             'fee_refund': ApplicationFeeRefund,
             'bitcoin_receiver': BitcoinReceiver,
             'bitcoin_transaction': BitcoinTransaction,
             'transfer_reversal': Reversal}

    if isinstance(resp, list):
        return [convert_to_stripe_object(i, api_key, account) for i in resp]
    elif isinstance(resp, dict) and not isinstance(resp, StripeObject):
        resp = resp.copy()
        klass_name = resp.get('object')
        if isinstance(klass_name, basestring):
            klass = types.get(klass_name, StripeObject)
        else:
            klass = StripeObject
        return klass.construct_from(resp, api_key, stripe_account=account)
    else:
        return resp


def populate_headers(idempotency_key):
    if idempotency_key is not None:
        return {"Idempotency-Key": idempotency_key}
    return None


class StripeObject(dict):
    def __init__(self, id=None, api_key=None, stripe_account=None, **params):
        super(StripeObject, self).__init__()

        self._unsaved_values = set()
        self._transient_values = set()

        self._retrieve_params = params
        self._previous = None

        object.__setattr__(self, 'api_key', api_key)
        object.__setattr__(self, 'stripe_account', stripe_account)

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
    def construct_from(cls, values, key, stripe_account=None):
        instance = cls(values.get('id'), api_key=key,
                       stripe_account=stripe_account)
        instance.refresh_from(values, api_key=key,
                              stripe_account=stripe_account)
        return instance

    def refresh_from(self, values, api_key=None, partial=False,
                     stripe_account=None):
        self.api_key = api_key or getattr(values, 'api_key', None)
        self.stripe_account = \
            stripe_account or getattr(values, 'stripe_account', None)

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
                k, convert_to_stripe_object(v, api_key, stripe_account))

        self._previous = values

    @classmethod
    def api_base(cls):
        return None

    def request(self, method, url, params=None, headers=None):
        if params is None:
            params = self._retrieve_params
        requestor = api_requestor.APIRequestor(
            key=self.api_key, api_base=self.api_base(),
            account=self.stripe_account)
        response, api_key = requestor.request(method, url, params, headers)

        return convert_to_stripe_object(response, api_key, self.stripe_account)

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
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
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

    def create(self, idempotency_key=None, **params):
        headers = populate_headers(idempotency_key)
        return self.request('post', self['url'], params, headers)

    def retrieve(self, id, **params):
        base = self.get('url')
        id = util.utf8(id)
        extn = urllib.quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request('get', url, params)


class SingletonAPIResource(APIResource):

    @classmethod
    def retrieve(cls, api_key=None, stripe_account=None):
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
    def all(cls, api_key=None, idempotency_key=None,
            stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key, account=stripe_account)
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        return convert_to_stripe_object(response, api_key, stripe_account)


class CreateableAPIResource(APIResource):

    @classmethod
    def create(cls, api_key=None, idempotency_key=None,
               stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key, account=stripe_account)
        url = cls.class_url()
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)
        return convert_to_stripe_object(response, api_key, stripe_account)


class UpdateableAPIResource(APIResource):

    def save(self, idempotency_key=None):
        updated_params = self.serialize(self)
        headers = populate_headers(idempotency_key)

        for k, v in self.items():
            if k == 'id' or k.startswith('_'):
                continue
            if isinstance(v, dict):
                updated_params[k] = self.serialize_nested(k)

        if updated_params:
            self.refresh_from(self.request('post', self.instance_url(),
                                           updated_params, headers))
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self

    def serialize_nested(self, key):
        if key in self._unsaved_values:
            # the object has been reassigned
            # i.e. as object.key = {foo: bar}
            update = getattr(self, key)
            previous = (self._previous or {}).get(key) or {}
            for key in set(previous.keys()) - set(update.keys()):
                update[key] = ""
            return update
        else:
            return self.serialize(getattr(self, key))

    def serialize(self, obj):
        params = {}
        if obj._unsaved_values:
            for k in obj._unsaved_values:
                if k == 'id' or k.startswith('_'):
                    continue
                v = getattr(obj, k)
                params[k] = v if v is not None else ""
        return params


class DeletableAPIResource(APIResource):

    def delete(self, **params):
        self.refresh_from(self.request('delete', self.instance_url(), params))
        return self


# API objects
class Account(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource):
    @classmethod
    def retrieve(cls, id=None, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    def instance_url(self):
        id = self.get('id')
        if not id:
            return "/v1/account"
        id = util.utf8(id)
        base = self.class_url()
        extn = urllib.quote_plus(id)
        return "%s/%s" % (base, extn)


class Balance(SingletonAPIResource):
    pass


class BalanceTransaction(ListableAPIResource):

    @classmethod
    def class_url(cls):
        return '/v1/balance/history'


class Card(UpdateableAPIResource, DeletableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        extn = urllib.quote_plus(self.id)
        if (hasattr(self, 'customer')):
            self.customer = util.utf8(self.customer)

            base = Customer.class_url()
            owner_extn = urllib.quote_plus(self.customer)

        elif (hasattr(self, 'recipient')):
            self.recipient = util.utf8(self.recipient)

            base = Recipient.class_url()
            owner_extn = urllib.quote_plus(self.recipient)

        else:
            raise error.InvalidRequestError(
                "Could not determine whether card_id %s is "
                "attached to a customer "
                "or a recipient." % self.id, 'id')

        return "%s/%s/cards/%s" % (base, owner_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
        raise NotImplementedError(
            "Can't retrieve a card without a customer or recipient"
            "ID. Use customer.cards.retrieve('card_id') or "
            "recipient.cards.retrieve('card_id') instead.")


class Charge(CreateableAPIResource, ListableAPIResource,
             UpdateableAPIResource):

    def refund(self, idempotency_key=None, **params):
        url = self.instance_url() + '/refund'
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def capture(self, idempotency_key=None, **params):
        url = self.instance_url() + '/capture'
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def update_dispute(self, idempotency_key=None, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/dispute'
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)
        self.refresh_from({'dispute': response}, api_key, True)
        return self.dispute

    def close_dispute(self, idempotency_key=None):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/dispute/close'
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, {}, headers)
        self.refresh_from({'dispute': response}, api_key, True)
        return self.dispute

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {
            'fraud_details': {'user_report': 'fraudulent'}
        }
        url = self.instance_url()
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {
            'fraud_details': {'user_report': 'safe'}
        }
        url = self.instance_url()
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self


class Customer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):

    def add_invoice_item(self, idempotency_key=None, **params):
        params['customer'] = self.id
        ii = InvoiceItem.create(self.api_key,
                                idempotency_key=idempotency_key, **params)
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

    def update_subscription(self, idempotency_key=None, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/subscription'
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    def cancel_subscription(self, idempotency_key=None, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/subscription'
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('delete', url, params, headers)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)


class Invoice(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource):

    def pay(self, idempotency_key=None):
        headers = populate_headers(idempotency_key)
        return self.request('post', self.instance_url() + '/pay', {}, headers)

    @classmethod
    def upcoming(cls, api_key=None, stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               account=stripe_account)
        url = cls.class_url() + '/upcoming'
        response, api_key = requestor.request('get', url, params)
        return convert_to_stripe_object(response, api_key, stripe_account)


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
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)


class Refund(UpdateableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.charge = util.utf8(self.charge)
        base = Charge.class_url()
        cust_extn = urllib.quote_plus(self.charge)
        extn = urllib.quote_plus(self.id)
        return "%s/%s/refunds/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a refund without a charge ID. "
            "Use charge.refunds.retrieve('refund_id') instead.")


class Token(CreateableAPIResource):
    pass


class Coupon(CreateableAPIResource, UpdateableAPIResource,
             DeletableAPIResource, ListableAPIResource):
    pass


class Event(ListableAPIResource):
    pass


class Transfer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource):

    def cancel(self):
        self.refresh_from(self.request('post',
                          self.instance_url() + '/cancel'))


class Reversal(UpdateableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.charge = util.utf8(self.transfer)
        base = Transfer.class_url()
        cust_extn = urllib.quote_plus(self.transfer)
        extn = urllib.quote_plus(self.id)
        return "%s/%s/reversals/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a reversal without a transfer"
            "ID. Use transfer.reversals.retrieve('reversal_id')")


class Recipient(CreateableAPIResource, UpdateableAPIResource,
                ListableAPIResource, DeletableAPIResource):

    def transfers(self, **params):
        params['recipient'] = self.id
        transfers = Transfer.all(self.api_key, **params)
        return transfers


class FileUpload(ListableAPIResource):
    @classmethod
    def api_base(cls):
        return upload_api_base

    @classmethod
    def class_name(cls):
        return 'file'

    @classmethod
    def create(cls, api_key=None, stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(
            api_key, api_base=cls.api_base(), account=stripe_account)
        url = cls.class_url()
        supplied_headers = {
            "Content-Type": "multipart/form-data"
        }
        response, api_key = requestor.request(
            'post', url, params=params, headers=supplied_headers)
        return convert_to_stripe_object(response, api_key, stripe_account)


class ApplicationFee(ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'application_fee'

    def refund(self, idempotency_key=None, **params):
        headers = populate_headers(idempotency_key)
        url = self.instance_url() + '/refund'
        self.refresh_from(self.request('post', url, params, headers))
        return self


class ApplicationFeeRefund(UpdateableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.fee = util.utf8(self.fee)
        base = ApplicationFee.class_url()
        cust_extn = urllib.quote_plus(self.fee)
        extn = urllib.quote_plus(self.id)
        return "%s/%s/refunds/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a refund without an application fee ID. "
            "Use application_fee.refunds.retrieve('refund_id') instead.")


class BitcoinReceiver(CreateableAPIResource, UpdateableAPIResource,
                      DeletableAPIResource, ListableAPIResource):

    def instance_url(self):
        self.id = util.utf8(self.id)
        extn = urllib.quote_plus(self.id)

        if (hasattr(self, 'customer')):
            self.customer = util.utf8(self.customer)
            base = Customer.class_url()
            cust_extn = urllib.quote_plus(self.customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)

    @classmethod
    def class_url(cls):
        return '/v1/bitcoin/receivers'


class BitcoinTransaction(StripeObject):
    pass
