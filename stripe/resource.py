import urllib
import warnings
import sys
from copy import deepcopy

from stripe import api_requestor, error, util, upload_api_base


def convert_to_stripe_object(resp, api_key, account):
    types = {
        'account': Account,
        'alipay_account': AlipayAccount,
        'apple_pay_domain': ApplePayDomain,
        'application_fee': ApplicationFee,
        'bank_account': BankAccount,
        'bitcoin_receiver': BitcoinReceiver,
        'bitcoin_transaction': BitcoinTransaction,
        'card': Card,
        'charge': Charge,
        'country_spec': CountrySpec,
        'coupon': Coupon,
        'customer': Customer,
        'dispute': Dispute,
        'event': Event,
        'fee_refund': ApplicationFeeRefund,
        'file_upload': FileUpload,
        'invoice': Invoice,
        'invoiceitem': InvoiceItem,
        'list': ListObject,
        'plan': Plan,
        'recipient': Recipient,
        'refund': Refund,
        'source': Source,
        'subscription': Subscription,
        'subscription_item': SubscriptionItem,
        'three_d_secure': ThreeDSecure,
        'token': Token,
        'transfer': Transfer,
        'transfer_reversal': Reversal,
        'product': Product,
        'sku': SKU,
        'order': Order,
        'order_return': OrderReturn
    }

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


def convert_array_to_dict(arr):
    if isinstance(arr, list):
        d = {}
        for i, value in enumerate(arr):
            d[str(i)] = value
        return d
    else:
        return arr


def populate_headers(idempotency_key):
    if idempotency_key is not None:
        return {"Idempotency-Key": idempotency_key}
    return None


def _compute_diff(current, previous):
    if isinstance(current, dict):
        previous = previous or {}
        diff = current.copy()
        for key in set(previous.keys()) - set(diff.keys()):
            diff[key] = ""
        return diff
    return current if current is not None else ""


def _serialize_list(array, previous):
    array = array or []
    previous = previous or []
    params = {}

    for i, v in enumerate(array):
        previous_item = previous[i] if len(previous) > i else None
        if hasattr(v, 'serialize'):
            params[str(i)] = v.serialize(previous_item)
        else:
            params[str(i)] = _compute_diff(v, previous_item)

    return params


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

    def update(self, update_dict):
        for k in update_dict:
            self._unsaved_values.add(k)

        return super(StripeObject, self).update(update_dict)

    def __setattr__(self, k, v):
        if k[0] == '_' or k in self.__dict__:
            return super(StripeObject, self).__setattr__(k, v)

        self[k] = v
        return None

    def __getattr__(self, k):
        if k[0] == '_':
            raise AttributeError(k)

        try:
            return self[k]
        except KeyError as err:
            raise AttributeError(*err.args)

        return None

    def __delattr__(self, k):
        if k[0] == '_' or k in self.__dict__:
            return super(StripeObject, self).__delattr__(k)
        else:
            del self[k]

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
        except KeyError as err:
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
        super(StripeObject, self).__delitem__(k)

        # Allows for unpickling in Python 3.x
        if hasattr(self, '_unsaved_values'):
            self._unsaved_values.remove(k)

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

    def serialize(self, previous):
        params = {}
        unsaved_keys = self._unsaved_values or set()
        previous = previous or self._previous or {}

        for k, v in self.items():
            if k == 'id' or (isinstance(k, str) and k.startswith('_')):
                continue
            elif isinstance(v, APIResource):
                continue
            elif hasattr(v, 'serialize'):
                params[k] = v.serialize(previous.get(k, None))
            elif k in unsaved_keys:
                params[k] = _compute_diff(v, previous.get(k, None))
            elif k == 'additional_owners' and v is not None:
                params[k] = _serialize_list(v, previous.get(k, None))

        return params

    # This class overrides __setitem__ to throw exceptions on inputs that it
    # doesn't like. This can cause problems when we try to copy an object
    # wholesale because some data that's returned from the API may not be valid
    # if it was set to be set manually. Here we override the class' copy
    # arguments so that we can bypass these possible exceptions on __setitem__.
    def __copy__(self):
        copied = StripeObject(self.get('id'), self.api_key,
                              stripe_account=self.stripe_account)

        copied._retrieve_params = self._retrieve_params

        for k, v in self.items():
            # Call parent's __setitem__ to avoid checks that we've added in the
            # overridden version that can throw exceptions.
            super(StripeObject, copied).__setitem__(k, v)

        return copied

    # This class overrides __setitem__ to throw exceptions on inputs that it
    # doesn't like. This can cause problems when we try to copy an object
    # wholesale because some data that's returned from the API may not be valid
    # if it was set to be set manually. Here we override the class' copy
    # arguments so that we can bypass these possible exceptions on __setitem__.
    def __deepcopy__(self, memo):
        copied = self.__copy__()
        memo[id(self)] = copied

        for k, v in self.items():
            # Call parent's __setitem__ to avoid checks that we've added in the
            # overridden version that can throw exceptions.
            super(StripeObject, copied).__setitem__(k, deepcopy(v, memo))

        return copied


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

    def list(self, **params):
        return self.request('get', self['url'], params)

    def all(self, **params):
        warnings.warn("The `all` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list` method instead",
                      DeprecationWarning)
        return self.list(**params)

    def auto_paging_iter(self):
        page = self
        params = dict(self._retrieve_params)

        while True:
            item_id = None
            for item in page:
                item_id = item.get('id', None)
                yield item

            if not getattr(page, 'has_more', False) or item_id is None:
                return

            params['starting_after'] = item_id
            page = self.list(**params)

    def create(self, idempotency_key=None, **params):
        headers = populate_headers(idempotency_key)
        return self.request('post', self['url'], params, headers)

    def retrieve(self, id, **params):
        base = self.get('url')
        id = util.utf8(id)
        extn = urllib.quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request('get', url, params)

    def __iter__(self):
        return getattr(self, 'data', []).__iter__()


