# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.issuing.authorization import Authorization
    from stripe.api_resources.treasury.credit_reversal import CreditReversal
    from stripe.api_resources.treasury.debit_reversal import DebitReversal
    from stripe.api_resources.treasury.inbound_transfer import InboundTransfer
    from stripe.api_resources.treasury.outbound_payment import OutboundPayment
    from stripe.api_resources.treasury.outbound_transfer import (
        OutboundTransfer,
    )
    from stripe.api_resources.treasury.received_credit import ReceivedCredit
    from stripe.api_resources.treasury.received_debit import ReceivedDebit
    from stripe.api_resources.treasury.transaction_entry import (
        TransactionEntry,
    )


class Transaction(ListableAPIResource["Transaction"]):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME = "treasury.transaction"

    class BalanceImpact(StripeObject):
        cash: int
        inbound_pending: int
        outbound_pending: int

    class FlowDetails(StripeObject):
        credit_reversal: Optional["CreditReversal"]
        debit_reversal: Optional["DebitReversal"]
        inbound_transfer: Optional["InboundTransfer"]
        issuing_authorization: Optional["Authorization"]
        outbound_payment: Optional["OutboundPayment"]
        outbound_transfer: Optional["OutboundTransfer"]
        received_credit: Optional["ReceivedCredit"]
        received_debit: Optional["ReceivedDebit"]
        type: Literal[
            "credit_reversal",
            "debit_reversal",
            "inbound_transfer",
            "issuing_authorization",
            "other",
            "outbound_payment",
            "outbound_transfer",
            "received_credit",
            "received_debit",
        ]

    class StatusTransitions(StripeObject):
        posted_at: Optional[int]
        void_at: Optional[int]

    amount: int
    balance_impact: BalanceImpact
    created: int
    currency: str
    description: str
    entries: Optional[ListObject["TransactionEntry"]]
    financial_account: str
    flow: Optional[str]
    flow_details: Optional[FlowDetails]
    flow_type: Literal[
        "credit_reversal",
        "debit_reversal",
        "inbound_transfer",
        "issuing_authorization",
        "other",
        "outbound_payment",
        "outbound_transfer",
        "received_credit",
        "received_debit",
    ]
    id: str
    livemode: bool
    object: Literal["treasury.transaction"]
    status: Literal["open", "posted", "void"]
    status_transitions: StatusTransitions

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Transaction"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Transaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "balance_impact": BalanceImpact,
        "flow_details": FlowDetails,
        "status_transitions": StatusTransitions,
    }
