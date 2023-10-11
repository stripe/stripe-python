# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.product import Product


class Price(
    CreateableAPIResource["Price"],
    ListableAPIResource["Price"],
    SearchableAPIResource["Price"],
    UpdateableAPIResource["Price"],
):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    OBJECT_NAME = "price"

    class CreateParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        billing_scheme: NotRequired[Optional[Literal["per_unit", "tiered"]]]
        currency: str
        currency_options: NotRequired[
            Optional[Dict[str, "Price.CreateParamsCurrencyOptions"]]
        ]
        custom_unit_amount: NotRequired[
            Optional["Price.CreateParamsCustomUnitAmount"]
        ]
        expand: NotRequired[Optional[List[str]]]
        lookup_key: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        nickname: NotRequired[Optional[str]]
        product: NotRequired[Optional[str]]
        product_data: NotRequired[Optional["Price.CreateParamsProductData"]]
        recurring: NotRequired[Optional["Price.CreateParamsRecurring"]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tiers: NotRequired[Optional[List["Price.CreateParamsTier"]]]
        tiers_mode: NotRequired[Optional[Literal["graduated", "volume"]]]
        transfer_lookup_key: NotRequired[Optional[bool]]
        transform_quantity: NotRequired[
            Optional["Price.CreateParamsTransformQuantity"]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsTransformQuantity(TypedDict):
        divide_by: int
        round: Literal["down", "up"]

    class CreateParamsTier(TypedDict):
        flat_amount: NotRequired[Optional[int]]
        flat_amount_decimal: NotRequired[Optional[float]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]
        up_to: Union[Literal["inf"], int]

    class CreateParamsRecurring(TypedDict):
        aggregate_usage: NotRequired[
            Optional[Literal["last_during_period", "last_ever", "max", "sum"]]
        ]
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        trial_period_days: NotRequired[Optional[int]]
        usage_type: NotRequired[Optional[Literal["licensed", "metered"]]]

    class CreateParamsProductData(TypedDict):
        active: NotRequired[Optional[bool]]
        id: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        name: str
        statement_descriptor: NotRequired[Optional[str]]
        tax_code: NotRequired[Optional[str]]
        unit_label: NotRequired[Optional[str]]

    class CreateParamsCustomUnitAmount(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]
        preset: NotRequired[Optional[int]]

    class CreateParamsCurrencyOptions(TypedDict):
        custom_unit_amount: NotRequired[
            Optional["Price.CreateParamsCurrencyOptionsCustomUnitAmount"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tiers: NotRequired[
            Optional[List["Price.CreateParamsCurrencyOptionsTier"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsCurrencyOptionsTier(TypedDict):
        flat_amount: NotRequired[Optional[int]]
        flat_amount_decimal: NotRequired[Optional[float]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]
        up_to: Union[Literal["inf"], int]

    class CreateParamsCurrencyOptionsCustomUnitAmount(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]
        preset: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        created: NotRequired[Optional[Union["Price.ListParamsCreated", int]]]
        currency: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        lookup_keys: NotRequired[Optional[List[str]]]
        product: NotRequired[Optional[str]]
        recurring: NotRequired[Optional["Price.ListParamsRecurring"]]
        starting_after: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["one_time", "recurring"]]]

    class ListParamsRecurring(TypedDict):
        interval: NotRequired[
            Optional[Literal["day", "month", "week", "year"]]
        ]
        usage_type: NotRequired[Optional[Literal["licensed", "metered"]]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        currency_options: NotRequired[
            Optional[
                Union[
                    Literal[""], Dict[str, "Price.ModifyParamsCurrencyOptions"]
                ]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        lookup_key: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        nickname: NotRequired[Optional[str]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        transfer_lookup_key: NotRequired[Optional[bool]]

    class ModifyParamsCurrencyOptions(TypedDict):
        custom_unit_amount: NotRequired[
            Optional["Price.ModifyParamsCurrencyOptionsCustomUnitAmount"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tiers: NotRequired[
            Optional[List["Price.ModifyParamsCurrencyOptionsTier"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsCurrencyOptionsTier(TypedDict):
        flat_amount: NotRequired[Optional[int]]
        flat_amount_decimal: NotRequired[Optional[float]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]
        up_to: Union[Literal["inf"], int]

    class ModifyParamsCurrencyOptionsCustomUnitAmount(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]
        preset: NotRequired[Optional[int]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
        query: str

    active: bool
    billing_scheme: Literal["per_unit", "tiered"]
    created: int
    currency: str
    currency_options: Optional[Dict[str, StripeObject]]
    custom_unit_amount: Optional[StripeObject]
    id: str
    livemode: bool
    lookup_key: Optional[str]
    metadata: Dict[str, str]
    nickname: Optional[str]
    object: Literal["price"]
    product: ExpandableField["Product"]
    recurring: Optional[StripeObject]
    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]]
    tiers: Optional[List[StripeObject]]
    tiers_mode: Optional[Literal["graduated", "volume"]]
    transform_quantity: Optional[StripeObject]
    type: Literal["one_time", "recurring"]
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[float]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Price.CreateParams"]
    ) -> "Price":
        return cast(
            "Price",
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
        **params: Unpack["Price.ListParams"]
    ) -> ListObject["Price"]:
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
    def modify(cls, id, **params: Unpack["Price.ModifyParams"]) -> "Price":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Price",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Price.RetrieveParams"]
    ) -> "Price":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Price.SearchParams"]
    ) -> SearchResultObject["Price"]:
        return cls._search(search_url="/v1/prices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
