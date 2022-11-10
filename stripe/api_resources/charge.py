# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Charge(
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    """
    To charge a credit or a debit card, you create a `Charge` object. You can
    retrieve and refund individual charges as well as list all charges. Charges
    are identified by a unique, random ID.

    Related guide: [Accept a payment with the Charges API](https://stripe.com/docs/payments/accept-a-payment-charges).
    """

    OBJECT_NAME = "charge"

    @classmethod
    def _cls_capture(
        cls,
        charge,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(charge)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_capture")
    def capture(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/charges/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "fraudulent"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "safe"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
