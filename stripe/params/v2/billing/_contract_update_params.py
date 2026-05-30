# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class ContractUpdateParams(TypedDict):
    include: NotRequired[
        List[
            Literal[
                "contract_line_details",
                "license_quantities",
                "one_time_fees",
                "pricing_lines",
                "pricing_overrides",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    license_quantity_actions: NotRequired[
        List["ContractUpdateParamsLicenseQuantityAction"]
    ]
    """
    Schema-only: License quantity actions (implementation to follow).
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


class ContractUpdateParamsLicenseQuantityAction(TypedDict):
    effective_at: "ContractUpdateParamsLicenseQuantityActionEffectiveAt"
    """
    The effective at for the license quantity action.
    """
    license_pricing_id: NotRequired[str]
    """
    The ID of the license pricing.
    """
    license_pricing_lookup_key: NotRequired[str]
    """
    The lookup key for the license pricing.
    """
    license_pricing_type: Literal["license_fee", "price"]
    """
    The type of the license pricing.
    """
    pricing_line: NotRequired[str]
    """
    The pricing line ID for the license quantity action.
    """
    pricing_line_lookup_key: NotRequired[str]
    """
    The pricing line lookup key for the license quantity action.
    """
    set: NotRequired["ContractUpdateParamsLicenseQuantityActionSet"]
    """
    The set quantity for the license quantity action.
    """
    type: Literal["set"]
    """
    The type of the license quantity action.
    """


class ContractUpdateParamsLicenseQuantityActionEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp for the effective at.
    """
    type: Literal["timestamp"]
    """
    The type of the effective at.
    """


class ContractUpdateParamsLicenseQuantityActionSet(TypedDict):
    quantity: int
    """
    The quantity to set.
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
    quantity: NotRequired[int]
    """
    The quantity for the price. Only applicable for licensed prices.
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
    The priority for the pricing override.
    """
    starts_at: "ContractUpdateParamsPricingOverrideActionAddStartsAt"
    """
    The start time for the pricing override.
    """
    type: Literal["multiplier", "overwrite_price"]
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
    price: str
    """
    The ID of the V1 price to overwrite.
    """
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
