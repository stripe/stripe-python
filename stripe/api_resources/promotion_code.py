# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
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

    class Restrictions(StripeObject):
        class CurrencyOptions(StripeObject):
            minimum_amount: int

        currency_options: Optional[Dict[str, CurrencyOptions]]
        first_time_transaction: bool
        minimum_amount: Optional[int]
        minimum_amount_currency: Optional[str]
        _inner_class_types = {"currency_options": CurrencyOptions}
        _inner_class_dicts = ["currency_options"]

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
    restrictions: Restrictions
    times_redeemed: int

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "PromotionCode":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PromotionCode",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PromotionCode":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"restrictions": Restrictions}
