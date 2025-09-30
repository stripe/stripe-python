# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import Literal, NotRequired, TypedDict

_OutboundPaymentQuoteCreateParamsBase = TypedDict(
    "OutboundPaymentQuoteCreateParams",
    {"from": "OutboundPaymentQuoteCreateParamsFrom"},
)


class OutboundPaymentQuoteCreateParams(_OutboundPaymentQuoteCreateParamsBase):
    amount: AmountParam
    """
    The "presentment amount" to be sent to the recipient.
    """
    delivery_options: NotRequired[
        "OutboundPaymentQuoteCreateParamsDeliveryOptions"
    ]
    """
    Method to be used to send the OutboundPayment.
    """
    to: "OutboundPaymentQuoteCreateParamsTo"
    """
    Request details about the recipient of an OutboundPaymentQuote.
    """


class OutboundPaymentQuoteCreateParamsDeliveryOptions(TypedDict):
    bank_account: NotRequired[Literal["automatic", "local", "wire"]]
    """
    Open Enum. Method for bank account.
    """


class OutboundPaymentQuoteCreateParamsFrom(TypedDict):
    currency: str
    """
    Describes the FinancialAccount's currency drawn from.
    """
    financial_account: str
    """
    The FinancialAccount that funds were pulled from.
    """


class OutboundPaymentQuoteCreateParamsTo(TypedDict):
    currency: NotRequired[str]
    """
    Describes the currency to send to the recipient.
    If included, this currency must match a currency supported by the destination.
    Can be omitted in the following cases:
    - destination only supports one currency
    - destination supports multiple currencies and one of the currencies matches the FA currency
    - destination supports multiple currencies and one of the currencies matches the presentment currency
    Note - when both FA currency and presentment currency are supported, we pick the FA currency to minimize FX.
    """
    payout_method: NotRequired[str]
    """
    The payout method which the OutboundPayment uses to send payout.
    """
    recipient: str
    """
    To which account the OutboundPayment is sent.
    """
