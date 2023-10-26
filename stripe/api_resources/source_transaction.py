# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class SourceTransaction(StripeObject):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    OBJECT_NAME: ClassVar[Literal["source_transaction"]] = "source_transaction"
    ach_credit_transfer: Optional[StripeObject]
    amount: int
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount your customer has pushed to the receiver.
    """
    chf_credit_transfer: Optional[StripeObject]
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    gbp_credit_transfer: Optional[StripeObject]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["source_transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    paper_check: Optional[StripeObject]
    sepa_credit_transfer: Optional[StripeObject]
    source: str
    """
    The ID of the source this transaction is attached to.
    """
    status: str
    """
    The status of the transaction, one of `succeeded`, `pending`, or `failed`.
    """
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
    """
    The type of source this transaction is attached to.
    """
