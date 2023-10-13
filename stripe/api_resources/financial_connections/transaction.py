# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


class Transaction(ListableAPIResource["Transaction"]):
    """
    A Transaction represents a real transaction that affects a Financial Connections Account balance.
    """

    OBJECT_NAME = "financial_connections.transaction"

    class StatusTransitions(StripeObject):
        posted_at: Optional[int]
        void_at: Optional[int]

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            account: str
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            transacted_at: NotRequired[
                "Transaction.ListParamsTransactedAt|int|None"
            ]
            transaction_refresh: NotRequired[
                "Transaction.ListParamsTransactionRefresh|None"
            ]

        class ListParamsTransactionRefresh(TypedDict):
            after: str

        class ListParamsTransactedAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

    account: str
    amount: int
    currency: str
    description: str
    id: str
    livemode: bool
    object: Literal["financial_connections.transaction"]
    status: Literal["pending", "posted", "void"]
    status_transitions: StatusTransitions
    transacted_at: int
    transaction_refresh: str
    updated: int

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

    _inner_class_types = {"status_transitions": StatusTransitions}
