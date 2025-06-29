# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class TransactionEntry(StripeObject):
    """
    TransactionEntries represent individual money movements across different states within a Transaction.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.transaction_entry"]] = (
        "v2.money_management.transaction_entry"
    )

    class BalanceImpact(StripeObject):
        available: Amount
        """
        Impact to the available balance.
        """
        inbound_pending: Amount
        """
        Impact to the inbound_pending balance.
        """
        outbound_pending: Amount
        """
        Impact to the outbound_pending balance.
        """

    class TransactionDetails(StripeObject):
        class Flow(StripeObject):
            adjustment: Optional[str]
            """
            If applicable, the ID of the Adjustment that created this Transaction.
            """
            fee_transaction: Optional[str]
            """
            If applicable, the ID of the FeeTransaction that created this Transaction.
            """
            inbound_transfer: Optional[str]
            """
            If applicable, the ID of the InboundTransfer that created this Transaction.
            """
            outbound_payment: Optional[str]
            """
            If applicable, the ID of the OutboundPayment that created this Transaction.
            """
            outbound_transfer: Optional[str]
            """
            If applicable, the ID of the OutboundTransfer that created this Transaction.
            """
            received_credit: Optional[str]
            """
            If applicable, the ID of the ReceivedCredit that created this Transaction.
            """
            received_debit: Optional[str]
            """
            If applicable, the ID of the ReceivedDebit that created this Transaction.
            """
            type: Literal[
                "adjustment",
                "fee_transaction",
                "inbound_transfer",
                "outbound_payment",
                "outbound_transfer",
                "received_credit",
                "received_debit",
            ]
            """
            Open Enum. Type of the flow that created the Transaction. The field matching this value will contain the ID of the flow.
            """

        category: Literal[
            "adjustment",
            "inbound_transfer",
            "outbound_payment",
            "outbound_transfer",
            "received_credit",
            "received_debit",
            "return",
            "stripe_fee",
        ]
        """
        Closed Enum for now, and will be turned into an Open Enum soon. A descriptive category used to classify the Transaction.
        """
        financial_account: str
        """
        Indicates the FinancialAccount affected by this Transaction.
        """
        flow: Flow
        """
        Details about the Flow object that created the Transaction.
        """
        _inner_class_types = {"flow": Flow}

    balance_impact: BalanceImpact
    """
    The delta to the FinancialAccount's balance.
    """
    created: str
    """
    Time at which the object was created.
    """
    effective_at: str
    """
    Time at which the entry impacted (or will impact if it's in the future) the FinancialAccount balance.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.transaction_entry"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    transaction: str
    """
    The Transaction that this TransactionEntry belongs to.
    """
    transaction_details: TransactionDetails
    """
    Details copied from the transaction that this TransactionEntry belongs to.
    """
    _inner_class_types = {
        "balance_impact": BalanceImpact,
        "transaction_details": TransactionDetails,
    }
