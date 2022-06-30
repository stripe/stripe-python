# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Invoice(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "invoice"

    @classmethod
    def _cls_finalize_invoice(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/invoices/{invoice}/finalize".format(
            invoice=util.sanitize_id(invoice)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_finalize_invoice")
    def finalize_invoice(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/finalize".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_mark_uncollectible(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/invoices/{invoice}/mark_uncollectible".format(
            invoice=util.sanitize_id(invoice)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_mark_uncollectible")
    def mark_uncollectible(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/mark_uncollectible".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_pay(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/invoices/{invoice}/pay".format(
            invoice=util.sanitize_id(invoice)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_pay")
    def pay(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/pay".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_send_invoice(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/invoices/{invoice}/send".format(
            invoice=util.sanitize_id(invoice)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_send_invoice")
    def send_invoice(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/send".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_void_invoice(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/invoices/{invoice}/void".format(
            invoice=util.sanitize_id(invoice)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_void_invoice")
    def void_invoice(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/void".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/invoices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    def upcoming(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = cls.class_url() + "/upcoming"
        response, api_key = requestor.request("get", url, params)
        return util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
