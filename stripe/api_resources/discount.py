# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.coupon import Coupon
    from stripe.api_resources.promotion_code import PromotionCode


class Discount(StripeObject):
    """
    A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
    It contains information about when the discount began, when it will end, and what it is applied to.

    Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
    """

    OBJECT_NAME = "discount"
    checkout_session: Optional[str]
    coupon: "Coupon"
    customer: Optional[ExpandableField[Any]]
    end: Optional[str]
    id: str
    invoice: Optional[str]
    invoice_item: Optional[str]
    object: Literal["discount"]
    promotion_code: Optional[ExpandableField["PromotionCode"]]
    start: str
    subscription: Optional[str]
