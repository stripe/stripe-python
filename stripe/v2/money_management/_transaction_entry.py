# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
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
        class Available(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class InboundPending(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class OutboundPending(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        available: Available
        """
        Impact to the available balance.
        """
        inbound_pending: InboundPending
        """
        Impact to the inbound_pending balance.
        """
        outbound_pending: OutboundPending
        """
        Impact to the outbound_pending balance.
        """
        _inner_class_types = {
            "available": Available,
            "inbound_pending": InboundPending,
            "outbound_pending": OutboundPending,
        }

    class TransactionDetails(StripeObject):
        class Flow(StripeObject):
            adjustment: Optional[str]
            """
            If applicable, the ID of the Adjustment that created this Transaction.
            """
            currency_conversion: Optional[str]
            """
            In the future, this will be the ID of the currency conversion that created this Transaction. For now, this field is always null.
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
                "currency_conversion",
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
            "currency_conversion",
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