class SingletonAPIResource(APIResource):

    @classmethod
    def retrieve(cls, **params):
        return super(SingletonAPIResource, cls).retrieve(None, **params)

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()


# Classes of API operations


class ListableAPIResource(APIResource):

    @classmethod
    def all(cls, *args, **params):
        warnings.warn("The `all` class method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list` class method instead",
                      DeprecationWarning)
        return cls.list(*args, **params)

    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(cls, api_key=None, idempotency_key=None,
             stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_base=cls.api_base(),
                                               account=stripe_account)
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        stripe_object = convert_to_stripe_object(response, api_key,
                                                 stripe_account)
        stripe_object._retrieve_params = params
        return stripe_object


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

    @classmethod
    def _modify(cls, url, api_key=None, idempotency_key=None,
                stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key, account=stripe_account)
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)
        return convert_to_stripe_object(response, api_key, stripe_account)

    @classmethod
    def modify(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), urllib.quote_plus(util.utf8(sid)))
        return cls._modify(url, **params)

    def save(self, idempotency_key=None):
        updated_params = self.serialize(None)
        headers = populate_headers(idempotency_key)

        if updated_params:
            self.refresh_from(self.request('post', self.instance_url(),
                                           updated_params, headers))
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self


class DeletableAPIResource(APIResource):

    def delete(self, **params):
        self.refresh_from(self.request('delete', self.instance_url(), params))
        return self


