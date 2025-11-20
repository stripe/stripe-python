# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Transaction(StripeObject):
    """
    Use Transactions to view changes to your FinancialAccount balance over time. Every flow that moves money, such as OutboundPayments or ReceivedCredits, will have one or more Transactions that describes how the flow impacted your balance. Note that while the FinancialAccount balance will always be up to date, be aware that Transactions and TransactionEntries are created shortly after to reflect changes.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.transaction"]] = (
        "v2.money_management.transaction"
    )

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

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

    class StatusTransitions(StripeObject):
        posted_at: Optional[str]
        """
        The time at which the Transaction became posted. Only present if status == posted.
        """
        void_at: Optional[str]
        """
        The time at which the Transaction became void. Only present if status == void.
        """

    amount: Amount
    """
    The amount of the Transaction.
    """
    balance_impact: BalanceImpact
    """
    The delta to the FinancialAccount's balance. The balance_impact for the Transaction is equal to sum of its
    TransactionEntries that have `effective_at`s in the past.
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
    Open Enum. A descriptive category used to classify the Transaction.
    """
    created: str
    """
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    financial_account: str
    """
    Indicates the FinancialAccount affected by this Transaction.
    """
    flow: Flow
    """
    Details about the Flow object that created the Transaction.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.transaction"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["pending", "posted", "void"]
    """
    Closed Enum. Current status of the Transaction.
    A Transaction is `pending` if either `balance_impact.inbound_pending` or `balance_impact.outbound_pending` is non-zero.
    A Transaction is `posted` if only `balance_impact.available` is non-zero.
    A Transaction is `void` if there is no balance impact.
    `posted` and `void` are terminal states, and no additional entries will be added to the Transaction.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for when the Transaction transitioned to a particular status.
    """
    _inner_class_types = {
        "amount": Amount,
        "balance_impact": BalanceImpact,
        "flow": Flow,
        "status_transitions": StatusTransitions,
    }
