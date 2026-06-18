# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class PayoutIntent(StripeObject):
    """
    PayoutIntent represents an intent to send funds from a Financial Account to a payout method.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.payout_intent"]] = (
        "v2.money_management.payout_intent"
    )

    class From(StripeObject):
        currency: str
        """
        The currency of the financial account.
        """
        financial_account: str
        """
        The FinancialAccount that funds are pulled from.
        """

    class LatestPayout(StripeObject):
        outbound_payment: Optional[str]
        """
        The ID of the OutboundPayment, if applicable.
        """
        outbound_transfer: Optional[str]
        """
        The ID of the OutboundTransfer, if applicable.
        """
        type: Literal["outbound_payment", "outbound_transfer"]
        """
        The type of payout.
        """

    class NextAction(StripeObject):
        class HandleFailure(StripeObject):
            failure_reason: Literal[
                "account_not_configured_as_recipient",
                "currency_not_supported_for_financial_account_balance",
                "feature_not_active_for_recipient",
                "fx_rate_drift_exceeded_after_review",
                "insufficient_funds",
                "payout_method_account_type_incorrect",
                "payout_method_amount_limit_exceeded",
                "payout_method_canceled_by_customer",
                "payout_method_closed",
                "payout_method_currency_unsupported",
                "payout_method_declined",
                "payout_method_does_not_exist",
                "payout_method_expired",
                "payout_method_holder_address_incorrect",
                "payout_method_holder_details_incorrect",
                "payout_method_holder_name_incorrect",
                "payout_method_invalid_account_number",
                "payout_method_restricted",
                "payout_method_unsupported",
                "payout_method_usage_frequency_limit_exceeded",
                "recalled",
                "review_rejected",
                "to_destination_invalid",
                "unknown_failure",
            ]
            """
            Open Enum. The reason for the failure.
            """

        handle_failure: Optional[HandleFailure]
        """
        Details about a failure that requires user action. Populated when type is handle_failure.
        """
        type: Literal["handle_failure"]
        """
        Open Enum. The type of next action required.
        """
        _inner_class_types = {"handle_failure": HandleFailure}

    class RecipientNotification(StripeObject):
        setting: Literal["configured", "none"]
        """
        Closed Enum. Configuration option to enable or disable notifications to recipients.
        Do not send notifications when setting is NONE. Default to account setting when setting is CONFIGURED or not set.
        """

    class ScheduleOptions(StripeObject):
        execute_on: Optional[str]
        """
        The date when the payout should be executed, in YYYY-MM-DD format.
        """

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Timestamp describing when a PayoutIntent changed status to `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        posted_at: Optional[str]
        """
        Timestamp describing when a PayoutIntent changed status to `posted`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        processing_at: Optional[str]
        """
        Timestamp describing when a PayoutIntent changed status to `processing`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        requires_action_at: Optional[str]
        """
        Timestamp describing when a PayoutIntent changed status to `requires_action`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """

    class To(StripeObject):
        class PayoutMethodOptions(StripeObject):
            class BankAccount(StripeObject):
                class PreferredNetworkOptions(StripeObject):
                    class Ach(StripeObject):
                        submission: Optional[Literal["next_day", "same_day"]]
                        """
                        Open Enum. ACH submission timing.
                        """
                        transaction_purpose: Optional[Literal["payroll"]]
                        """
                        The transaction purpose for this ACH payment.
                        """

                    ach: Optional[Ach]
                    """
                    ACH-specific network options.
                    """
                    _inner_class_types = {"ach": Ach}

                preferred_network_options: Optional[PreferredNetworkOptions]
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
                _inner_class_types = {
                    "preferred_network_options": PreferredNetworkOptions,
                }

            bank_account: Optional[BankAccount]
            """
            Options for bank account payout methods.
            """
            _inner_class_types = {"bank_account": BankAccount}

        currency: Optional[str]
        """
        The currency to send to the recipient.
        """
        payout_method: Optional[str]
        """
        The payout method ID. Optional for OutboundPayment if recipient has default payment method. Required for OutboundTransfer.
        """
        payout_method_options: Optional[PayoutMethodOptions]
        """
        Payout method options for the PayoutIntent.
        """
        recipient: Optional[str]
        """
        The recipient ID. Only relevant for OutboundPayment.
        """
        _inner_class_types = {"payout_method_options": PayoutMethodOptions}

    amount: Amount
    """
    The monetary amount to be sent.
    """
    created: str
    """
    Time at which the PayoutIntent was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the PayoutIntent. Often useful for displaying to users.
    """
    from_: From
    """
    The FinancialAccount that funds are pulled from.
    """
    id: str
    """
    Unique identifier for the PayoutIntent.
    """
    latest_payout: LatestPayout
    """
    Details about the latest payout associated with this PayoutIntent.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_action: Optional[NextAction]
    """
    Next action required for a PayoutIntent in the requires_action state. Populated when status is requires_action.
    """
    object: Literal["v2.money_management.payout_intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    recipient_notification: Optional[RecipientNotification]
    """
    Details about the OutboundPayment notification settings for recipient. Only applicable to OutboundPayment.
    """
    schedule_options: Optional[ScheduleOptions]
    """
    Scheduling options for the payout. If this is nil, we assume immediate execution.
    """
    statement_descriptor: Optional[str]
    """
    The description that appears on the receiving end for the payout (for example, on a bank statement).
    """
    status: Literal[
        "canceled", "pending", "posted", "processing", "requires_action"
    ]
    """
    Open Enum. Current status of the PayoutIntent: `pending`, `processing`, `posted`, `canceled`, `requires_action`.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when transitioned to a particular status.
    """
    to: To
    """
    To which payout method the payout is sent.
    """
    _inner_class_types = {
        "from": From,
        "latest_payout": LatestPayout,
        "next_action": NextAction,
        "recipient_notification": RecipientNotification,
        "schedule_options": ScheduleOptions,
        "status_transitions": StatusTransitions,
        "to": To,
    }
    _field_remappings = {"from_": "from"}
