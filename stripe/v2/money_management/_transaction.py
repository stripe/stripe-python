# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class Transaction(StripeObject):
    """
    A Transaction records how a money movement flow affects your FinancialAccount balance.
    A flow can create one or more Transactions.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.transaction"]] = (
        "v2.money_management.transaction"
    )

    class BalanceImpact(StripeObject):
        available: Amount
        """
        The change to the available balance.
        """
        inbound_pending: Amount
        """
        The change to the `inbound_pending` balance.
        """
        outbound_pending: Amount
        """
        The change to the `outbound_pending` balance.
        """

    class Counterparty(StripeObject):
        name: Optional[str]
        """
        Name of the counterparty.
        """

    class Flow(StripeObject):
        account: Optional[str]
        """
        If applicable, the connected account associated with this Transaction's flow.
        """
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
        When available, the ID of the CurrencyConversion that created this Transaction.
        """
        debit_dispute: Optional[str]
        """
        If applicable, the ID of the DebitDispute that created this Transaction.
        """
        dispute: Optional[str]
        """
        If applicable, the ID of the Dispute that created this Transaction.
        """
        earned_credit: Optional[str]
        """
        If applicable, the ID of the EarnedCredit that created this Transaction.
        """
        fee_batch: Optional[str]
        """
        If applicable, the ID of the FeeBatch that created this Transaction.
        """
        inbound_transfer: Optional[str]
        """
        If applicable, the ID of the InboundTransfer that created this Transaction.
        """
        issuing_authorization: Optional[str]
        """
        If applicable, the ID of the Issuing authorization that created this Transaction.
        """
        issuing_dispute: Optional[str]
        """
        If applicable, the ID of the Issuing dispute that created this Transaction.
        """
        issuing_transaction: Optional[str]
        """
        If applicable, the ID of the Issuing transaction that created this Transaction.
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
        tax_fund: Optional[str]
        """
        If applicable, the ID of the TaxFund that created this Transaction.
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
        treasury_credit_reversal: Optional[str]
        """
        If applicable, the ID of the Treasury CreditReversal that created this Transaction.
        """
        treasury_debit_reversal: Optional[str]
        """
        If applicable, the ID of the Treasury DebitReversal that created this Transaction.
        """
        treasury_inbound_transfer: Optional[str]
        """
        If applicable, the ID of the Treasury InboundTransfer that created this Transaction.
        """
        treasury_issuing_authorization: Optional[str]
        """
        If applicable, the ID of the Treasury IssuingAuthorization that created this Transaction.
        """
        treasury_outbound_payment: Optional[str]
        """
        If applicable, the ID of the Treasury OutboundPayment that created this Transaction.
        """
        treasury_outbound_transfer: Optional[str]
        """
        If applicable, the ID of the Treasury OutboundTransfer that created this Transaction.
        """
        treasury_received_credit: Optional[str]
        """
        If applicable, the ID of the Treasury ReceivedCredit that created this Transaction.
        """
        treasury_received_debit: Optional[str]
        """
        If applicable, the ID of the Treasury ReceivedDebit that created this Transaction.
        """
        type: Union[
            Literal[
                "adjustment",
                "application_fee",
                "application_fee_refund",
                "charge",
                "currency_conversion",
                "debit_dispute",
                "dispute",
                "earned_credit",
                "fee_batch",
                "inbound_transfer",
                "issuing_authorization",
                "issuing_dispute",
                "issuing_transaction",
                "outbound_payment",
                "outbound_transfer",
                "payout",
                "received_credit",
                "received_debit",
                "refund",
                "reserve_hold",
                "reserve_release",
                "tax_fund",
                "topup",
                "transfer",
                "transfer_reversal",
                "treasury_credit_reversal",
                "treasury_debit_reversal",
                "treasury_inbound_transfer",
                "treasury_issuing_authorization",
                "treasury_other",
                "treasury_outbound_payment",
                "treasury_outbound_transfer",
                "treasury_received_credit",
                "treasury_received_debit",
            ],
            str,
        ]
        """
        Open Enum. The type of flow that created the Transaction. When available, the flow's ID is provided in the corresponding field.
        """

    class RegulatoryReceipt(StripeObject):
        status: Literal[
            "available", "not_applicable", "pending", "url_expired"
        ]
        """
        Current availability of the regulatory receipt.
        """
        url: Optional[str]
        """
        Hosted URL for the receipt.
        """
        url_expires_at: Optional[str]
        """
        Time until which `url` is valid.
        """

    class StatusTransitions(StripeObject):
        posted_at: Optional[str]
        """
        The time at which the Transaction became `posted`. Only present when `status` is `posted`.
        """
        void_at: Optional[str]
        """
        The time at which the Transaction became `void`. Only present when `status` is `void`.
        """

    amount: Amount
    """
    The amount of the Transaction.
    """
    balance_impact: BalanceImpact
    """
    The change to the FinancialAccount's balance. This is the sum of the balance impacts of this Transaction's
    TransactionEntries with `effective_at` timestamps in the past.
    """
    category: Union[
        Literal[
            "adjustment",
            "advance",
            "anticipation_repayment",
            "balance_transfer",
            "climate_order_purchase",
            "climate_order_refund",
            "connect_collection_transfer",
            "connect_reserved_funds",
            "contribution",
            "crypto_wallet_export",
            "currency_conversion",
            "debit_dispute",
            "dispute",
            "dispute_reversal",
            "earned_credit",
            "financing_paydown",
            "financing_paydown_reversal",
            "inbound_payment",
            "inbound_payment_failure",
            "inbound_transfer",
            "inbound_transfer_reversal",
            "india_mdr_processing_fee",
            "issuing_authorization",
            "issuing_dispute",
            "issuing_dispute_fraud_liability_debit",
            "issuing_dispute_provisional_credit",
            "issuing_dispute_provisional_credit_reversal",
            "issuing_transaction",
            "minimum_balance_hold",
            "network_cost",
            "obligation",
            "outbound_payment",
            "outbound_payment_reversal",
            "outbound_transfer",
            "outbound_transfer_reversal",
            "partial_capture_reversal",
            "payment_method_passthrough_fee",
            "payment_network_reserved_funds",
            "platform_earning",
            "platform_earning_refund",
            "platform_fee",
            "platform_funded_credit_transaction",
            "received_credit",
            "received_credit_reversal",
            "received_debit",
            "received_debit_reversal",
            "refund",
            "refund_failure",
            "risk_reserved_funds",
            "stripe_balance_payment_debit",
            "stripe_balance_payment_debit_reversal",
            "stripe_fee",
            "stripe_fee_tax",
            "tax_fund",
            "tax_withholding",
            "transfer_reversal",
            "unreconciled_customer_funds",
        ],
        str,
    ]
    """
    Open Enum. A category used to classify the Transaction.
    """
    counterparty: Optional[Counterparty]
    """
    Details about the counterparty to this Transaction.
    """
    created: str
    """
    Time at which the object was created. Represented as an RFC 3339 timestamp in UTC with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
    """
    description: Optional[str]
    """
    A description of the Transaction. When applicable, the description is copied from the flow object when
    the Transaction is created. You can update it using the Update Transaction endpoint.
    """
    financial_account: str
    """
    The ID of the FinancialAccount affected by this Transaction.
    """
    flow: Optional[Flow]
    """
    Details about the flow object that created the Transaction, such as an InboundTransfer or OutboundPayment.
    `flow.type` identifies the kind of object. The corresponding field contains its ID, when available:
    for an InboundTransfer, `flow.inbound_transfer` contains the InboundTransfer's ID. Pass that ID to
    the `flow` parameter on List Transactions.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information
    about the object in a structured format.
    """
    object: Literal["v2.money_management.transaction"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    regulatory_receipt: RegulatoryReceipt
    """
    Hosted transaction receipt that is provided when money movement is considered regulated under Stripe's money transmission licenses. If not applicable, `regulatory_receipt.status` will be `not_applicable` and no URL will be provided unless you opt in by calling `/refresh_regulatory_receipt`.
    """
    status: Literal["pending", "posted", "void"]
    """
    Closed Enum. The current status of the Transaction.
    A Transaction is `pending` if either `balance_impact.inbound_pending` or `balance_impact.outbound_pending` is non-zero.
    A Transaction is `posted` if only `balance_impact.available` is non-zero.
    A Transaction is `void` if there is no balance impact.
    `posted` and `void` are terminal states, and no additional TransactionEntries will be added to the Transaction.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for when the Transaction transitioned to each status.
    """
    treasury_transaction: Optional[str]
    """
    The v1 Treasury transaction associated with this transaction.
    """
    _inner_class_types = {
        "balance_impact": BalanceImpact,
        "counterparty": Counterparty,
        "flow": Flow,
        "regulatory_receipt": RegulatoryReceipt,
        "status_transitions": StatusTransitions,
    }
