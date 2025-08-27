# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class PricingPlanVersion(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.pricing_plan_version"]] = (
        "v2.billing.pricing_plan_version"
    )
    created: str
    """
    Time at which the object was created.
    """
    end_date: Optional[str]
    """
    The timestamp when this version became inactive. Null if it's the latest version.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.pricing_plan_version"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_plan: str
    """
    The ID of the PricingPlan this version belongs to.
    """
    start_date: str
    """
    The timestamp when this version became active.
    """
