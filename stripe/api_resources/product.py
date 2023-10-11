# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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

    class CreateParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        default_price_data: NotRequired[
            Optional["Product.CreateParamsDefaultPriceData"]
        ]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[Optional[List["Product.CreateParamsFeature"]]]
        id: NotRequired[Optional[str]]
        images: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        name: str
        package_dimensions: NotRequired[
            Optional["Product.CreateParamsPackageDimensions"]
        ]
        shippable: NotRequired[Optional[bool]]
        statement_descriptor: NotRequired[Optional[str]]
        tax_code: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["good", "service"]]]
        unit_label: NotRequired[Optional[str]]
        url: NotRequired[Optional[str]]

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
            Optional[
                Dict[
                    str, "Product.CreateParamsDefaultPriceDataCurrencyOptions"
                ]
            ]
        ]
        recurring: NotRequired[
            Optional["Product.CreateParamsDefaultPriceDataRecurring"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsDefaultPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateParamsDefaultPriceDataCurrencyOptions(TypedDict):
        custom_unit_amount: NotRequired[
            Optional[
                "Product.CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount"
            ]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tiers: NotRequired[
            Optional[
                List["Product.CreateParamsDefaultPriceDataCurrencyOptionsTier"]
            ]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsDefaultPriceDataCurrencyOptionsTier(TypedDict):
        flat_amount: NotRequired[Optional[int]]
        flat_amount_decimal: NotRequired[Optional[float]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]
        up_to: Union[Literal["inf"], int]

    class CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount(
        TypedDict,
    ):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]
        preset: NotRequired[Optional[int]]

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        created: NotRequired[Optional[Union["Product.ListParamsCreated", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        ids: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        shippable: NotRequired[Optional[bool]]
        starting_after: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["good", "service"]]]
        url: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        default_price: NotRequired[Optional[str]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[
            Optional[Union[Literal[""], List["Product.ModifyParamsFeature"]]]
        ]
        images: NotRequired[Optional[Union[Literal[""], List[str]]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]
        package_dimensions: NotRequired[
            Optional[
                Union[Literal[""], "Product.ModifyParamsPackageDimensions"]
            ]
        ]
        shippable: NotRequired[Optional[bool]]
        statement_descriptor: NotRequired[Optional[str]]
        tax_code: NotRequired[Optional[Union[Literal[""], str]]]
        unit_label: NotRequired[Optional[Union[Literal[""], str]]]
        url: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsPackageDimensions(TypedDict):
        height: float
        length: float
        weight: float
        width: float

    class ModifyParamsFeature(TypedDict):
        name: str

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
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
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
