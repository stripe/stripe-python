# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
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

    OBJECT_NAME: ClassVar[Literal["tax.transaction"]] = "tax.transaction"
    if TYPE_CHECKING:

        class CreateFromCalculationParams(RequestOptions):
            calculation: str
            """
            Tax Calculation ID to be used as input when creating the transaction.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            reference: str
            """
            A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals.
            """

        class CreateReversalParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            flat_amount: NotRequired["int|None"]
            """
            A flat amount to reverse across the entire transaction, in negative integer cents. This value represents the total amount to refund from the transaction, including taxes.
            """
            line_items: NotRequired[
                "List[Transaction.CreateReversalParamsLineItem]|None"
            ]
            """
            The line item amounts to reverse.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            mode: Literal["full", "partial"]
            """
            If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
            """
            original_transaction: str
            """
            The ID of the Transaction to partially or fully reverse.
            """
            reference: str
            """
            A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports).
            """
            shipping_cost: NotRequired[
                "Transaction.CreateReversalParamsShippingCost|None"
            ]
            """
            The shipping cost to reverse.
            """

        class CreateReversalParamsShippingCost(TypedDict):
            amount: int
            """
            The amount to reverse, in negative integer cents.
            """
            amount_tax: int
            """
            The amount of tax to reverse, in negative integer cents.
            """

        class CreateReversalParamsLineItem(TypedDict):
            amount: int
            """
            The amount to reverse, in negative integer cents.
            """
            amount_tax: int
            """
            The amount of tax to reverse, in negative integer cents.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            original_line_item: str
            """
            The `id` of the line item to reverse in the original transaction.
            """
            quantity: NotRequired["int|None"]
            """
            The quantity reversed. Appears in [tax exports](https://stripe.com/docs/tax/reports), but does not affect the amount of tax reversed.
            """
            reference: str
            """
            A custom identifier for this line item in the reversal transaction, such as 'L1-refund'.
            """

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[str]
    """
    The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource.
    """
    customer_details: StripeObject
    id: str
    """
    Unique identifier for the transaction.
    """
    line_items: Optional[ListObject["TransactionLineItem"]]
    """
    The tax collected or refunded, by line item.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["tax.transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reference: str
    """
    A custom unique identifier, such as 'myOrder_123'.
    """
    reversal: Optional[StripeObject]
    """
    If `type=reversal`, contains information about what was reversed.
    """
    shipping_cost: Optional[StripeObject]
    """
    The shipping cost details for the transaction.
    """
    tax_date: int
    """
    Timestamp of date at which the tax rules and rates in effect applies for the calculation.
    """
    type: Literal["reversal", "transaction"]
    """
    If `reversal`, this transaction reverses an earlier transaction.
    """

    @classmethod
    def create_from_calculation(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CreateFromCalculationParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            cls._static_request(
                "post",
                "/v1/tax/transactions/create_from_calculation",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_reversal(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CreateReversalParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            cls._static_request(
                "post",
                "/v1/tax/transactions/create_reversal",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ) -> ListObject["TransactionLineItem"]:
        return cast(
            ListObject["TransactionLineItem"],
            cls._static_request(
                "get",
                "/v1/tax/transactions/{transaction}/line_items".format(
                    transaction=util.sanitize_id(transaction)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_line_items(
        cls,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ) -> ListObject["TransactionLineItem"]:
        ...

    @overload
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ) -> ListObject["TransactionLineItem"]:
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ListLineItemsParams"]
    ) -> ListObject["TransactionLineItem"]:
        return cast(
            ListObject["TransactionLineItem"],
            self._request(
                "get",
                "/v1/tax/transactions/{transaction}/line_items".format(
                    transaction=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance
