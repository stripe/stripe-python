# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanCreateParams(TypedDict):
    currency: str
    """
    The currency of the PricingPlan.
    """
    description: NotRequired[str]
    """
    Description of pricing plan subscription.
    """
    display_name: str
    """
    Display name of the PricingPlan. Maximum 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular PricingPlan. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The Stripe Tax tax behavior - whether the PricingPlan is inclusive or exclusive of tax.
    """
