# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict

_OutboundPaymentCreateParamsBase = TypedDict(
    "OutboundPaymentCreateParams",
    {"from": "OutboundPaymentCreateParamsFrom"},
)


class OutboundPaymentCreateParams(_OutboundPaymentCreateParamsBase):
    amount: AmountParam
    """
    The "presentment amount" to be sent to the recipient.
    """
    delivery_options: NotRequired["OutboundPaymentCreateParamsDeliveryOptions"]
    """
    Delivery options to be used to send the OutboundPayment.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the OutboundPayment. Often useful for displaying to users.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    outbound_payment_quote: NotRequired[str]
    """
    The quote for this OutboundPayment. Only required for countries with regulatory mandates to display fee estimates before OutboundPayment creation.
    """
    recipient_notification: NotRequired[
        "OutboundPaymentCreateParamsRecipientNotification"
    ]
    """
    Details about the notification settings for the OutboundPayment recipient.
    """
    to: "OutboundPaymentCreateParamsTo"
    """
    To which payout method to send the OutboundPayment.
    """


class OutboundPaymentCreateParamsDeliveryOptions(TypedDict):
    bank_account: NotRequired[Literal["automatic", "local", "wire"]]
    """
    Open Enum. Method for bank account.
    """


class OutboundPaymentCreateParamsFrom(TypedDict):
    currency: str
    """
    Describes the FinancialAmount's currency drawn from.
    """
    financial_account: str
    """
    The FinancialAccount that funds were pulled from.
    """


class OutboundPaymentCreateParamsRecipientNotification(TypedDict):
    setting: Literal["configured", "none"]
    """
    Closed Enum. Configuration option to enable or disable notifications to recipients.
    Do not send notifications when setting is NONE. Default to account setting when setting is CONFIGURED or not set.
    """


class OutboundPaymentCreateParamsTo(TypedDict):
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
