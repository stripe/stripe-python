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
        return self._request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def mark_uncollectible(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def pay(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def send_invoice(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/send".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def upcoming(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "get",
            "/v1/invoices/upcoming",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    def void_invoice(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/invoices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
