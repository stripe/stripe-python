# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax_code import TaxCode


class ShippingRate(
    CreateableAPIResource["ShippingRate"],
    ListableAPIResource["ShippingRate"],
    UpdateableAPIResource["ShippingRate"],
):
    """
    Shipping rates describe the price of shipping presented to your customers and
    applied to a purchase. For more information, see [Charge for shipping](https://stripe.com/docs/payments/during-payment/charge-shipping).
    """

    OBJECT_NAME = "shipping_rate"

    class CreateParams(RequestOptions):
        delivery_estimate: NotRequired[
            Optional["ShippingRate.CreateDeliveryEstimateParams"]
        ]
        display_name: str
        expand: NotRequired[Optional[List[str]]]
        fixed_amount: NotRequired[
            Optional["ShippingRate.CreateFixedAmountParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["fixed_amount"]]]

    class CreateFixedAmountParams(TypedDict):
        amount: int
        currency: str
        currency_options: NotRequired[
            Optional[
                Dict[
                    str, "ShippingRate.CreateFixedAmountCurrencyOptionsParams"
                ]
            ]
        ]

    class CreateFixedAmountCurrencyOptionsParams(TypedDict):
        amount: int
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class CreateDeliveryEstimateParams(TypedDict):
        maximum: NotRequired[
            Optional["ShippingRate.CreateDeliveryEstimateMaximumParams"]
        ]
        minimum: NotRequired[
            Optional["ShippingRate.CreateDeliveryEstimateMinimumParams"]
        ]

    class CreateDeliveryEstimateMinimumParams(TypedDict):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        value: int

    class CreateDeliveryEstimateMaximumParams(TypedDict):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        value: int

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        created: NotRequired[
            Optional[Union["ShippingRate.ListCreatedParams", int]]
        ]
        currency: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        fixed_amount: NotRequired[
            Optional["ShippingRate.ModifyFixedAmountParams"]
        ]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class ModifyFixedAmountParams(TypedDict):
        currency_options: NotRequired[
            Optional[
                Dict[
                    str, "ShippingRate.ModifyFixedAmountCurrencyOptionsParams"
                ]
            ]
        ]

    class ModifyFixedAmountCurrencyOptionsParams(TypedDict):
        amount: NotRequired[Optional[int]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    active: bool
    created: int
    delivery_estimate: Optional[StripeObject]
    display_name: Optional[str]
    fixed_amount: Optional[StripeObject]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["shipping_rate"]
    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]]
    tax_code: Optional[ExpandableField["TaxCode"]]
    type: Literal["fixed_amount"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ShippingRate.CreateParams"]
    ) -> "ShippingRate":
        return cast(
            "ShippingRate",
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
        **params: Unpack["ShippingRate.ListParams"]
    ) -> ListObject["ShippingRate"]:
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
    def modify(
        cls, id, **params: Unpack["ShippingRate.ModifyParams"]
    ) -> "ShippingRate":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "ShippingRate",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ShippingRate.RetrieveParams"]
    ) -> "ShippingRate":
        instance = cls(id, **params)
        instance.refresh()
        return instance