# API objects
class Account(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource, DeletableAPIResource):
    @classmethod
    def retrieve(cls, id=None, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def modify(cls, id=None, **params):
        return cls._modify(cls._build_instance_url(id), **params)

    @classmethod
    def _build_instance_url(cls, sid):
        if not sid:
            return "/v1/account"
        sid = util.utf8(sid)
        base = cls.class_url()
        extn = urllib.quote_plus(sid)
        return "%s/%s" % (base, extn)

    def instance_url(self):
        return self._build_instance_url(self.get('id'))

    def reject(self, reason=None, idempotency_key=None):
        url = self.instance_url() + '/reject'
        headers = populate_headers(idempotency_key)
        if reason:
            params = {"reason": reason}
        else:
            params = {}
        self.refresh_from(
            self.request('post', url, params, headers)
        )
        return self


class AlipayAccount(UpdateableAPIResource, DeletableAPIResource):

    @classmethod
    def _build_instance_url(cls, customer, sid):
        token = util.utf8(sid)
        extn = urllib.quote_plus(token)
        customer = util.utf8(customer)

        base = Customer.class_url()
        owner_extn = urllib.quote_plus(customer)

        return "%s/%s/sources/%s" % (base, owner_extn, extn)

    def instance_url(self):
        return self._build_instance_url(self.customer, self.id)

    @classmethod
    def modify(cls, customer, id, **params):
        url = cls._build_instance_url(customer, id)
        return cls._modify(url, **params)

    @classmethod
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
        raise NotImplementedError(
            "Can't retrieve an Alipay account without a customer ID. "
            "Use customer.sources.retrieve('alipay_account_id') instead.")


class Balance(SingletonAPIResource):
    pass


class BalanceTransaction(ListableAPIResource):

    @classmethod
    def class_url(cls):
        return '/v1/balance/history'


class Card(UpdateableAPIResource, DeletableAPIResource):

    def instance_url(self):
        token = util.utf8(self.id)
        extn = urllib.quote_plus(token)
        if (hasattr(self, 'customer')):
            customer = util.utf8(self.customer)

            base = Customer.class_url()
            owner_extn = urllib.quote_plus(customer)
            class_base = "sources"

        elif (hasattr(self, 'recipient')):
            recipient = util.utf8(self.recipient)

            base = Recipient.class_url()
            owner_extn = urllib.quote_plus(recipient)
            class_base = "cards"

        elif (hasattr(self, 'account')):
            account = util.utf8(self.account)

            base = Account.class_url()
            owner_extn = urllib.quote_plus(account)
            class_base = "external_accounts"

        else:
            raise error.InvalidRequestError(
                "Could not determine whether card_id %s is "
                "attached to a customer, recipient, or "
                "account." % token, 'id')

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a card without a customer, recipient or account "
            "ID. Call save on customer.sources.retrieve('card_id'), "
            "recipient.cards.retrieve('card_id'), or "
            "account.external_accounts.retrieve('card_id') instead.")

    @classmethod
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
        raise NotImplementedError(
            "Can't retrieve a card without a customer, recipient or account "
            "ID. Use customer.sources.retrieve('card_id'), "
            "recipient.cards.retrieve('card_id'), or "
            "account.external_accounts.retrieve('card_id') instead.")


class VerifyMixin(object):

    def verify(self, idempotency_key=None, **params):
        url = self.instance_url() + '/verify'
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self


class BankAccount(UpdateableAPIResource, DeletableAPIResource, VerifyMixin):

    def instance_url(self):
        token = util.utf8(self.id)
        extn = urllib.quote_plus(token)
        if (hasattr(self, 'customer')):
            customer = util.utf8(self.customer)

            base = Customer.class_url()
            owner_extn = urllib.quote_plus(customer)
            class_base = "sources"

        elif (hasattr(self, 'account')):
            account = util.utf8(self.account)

            base = Account.class_url()
            owner_extn = urllib.quote_plus(account)
            class_base = "external_accounts"

        else:
            raise error.InvalidRequestError(
                "Could not determine whether bank_account_id %s is "
                "attached to a customer or an account." % token, 'id')

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a bank account without a customer or account ID. "
            "Call save on customer.sources.retrieve('bank_account_id') or "
            "account.external_accounts.retrieve('bank_account_id') instead.")

    @classmethod
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
        raise NotImplementedError(
            "Can't retrieve a bank account without a customer or account ID. "
            "Use customer.sources.retrieve('bank_account_id') or "
            "account.external_accounts.retrieve('bank_account_id') instead.")


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


class Dispute(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource):

    def close(self, idempotency_key=None):
        url = self.instance_url() + '/close'
        headers = populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, {}, headers))
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
        invoices = Invoice.list(self.api_key, **params)
        return invoices

    def invoice_items(self, **params):
        params['customer'] = self.id
        iis = InvoiceItem.list(self.api_key, **params)
        return iis

    def charges(self, **params):
        params['customer'] = self.id
        charges = Charge.list(self.api_key, **params)
        return charges

    def update_subscription(self, idempotency_key=None, **params):
        warnings.warn(
            'The `update_subscription` method is deprecated. Instead, use the '
            '`subscriptions` resource on the customer object to update a '
            'subscription',
            DeprecationWarning)
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/subscription'
        headers = populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    def cancel_subscription(self, idempotency_key=None, **params):
        warnings.warn(
            'The `cancel_subscription` method is deprecated. Instead, use the '
            '`subscriptions` resource on the customer object to cancel a '
            'subscription',
            DeprecationWarning)
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


