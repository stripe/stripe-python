from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Invoice(CreateableAPIResource, UpdateableAPIResource,
              DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'invoice'

    def finalize_invoice(self, idempotency_key=None, **params):
        url = self.instance_url() + '/finalize'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def mark_uncollectible(self, idempotency_key=None, **params):
        url = self.instance_url() + '/mark_uncollectible'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def pay(self, idempotency_key=None, **params):
        url = self.instance_url() + '/pay'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def send_invoice(self, idempotency_key=None, **params):
        url = self.instance_url() + '/send'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    @classmethod
    def upcoming(cls, api_key=None, stripe_version=None, stripe_account=None,
                 **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_version=stripe_version,
                                               account=stripe_account)
        url = cls.class_url() + '/upcoming'
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_stripe_object(response, api_key, stripe_version,
                                             stripe_account)

    def void_invoice(self, idempotency_key=None, **params):
        url = self.instance_url() + '/void'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self
