# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class ContractUpdateParams(TypedDict):
    include: NotRequired[
        List[Literal["one_time_fees", "pricing_lines", "pricing_overrides"]]
    ]
    """
    Additional fields to include in the response.
    """
    pricing_line_actions: NotRequired[
        List["ContractUpdateParamsPricingLineAction"]
    ]
    """
    Pricing line actions to apply.
    """
    pricing_override_actions: NotRequired[
        List["ContractUpdateParamsPricingOverrideAction"]
    ]
    """
    Pricing override actions to apply.
    """


class ContractUpdateParamsPricingLineAction(TypedDict):
    add: NotRequired["ContractUpdateParamsPricingLineActionAdd"]
    """
    Parameters for adding a pricing line.
    """
    remove: NotRequired["ContractUpdateParamsPricingLineActionRemove"]
    """
    Parameters for removing a pricing line.
    """
    type: Literal["add", "remove", "update"]
    """
    The type of pricing line action.
    """
    update: NotRequired["ContractUpdateParamsPricingLineActionUpdate"]
    """
    Parameters for updating a pricing line.
    """


class ContractUpdateParamsPricingLineActionAdd(TypedDict):
    ends_at: "ContractUpdateParamsPricingLineActionAddEndsAt"
    """
    The end time for the pricing line.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the pricing line.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata for the pricing line.
    """
    pricing: "ContractUpdateParamsPricingLineActionAddPricing"
    """
    The pricing configuration for the pricing line.
    """
    starts_at: "ContractUpdateParamsPricingLineActionAddStartsAt"
    """
    The start time for the pricing line.
    """


class ContractUpdateParamsPricingLineActionAddEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionAddPricing(TypedDict):
    price_details: NotRequired[
        "ContractUpdateParamsPricingLineActionAddPricingPriceDetails"
    ]
    """
    V1 price details. Required if `type` is `price`.
    """
    type: Literal["price"]
    """
    The type of pricing.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetails(TypedDict):
    price: str
    """
    The ID of the V1 price.
    """
    pricing_overrides: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverride"
        ]
    ]
    """
    Pricing overrides embedded directly on this pricing line.
    """
    quantity_changes: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsQuantityChange"
        ]
    ]
    """
    Quantity changes for the pricing line. For now, at most one entry is allowed.
    A quantity change clears all future quantity changes on this pricing line.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverride(
    TypedDict,
):
    ends_at: NotRequired[
        "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideEndsAt"
    ]
    """
    When the override ends. Defaults to the pricing line's end if not specified.
    """
    lookup_key: NotRequired[str]
    """
    A user-provided lookup key to reference this override.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    overwrite_price: NotRequired[
        "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePrice"
    ]
    """
    Parameters for the overwrite_price override. Required if `type` is `overwrite_price`.
    """
    priority: NotRequired[int]
    """
    The priority of this override relative to others. 0 is highest, 100 is lowest. Defaults to 50.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideStartsAt"
    ]
    """
    When the override starts. Defaults to the pricing line's start if not specified.
    """
    type: Literal["overwrite_price"]
    """
    The type of override. Currently only `overwrite_price` is supported.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Literal["contract_end", "timestamp"]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePrice(
    TypedDict,
):
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based.
    """
    tiers: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePriceTier"
        ]
    ]
    """
    Each element represents a pricing tier.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePriceTier(
    TypedDict,
):
    flat_amount: NotRequired[str]
    """
    Price for the entire tier, represented as a decimal string in minor currency units.
    """
    unit_amount: NotRequired[str]
    """
    Per-unit price for units included in this tier, represented as a decimal string in minor currency units.
    """
    up_to_decimal: NotRequired[Decimal]
    """
    Up to and including this quantity will be contained in the tier.
    """
    up_to_inf: NotRequired[Literal["inf"]]
    """
    No upper bound to this tier.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Literal["contract_start", "timestamp"]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsQuantityChange(
    TypedDict,
):
    effective_at: "ContractUpdateParamsPricingLineActionAddPricingPriceDetailsQuantityChangeEffectiveAt"
    """
    When this quantity change takes effect.
    """
    set: Decimal
    """
    The quantity to set.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsQuantityChangeEffectiveAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp for the effective at.
    """
    type: Literal["timestamp"]
    """
    The type of the effective at.
    """


class ContractUpdateParamsPricingLineActionAddStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingLineActionRemove(TypedDict):
    id: str
    """
    The ID of the pricing line to remove.
    """


class ContractUpdateParamsPricingLineActionUpdate(TypedDict):
    ends_at: NotRequired["ContractUpdateParamsPricingLineActionUpdateEndsAt"]
    """
    The updated end time for the pricing line.
    """
    id: str
    """
    The ID of the pricing line.
    """
    pricing: NotRequired["ContractUpdateParamsPricingLineActionUpdatePricing"]
    """
    Pricing updates for the pricing line (quantity changes and pricing override actions).
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdateStartsAt"
    ]
    """
    The updated start time for the pricing line.
    """


class ContractUpdateParamsPricingLineActionUpdateEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricing(TypedDict):
    price_details: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetails"
    ]
    """
    V1 price details. Present when the pricing line type is `price`.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetails(
    TypedDict
):
    pricing_override_actions: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideAction"
        ]
    ]
    """
    Pricing override actions to apply to the overrides embedded on this pricing line.
    """
    quantity_changes: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsQuantityChange"
        ]
    ]
    """
    Quantity changes for the pricing line. Setting this clears all future quantity changes.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideAction(
    TypedDict,
):
    add: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAdd"
    ]
    """
    Parameters for adding a pricing line override.
    """
    remove: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionRemove"
    ]
    """
    Parameters for removing a pricing line override.
    """
    type: Literal["add", "remove", "update"]
    """
    The type of pricing line override action.
    """
    update: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdate"
    ]
    """
    Parameters for updating a pricing line override.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAdd(
    TypedDict,
):
    ends_at: "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddEndsAt"
    """
    The end time for the override.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the override.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    overwrite_price: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePrice"
    ]
    """
    Parameters for an overwrite_price override. Required if `type` is `overwrite_price`.
    """
    priority: NotRequired[int]
    """
    The priority of this override relative to others. 0 is highest, 100 is lowest. Defaults to 50.
    """
    starts_at: "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddStartsAt"
    """
    The start time for the override.
    """
    type: Literal["overwrite_price"]
    """
    The type of override to add.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePrice(
    TypedDict,
):
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based.
    """
    tiers: NotRequired[
        List[
            "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePriceTier"
        ]
    ]
    """
    Each element represents a pricing tier.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePriceTier(
    TypedDict,
):
    flat_amount: NotRequired[str]
    """
    Price for the entire tier, represented as a decimal string in minor currency units.
    """
    unit_amount: NotRequired[str]
    """
    Per-unit price for units included in this tier, represented as a decimal string in minor currency units.
    """
    up_to_decimal: NotRequired[Decimal]
    """
    Up to and including this quantity will be contained in the tier.
    """
    up_to_inf: NotRequired[Literal["inf"]]
    """
    No upper bound to this tier.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionRemove(
    TypedDict,
):
    id: NotRequired[str]
    """
    The ID of the pricing line override to remove.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the override to remove.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdate(
    TypedDict,
):
    ends_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateEndsAt"
    ]
    """
    The updated end time for the override.
    """
    id: NotRequired[str]
    """
    The ID of the pricing line override to update.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the override to update.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateStartsAt"
    ]
    """
    The updated start time for the override.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsQuantityChange(
    TypedDict,
):
    effective_at: "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsQuantityChangeEffectiveAt"
    """
    When this quantity change takes effect.
    """
    set: Decimal
    """
    The quantity to set.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsQuantityChangeEffectiveAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp for the effective at.
    """
    type: Literal["timestamp"]
    """
    The type of the effective at.
    """


class ContractUpdateParamsPricingLineActionUpdateStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingOverrideAction(TypedDict):
    add: NotRequired["ContractUpdateParamsPricingOverrideActionAdd"]
    """
    Parameters for adding a pricing override.
    """
    remove: NotRequired["ContractUpdateParamsPricingOverrideActionRemove"]
    """
    Parameters for removing a pricing override.
    """
    type: Literal["add", "remove", "update"]
    """
    The type of pricing override action.
    """
    update: NotRequired["ContractUpdateParamsPricingOverrideActionUpdate"]
    """
    Parameters for updating a pricing override.
    """


