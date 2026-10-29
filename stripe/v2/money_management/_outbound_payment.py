# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class OutboundPayment(StripeObject):
    """
    OutboundPayment represents a single money movement from one FinancialAccount you own to a payout method someone else owns.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.outbound_payment"]] = (
        "v2.money_management.outbound_payment"
    )

    class From(StripeObject):
        debited: Amount
        """
        The monetary amount debited from the sender, only set on responses.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """

    class RecipientNotification(StripeObject):
        setting: Literal["configured", "none"]
        """
        Closed Enum. Configuration option to enable or disable notifications to recipients.
        Do not send notifications when `setting` is `none`. Use the account setting when `setting` is `configured` or omitted.
        """

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Union[
                Literal[
                    "fx_rate_drift_exceeded_after_review",
                    "payout_method_amount_limit_exceeded",
                    "payout_method_declined",
                    "payout_method_does_not_exist",
                    "payout_method_expired",
                    "payout_method_unsupported",
                    "payout_method_usage_frequency_limit_exceeded",
                    "review_rejected",
                    "unknown_failure",
                ],
                str,
            ]
            """
            Open Enum. The `failed` status reason.
            """

        class Processing(StripeObject):
            reason: Union[Literal["under_review"], str]
            """
            Open Enum. The `processing` status reason.
            """

        class Returned(StripeObject):
            reason: Union[
                Literal[
                    "payout_method_canceled_by_customer",
                    "payout_method_closed",
                    "payout_method_currency_unsupported",
                    "payout_method_does_not_exist",
                    "payout_method_holder_address_incorrect",
                    "payout_method_holder_details_incorrect",
                    "payout_method_holder_name_incorrect",
                    "payout_method_invalid_account_number",
                    "payout_method_restricted",
                    "recalled",
                    "unknown_failure",
                ],
                str,
            ]
            """
            Open Enum. The `returned` status reason.
            """

        failed: Optional[Failed]
        """
        The `failed` status reason.
        """
        processing: Optional[Processing]
        """
        The `processing` status details.
        """
        returned: Optional[Returned]
        """
        The `returned` status reason.
        """
        _inner_class_types = {
            "failed": Failed,
            "processing": Processing,
            "returned": Returned,
        }

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Timestamp describing when an OutboundPayment changed status to `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        failed_at: Optional[str]
        """
        Timestamp describing when an OutboundPayment changed status to `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        posted_at: Optional[str]
        """
        Timestamp describing when an OutboundPayment changed status to `posted`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        returned_at: Optional[str]
        """
        Timestamp describing when an OutboundPayment changed status to `returned`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """

    class To(StripeObject):
        class PayoutMethodOptions(StripeObject):
            class BankAccount(StripeObject):
                class PreferredNetworkOptions(StripeObject):
                    class Ach(StripeObject):
                        submission: Optional[
                            Union[Literal["next_day", "same_day"], str]
                        ]
                        """
                        Open Enum. ACH submission timing.
                        """
                        transaction_purpose: Optional[
                            Union[Literal["payroll"], str]
                        ]
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
                preferred_networks: Optional[
                    List[
                        Union[
                            Literal[
                                "ach", "fedwire", "fps", "rtp", "sepa", "swift"
                            ],
                            str,
                        ]
                    ]
                ]
                """
                The preferred networks to use for this OutboundPayment.
                """
                _inner_class_types = {
                    "preferred_network_options": PreferredNetworkOptions,
                }

            bank_account: Optional[BankAccount]
            """
            Options for bank account payout methods.
            """
            _inner_class_types = {"bank_account": BankAccount}

        credited: Amount
        """
        The monetary amount being credited to the destination.
        """
        payout_method: Optional[str]
        """
        The payout method which the OutboundPayment uses to send payout.
        """
        payout_method_options: Optional[PayoutMethodOptions]
        """
        Payout method options for the OutboundPayment.
        """
        recipient: str
        """
        To which account the OutboundPayment is sent.
        """
        _inner_class_types = {"payout_method_options": PayoutMethodOptions}

    class TrackingDetails(StripeObject):
        class BankAccount(StripeObject):
            trace_id: Optional[str]
            """
            A unique identifier that can be used to track this OutboundPayment with the recipient bank. Banks might call this a “reference number” or something similar.
            """

        class Card(StripeObject):
            retrieval_reference: Optional[str]
            """
            A unique identifier that can be used to track this OutboundPayment with the recipient card.
            """

        bank_account: Optional[BankAccount]
        """
        Bank account tracking details.
        """
        card: Optional[Card]
        """
        Card tracking details.
        """
        status: Union[Literal["pending", "supported", "unsupported"], str]
        """
        The status of the tracking details for this OutboundPayment.
        """
        type: Union[Literal["bank_account", "card"], str]
        """
        The type of tracking details for this OutboundPayment.
        """
        _inner_class_types = {"bank_account": BankAccount, "card": Card}

    amount: Amount
    """
    The amount and currency requested for this OutboundPayment.
    """
    cancelable: bool
    """
    Returns true if the OutboundPayment can be canceled, and false otherwise.
    """
    created: str
    """
    Time at which the OutboundPayment was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the OutboundPayment. Often useful for displaying to users.
    """
    expected_arrival_date: Optional[str]
    """
    The date when funds are expected to arrive in the payout method. This field is not set if the payout method is in a `failed`, `canceled`, or `returned` state.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    from_: From
    """
    The FinancialAccount that funds were pulled from.
    """
    id: str
    """
    Unique identifier for the OutboundPayment.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.money_management.outbound_payment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payout_intent: Optional[str]
    """
    The PayoutIntent ID that triggered this OutboundPayment.
    """
    recipient_notification: RecipientNotification
    """
    Details about the OutboundPayment notification settings for recipient.
    """
    recipient_verification: Optional[str]
    """
    The ID of the RecipientVerification for this OutboundPayment. Required where recipient-name verification is mandated before creating an OutboundPayment.
    """
    statement_descriptor: str
    """
    The description that appears on the receiving end of an OutboundPayment (for example, on a bank statement). Defaults to `STRIPE` if not configured in the account settings.
    """
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    """
    Current status of the OutboundPayment.
    An OutboundPayment is `processing` after creation. It becomes `posted` when funds leave the account,
    `failed` if it cannot be sent, `canceled` if canceled before posting, or `returned` if the funds are returned.
    """
    status_details: Optional[StatusDetails]
    """
    Status details for an OutboundPayment in a `processing`, `failed`, or `returned` state.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when the object transitioned to a particular status.
    """
    to: To
    """
    To which payout method the OutboundPayment was sent.
    """
    tracking_details: Optional[TrackingDetails]
    """
    Information to track this OutboundPayment with the recipient bank.
    """
    _inner_class_types = {
        "from": From,
        "recipient_notification": RecipientNotification,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "to": To,
        "tracking_details": TrackingDetails,
    }
    _field_remappings = {"from_": "from"}
