# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class DebitReversal(
    CreateableAPIResource["DebitReversal"],
    ListableAPIResource["DebitReversal"],
):
    """
    You can reverse some [ReceivedDebits](https://stripe.com/docs/api#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.
    """

    OBJECT_NAME = "treasury.debit_reversal"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            received_debit: str

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            limit: NotRequired["int|None"]
            received_debit: NotRequired["str|None"]
            resolution: NotRequired["Literal['lost', 'won']|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['canceled', 'completed', 'processing']|None"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount: int
    created: int
    currency: str
    financial_account: Optional[str]
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    linked_flows: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    network: Literal["ach", "card"]
    object: Literal["treasury.debit_reversal"]
    received_debit: str
    status: Literal["failed", "processing", "succeeded"]
    status_transitions: StripeObject
    transaction: Optional[ExpandableField["Transaction"]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["DebitReversal.CreateParams"]
    ) -> "DebitReversal":
        return cast(
            "DebitReversal",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["DebitReversal.ListParams"]
    ) -> ListObject["DebitReversal"]:
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
        cls, id: str, **params: Unpack["DebitReversal.RetrieveParams"]
    ) -> "DebitReversal":
        instance = cls(id, **params)
        instance.refresh()
        return instance
