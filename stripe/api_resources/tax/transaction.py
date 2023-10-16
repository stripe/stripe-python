# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.tax.transaction_line_item import (
        TransactionLineItem,
    )


class Transaction(APIResource["Transaction"]):
    """
    A Tax Transaction records the tax collected from or refunded to your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom#tax-transaction)
    """

    OBJECT_NAME = "tax.transaction"
    if TYPE_CHECKING:

        class CreateFromCalculationParams(RequestOptions):
            calculation: str
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            reference: str

        class CreateReversalParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            flat_amount: NotRequired["int|None"]
            line_items: NotRequired[
                "List[Transaction.CreateReversalParamsLineItem]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            mode: Literal["full", "partial"]
            original_transaction: str
            reference: str
            shipping_cost: NotRequired[
                "Transaction.CreateReversalParamsShippingCost|None"
            ]

        class CreateReversalParamsShippingCost(TypedDict):
            amount: int
            amount_tax: int

        class CreateReversalParamsLineItem(TypedDict):
            amount: int
            amount_tax: int
            metadata: NotRequired["Dict[str, str]|None"]
            original_line_item: str
            quantity: NotRequired["int|None"]
            reference: str

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    created: int
    currency: str
    customer: Optional[str]
    customer_details: StripeObject
    id: str
    line_items: Optional[ListObject["TransactionLineItem"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax.transaction"]
    reference: str
    reversal: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    tax_date: int
    type: Literal["reversal", "transaction"]

    @classmethod
    def create_from_calculation(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CreateFromCalculationParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_from_calculation",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_reversal(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CreateReversalParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_reversal",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(transaction)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance
