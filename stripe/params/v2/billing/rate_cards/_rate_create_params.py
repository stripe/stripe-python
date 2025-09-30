# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RateCreateParams(TypedDict):
    custom_pricing_unit_amount: NotRequired[
        "RateCreateParamsCustomPricingUnitAmount"
    ]
    """
    The custom pricing unit that this rate binds to.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    metered_item: NotRequired[str]
    """
    The Metered Item that this rate binds to.
    """
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
    quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
    grows into new tiers. Can only be set if `tiers` is set.
    """
    tiers: NotRequired[List["RateCreateParamsTier"]]
    """
    Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
    """
    transform_quantity: NotRequired["RateCreateParamsTransformQuantity"]
    """
    Apply a transformation to the reported usage or set quantity before computing the amount billed.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
    places. Cannot be set if `tiers` is provided.
    """


class RateCreateParamsCustomPricingUnitAmount(TypedDict):
    id: str
    """
    The id of the custom pricing unit.
    """
    value: str
    """
    The unit value for the custom pricing unit, as a string.
    """


class RateCreateParamsTier(TypedDict):
    flat_amount: NotRequired[str]
    """
    Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
    """
    unit_amount: NotRequired[str]
    """
    Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
    most 12 decimal places.
    """
    up_to_decimal: NotRequired[str]
    """
    Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
    be set.
    """
    up_to_inf: NotRequired[Literal["inf"]]
    """
    No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
    """


class RateCreateParamsTransformQuantity(TypedDict):
    divide_by: int
    """
    Divide usage by this number.
    """
    round: Literal["down", "up"]
    """
    After division, round the result up or down.
    """
