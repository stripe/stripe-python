# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class PaymentMethodDomain(
    CreateableAPIResource["PaymentMethodDomain"],
    ListableAPIResource["PaymentMethodDomain"],
    UpdateableAPIResource["PaymentMethodDomain"],
):
    """
    A payment method domain represents a web domain that you have registered with Stripe.
    Stripe Elements use registered payment method domains to control where certain payment methods are shown.

    Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
    """

    OBJECT_NAME = "payment_method_domain"
    apple_pay: StripeObject
    created: str
    domain_name: str
    enabled: bool
    google_pay: StripeObject
    id: str
    link: StripeObject
    livemode: bool
    object: Literal["payment_method_domain"]
    paypal: StripeObject

    @classmethod
    def _cls_validate(
        cls,
        payment_method_domain,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                payment_method_domain=util.sanitize_id(payment_method_domain)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_validate")
    def validate(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                payment_method_domain=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
