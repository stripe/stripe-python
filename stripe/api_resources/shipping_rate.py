# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            delivery_estimate: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimate|None"
            ]
            display_name: str
            expand: NotRequired["List[str]|None"]
            fixed_amount: NotRequired[
                "ShippingRate.CreateParamsFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class CreateParamsFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, ShippingRate.CreateParamsFixedAmountCurrencyOptions]|None"
            ]

        class CreateParamsFixedAmountCurrencyOptions(TypedDict):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class CreateParamsDeliveryEstimate(TypedDict):
            maximum: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimateMinimum|None"
            ]

        class CreateParamsDeliveryEstimateMinimum(TypedDict):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsDeliveryEstimateMaximum(TypedDict):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            created: NotRequired["ShippingRate.ListParamsCreated|int|None"]
            currency: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            fixed_amount: NotRequired[
                "ShippingRate.ModifyParamsFixedAmount|None"
            ]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class ModifyParamsFixedAmount(TypedDict):
            currency_options: NotRequired[
                "Dict[str, ShippingRate.ModifyParamsFixedAmountCurrencyOptions]|None"
            ]

        class ModifyParamsFixedAmountCurrencyOptions(TypedDict):
            amount: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
