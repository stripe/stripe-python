# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List, Union
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
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    outbound_payment_quote: NotRequired[str]
    """
    The quote for this OutboundPayment. Only required for countries with regulatory mandates to display fee estimates before OutboundPayment creation.
    """
    payout_intent: NotRequired[str]
    """
    The PayoutIntent ID that triggered this OutboundPayment.
    """
    purpose: NotRequired[Literal["payroll"]]
    """
    The purpose of the OutboundPayment.
    """
    recipient_notification: NotRequired[
        "OutboundPaymentCreateParamsRecipientNotification"
    ]
    """
    Details about the notification settings for the OutboundPayment recipient.
    """
    recipient_verification: NotRequired[str]
    """
    The recipient verification id for this OutboundPayment. Only required for countries with regulatory mandates to verify recipient names before OutboundPayment creation.
    """
    statement_descriptor: NotRequired[str]
    """
    The description that appears on the receiving end for an OutboundPayment (for example, on a bank statement). Must be between 3 and 22 characters long for most destinations (500 for FinancialAccount destinations), and not contain profanity.
    """
    to: "OutboundPaymentCreateParamsTo"
    """
    To which payout method to send the OutboundPayment.
    """


class OutboundPaymentCreateParamsDeliveryOptions(TypedDict):
    bank_account: NotRequired["Literal['automatic', 'local', 'wire']|str"]
    """
    Open Enum. Method for bank account.
    """
    paper_check: NotRequired[
        "OutboundPaymentCreateParamsDeliveryOptionsPaperCheck"
    ]
    """
    Delivery options for paper check.
    """
    speed: NotRequired[
        "Literal['instant', 'next_business_day', 'standard']|str"
    ]
    """
    Open Enum. Speed of the payout.
    """


class OutboundPaymentCreateParamsDeliveryOptionsPaperCheck(TypedDict):
    attachment: NotRequired[str]
    """
    The ID of a file to include as an attachment with the paper check.
    """
    memo: NotRequired[str]
    """
    Memo printed on the memo field of the check.
    """
    shipping_speed: NotRequired["Literal['priority', 'standard']|str"]
    """
    Open Enum. Shipping speed of the paper check. Defaults to standard.
    """
    signature: str
    """
    Signature for the paper check.
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
    payout_method_options: NotRequired[
        "OutboundPaymentCreateParamsToPayoutMethodOptions"
    ]
    """
    Payout method options for the OutboundPayment.
    """
    recipient: str
    """
    To which account the OutboundPayment is sent.
    """


class OutboundPaymentCreateParamsToPayoutMethodOptions(TypedDict):
    bank_account: NotRequired[
        "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccount"
    ]
    """
    Options for bank account payout methods.
    """


class OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccount(TypedDict):
    preferred_network_options: NotRequired[
        "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions"
    ]
    """
    Per-network configuration options.
    """
    preferred_networks: List[
        Union[
            Literal[
                "ach",
                "becs",
                "eft",
                "fedwire",
                "fps",
                "npp",
                "rtp",
                "sepa_credit",
                "sepa_instant",
                "swift",
            ],
            str,
        ]
    ]
    """
    The preferred networks to use for this OutboundPayment.
    """


class OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions(
    TypedDict,
):
    ach: NotRequired[
        "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch"
    ]
    """
    ACH-specific network options.
    """


class OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch(
    TypedDict,
):
    submission: NotRequired["Literal['next_day', 'same_day']|str"]
    """
    Open Enum. ACH submission timing.
    """
    transaction_purpose: NotRequired[Literal["payroll"]]
    """
    The transaction purpose for this ACH payment.
    """
