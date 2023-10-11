# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class SourceTransaction(StripeObject):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    OBJECT_NAME = "source_transaction"
    ach_credit_transfer: Optional[StripeObject]
    amount: int
    chf_credit_transfer: Optional[StripeObject]
    created: int
    currency: str
    gbp_credit_transfer: Optional[StripeObject]
    id: str
    livemode: bool
    object: Literal["source_transaction"]
    paper_check: Optional[StripeObject]
    sepa_credit_transfer: Optional[StripeObject]
    source: str
    status: str
    type: Literal[
        "ach_credit_transfer",
        "ach_debit",
        "alipay",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ]
