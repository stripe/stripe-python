# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer


class PaymentMethod(
    CreateableAPIResource["PaymentMethod"],
    ListableAPIResource["PaymentMethod"],
    UpdateableAPIResource["PaymentMethod"],
):
    """
    PaymentMethod objects represent your customer's payment instruments.
    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).
    """

    OBJECT_NAME = "payment_method"
    acss_debit: StripeObject
    affirm: StripeObject
    afterpay_clearpay: StripeObject
    alipay: StripeObject
    au_becs_debit: StripeObject
    bacs_debit: StripeObject
    bancontact: StripeObject
    billing_details: StripeObject
    blik: StripeObject
    boleto: StripeObject
    card: StripeObject
    card_present: StripeObject
    cashapp: StripeObject
    created: str
    customer: Optional[ExpandableField["Customer"]]
    customer_balance: StripeObject
    eps: StripeObject
    fpx: StripeObject
    giropay: StripeObject
    grabpay: StripeObject
    id: str
    ideal: StripeObject
    interac_present: StripeObject
    klarna: StripeObject
    konbini: StripeObject
    link: StripeObject
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["payment_method"]
    oxxo: StripeObject
    p24: StripeObject
    paynow: StripeObject
    paypal: StripeObject
    pix: StripeObject
    promptpay: StripeObject
    radar_options: StripeObject
    sepa_debit: StripeObject
    sofort: StripeObject
    type: str
    us_bank_account: StripeObject
    wechat_pay: StripeObject
    zip: StripeObject

    @classmethod
    def _cls_attach(
        cls,
        payment_method,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_attach")
    def attach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_detach(
        cls,
        payment_method,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_detach")
    def detach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
