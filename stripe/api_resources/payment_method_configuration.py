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
from typing import Optional, cast
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
    acss_debit: StripeObject
    active: bool
    affirm: StripeObject
    afterpay_clearpay: StripeObject
    alipay: StripeObject
    apple_pay: StripeObject
    application: Optional[str]
    au_becs_debit: StripeObject
    bacs_debit: StripeObject
    bancontact: StripeObject
    blik: StripeObject
    boleto: StripeObject
    card: StripeObject
    cartes_bancaires: StripeObject
    cashapp: StripeObject
    eps: StripeObject
    fpx: StripeObject
    giropay: StripeObject
    google_pay: StripeObject
    grabpay: StripeObject
    id: str
    id_bank_transfer: StripeObject
    ideal: StripeObject
    is_default: bool
    jcb: StripeObject
    klarna: StripeObject
    konbini: StripeObject
    link: StripeObject
    livemode: bool
    multibanco: StripeObject
    name: str
    netbanking: StripeObject
    object: Literal["payment_method_configuration"]
    oxxo: StripeObject
    p24: StripeObject
    parent: Optional[str]
    pay_by_bank: StripeObject
    paynow: StripeObject
    paypal: StripeObject
    promptpay: StripeObject
    sepa_debit: StripeObject
    sofort: StripeObject
    upi: StripeObject
    us_bank_account: StripeObject
    wechat_pay: StripeObject

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
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
    def modify(cls, id, **params) -> "PaymentMethodConfiguration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodConfiguration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id, api_key=None, **params
    ) -> "PaymentMethodConfiguration":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
