# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
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
    from stripe.api_resources.price import Price
    from stripe.api_resources.tax_code import TaxCode


class Product(
    CreateableAPIResource["Product"],
    DeletableAPIResource["Product"],
    ListableAPIResource["Product"],
    SearchableAPIResource["Product"],
    UpdateableAPIResource["Product"],
):
    """
    Products describe the specific goods or services you offer to your customers.
    For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
    They can be used in conjunction with [Prices](https://stripe.com/docs/api#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription),
    [share a Payment Link](https://stripe.com/docs/payment-links),
    [accept payments with Checkout](https://stripe.com/docs/payments/accept-a-payment#create-product-prices-upfront),
    and more about [Products and Prices](https://stripe.com/docs/products-prices/overview)
    """

    OBJECT_NAME = "product"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            default_price_data: NotRequired[
                "Product.CreateParamsDefaultPriceData|None"
            ]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            features: NotRequired["List[Product.CreateParamsFeature]|None"]
            id: NotRequired["str|None"]
            images: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str
            package_dimensions: NotRequired[
                "Product.CreateParamsPackageDimensions|None"
            ]
            shippable: NotRequired["bool|None"]
            statement_descriptor: NotRequired["str|None"]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['good', 'service']|None"]
            unit_label: NotRequired["str|None"]
            url: NotRequired["str|None"]

        class CreateParamsPackageDimensions(TypedDict):
            height: float
            length: float
            weight: float
            width: float

        class CreateParamsFeature(TypedDict):
            name: str

        class CreateParamsDefaultPriceData(TypedDict):
            currency: str
            currency_options: NotRequired[
                "Dict[str, Product.CreateParamsDefaultPriceDataCurrencyOptions]|None"
            ]
            recurring: NotRequired[
                "Product.CreateParamsDefaultPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsDefaultPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsDefaultPriceDataCurrencyOptions(TypedDict):
            custom_unit_amount: NotRequired[
                "Product.CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tiers: NotRequired[
                "List[Product.CreateParamsDefaultPriceDataCurrencyOptionsTier]|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsDefaultPriceDataCurrencyOptionsTier(TypedDict):
            flat_amount: NotRequired["int|None"]
            flat_amount_decimal: NotRequired["float|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]
            up_to: Union[Literal["inf"], int]

        class CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount(
            TypedDict,
        ):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]
            preset: NotRequired["int|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            created: NotRequired["Product.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            ids: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            shippable: NotRequired["bool|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired["Literal['good', 'service']|None"]
            url: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            default_price: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            expand: NotRequired["List[str]|None"]
            features: NotRequired[
                "Literal['']|List[Product.ModifyParamsFeature]|None"
            ]
            images: NotRequired["Literal['']|List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: NotRequired["str|None"]
            package_dimensions: NotRequired[
                "Literal['']|Product.ModifyParamsPackageDimensions|None"
            ]
            shippable: NotRequired["bool|None"]
            statement_descriptor: NotRequired["str|None"]
            tax_code: NotRequired["Literal['']|str|None"]
            unit_label: NotRequired["Literal['']|str|None"]
            url: NotRequired["Literal['']|str|None"]

        class ModifyParamsPackageDimensions(TypedDict):
            height: float
            length: float
            weight: float
            width: float

        class ModifyParamsFeature(TypedDict):
            name: str

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
            query: str

    active: bool
    created: int
    default_price: Optional[ExpandableField["Price"]]
    description: Optional[str]
    features: List[StripeObject]
    id: str
    images: List[str]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["product"]
    package_dimensions: Optional[StripeObject]
    shippable: Optional[bool]
    statement_descriptor: Optional[str]
    tax_code: Optional[ExpandableField["TaxCode"]]
    type: Literal["good", "service"]
    unit_label: Optional[str]
    updated: int
    url: Optional[str]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Product.CreateParams"]
    ) -> "Product":
        return cast(
            "Product",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Product",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Product.DeleteParams"]) -> "Product":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Product.ListParams"]
    ) -> ListObject["Product"]:
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
    def modify(cls, id, **params: Unpack["Product.ModifyParams"]) -> "Product":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Product",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Product.RetrieveParams"]
    ) -> "Product":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ) -> SearchResultObject["Product"]:
        return cls._search(search_url="/v1/products/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()
