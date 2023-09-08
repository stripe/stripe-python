# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

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
    active: bool
    created: str
    delivery_estimate: Optional[StripeObject]
    display_name: Optional[str]
    fixed_amount: StripeObject
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["shipping_rate"]
    tax_behavior: Optional[str]
    tax_code: Optional[ExpandableField["TaxCode"]]
    type: Literal["fixed_amount"]
