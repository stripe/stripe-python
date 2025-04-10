# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ReceivedDebit(StripeObject):
    """
    ReceivedDebit resource
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.received_debit"]] = (
        "v2.money_management.received_debit"
    )

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Literal[
                "financial_address_inactive",
                "insufficient_funds",
                "stripe_rejected",
            ]
            """
            Open Enum. The reason for the failure of the ReceivedDebit.
            """

        failed: Failed
        """
        Information that elaborates on the `failed` status of a ReceivedDebit.
        It is only present when the ReceivedDebit status is `failed`.
        """
        _inner_class_types = {"failed": Failed}

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """
        failed_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """
        succeeded_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `succeeded`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """

    class BankTransfer(StripeObject):
        class UsBankAccount(StripeObject):
            bank_name: Optional[str]
            """
            The name of the bank the debit originated from.
            """
            network: Literal["ach"]
            """
            Open Enum. The bank network the debit was originated on.
            """
            routing_number: Optional[str]
            """
            The routing number of the bank that originated the debit.
            """

        financial_address: str
        """
        The Financial Address that was debited.
        """
        payment_method_type: Literal["us_bank_account"]
        """
        Open Enum. The type of the payment method used to originate the debit.
        """
        statement_descriptor: Optional[str]
        """
        The statement descriptor set by the originator of the debit.
        """
        us_bank_account: UsBankAccount
        """
        The payment method used to originate the debit.
        """
        _inner_class_types = {"us_bank_account": UsBankAccount}

    class CardSpend(StripeObject):
        class Authorization(StripeObject):
            amount: Amount
            """
            Amount associated with this issuing authorization.
            """
            issuing_authorization_v1: str
            """
            The reference to the v1 issuing authorization ID.
            """

        class CardTransaction(StripeObject):
            amount: Amount
            """
            Amount associated with this issuing transaction.
            """
            issuing_transaction_v1: str
            """
            The reference to the v1 issuing transaction ID.
            """

        authorization: Optional[Authorization]
        """
        The Issuing Authorization for this card_spend. Contains the reference id and the amount.
        """
        card_transactions: List[CardTransaction]
        """
        The list of card spend transactions. These contain the transaction reference ID and the amount.
        """
        card_v1_id: str
        """
        The reference to the card object that resulted in the debit.
        """
        _inner_class_types = {
            "authorization": Authorization,
            "card_transactions": CardTransaction,
        }

    amount: Amount
    """
    Amount and currency of the ReceivedDebit.
    """
    created: str
    """
    The time at which the ReceivedDebit was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
    """
    description: Optional[str]
    """
    Freeform string sent by the originator of the ReceivedDebit.
    """
    financial_account: str
    """
    Financial Account on which funds for ReceivedDebit were debited.
    """
    id: str
    """
    Unique identifier for the ReceivedDebit.
    """
    object: Literal["v2.money_management.received_debit"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A link to the Stripe-hosted receipt for this ReceivedDebit.
    """
    status: Literal["canceled", "failed", "pending", "returned", "succeeded"]
    """
    Open Enum. The status of the ReceivedDebit.
    """
    status_details: Optional[StatusDetails]
    """
    Detailed information about the status of the ReceivedDebit.
    """
    status_transitions: Optional[StatusTransitions]
    """
    The time at which the ReceivedDebit transitioned to a particular status.
    """
    type: Literal["bank_transfer", "card_spend", "external_debit"]
    """
    Open Enum. The type of the ReceivedDebit.
    """
    bank_transfer: Optional[BankTransfer]
    """
    This object stores details about the originating banking transaction that resulted in the ReceivedDebit. Present if `type` field value is `bank_transfer`.
    """
    card_spend: Optional[CardSpend]
    """
    This object stores details about the issuing transactions that resulted in the ReceivedDebit. Present if `type` field value is `card_spend`.
    """
    _inner_class_types = {
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "bank_transfer": BankTransfer,
        "card_spend": CardSpend,
    }
