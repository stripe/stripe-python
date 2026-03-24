# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RateCardModifyRatesParams(TypedDict):
    rates_to_create: List["RateCardModifyRatesParamsRatesToCreate"]
    """
    The list of RateCard rates to create or update. Maximum of 100 rates.
    """
    rates_to_delete: List["RateCardModifyRatesParamsRatesToDelete"]
    """
    The list of RateCard rates to delete. Maximum of 100 rates.
    """


class RateCardModifyRatesParamsRatesToCreate(TypedDict):
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    metered_item: NotRequired[str]
    """
    The Metered Item that this rate binds to. Cannot be set if `metered_item_data` is provided, and must be set if it isn't.
    """
    metered_item_data: NotRequired[
        "RateCardModifyRatesParamsRatesToCreateMeteredItemData"
    ]
    """
    The data to create a metered item that binds to this rate. Cannot be set if `metered_item` is provided, and must be set if it isn't.
    """
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
    quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
    grows into new tiers. Can only be set if `tiers` is set.
    """
    tiers: NotRequired[List["RateCardModifyRatesParamsRatesToCreateTier"]]
    """
    Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
    """
    transform_quantity: NotRequired[
        "RateCardModifyRatesParamsRatesToCreateTransformQuantity"
    ]
    """
    Apply a transformation to the reported usage or set quantity before computing the amount billed.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
    places. Cannot be set if `tiers` is provided.
    """


class RateCardModifyRatesParamsRatesToCreateMeteredItemData(TypedDict):
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular metered item.
    Must be unique among metered items.
    Maximum length of 200 characters.
    """
    meter: str
    """
    ID of the Meter that measures usage for this Metered Item.
    """
    meter_segment_conditions: List[
        "RateCardModifyRatesParamsRatesToCreateMeteredItemDataMeterSegmentCondition"
    ]
    """
    Optional array of Meter segments to filter event dimension keys for billing.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
    to "CPU-hour" for Checkout to display "(price) per CPU-hour", or "1 million events" to display "(price) per 1
    million events".
    Maximum length of 100 characters.
    """


class RateCardModifyRatesParamsRatesToCreateMeteredItemDataMeterSegmentCondition(
    TypedDict,
):
    dimension: str
    """
    A Meter dimension.
    """
    value: str
    """
    To count usage towards this metered item, the dimension must have this value.
    """


class RateCardModifyRatesParamsRatesToCreateTier(TypedDict):
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


class RateCardModifyRatesParamsRatesToCreateTransformQuantity(TypedDict):
    divide_by: int
    """
    Divide usage by this number.
    """
    round: Literal["down", "up"]
    """
    After division, round the result up or down.
    """


class RateCardModifyRatesParamsRatesToDelete(TypedDict):
    id: str
    """
    The ID of the RateCard rate to delete.
    """
