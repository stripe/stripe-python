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

    class CreateParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        code: NotRequired[Optional[str]]
        coupon: str
        customer: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]
        max_redemptions: NotRequired[Optional[int]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        restrictions: NotRequired[
            Optional["PromotionCode.CreateParamsRestrictions"]
        ]

    class CreateParamsRestrictions(TypedDict):
        currency_options: NotRequired[
            Optional[
                Dict[
                    str,
                    "PromotionCode.CreateParamsRestrictionsCurrencyOptions",
                ]
            ]
        ]
        first_time_transaction: NotRequired[Optional[bool]]
        minimum_amount: NotRequired[Optional[int]]
        minimum_amount_currency: NotRequired[Optional[str]]

    class CreateParamsRestrictionsCurrencyOptions(TypedDict):
        minimum_amount: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        code: NotRequired[Optional[str]]
        coupon: NotRequired[Optional[str]]
        created: NotRequired[
            Optional[Union["PromotionCode.ListParamsCreated", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        restrictions: NotRequired[
            Optional["PromotionCode.ModifyParamsRestrictions"]
        ]

    class ModifyParamsRestrictions(TypedDict):
        currency_options: NotRequired[
            Optional[
                Dict[
                    str,
                    "PromotionCode.ModifyParamsRestrictionsCurrencyOptions",
                ]
            ]
        ]

    class ModifyParamsRestrictionsCurrencyOptions(TypedDict):
        minimum_amount: NotRequired[Optional[int]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
