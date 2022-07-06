# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("apply_customer_balance", http_verb="post")
@custom_method("cancel", http_verb="post")
@custom_method("capture", http_verb="post")
@custom_method("confirm", http_verb="post")
@custom_method("increment_authorization", http_verb="post")
@custom_method("verify_microdeposits", http_verb="post")
class PaymentIntent(
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_intent"

    def apply_customer_balance(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/apply_customer_balance".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/cancel".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def capture(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/capture".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def confirm(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/confirm".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def increment_authorization(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/increment_authorization".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def verify_microdeposits(self, idempotency_key=None, **params):
        url = "/v1/payment_intents/{intent}/verify_microdeposits".format(
            intent=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(
            search_url="/v1/payment_intents/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
