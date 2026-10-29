# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class TransactionEntry(StripeObject):
    """
    TransactionEntries model funds moving between availability states for a given Transaction.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.transaction_entry"]] = (
        "v2.money_management.transaction_entry"
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

    class TransactionDetails(StripeObject):
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
        Open Enum. The category of this TransactionEntry's parent Transaction.
        """
        financial_account: str
        """
        The ID of the FinancialAccount affected by this Transaction.
        """
        flow: Optional[Flow]
        """
        Details about the flow object that created the Transaction this entry belongs to, such as an
        InboundTransfer or OutboundPayment. `transaction_details.flow.type` identifies the kind of object.
        The corresponding field contains its ID, when available: for an InboundTransfer,
        `transaction_details.flow.inbound_transfer` contains the InboundTransfer's ID. To list entries for
        the parent Transaction, pass the TransactionEntry's `transaction` ID to the `transaction` parameter
        on List Transaction Entries.
        """
        _inner_class_types = {"flow": Flow}

    balance_impact: BalanceImpact
    """
    The change to the FinancialAccount's balance that takes effect at this TransactionEntry's `effective_at` timestamp.
    """
    created: str
    """
    Time at which the object was created. Represented as an RFC 3339 timestamp in UTC with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
    """
    effective_at: str
    """
    Time at which the TransactionEntry affects the FinancialAccount balance. This can be in the past or future.
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
    The ID of the Transaction that this TransactionEntry belongs to.
    """
    transaction_details: TransactionDetails
    """
    Details copied from the Transaction that this TransactionEntry belongs to.
    """
    _inner_class_types = {
        "balance_impact": BalanceImpact,
        "transaction_details": TransactionDetails,
    }
