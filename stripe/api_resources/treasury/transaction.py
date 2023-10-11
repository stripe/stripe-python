# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction_entry import (
        TransactionEntry,
    )


class Transaction(ListableAPIResource["Transaction"]):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME = "treasury.transaction"

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["Transaction.ListCreatedParams", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        financial_account: str
        limit: NotRequired[Optional[int]]
        order_by: NotRequired[Optional[Literal["created", "posted_at"]]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[Optional[Literal["open", "posted", "void"]]]
        status_transitions: NotRequired[
            Optional["Transaction.ListStatusTransitionsParams"]
        ]

    class ListStatusTransitionsParams(TypedDict):
        posted_at: NotRequired[
            Optional[
                Union["Transaction.ListStatusTransitionsPostedAtParams", int]
            ]
        ]

    class ListStatusTransitionsPostedAtParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    amount: int
    balance_impact: StripeObject
    created: int
    currency: str
    description: str
    entries: Optional[ListObject["TransactionEntry"]]
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
    object: Literal["treasury.transaction"]
    status: Literal["open", "posted", "void"]
    status_transitions: StripeObject

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ListParams"]
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
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance
