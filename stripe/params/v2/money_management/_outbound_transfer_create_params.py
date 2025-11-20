# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict

_OutboundTransferCreateParamsBase = TypedDict(
    "OutboundTransferCreateParams",
    {"from": "OutboundTransferCreateParamsFrom"},
)


class OutboundTransferCreateParams(_OutboundTransferCreateParamsBase):
    amount: "OutboundTransferCreateParamsAmount"
    """
    The "presentment amount" for the OutboundPayment.
    """
    delivery_options: NotRequired[
        "OutboundTransferCreateParamsDeliveryOptions"
    ]
    """
    Delivery options to be used to send the OutboundTransfer.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the OutboundTransfer. Often useful for displaying to users.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    recipient_verification: NotRequired[str]
    """
    The recipient verification id for this OutboundTransfer. Only required for countries with regulatory mandates to verify recipient names before OutboundTransfer creation.
    """
    to: "OutboundTransferCreateParamsTo"
    """
    To which payout method to send the OutboundTransfer.
    """


class OutboundTransferCreateParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class OutboundTransferCreateParamsDeliveryOptions(TypedDict):
    bank_account: NotRequired[Literal["automatic", "local", "wire"]]
    """
    Open Enum. Method for bank account.
    """


class OutboundTransferCreateParamsFrom(TypedDict):
    currency: str
    """
    Describes the FinancialAmount's currency drawn from.
    """
    financial_account: str
    """
    The FinancialAccount that funds were pulled from.
    """


class OutboundTransferCreateParamsTo(TypedDict):
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
    payout_method: str
    """
    The payout method which the OutboundTransfer uses to send payout.
    """
