# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


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