class ContractUpdateParamsPricingOverrideActionAdd(TypedDict):
    ends_at: "ContractUpdateParamsPricingOverrideActionAddEndsAt"
    """
    The end time for the pricing override.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the pricing override.
    """
    multiplier: NotRequired[
        "ContractUpdateParamsPricingOverrideActionAddMultiplier"
    ]
    """
    A multiplier override to add.
    """
    overwrite_price: NotRequired[
        "ContractUpdateParamsPricingOverrideActionAddOverwritePrice"
    ]
    """
    An overwrite price override to add.
    """
    priority: int
    """
    The priority for the pricing override. The highest priority is 0 and the lowest is 100.
    """
    starts_at: "ContractUpdateParamsPricingOverrideActionAddStartsAt"
    """
    The start time for the pricing override.
    """
    type: Literal["multiplier"]
    """
    The type of pricing override to add.
    """


class ContractUpdateParamsPricingOverrideActionAddEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplier(TypedDict):
    criteria: List[
        "ContractUpdateParamsPricingOverrideActionAddMultiplierCriterion"
    ]
    """
    Criteria determining which rates the multiplier applies to.
    """
    factor: str
    """
    The multiplier factor, represented as a decimal string. e.g. "0.8" for a 20% reduction.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplierCriterion(
    TypedDict,
):
    billable_item_ids: List[str]
    """
    Filter by billable item IDs.
    """
    billable_item_lookup_keys: List[str]
    """
    Filter by billable item lookup keys.
    """
    billable_item_types: List[Literal["licensed", "metered"]]
    """
    Filter by billable item type.
    """
    metadata_conditions: List[
        "ContractUpdateParamsPricingOverrideActionAddMultiplierCriterionMetadataCondition"
    ]
    """
    Filter by metadata conditions.
    """
    rate_card_ids: List[str]
    """
    Filter by rate card IDs. Only applicable for `multiplier` overrides.
    """
    type: Literal["exclude", "include"]
    """
    Whether to include or exclude items matching these criteria.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplierCriterionMetadataCondition(
    TypedDict,
):
    all_of: List[
        "ContractUpdateParamsPricingOverrideActionAddMultiplierCriterionMetadataConditionAllOf"
    ]
    """
    All of these key-value conditions must match.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplierCriterionMetadataConditionAllOf(
    TypedDict,
):
    key: str
    """
    The metadata key.
    """
    value: str
    """
    The metadata value.
    """


class ContractUpdateParamsPricingOverrideActionAddOverwritePrice(TypedDict):
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based.
    """
    tiers: List[
        "ContractUpdateParamsPricingOverrideActionAddOverwritePriceTier"
    ]
    """
    Each element represents a pricing tier.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingOverrideActionAddOverwritePriceTier(
    TypedDict
):
    flat_amount: NotRequired[str]
    """
    Price for the entire tier, represented as a decimal string in minor currency units.
    """
    unit_amount: NotRequired[str]
    """
    Per-unit price for units included in this tier, represented as a decimal string in minor currency units.
    """
    up_to_decimal: NotRequired[Decimal]
    """
    Up to and including this quantity will be contained in the tier.
    """
    up_to_inf: NotRequired[Literal["inf"]]
    """
    No upper bound to this tier.
    """


class ContractUpdateParamsPricingOverrideActionAddStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingOverrideActionRemove(TypedDict):
    id: str
    """
    The ID of the pricing override to remove.
    """


class ContractUpdateParamsPricingOverrideActionUpdate(TypedDict):
    ends_at: NotRequired[
        "ContractUpdateParamsPricingOverrideActionUpdateEndsAt"
    ]
    """
    The updated end time for the pricing override.
    """
    id: str
    """
    The ID of the pricing override.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingOverrideActionUpdateStartsAt"
    ]
    """
    The updated start time for the pricing override.
    """


class ContractUpdateParamsPricingOverrideActionUpdateEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends.
    """
    type: Literal["billing_period_end", "timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingOverrideActionUpdateStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts.
    """
    type: Literal["billing_period_start", "timestamp"]
    """
    The type of start time to apply.
    """
