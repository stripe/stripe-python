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
        adjustment: Optional[str]
        """
        If applicable, the ID of the Adjustment that created this Transaction.
        """
        currency_conversion: Optional[str]
        """
        When available, the ID of the CurrencyConversion that created this Transaction.
        """
        fee_batch: Optional[str]
        """
        If applicable, the ID of the FeeBatch that created this Transaction.
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
        type: Union[
            Literal[
                "adjustment",
                "currency_conversion",
                "fee_batch",
                "inbound_transfer",
                "outbound_payment",
                "outbound_transfer",
                "received_credit",
                "received_debit",
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
            "currency_conversion",
            "inbound_transfer",
            "inbound_transfer_reversal",
            "outbound_payment",
            "outbound_payment_reversal",
            "outbound_transfer",
            "outbound_transfer_reversal",
            "received_credit",
            "received_credit_reversal",
            "received_debit",
            "received_debit_reversal",
            "stripe_fee",
            "stripe_fee_tax",
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
    _inner_class_types = {
        "balance_impact": BalanceImpact,
        "counterparty": Counterparty,
        "flow": Flow,
        "regulatory_receipt": RegulatoryReceipt,
        "status_transitions": StatusTransitions,
    }
