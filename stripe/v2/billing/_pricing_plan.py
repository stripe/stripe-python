# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class PricingPlan(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.pricing_plan"]] = (
        "v2.billing.pricing_plan"
    )
    active: bool
    """
    Whether the PricingPlan is active.
    """
    created: str
    """
    Time at which the object was created.
    """
    currency: str
    """
    The currency of the PricingPlan.
    """
    description: Optional[str]
    """
    A description for pricing plan subscription.
    Maximum length of 500 characters.
    """
    display_name: str
    """
    Display name of the PricingPlan.
    """
    id: str
    """
    Unique identifier for the object.
    """
    latest_version: str
    """
    The ID of the latest version of the PricingPlan.
    """
    live_version: Optional[str]
    """
    The ID of the live version of the PricingPlan.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular PricingPlan. Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.pricing_plan"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The Stripe Tax tax behavior - whether the PricingPlan is inclusive or exclusive of tax.
    """