class Subscription(CreateableAPIResource, DeletableAPIResource,
                   UpdateableAPIResource, ListableAPIResource):

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               account=self.stripe_account)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)

    @classmethod
    def modify(cls, sid, **params):
        if "items" in params:
            params["items"] = convert_array_to_dict(params["items"])
        return super(Subscription, cls).modify(sid, **params)

    @classmethod
    def create(cls, **params):
        if "items" in params:
            params["items"] = convert_array_to_dict(params["items"])
        return super(Subscription, cls).create(**params)


class SubscriptionItem(CreateableAPIResource, DeletableAPIResource,
                       UpdateableAPIResource, ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'subscription_item'


class Refund(CreateableAPIResource, ListableAPIResource,
             UpdateableAPIResource):
    pass


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
        token = util.utf8(self.id)
        transfer = util.utf8(self.transfer)
        base = Transfer.class_url()
        cust_extn = urllib.quote_plus(transfer)
        extn = urllib.quote_plus(token)
        return "%s/%s/reversals/%s" % (base, cust_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a reversal without a transfer"
            "ID. Call save on transfer.reversals.retrieve('reversal_id')")

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a reversal without a transfer"
            "ID. Use transfer.reversals.retrieve('reversal_id')")


class Recipient(CreateableAPIResource, UpdateableAPIResource,
                ListableAPIResource, DeletableAPIResource):

    def transfers(self, **params):
        params['recipient'] = self.id
        transfers = Transfer.list(self.api_key, **params)
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

    @classmethod
    def _build_instance_url(cls, fee, sid):
        fee = util.utf8(fee)
        sid = util.utf8(sid)
        base = ApplicationFee.class_url()
        cust_extn = urllib.quote_plus(fee)
        extn = urllib.quote_plus(sid)
        return "%s/%s/refunds/%s" % (base, cust_extn, extn)

    @classmethod
    def modify(cls, fee, sid, **params):
        url = cls._build_instance_url(fee, sid)
        return cls._modify(url, **params)

    def instance_url(self):
        return self._build_instance_url(self.fee, self.id)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a refund without an application fee ID. "
            "Use application_fee.refunds.retrieve('refund_id') instead.")


class BitcoinReceiver(CreateableAPIResource, UpdateableAPIResource,
                      DeletableAPIResource, ListableAPIResource):

    def instance_url(self):
        token = util.utf8(self.id)
        extn = urllib.quote_plus(token)

        if (hasattr(self, 'customer')):
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            cust_extn = urllib.quote_plus(customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)

    @classmethod
    def class_url(cls):
        return '/v1/bitcoin/receivers'


class BitcoinTransaction(StripeObject):
    pass


class Product(CreateableAPIResource, UpdateableAPIResource,
              ListableAPIResource, DeletableAPIResource):
    pass


class SKU(CreateableAPIResource, UpdateableAPIResource,
          ListableAPIResource, DeletableAPIResource):
    pass


class Order(CreateableAPIResource, UpdateableAPIResource,
            ListableAPIResource):
    def pay(self, idempotency_key=None, **params):
        headers = populate_headers(idempotency_key)
        return self.request(
            'post', self.instance_url() + '/pay', params, headers)

    def return_order(self, idempotency_key=None, **params):
        headers = populate_headers(idempotency_key)
        return self.request(
            'post', self.instance_url() + '/returns', params, headers)


class OrderReturn(ListableAPIResource):
    @classmethod
    def class_url(cls):
        return '/v1/order_returns'


class CountrySpec(ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'country_spec'


class ThreeDSecure(CreateableAPIResource):
    @classmethod
    def class_url(cls):
        return '/v1/3d_secure'

    @classmethod
    def retrieve(cls, id, api_key=None, stripe_account=None, **params):
        raise NotImplementedError("Can't retrieve 3D Secure objects.")


class ApplePayDomain(CreateableAPIResource, ListableAPIResource,
                     DeletableAPIResource):
    @classmethod
    def class_url(cls):
        return '/v1/apple_pay/domains'


class Source(CreateableAPIResource):
    pass
