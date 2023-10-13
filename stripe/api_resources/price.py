# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            billing_scheme: NotRequired["Literal['per_unit', 'tiered']|None"]
            currency: str
            currency_options: NotRequired[
                "Dict[str, Price.CreateParamsCurrencyOptions]|None"
            ]
            custom_unit_amount: NotRequired[
                "Price.CreateParamsCustomUnitAmount|None"
            ]
            expand: NotRequired["List[str]|None"]
            lookup_key: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            nickname: NotRequired["str|None"]
            product: NotRequired["str|None"]
            product_data: NotRequired["Price.CreateParamsProductData|None"]
            recurring: NotRequired["Price.CreateParamsRecurring|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tiers: NotRequired["List[Price.CreateParamsTier]|None"]
            tiers_mode: NotRequired["Literal['graduated', 'volume']|None"]
            transfer_lookup_key: NotRequired["bool|None"]
            transform_quantity: NotRequired[
                "Price.CreateParamsTransformQuantity|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsTransformQuantity(TypedDict):
            divide_by: int
            round: Literal["down", "up"]

        class CreateParamsTier(TypedDict):
            flat_amount: NotRequired["int|None"]
            flat_amount_decimal: NotRequired["float|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]
            up_to: Union[Literal["inf"], int]

        class CreateParamsRecurring(TypedDict):
            aggregate_usage: NotRequired[
                "Literal['last_during_period', 'last_ever', 'max', 'sum']|None"
            ]
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]
            trial_period_days: NotRequired["int|None"]
            usage_type: NotRequired["Literal['licensed', 'metered']|None"]

        class CreateParamsProductData(TypedDict):
            active: NotRequired["bool|None"]
            id: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str
            statement_descriptor: NotRequired["str|None"]
            tax_code: NotRequired["str|None"]
            unit_label: NotRequired["str|None"]

        class CreateParamsCustomUnitAmount(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]
            preset: NotRequired["int|None"]

        class CreateParamsCurrencyOptions(TypedDict):
            custom_unit_amount: NotRequired[
                "Price.CreateParamsCurrencyOptionsCustomUnitAmount|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tiers: NotRequired[
                "List[Price.CreateParamsCurrencyOptionsTier]|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsCurrencyOptionsTier(TypedDict):
            flat_amount: NotRequired["int|None"]
            flat_amount_decimal: NotRequired["float|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]
            up_to: Union[Literal["inf"], int]

        class CreateParamsCurrencyOptionsCustomUnitAmount(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]
            preset: NotRequired["int|None"]

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            created: NotRequired["Price.ListParamsCreated|int|None"]
            currency: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            lookup_keys: NotRequired["List[str]|None"]
            product: NotRequired["str|None"]
            recurring: NotRequired["Price.ListParamsRecurring|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired["Literal['one_time', 'recurring']|None"]

        class ListParamsRecurring(TypedDict):
            interval: NotRequired[
                "Literal['day', 'month', 'week', 'year']|None"
            ]
            usage_type: NotRequired["Literal['licensed', 'metered']|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            currency_options: NotRequired[
                "Literal['']|Dict[str, Price.ModifyParamsCurrencyOptions]|None"
            ]
            expand: NotRequired["List[str]|None"]
            lookup_key: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            nickname: NotRequired["str|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            transfer_lookup_key: NotRequired["bool|None"]

        class ModifyParamsCurrencyOptions(TypedDict):
            custom_unit_amount: NotRequired[
                "Price.ModifyParamsCurrencyOptionsCustomUnitAmount|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tiers: NotRequired[
                "List[Price.ModifyParamsCurrencyOptionsTier]|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsCurrencyOptionsTier(TypedDict):
            flat_amount: NotRequired["int|None"]
            flat_amount_decimal: NotRequired["float|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]
            up_to: Union[Literal["inf"], int]

        class ModifyParamsCurrencyOptionsCustomUnitAmount(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]
            preset: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
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
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Price.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()
