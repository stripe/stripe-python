# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class OutboundTransfer(StripeObject):
    """
    OutboundTransfer represents a single money movement from one FinancialAccount you own to a payout method you also own.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.outbound_transfer"]] = (
        "v2.money_management.outbound_transfer"
    )

    class DeliveryOptions(StripeObject):
        bank_account: Optional[Literal["automatic", "local", "wire"]]
        """
        Open Enum. Method for bank account.
        """

    class From(StripeObject):
        debited: Amount
        """
        The monetary amount debited from the sender, only set on responses.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Literal[
                "payout_method_declined",
                "payout_method_does_not_exist",
                "payout_method_expired",
                "payout_method_unsupported",
                "payout_method_usage_frequency_limit_exceeded",
                "unknown_failure",
            ]
            """
            Open Enum. The `failed` status reason.
            """

        class Returned(StripeObject):
            reason: Literal[
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
            ]
            """
            Open Enum. The `returned` status reason.
            """

        failed: Optional[Failed]
        """
        The `failed` status reason.
        """
        returned: Optional[Returned]
        """
        The `returned` status reason.
        """
        _inner_class_types = {"failed": Failed, "returned": Returned}

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Timestamp describing when an OutboundTransfer changed status to `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        failed_at: Optional[str]
        """
        Timestamp describing when an OutboundTransfer changed status to `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        posted_at: Optional[str]
        """
        Timestamp describing when an OutboundTransfer changed status to `posted`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        returned_at: Optional[str]
        """
        Timestamp describing when an OutboundTransfer changed status to `returned`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """

    class To(StripeObject):
        credited: Amount
        """
        The monetary amount being credited to the destination.
        """
        payout_method: str
        """
        The payout method which the OutboundTransfer uses to send payout.
        """

    class TraceId(StripeObject):
        status: Literal["pending", "supported", "unsupported"]
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

    amount: Amount
    """
    The "presentment amount" for the OutboundTransfer.
    """
    cancelable: bool
    """
    Returns true if the OutboundTransfer can be canceled, and false otherwise.
    """
    created: str
    """
    Time at which the OutboundTransfer was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    delivery_options: Optional[DeliveryOptions]
    """
    Delivery options to be used to send the OutboundTransfer.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the OutboundTransfer. Often useful for displaying to users.
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
    Unique identifier for the OutboundTransfer.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.money_management.outbound_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A link to the Stripe-hosted receipt for this OutboundTransfer. The receipt link remains active for 60 days from the OutboundTransfer creation date. After this period, the link will expire and the receipt url value will be null.
    """
    statement_descriptor: str
    """
    The description that appears on the receiving end for an OutboundTransfer (for example, bank statement for external bank transfer). It will default to `STRIPE` if not set on the account settings.
    """
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    """
    Closed Enum. Current status of the OutboundTransfer: `processing`, `failed`, `posted`, `returned`, `canceled`.
    An OutboundTransfer is `processing` if it has been created and is processing.
    The status changes to `posted` once the OutboundTransfer has been "confirmed" and funds have left the account, or to `failed` or `canceled`.
    If an OutboundTransfer fails to arrive at its payout method, its status will change to `returned`.
    """
    status_details: Optional[StatusDetails]
    """
    Status details for an OutboundTransfer in a `failed` or `returned` state.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when the object transitioned to a particular status.
    """
    to: To
    """
    To which payout method the OutboundTransfer was sent.
    """
    trace_id: TraceId
    """
    A unique identifier that can be used to track this OutboundTransfer with recipient bank. Banks might call this a “reference number” or something similar.
    """
    _inner_class_types = {
        "delivery_options": DeliveryOptions,
        "from": From,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "to": To,
        "trace_id": TraceId,
    }
    _field_remappings = {"from_": "from"}
