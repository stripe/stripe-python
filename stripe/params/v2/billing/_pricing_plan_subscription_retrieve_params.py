# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanSubscriptionRetrieveParams(TypedDict):
    include: NotRequired[
        List[Literal["discount_details", "pricing_plan_component_details"]]
    ]
    """
    Expand to include additional data such as discount_details.
    """
