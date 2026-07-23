# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanSubscriptionRetrieveParams(TypedDict):
    include: NotRequired[
        List[
            Union[
                Literal["discount_details", "pricing_plan_component_details"],
                str,
            ]
        ]
    ]
    """
    Expand to include additional data such as discount_details.
    """
