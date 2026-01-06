# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict

_OutboundPaymentQuoteCreateParamsBase = TypedDict(
    "OutboundPaymentQuoteCreateParams",
    {"from": "OutboundPaymentQuoteCreateParamsFrom"},
)


class OutboundPaymentQuoteCreateParams(_OutboundPaymentQuoteCreateParamsBase):
    amount: "OutboundPaymentQuoteCreateParamsAmount"
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


class OutboundPaymentQuoteCreateParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class OutboundPaymentQuoteCreateParamsDeliveryOptions(TypedDict):
    speed: NotRequired[Literal["instant", "next_business_day", "standard"]]
    """
    Open Enum. Speed of the payout.
    """
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
