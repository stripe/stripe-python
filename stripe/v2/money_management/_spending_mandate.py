# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class SpendingMandate(StripeObject):
    """
    A SpendingMandate authorizes a counterparty to pull money from a Financial Account.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.spending_mandate"]] = (
        "v2.money_management.spending_mandate"
    )

    class BankTransfer(StripeObject):
        account_holder_name: Optional[str]
        """
        The name of the account holder that initiated the debit.
        """
        financial_address: str
        """
        The financial address associated with this mandate.
        """
        network: Union[Literal["bacs"], str]
        """
        The bank transfer network for this mandate.
        """
        reference: Optional[str]
        """
        The bank transfer reference provided by the bank. Only present when `network` is `bacs`.
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
        Timestamp describing when the SpendingMandate changed status to `active`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """
        canceled_at: Optional[str]
        """
        Timestamp describing when the SpendingMandate changed status to `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """
        created_at: Optional[str]
        """
        Timestamp describing when the SpendingMandate was created.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """
        expired_at: Optional[str]
        """
        Timestamp describing when the SpendingMandate changed status to `expired`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """
        pending_cancellation_at: Optional[str]
        """
        Timestamp describing when the SpendingMandate changed status to `pending_cancellation`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision.
        """

    bank_transfer: Optional[BankTransfer]
    """
    Bank transfer details. Present if `type` is `bank_transfer`.
    """
    created: str
    """
    The time at which the SpendingMandate was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision.
    """
    currency: str
    """
    The currency in ISO 4217 format that debits will be collected in.
    """
    financial_account: str
    """
    Financial account ID associated with this mandate.
    """
    id: str
    """
    The unique identifier for the SpendingMandate.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.spending_mandate"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[
        Literal["active", "canceled", "expired", "pending_cancellation"], str
    ]
    """
    The status of the SpendingMandate.
    """
    status_details: Optional[StatusDetails]
    """
    Detailed information about the status of the SpendingMandate.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Timestamps describing when the mandate changed status.
    """
    type: Union[Literal["bank_transfer"], str]
    """
    The type of the SpendingMandate.
    """
    _inner_class_types = {
        "bank_transfer": BankTransfer,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
    }
