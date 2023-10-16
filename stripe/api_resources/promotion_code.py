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
    from stripe.api_resources.coupon import Coupon
    from stripe.api_resources.customer import Customer


class PromotionCode(
    CreateableAPIResource["PromotionCode"],
    ListableAPIResource["PromotionCode"],
    UpdateableAPIResource["PromotionCode"],
):
    """
    A Promotion Code represents a customer-redeemable code for a [coupon](https://stripe.com/docs/api#coupons). It can be used to
    create multiple codes for a single coupon.
    """

    OBJECT_NAME = "promotion_code"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            code: NotRequired["str|None"]
            coupon: str
            customer: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]
            max_redemptions: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            restrictions: NotRequired[
                "PromotionCode.CreateParamsRestrictions|None"
            ]

        class CreateParamsRestrictions(TypedDict):
            currency_options: NotRequired[
                "Dict[str, PromotionCode.CreateParamsRestrictionsCurrencyOptions]|None"
            ]
            first_time_transaction: NotRequired["bool|None"]
            minimum_amount: NotRequired["int|None"]
            minimum_amount_currency: NotRequired["str|None"]

        class CreateParamsRestrictionsCurrencyOptions(TypedDict):
            minimum_amount: NotRequired["int|None"]

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            code: NotRequired["str|None"]
            coupon: NotRequired["str|None"]
            created: NotRequired["PromotionCode.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
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
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            restrictions: NotRequired[
                "PromotionCode.ModifyParamsRestrictions|None"
            ]

        class ModifyParamsRestrictions(TypedDict):
            currency_options: NotRequired[
                "Dict[str, PromotionCode.ModifyParamsRestrictionsCurrencyOptions]|None"
            ]

        class ModifyParamsRestrictionsCurrencyOptions(TypedDict):
            minimum_amount: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    active: bool
    code: str
    coupon: "Coupon"
    created: int
    customer: Optional[ExpandableField["Customer"]]
    expires_at: Optional[int]
    id: str
    livemode: bool
    max_redemptions: Optional[int]
    metadata: Optional[Dict[str, str]]
    object: Literal["promotion_code"]
    restrictions: StripeObject
    times_redeemed: int

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PromotionCode.CreateParams"]
    ) -> "PromotionCode":
        return cast(
            "PromotionCode",
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
        **params: Unpack["PromotionCode.ListParams"]
    ) -> ListObject["PromotionCode"]:
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
        cls, id, **params: Unpack["PromotionCode.ModifyParams"]
    ) -> "PromotionCode":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PromotionCode",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PromotionCode.RetrieveParams"]
    ) -> "PromotionCode":
        instance = cls(id, **params)
        instance.refresh()
        return instance
