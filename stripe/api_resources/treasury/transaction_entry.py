# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class TransactionEntry(ListableAPIResource["TransactionEntry"]):
    """
    TransactionEntries represent individual units of money movements within a single [Transaction](https://stripe.com/docs/api#transactions).
    """

    OBJECT_NAME = "treasury.transaction_entry"
    balance_impact: StripeObject
    created: int
    currency: str
    effective_at: int
    financial_account: str
    flow: Optional[str]
    flow_details: Optional[StripeObject]
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
    object: Literal["treasury.transaction_entry"]
    transaction: ExpandableField["Transaction"]
    type: Literal[
        "credit_reversal",
        "credit_reversal_posting",
        "debit_reversal",
        "inbound_transfer",
        "inbound_transfer_return",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "other",
        "outbound_payment",
        "outbound_payment_cancellation",
        "outbound_payment_failure",
        "outbound_payment_posting",
        "outbound_payment_return",
        "outbound_transfer",
        "outbound_transfer_cancellation",
        "outbound_transfer_failure",
        "outbound_transfer_posting",
        "outbound_transfer_return",
        "received_credit",
        "received_debit",
    ]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["TransactionEntry"]:
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
    ) -> "TransactionEntry":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/treasury/transaction_entries"
