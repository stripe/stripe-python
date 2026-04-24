# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class InboundTransfer(StripeObject):
    """
    An InboundTransfer object, representing a money movement from a
    user owned PaymentMethod to a FinancialAccount belonging to the same user.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.inbound_transfer"]] = (
        "v2.money_management.inbound_transfer"
    )

    class From(StripeObject):
        class PaymentMethod(StripeObject):
            type: str
            """
            The type of object this destination represents. For a us bank account, we expect us_bank_account.
            """
            us_bank_account: Optional[str]
            """
            The destination US bank account identifier. eg "usba_***".
            """

        debited: Amount
        """
        The amount in specified currency that was debited from the Payment Method.
        """
        payment_method: PaymentMethod
        """
        The Payment Method object used to create the InboundTransfer.
        """
        _inner_class_types = {"payment_method": PaymentMethod}

    class To(StripeObject):
        credited: Amount
        """
        The amount by which the FinancialAccount balance is credited.
        """
        financial_account: str
        """
        The FinancialAccount that funds will land in.
        """

    class TransferHistory(StripeObject):
        class BankDebitFailed(StripeObject):
            failure_reason: Literal[
                "bank_account_closed",
                "bank_account_not_found",
                "bank_debit_could_not_be_processed",
                "bank_debit_not_authorized",
                "insufficient_funds",
            ]
            """
            Open Enum. The return reason for the failed InboundTransfer.
            """

        class BankDebitProcessing(StripeObject):
            pass

        class BankDebitQueued(StripeObject):
            pass

        class BankDebitReturned(StripeObject):
            return_reason: Literal[
                "bank_account_closed",
                "bank_account_not_found",
                "bank_debit_could_not_be_processed",
                "bank_debit_not_authorized",
                "insufficient_funds",
            ]
            """
            Open Enum. The return reason for the returned InboundTransfer.
            """

        class BankDebitSucceeded(StripeObject):
            pass

        bank_debit_failed: Optional[BankDebitFailed]
        """
        The history entry for a failed InboundTransfer.
        """
        bank_debit_processing: Optional[BankDebitProcessing]
        """
        The history entry for a processing InboundTransfer.
        """
        bank_debit_queued: Optional[BankDebitQueued]
        """
        The history entry for a queued InboundTransfer.
        """
        bank_debit_returned: Optional[BankDebitReturned]
        """
        The history entry for a returned InboundTransfer.
        """
        bank_debit_succeeded: Optional[BankDebitSucceeded]
        """
        The history entry for a succeeded InboundTransfer.
        """
        created: str
        """
        Creation time of the HistoryEntry in RFC 3339 format and UTC.
        """
        effective_at: str
        """
        Effective at time of the HistoryEntry in RFC 3339 format and UTC.
        """
        id: str
        """
        A unique ID for the HistoryEntry.
        """
        level: Literal["canonical", "debug"]
        """
        Open Enum. The Level of the HistoryEntry.
        """
        type: Literal[
            "bank_debit_failed",
            "bank_debit_processing",
            "bank_debit_queued",
            "bank_debit_returned",
            "bank_debit_succeeded",
        ]
        """
        Open Enum. The type of the HistoryEntry.
        """
        _inner_class_types = {
            "bank_debit_failed": BankDebitFailed,
            "bank_debit_processing": BankDebitProcessing,
            "bank_debit_queued": BankDebitQueued,
            "bank_debit_returned": BankDebitReturned,
            "bank_debit_succeeded": BankDebitSucceeded,
        }

    amount: Amount
    """
    The amount in specified currency that will land in the FinancialAccount balance.
    """
    created: str
    """
    Creation time of the InboundTransfer. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    description: str
    """
    A freeform text field provided by user, containing metadata.
    """
    from_: From
    """
    A nested object containing information about the origin of the InboundTransfer.
    """
    id: str
    """
    Unique identifier for the InboundTransfer.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.inbound_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    to: To
    """
    A nested object containing information about the destination of the InboundTransfer.
    """
    transfer_history: List[TransferHistory]
    """
    A list of history objects, representing changes in the state of the InboundTransfer.
    """
    _inner_class_types = {
        "from": From,
        "to": To,
        "transfer_history": TransferHistory,
    }
    _field_remappings = {"from_": "from"}
