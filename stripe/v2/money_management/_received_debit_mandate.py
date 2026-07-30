# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class ReceivedDebitMandate(StripeObject):
    """
    A ReceivedDebitMandate represents an authorization from a third party to debit a financial account on a recurring basis.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.received_debit_mandate"]
    ] = "v2.money_management.received_debit_mandate"

    class BankTransfer(StripeObject):
        account_holder_name: Optional[str]
        """
        The name of the account holder that initiated the debit.
        """
        financial_address: str
        """
        The financial address associated with this mandate.
        """
        network: Literal["bacs"]
        """
        The bank transfer network for this mandate.
        """
        reference: Optional[str]
        """
        The bank transfer reference provided by the bank.
        """

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Union[
                Literal[
                    "canceled_by_beneficiary",
                    "canceled_by_stripe",
                    "user_action",
                ],
                str,
            ]
            """
            The `canceled` status reason.
            """

        canceled: Optional[Canceled]
        """
        If the mandate is canceled, this field provides more details on the cancellation reason.
        """
        _inner_class_types = {"canceled": Canceled}

    class StatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        Timestamp describing when the ReceivedDebitMandate changed status to `active`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """
        canceled_at: Optional[str]
        """
        Timestamp describing when the ReceivedDebitMandate changed status to `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision for example: 2026-06-03T13:22:18.123Z.
        """
        created_at: Optional[str]
        """
        Timestamp describing when the ReceivedDebitMandate was created.
        Represented as a RFC 3339 date & time UTC value in millisecond precision for example: 2026-06-03T13:22:18.123Z.
        """
        expired_at: Optional[str]
        """
        Timestamp describing when the ReceivedDebitMandate changed status to `expired`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2026-06-03T13:22:18.123Z.
        """
        pending_cancellation_at: Optional[str]
        """
        Timestamp describing when the ReceivedDebitMandate changed status to `pending_cancellation`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """

    bank_transfer: Optional[BankTransfer]
    """
    This object stores details about the originating bank transfer that resulted in the ReceivedDebitMandate. Present if `type` field value is `bank_transfer`.
    """
    created: str
    """
    The time at which the ReceivedDebitMandate was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2026-06-03T13:22:18.123Z`.
    """
    currency: str
    """
    The currency of the ReceivedDebitMandate in ISO 4217 format. This is the currency that debits will be collected in.
    """
    financial_account: str
    """
    Financial account ID associated with this mandate.
    """
    id: str
    """
    The unique identifier for the ReceivedDebitMandate.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.received_debit_mandate"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[
        Literal["active", "canceled", "expired", "pending_cancellation"], str
    ]
    """
    The status of the ReceivedDebitMandate.
    """
    status_details: Optional[StatusDetails]
    """
    Detailed information that elaborates on the specific status of the ReceivedDebitMandate.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Timestamps describing when the mandate changed status.
    """
    type: Literal["bank_transfer"]
    """
    The type of the ReceivedDebitMandate.
    """
    _inner_class_types = {
        "bank_transfer": BankTransfer,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
    }
