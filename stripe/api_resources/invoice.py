# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("finalize_invoice", http_verb="post", http_path="finalize")
@custom_method("mark_uncollectible", http_verb="post")
@custom_method("pay", http_verb="post")
@custom_method("send_invoice", http_verb="post", http_path="send")
@custom_method("void_invoice", http_verb="post", http_path="void")
class Invoice(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "invoice"

    def finalize_invoice(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/finalize".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_uncollectible(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/mark_uncollectible".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def pay(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/pay".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def send_invoice(self, idempotency_key=None, **params):
        url = "/v1/invoices/{invoice}/send".format(
            invoice=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

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
