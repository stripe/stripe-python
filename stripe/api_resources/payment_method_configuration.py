# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class PaymentMethodConfiguration(
    CreateableAPIResource["PaymentMethodConfiguration"],
    ListableAPIResource["PaymentMethodConfiguration"],
    UpdateableAPIResource["PaymentMethodConfiguration"],
):
    """
    An object detailing payment method configurations.
    """

    OBJECT_NAME = "payment_method_configuration"
    acss_debit: Optional[StripeObject]
    active: bool
    affirm: Optional[StripeObject]
    afterpay_clearpay: Optional[StripeObject]
    alipay: Optional[StripeObject]
    apple_pay: Optional[StripeObject]
    application: Optional[str]
    au_becs_debit: Optional[StripeObject]
    bacs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    blik: Optional[StripeObject]
    boleto: Optional[StripeObject]
    card: Optional[StripeObject]
    cartes_bancaires: Optional[StripeObject]
    cashapp: Optional[StripeObject]
    eps: Optional[StripeObject]
    fpx: Optional[StripeObject]
    giropay: Optional[StripeObject]
    google_pay: Optional[StripeObject]
    grabpay: Optional[StripeObject]
    id: str
    id_bank_transfer: Optional[StripeObject]
    ideal: Optional[StripeObject]
    is_default: bool
    jcb: Optional[StripeObject]
    klarna: Optional[StripeObject]
    konbini: Optional[StripeObject]
    link: Optional[StripeObject]
    livemode: bool
    multibanco: Optional[StripeObject]
    name: str
    netbanking: Optional[StripeObject]
    object: Literal["payment_method_configuration"]
    oxxo: Optional[StripeObject]
    p24: Optional[StripeObject]
    parent: Optional[str]
    pay_by_bank: Optional[StripeObject]
    paynow: Optional[StripeObject]
    paypal: Optional[StripeObject]
    promptpay: Optional[StripeObject]
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
    upi: Optional[StripeObject]
    us_bank_account: Optional[StripeObject]
    wechat_pay: Optional[StripeObject]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "PaymentMethodConfiguration":
        return cast(
            "PaymentMethodConfiguration",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["PaymentMethodConfiguration"]:
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
    def modify(cls, id, **params: Any) -> "PaymentMethodConfiguration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodConfiguration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentMethodConfiguration":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
