# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.plan import Plan
    from stripe.api_resources.price import Price
    from stripe.api_resources.tax_rate import TaxRate


@nested_resource_class_methods(
    "usage_record",
    operations=["create"],
)
@nested_resource_class_methods(
    "usage_record_summary",
    operations=["list"],
    resource_plural="usage_record_summaries",
)
class SubscriptionItem(
    CreateableAPIResource["SubscriptionItem"],
    DeletableAPIResource["SubscriptionItem"],
    ListableAPIResource["SubscriptionItem"],
    UpdateableAPIResource["SubscriptionItem"],
):
    """
    Subscription items allow you to create customer subscriptions with more than
    one plan, making it easy to represent complex billing relationships.
    """

    OBJECT_NAME = "subscription_item"
    billing_thresholds: Optional[StripeObject]
    created: int
    id: str
    metadata: Dict[str, str]
    object: Literal["subscription_item"]
    plan: "Plan"
    price: "Price"
    quantity: int
    subscription: str
    tax_rates: Optional[List["TaxRate"]]
