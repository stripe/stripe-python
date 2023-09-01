# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal


class Coupon(
    CreateableAPIResource["Coupon"],
    DeletableAPIResource["Coupon"],
    ListableAPIResource["Coupon"],
    UpdateableAPIResource["Coupon"],
):
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).
    """

    OBJECT_NAME = "coupon"
    amount_off: Optional[int]
    applies_to: StripeObject
    created: str
    currency: Optional[str]
    currency_options: Dict[str, StripeObject]
    duration: str
    duration_in_months: Optional[int]
    id: str
    livemode: bool
    max_redemptions: Optional[int]
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["coupon"]
    percent_off: Optional[float]
    redeem_by: Optional[str]
    times_redeemed: int
    valid: bool
