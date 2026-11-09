# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class PayoutIntent(StripeObject):
    """
    PayoutIntent represents an intent to send funds from a Financial Account to a payout method.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.payout_intent"]] = (
        "v2.money_management.payout_intent"
    )

    class EstimatedFee(StripeObject):
        class NetworkFeeDetails(StripeObject):
            class NetworkOptions(StripeObject):
                class Ach(StripeObject):
                    submission: Optional[
                        Union[Literal["next_day", "same_day"], str]
                    ]
                    """
                    Open Enum. ACH submission timing.
                    """

                ach: Optional[Ach]
                """
                ACH-specific network fee options.
                """
                _inner_class_types = {"ach": Ach}

            network: Union[
                Literal[
                    "ach", "fedwire", "fps", "local", "rtp", "sepa", "swift"
                ],
                str,
            ]
            """
            The network associated with the fee.
            """
            network_options: NetworkOptions
            """
            Per-network options that affect the fee.
            """
            _inner_class_types = {"network_options": NetworkOptions}

        class TaxAmount(StripeObject):
            currency: str
            """
            Currency code.
            """
            value_decimal: str
            """
            Tax amount value represented as a decimal string in major units.
            """

        amount: Amount
        """
        The fee amount.
        """
        network_fee_details: Optional[NetworkFeeDetails]
        """
        Details about the network and options associated with this fee. Present when `type` is `network_fee`.
        """
        tax_amount: Optional[TaxAmount]
        """
        Tax charged for this fee, if applicable. Value expressed as a decimal string in major units.
        """
        type: Union[
            Literal[
                "cross_border_fee",
                "foreign_exchange_fee",
                "instant_card_payout_fee",
                "network_fee",
                "next_day_payout_fee",
                "real_time_payout_fee",
                "standard_payout_fee",
                "wire_payout_fee",
            ],
            str,
        ]
        """
        Open Enum. The type of fee.
        """
        _inner_class_types = {
            "network_fee_details": NetworkFeeDetails,
            "tax_amount": TaxAmount,
        }

    class From(StripeObject):
        currency: str
        """
        The currency of the financial account.
        """
        debited: Optional[Amount]
        """
        Estimated amount to be debited from the financial account.
        """
        financial_account: str
        """
        The FinancialAccount that funds are pulled from.
        """

    class FxQuote(StripeObject):
        class Rates(StripeObject):
            exchange_rate: str
            """
            The exchange rate from the source currency to `to_currency`, represented as a decimal string
            (for example, `1.1520`) to preserve the full precision of the rate.
            """

        lock_duration: Union[Literal["five_minutes", "none"], str]
        """
        Open Enum. Duration of the FX rate lock.
        """
        lock_expires_at: Optional[str]
        """
        Timestamp when the rate lock expires. Null when rate locking is not supported.
        """
        lock_status: Union[Literal["active", "expired", "none"], str]
        """
        Open Enum. Lock status of the FX rate.
        """
        rates: UntypedStripeObject[Rates]
        """
        Maps each source currency to its exchange rate into `to_currency`.
        """
        to_currency: str
        """
        The destination currency.
        """
        _inner_class_types = {"rates": Rates}
        _inner_class_dicts = ["rates"]

    class LatestPayout(StripeObject):
        outbound_payment: Optional[str]
        """
        The ID of the OutboundPayment, if applicable.
        """
        outbound_transfer: Optional[str]
        """
        The ID of the OutboundTransfer, if applicable.
        """
        type: Union[Literal["outbound_payment", "outbound_transfer"], str]
        """
        The type of payout.
        """

    class NextAction(StripeObject):
        class Confirm(StripeObject):
            fields_to_review: Optional[
                List[
                    Union[
                        Literal[
                            "estimated_fees",
                            "fx_quote",
                            "recipient_verification",
                        ],
                        str,
                    ]
                ]
            ]
            """
            The PayoutIntent fields that must be reviewed before confirmation.
            """
            reason: Union[
                Literal["automatically_required", "manually_requested"], str
            ]
            """
            Open Enum. The reason the PayoutIntent requires confirmation.
            """

        class HandleFailure(StripeObject):
            failure_reason: Union[
                Literal[
                    "account_not_configured_as_recipient",
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
                    "payout_method_invalid",
                    "payout_method_invalid_account_number",
                    "payout_method_restricted",
                    "payout_method_unsupported",
                    "payout_method_usage_frequency_limit_exceeded",
                    "recalled",
                    "recipient_capability_not_active",
                    "review_rejected",
                    "unknown_failure",
                ],
                str,
            ]
            """
            Open Enum. The reason for the failure.
            """

        confirm: Optional[Confirm]
        """
        Details about a confirmation required. Populated when `type` is `confirm`.
        """
        handle_failure: Optional[HandleFailure]
        """
        Details about a failure that requires user action. Populated when `type` is `handle_failure`.
        """
        type: Union[Literal["confirm", "handle_failure"], str]
        """
        Open Enum. The type of next action required.
        """
        _inner_class_types = {
            "confirm": Confirm,
            "handle_failure": HandleFailure,
        }

    class RecipientNotification(StripeObject):
        setting: Literal["configured", "none"]
        """
        Closed Enum. Configuration option to enable or disable notifications to recipients.
        Do not send notifications when `setting` is `none`. Use the account setting when `setting` is `configured` or omitted.
        """

    class RecipientVerification(StripeObject):
        class MatchResultDetails(StripeObject):
            matched_business_type: Optional[Literal["business", "personal"]]
            """
            The business type returned by the recipient-verification provider.
            """
            matched_name: Optional[str]
            """
            The account name returned by the recipient-verification provider.
            """
            message: str
            """
            A message describing the match result.
            """
            provided_business_type: Optional[Literal["business", "personal"]]
            """
            The business type provided for recipient verification.
            """
            provided_name: str
            """
            The name associated with the provided recipient.
            """

        match_result: Literal[
            "close_match", "match", "no_match", "unavailable"
        ]
        """
        Closed Enum. The recipient-verification provider's match result.
        """
        match_result_details: MatchResultDetails
        """
        Details associated with the match result.
        """
        _inner_class_types = {"match_result_details": MatchResultDetails}

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

        credited: Optional[Amount]
        """
        Estimated amount to be credited to the recipient in the destination currency.
        """
        currency: Optional[str]
        """
        The currency to send to the recipient.
        """
        payout_method: Optional[str]
        """
        The payout method ID for the PayoutIntent. Optional when the PayoutIntent creates an OutboundPayment and the recipient has a default payout method. Required when the PayoutIntent creates an OutboundTransfer.
        """
        payout_method_options: Optional[PayoutMethodOptions]
        """
        Payout method options for the PayoutIntent.
        """
        recipient: Optional[str]
        """
        The recipient ID for the PayoutIntent.
        """
        _inner_class_types = {"payout_method_options": PayoutMethodOptions}

    amount: Amount
    """
    The monetary amount to be sent.
    """
    confirmation_method: Union[Literal["automatic", "manual"], str]
    """
    Controls whether the PayoutIntent requires explicit confirmation before transitioning to `pending`.
    Even when `automatic`, regulatory requirements may require confirmation. See [Send money with Global Payouts](https://docs.stripe.com/global-payouts/send-money) for details.
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
    estimated_fees: Optional[List[EstimatedFee]]
    """
    Estimated fees and taxes.
    """
    from_: From
    """
    The FinancialAccount that funds are pulled from.
    """
    fx_quote: Optional[FxQuote]
    """
    FX rate information for fee transparency.
    """
    id: str
    """
    Unique identifier for the PayoutIntent.
    """
    latest_payout: Optional[LatestPayout]
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
    Next action required for a PayoutIntent in the `requires_action` state. Populated when `status` is `requires_action`.
    """
    object: Literal["v2.money_management.payout_intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    recipient_notification: Optional[RecipientNotification]
    """
    Recipient notification settings for the PayoutIntent. Only applicable when the PayoutIntent creates an OutboundPayment.
    """
    recipient_verification: Optional[RecipientVerification]
    """
    Recipient verification details for this PayoutIntent.
    """
    schedule_options: Optional[ScheduleOptions]
    """
    Scheduling options for the payout. If omitted, the payout is scheduled for immediate execution.
    """
    statement_descriptor: Optional[str]
    """
    The description that appears on the receiving end for the payout (for example, on a bank statement).
    """
    status: Union[
        Literal[
            "canceled", "pending", "posted", "processing", "requires_action"
        ],
        str,
    ]
    """
    Current status of the PayoutIntent.
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
        "estimated_fees": EstimatedFee,
        "from": From,
        "fx_quote": FxQuote,
        "latest_payout": LatestPayout,
        "next_action": NextAction,
        "recipient_notification": RecipientNotification,
        "recipient_verification": RecipientVerification,
        "schedule_options": ScheduleOptions,
        "status_transitions": StatusTransitions,
        "to": To,
    }
    _field_remappings = {"from_": "from"}
