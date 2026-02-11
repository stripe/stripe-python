# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitOverageRateCreateParams(TypedDict):
    custom_pricing_unit: str
    """
    The ID of the custom pricing unit this overage rate applies to.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    one_time_item: str
    """
    The ID of the one-time item to use for overage line items.
    """
    unit_amount: str
    """
    The per-unit amount to charge for overages, represented as a decimal string in minor currency units with at most 12 decimal places.
    """
