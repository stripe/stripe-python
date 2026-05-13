# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class DebitDispute(StripeObject):
    """
    A DebitDispute represents a dispute raised against a received debit.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.debit_dispute"]] = (
        "v2.money_management.debit_dispute"
    )

    class BankTransfer(StripeObject):
        network: Literal["ach"]
        """
        The bank network the dispute was originated on.
        """
        reason: Optional[Literal["incorrect_amount_or_date", "unauthorized"]]
        """
        The reason for the dispute.
        """
        statement_descriptor: Optional[str]
        """
        The statement descriptor set by the originator of the debit.
        """

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Literal["unknown"]
            """
            The reason for the failure of the DebitDispute.
            """

        failed: Failed
        """
        Information that elaborates on the `failed` status of a DebitDispute.
        It is only present when the DebitDispute status is `failed`.
        """
        _inner_class_types = {"failed": Failed}

    class StatusTransitions(StripeObject):
        failed_at: Optional[str]
        """
        The time when the DebitDispute was marked as `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2026-04-23T13:22:18.123Z`.
        """
        succeeded_at: Optional[str]
        """
        The time when the DebitDispute was marked as `succeeded`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2026-04-23T13:22:18.123Z`.
        """

    amount: Amount
    """
    The amount of the DebitDispute.
    """
    bank_transfer: Optional[BankTransfer]
    """
    Details about the bank transfer dispute. Present if `type` field value is `bank_transfer`.
    """
    created: str
    """
    Time at which the DebitDispute was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2026-03-23T13:22:18.123Z`.
    """
    financial_account: str
    """
    The Financial Account associated with the DebitDispute.
    """
    id: str
    """
    The ID of a DebitDispute.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.debit_dispute"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    received_debit: str
    """
    The ID of the ReceivedDebit that was disputed.
    """
    status: Literal["failed", "submitted", "succeeded"]
    """
    The status of the DebitDispute.
    """
    status_details: Optional[StatusDetails]
    """
    Detailed information about the status of the DebitDispute.
    """
    status_transitions: Optional[StatusTransitions]
    """
    The time at which the DebitDispute transitioned to a particular status.
    """
    type: Literal["bank_transfer"]
    """
    The type of the DebitDispute.
    """
    _inner_class_types = {
        "bank_transfer": BankTransfer,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
    }
