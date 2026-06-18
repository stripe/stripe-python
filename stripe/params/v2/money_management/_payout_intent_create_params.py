# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict

_PayoutIntentCreateParamsBase = TypedDict(
    "PayoutIntentCreateParams",
    {"from": "PayoutIntentCreateParamsFrom"},
)


class PayoutIntentCreateParams(_PayoutIntentCreateParamsBase):
    amount: AmountParam
    """
    The monetary amount to be sent.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the PayoutIntent. Often useful for displaying to users.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    recipient_notification: NotRequired[
        "PayoutIntentCreateParamsRecipientNotification"
    ]
    """
    Details about the OutboundPayment notification settings for recipient. Only applicable to OutboundPayment.
    """
    schedule_options: NotRequired["PayoutIntentCreateParamsScheduleOptions"]
    """
    Scheduling options for the payout. If this is nil, we assume immediate execution.
    """
    statement_descriptor: NotRequired[str]
    """
    The description that appears on the receiving end for the payout (for example, on a bank statement).
    """
    to: "PayoutIntentCreateParamsTo"
    """
    To which payout method the payout is sent.
    """


class PayoutIntentCreateParamsFrom(TypedDict):
    currency: str
    """
    The currency of the financial account.
    """
    financial_account: str
    """
    The FinancialAccount that funds are pulled from.
    """


class PayoutIntentCreateParamsRecipientNotification(TypedDict):
    setting: Literal["configured", "none"]
    """
    Closed Enum. Configuration option to enable or disable notifications to recipients.
    Do not send notifications when setting is NONE. Default to account setting when setting is CONFIGURED or not set.
    """


class PayoutIntentCreateParamsScheduleOptions(TypedDict):
    execute_on: NotRequired[str]
    """
    The date when the payout should be executed, in YYYY-MM-DD format.
    """


class PayoutIntentCreateParamsTo(TypedDict):
    currency: NotRequired[str]
    """
    The currency to send to the recipient.
    """
    payout_method: NotRequired[str]
    """
    The payout method ID. Optional for OutboundPayment if recipient has default payment method. Required for OutboundTransfer.
    """
    payout_method_options: NotRequired[
        "PayoutIntentCreateParamsToPayoutMethodOptions"
    ]
    """
    Payout method options for the PayoutIntent.
    """
    recipient: NotRequired[str]
    """
    The recipient ID. Only relevant for OutboundPayment.
    """


class PayoutIntentCreateParamsToPayoutMethodOptions(TypedDict):
    bank_account: NotRequired[
        "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccount"
    ]
    """
    Options for bank account payout methods.
    """


class PayoutIntentCreateParamsToPayoutMethodOptionsBankAccount(TypedDict):
    preferred_network_options: NotRequired[
        "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions"
    ]
    """
    Per-network configuration options.
    """
    preferred_networks: List[
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
        ]
    ]
    """
    The preferred networks to use for this PayoutIntent.
    """


class PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions(
    TypedDict,
):
    ach: NotRequired[
        "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch"
    ]
    """
    ACH-specific network options.
    """


class PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch(
    TypedDict,
):
    submission: NotRequired[Literal["next_day", "same_day"]]
    """
    Open Enum. ACH submission timing.
    """
    transaction_purpose: NotRequired[Literal["payroll"]]
    """
    The transaction purpose for this ACH payment.
    """
