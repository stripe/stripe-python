from __future__ import absolute_import, division, print_function

import warnings

from stripe import api_requestor, util
from stripe.api_resources.charge import Charge
from stripe.api_resources.invoice import Invoice
from stripe.api_resources.invoice_item import InvoiceItem
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    'source',
    operations=['create', 'retrieve', 'update', 'delete', 'list']
)
class Customer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = 'customer'

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
                                               api_version=self.stripe_version,
                                               account=self.stripe_account)
        url = self.instance_url() + '/subscription'
        headers = util.populate_headers(idempotency_key)
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
                                               api_version=self.stripe_version,
                                               account=self.stripe_account)
        url = self.instance_url() + '/subscription'
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request('delete', url, params, headers)
        self.refresh_from({'subscription': response}, api_key, True)
        return self.subscription

    # TODO: Remove arg in next major release.
    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               api_version=self.stripe_version,
                                               account=self.stripe_account)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url)
        self.refresh_from({'discount': None}, api_key, True)
