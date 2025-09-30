# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitUpdateParams(TypedDict):
    active: NotRequired[bool]
    """
    Whether the Custom Pricing Unit is active.
    """
    display_name: NotRequired[str]
    """
    Description that customers will see in the invoice line item.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular CustomPricingUnit item.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object.
    """
