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
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: int
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class InboundPending(StripeObject):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: int
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class OutboundPending(StripeObject):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: int
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
            application_fee: Optional[str]
            """
            If applicable, the ID of the Application Fee that created this Transaction.
            """
            application_fee_refund: Optional[str]
            """
            If applicable, the ID of the Application Fee Refund that created this Transaction.
            """
            charge: Optional[str]
            """
            If applicable, the ID of the Charge that created this Transaction.
            """
            currency_conversion: Optional[str]
            """
            In the future, this will be the ID of the currency conversion that created this Transaction. For now, this field is always null.
            """
            dispute: Optional[str]
            """
            If applicable, the ID of the Dispute that created this Transaction.
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
            payout: Optional[str]
            """
            If applicable, the ID of the Payout that created this Transaction.
            """
            received_credit: Optional[str]
            """
            If applicable, the ID of the ReceivedCredit that created this Transaction.
            """
            received_debit: Optional[str]
            """
            If applicable, the ID of the ReceivedDebit that created this Transaction.
            """
            refund: Optional[str]
            """
            If applicable, the ID of the Refund that created this Transaction.
            """
            reserve_hold: Optional[str]
            """
            If applicable, the ID of the Reserve Hold that created this Transaction.
            """
            reserve_release: Optional[str]
            """
            If applicable, the ID of the Reserve Release that created this Transaction.
            """
            topup: Optional[str]
            """
            If applicable, the ID of the Topup that created this Transaction.
            """
            transfer: Optional[str]
            """
            If applicable, the ID of the Transfer that created this Transaction.
            """
            transfer_reversal: Optional[str]
            """
            If applicable, the ID of the Transfer Reversal that created this Transaction.
            """
            type: Literal[
                "adjustment",
                "application_fee",
                "application_fee_refund",
                "charge",
                "currency_conversion",
                "dispute",
                "fee_transaction",
                "inbound_transfer",
                "outbound_payment",
                "outbound_transfer",
                "payout",
                "received_credit",
                "received_debit",
                "refund",
                "reserve_hold",
                "reserve_release",
                "topup",
                "transfer",
                "transfer_reversal",
            ]
            """
            Open Enum. Type of the flow that created the Transaction. The field matching this value will contain the ID of the flow.
            """

        category: Literal[
            "adjustment",
            "advance",
            "anticipation_repayment",
            "balance_transfer",
            "charge",
            "charge_failure",
            "climate_order_purchase",
            "climate_order_refund",
            "connect_collection_transfer",
            "connect_reserved_funds",
            "contribution",
            "currency_conversion",
            "dispute_reversal",
            "financing_paydown",
            "financing_paydown_reversal",
            "inbound_transfer",
            "inbound_transfer_reversal",
            "issuing_dispute",
            "issuing_dispute_fraud_liability_debit",
            "issuing_dispute_provisional_credit",
            "issuing_dispute_provisional_credit_reversal",
            "minimum_balance_hold",
            "network_cost",
            "obligation",
            "outbound_payment",
            "outbound_payment_reversal",
            "outbound_transfer",
            "outbound_transfer_reversal",
            "partial_capture_reversal",
            "payment_network_reserved_funds",
            "platform_earning",
            "platform_earning_refund",
            "platform_fee",
            "received_credit",
            "received_credit_reversal",
            "received_debit",
            "received_debit_reversal",
            "refund_failure",
            "return",
            "risk_reserved_funds",
            "stripe_balance_payment_debit",
            "stripe_balance_payment_debit_reversal",
            "stripe_fee",
            "stripe_fee_tax",
            "transfer_reversal",
            "unreconciled_customer_funds",
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
