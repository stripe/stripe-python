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
    The requested amount and currency for the OutboundPayment.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the OutboundPayment. Often useful for displaying to users.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    recipient_notification: NotRequired[
        "OutboundPaymentCreateParamsRecipientNotification"
    ]
    """
    Details about the notification settings for the OutboundPayment recipient.
    """
    recipient_verification: NotRequired[str]
    """
    The ID of the RecipientVerification for this OutboundPayment. Required where recipient-name verification is mandated before creating an OutboundPayment.
    """
    statement_descriptor: NotRequired[str]
    """
    The description that appears on the receiving end for an OutboundPayment (for example, on a bank statement). Must be between 3 and 22 characters long for most destinations (500 for FinancialAccount destinations), and not contain profanity.
    """
    to: "OutboundPaymentCreateParamsTo"
    """
    To which payout method to send the OutboundPayment.
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
    Do not send notifications when `setting` is `none`. Use the account setting when `setting` is `configured` or omitted.
    """


class OutboundPaymentCreateParamsTo(TypedDict):
    currency: NotRequired[str]
    """
    Describes the currency to send to the recipient.
    If included, this currency must match a currency supported by the destination.
    Can be omitted in the following cases:
    - destination only supports one currency
    - destination supports multiple currencies and one matches `from.currency`
    - destination supports multiple currencies and one matches `amount.currency`
    When both `from.currency` and `amount.currency` are supported, Stripe selects `from.currency` to minimize currency conversion.
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
    preferred_networks: NotRequired[
        List[
            Union[
                Literal["ach", "fedwire", "fps", "rtp", "sepa", "swift"], str
            ]
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
    transaction_purpose: NotRequired["Literal['payroll']|str"]
    """
    The transaction purpose for this ACH payment.
    """
