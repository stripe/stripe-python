# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

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
    acss_debit: Optional[StripeObject]
    affirm: Optional[StripeObject]
    afterpay_clearpay: Optional[StripeObject]
    alipay: Optional[StripeObject]
    au_becs_debit: Optional[StripeObject]
    bacs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    billing_details: StripeObject
    blik: Optional[StripeObject]
    boleto: Optional[StripeObject]
    card: Optional[StripeObject]
    card_present: Optional[StripeObject]
    cashapp: Optional[StripeObject]
    created: int
    customer: Optional[ExpandableField["Customer"]]
    customer_balance: Optional[StripeObject]
    eps: Optional[StripeObject]
    fpx: Optional[StripeObject]
    giropay: Optional[StripeObject]
    grabpay: Optional[StripeObject]
    id: str
    ideal: Optional[StripeObject]
    interac_present: Optional[StripeObject]
    klarna: Optional[StripeObject]
    konbini: Optional[StripeObject]
    link: Optional[StripeObject]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["payment_method"]
    oxxo: Optional[StripeObject]
    p24: Optional[StripeObject]
    paynow: Optional[StripeObject]
    paypal: Optional[StripeObject]
    pix: Optional[StripeObject]
    promptpay: Optional[StripeObject]
    radar_options: Optional[StripeObject]
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
    type: Literal[
        "acss_debit",
        "affirm",
        "afterpay_clearpay",
        "alipay",
        "au_becs_debit",
        "bacs_debit",
        "bancontact",
        "blik",
        "boleto",
        "card",
        "card_present",
        "cashapp",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "grabpay",
        "ideal",
        "interac_present",
        "klarna",
        "konbini",
        "link",
        "oxxo",
        "p24",
        "paynow",
        "paypal",
        "pix",
        "promptpay",
        "sepa_debit",
        "sofort",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    us_bank_account: Optional[StripeObject]
    wechat_pay: Optional[StripeObject]
    zip: Optional[StripeObject]

    @classmethod
    def _cls_attach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def attach(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "PaymentMethod":
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_detach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def detach(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["PaymentMethod"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Any) -> "PaymentMethod":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethod",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentMethod":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
