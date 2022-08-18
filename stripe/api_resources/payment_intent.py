# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class PaymentIntent(
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    """
    A PaymentIntent guides you through the process of collecting a payment from your customer.
    We recommend that you create exactly one PaymentIntent for each order or
    customer session in your system. You can reference the PaymentIntent later to
    see the history of payment attempts for a particular session.

    A PaymentIntent transitions through
    [multiple statuses](https://stripe.com/docs/payments/intents#intent-statuses)
    throughout its lifetime as it interfaces with Stripe.js to perform
    authentication flows and ultimately creates at most one successful charge.

    Related guide: [Payment Intents API](https://stripe.com/docs/payments/payment-intents).
    """

    OBJECT_NAME = "payment_intent"

    @classmethod
    def _cls_apply_customer_balance(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_apply_customer_balance")
    def apply_customer_balance(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_capture(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/capture".format(
                intent=util.sanitize_id(intent)
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
            "/v1/payment_intents/{intent}/capture".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_increment_authorization(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_increment_authorization")
    def increment_authorization(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_verify_microdeposits(
        cls,
        intent,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(
            search_url="/v1/payment_intents/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
