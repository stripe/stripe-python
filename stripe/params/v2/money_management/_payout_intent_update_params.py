# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PayoutIntentUpdateParams(TypedDict):
    description: NotRequired[str]
    """
    An arbitrary string attached to the PayoutIntent. Often useful for displaying to users.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    recipient_notification: NotRequired[
        "PayoutIntentUpdateParamsRecipientNotification"
    ]
    """
    Recipient notification settings for the PayoutIntent. Only applicable when the PayoutIntent creates an OutboundPayment.
    """
    schedule_options: NotRequired["PayoutIntentUpdateParamsScheduleOptions"]
    """
    Scheduling options for the payout. If omitted, the payout is scheduled for immediate execution.
    """
    statement_descriptor: NotRequired[str]
    """
    The description that appears on the receiving end for the payout (for example, on a bank statement).
    """
    to: NotRequired["PayoutIntentUpdateParamsTo"]
    """
    To which payout method the payout is sent.
    """


class PayoutIntentUpdateParamsRecipientNotification(TypedDict):
    setting: Literal["configured", "none"]
    """
    Closed Enum. Configuration option to enable or disable notifications to recipients.
    Do not send notifications when `setting` is `none`. Use the account setting when `setting` is `configured` or omitted.
    """


class PayoutIntentUpdateParamsScheduleOptions(TypedDict):
    execute_on: NotRequired[str]
    """
    The date when the payout should be executed, in YYYY-MM-DD format.
    """


class PayoutIntentUpdateParamsTo(TypedDict):
    currency: NotRequired[str]
    """
    The currency to send to the recipient.
    """
    payout_method: NotRequired[str]
    """
    The payout method ID for the PayoutIntent. Optional when the PayoutIntent creates an OutboundPayment and the recipient has a default payout method. Required when the PayoutIntent creates an OutboundTransfer.
    """
    payout_method_options: NotRequired[
        "PayoutIntentUpdateParamsToPayoutMethodOptions"
    ]
    """
    Payout method options for the PayoutIntent.
    """
    recipient: NotRequired[str]
    """
    The recipient ID for the PayoutIntent.
    """


class PayoutIntentUpdateParamsToPayoutMethodOptions(TypedDict):
    bank_account: NotRequired[
        "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccount"
    ]
    """
    Options for bank account payout methods.
    """


class PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccount(TypedDict):
    preferred_network_options: NotRequired[
        "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions"
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
    The preferred networks to use for this PayoutIntent.
    """


class PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions(
    TypedDict,
):
    ach: NotRequired[
        "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch"
    ]
    """
    ACH-specific network options.
    """


class PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch(
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
