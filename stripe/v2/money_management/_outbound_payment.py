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

    class DeliveryOptions(StripeObject):
        class PaperCheck(StripeObject):
            attachment: Optional[str]
            """
            The ID of a file to include as an attachment with the paper check.
            """
            memo: str
            """
            Memo printed on the memo field of the check.
            """
            shipping_speed: Union[Literal["priority", "standard"], str]
            """
            Open Enum. Shipping speed of the paper check.
            """
            signature: str
            """
            Signature for the paper check.
            """

        bank_account: Optional[
            Union[Literal["automatic", "local", "wire"], str]
        ]
        """
        Open Enum. Method for bank account.
        """
        paper_check: Optional[PaperCheck]
        """
        Delivery options for paper check.
        """
        speed: Optional[
            Union[Literal["instant", "next_business_day", "standard"], str]
        ]
        """
        Open Enum. Speed of the payout.
        """
        _inner_class_types = {"paper_check": PaperCheck}

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
        Do not send notifications when setting is NONE. Default to account setting when setting is CONFIGURED or not set.
        """

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Union[
                Literal[
                    "fx_rate_drift_exceeded_after_review",
                    "paper_check_attachment_too_large",
                    "paper_check_expired",
                    "paper_check_undeliverable",
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
            reason: Literal["under_review"]
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
        payout_method: str
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

    class TraceId(StripeObject):
        status: Union[Literal["pending", "supported", "unsupported"], str]
        """
        Possible values are `pending`, `supported`, and `unsupported`. Initially set to `pending`, it changes to
        `supported` when the recipient bank provides a trace ID, or `unsupported` if the recipient bank doesn't support it.
        Note that this status may not align with the OutboundPayment or OutboundTransfer status and can remain `pending`
        even after the payment or transfer is posted.
        """
        value: Optional[str]
        """
        The trace ID value if `trace_id.status` is `supported`, otherwise empty.
        """

    class TrackingDetails(StripeObject):
        class PaperCheck(StripeObject):
            class MailingAddress(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[str]
                """
                Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                """
                line1: Optional[str]
                """
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """

            carrier: Union[Literal["fedex", "usps"], str]
            """
            Open Enum. Carrier of the paper check.
            """
            check_number: str
            """
            Check number.
            """
            current_postal_code: str
            """
            Postal code of the latest tracking update.
            """
            mailing_address: MailingAddress
            """
            Mailing address of the paper check.
            """
            tracking_number: str
            """
            Tracking number for the check.
            """
            tracking_status: Union[
                Literal["delivered", "in_transit", "mailed"], str
            ]
            """
            Open Enum. Tracking status of the paper check.
            """
            updated_at: str
            """
            When the tracking details were last updated.
            """
            _inner_class_types = {"mailing_address": MailingAddress}

        paper_check: Optional[PaperCheck]
        """
        Paper check tracking details.
        """
        _inner_class_types = {"paper_check": PaperCheck}

    amount: Amount
    """
    The "presentment amount" for the OutboundPayment.
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
    delivery_options: Optional[DeliveryOptions]
    """
    Delivery options to be used to send the OutboundPayment.
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
    outbound_payment_quote: Optional[str]
    """
    The quote for this OutboundPayment. Only required for countries with regulatory mandates to display fee estimates before OutboundPayment creation.
    """
    purpose: Optional[Literal["payroll"]]
    """
    The purpose of the OutboundPayment.
    """
    receipt_url: Optional[str]
    """
    A link to the Stripe-hosted receipt for this OutboundPayment. The receipt link remains active for 60 days from the OutboundPayment creation date. After this period, the link will expire and the receipt url value will be null.
    """
    recipient_notification: RecipientNotification
    """
    Details about the OutboundPayment notification settings for recipient.
    """
    recipient_verification: Optional[str]
    """
    The recipient verification id for this OutboundPayment. Only required for countries with regulatory mandates to verify recipient names before OutboundPayment creation.
    """
    statement_descriptor: str
    """
    The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer). It will default to `STRIPE` if not set on the account settings.
    """
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    """
    Closed Enum. Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`.
    An OutboundPayment is `processing` if it has been created and is processing.
    The status changes to `posted` once the OutboundPayment has been "confirmed" and funds have left the account, or to `failed` or `canceled`.
    If an OutboundPayment fails to arrive at its payout method, its status will change to `returned`.
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
    trace_id: TraceId
    """
    A unique identifier that can be used to track this OutboundPayment with recipient bank. Banks might call this a "reference number" or something similar.
    """
    tracking_details: Optional[TrackingDetails]
    """
    Information to track this OutboundPayment with the recipient bank.
    """
    _inner_class_types = {
        "delivery_options": DeliveryOptions,
        "from": From,
        "recipient_notification": RecipientNotification,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "to": To,
        "trace_id": TraceId,
        "tracking_details": TrackingDetails,
    }
    _field_remappings = {"from_": "from"}
