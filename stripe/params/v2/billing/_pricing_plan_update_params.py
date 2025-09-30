# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class PricingPlanUpdateParams(TypedDict):
    active: NotRequired[bool]
    """
    Whether the PricingPlan is active.
    """
    description: NotRequired[str]
    """
    Description of pricing plan subscription.
    """
    display_name: NotRequired[str]
    """
    Display name of the PricingPlan. Maximum 250 characters.
    """
    live_version: NotRequired[str]
    """
    The ID of the live version of the PricingPlan.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular PricingPlan. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object.
    """
