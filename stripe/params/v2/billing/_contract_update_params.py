# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractUpdateParams(TypedDict):
    include: NotRequired[
        List[
            Union[
                Literal[
                    "billing_settings", "pricing_lines", "pricing_overrides"
                ],
                str,
            ]
        ]
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
    Add a pricing line.
    """
    remove: NotRequired["ContractUpdateParamsPricingLineActionRemove"]
    """
    Remove a pricing line.
    """
    type: Union[Literal["add", "remove", "update"], str]
    """
    The type of pricing line action.
    """
    update: NotRequired["ContractUpdateParamsPricingLineActionUpdate"]
    """
    Update a pricing line.
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
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
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
    The id of the price.
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
    A quantity change clears all future quantity changes on this pricing line. Defaults to 1.
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
    The type of override.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Literal["timestamp"]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePrice(
    TypedDict,
):
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Literal["timestamp"]
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
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingLineActionRemove(TypedDict):
    id: str
    """
    The id of the pricing line to remove.
    """


class ContractUpdateParamsPricingLineActionUpdate(TypedDict):
    ends_at: NotRequired["ContractUpdateParamsPricingLineActionUpdateEndsAt"]
    """
    Updated end time.
    """
    id: str
    """
    The id of the pricing line.
    """
    pricing: NotRequired["ContractUpdateParamsPricingLineActionUpdatePricing"]
    """
    Updated pricing configuration.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdateStartsAt"
    ]
    """
    Updated start time.
    """


class ContractUpdateParamsPricingLineActionUpdateEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
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
    Add a pricing line override.
    """
    remove: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionRemove"
    ]
    """
    Remove a pricing line override.
    """
    type: Union[Literal["add", "remove", "update"], str]
    """
    The type of pricing line override action.
    """
    update: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdate"
    ]
    """
    Update a pricing line override.
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
    Metadata for the pricing override.
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
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePrice(
    TypedDict,
):
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionRemove(
    TypedDict,
):
    id: NotRequired[str]
    """
    The id of the pricing override to remove.
    """
    lookup_key: NotRequired[str]
    """
    Lookup key of the override to remove.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdate(
    TypedDict,
):
    ends_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateEndsAt"
    ]
    """
    Updated end time.
    """
    id: NotRequired[str]
    """
    The id of the pricing override to update.
    """
    lookup_key: NotRequired[str]
    """
    Updated lookup key.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata for the pricing override.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateStartsAt"
    ]
    """
    Updated start time.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionUpdateStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
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
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingOverrideAction(TypedDict):
    add: NotRequired["ContractUpdateParamsPricingOverrideActionAdd"]
    """
    Add a pricing override.
    """
    remove: NotRequired["ContractUpdateParamsPricingOverrideActionRemove"]
    """
    Remove a pricing override.
    """
    type: Union[Literal["add", "remove", "update"], str]
    """
    The type of pricing override action.
    """
    update: NotRequired["ContractUpdateParamsPricingOverrideActionUpdate"]
    """
    Update a pricing override.
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
    multiply_pricing: NotRequired[
        "ContractUpdateParamsPricingOverrideActionAddMultiplyPricing"
    ]
    """
    A multiply_pricing override to add.
    """
    overwrite_price: NotRequired[
        "ContractUpdateParamsPricingOverrideActionAddOverwritePrice"
    ]
    """
    An overwrite price override to add.
    """
    priority: NotRequired[int]
    """
    The priority for the pricing override. The highest priority is 0 and the lowest is 100.
    """
    starts_at: "ContractUpdateParamsPricingOverrideActionAddStartsAt"
    """
    The start time for the pricing override.
    """
    type: Literal["multiply_pricing"]
    """
    The type of pricing override to add.
    """


class ContractUpdateParamsPricingOverrideActionAddEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplyPricing(TypedDict):
    criteria: List[
        "ContractUpdateParamsPricingOverrideActionAddMultiplyPricingCriterion"
    ]
    """
    Criteria determining which rates the multiply_pricing override applies to.
    """
    factor: str
    """
    The multiply_pricing factor, represented as a decimal string. e.g. "0.8" for a 20% reduction.
    """


class ContractUpdateParamsPricingOverrideActionAddMultiplyPricingCriterion(
    TypedDict,
):
    pricing_line_ids: NotRequired[List[str]]
    """
    Filter by pricing line IDs.
    """
    pricing_line_lookup_keys: NotRequired[List[str]]
    """
    Filter by pricing line lookup keys.
    """
    type: Union[Literal["exclude", "include"], str]
    """
    Whether to include or exclude items matching these criteria.
    """


class ContractUpdateParamsPricingOverrideActionAddOverwritePrice(TypedDict):
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractUpdateParamsPricingOverrideActionAddStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
    """
    The type of start time to apply.
    """


class ContractUpdateParamsPricingOverrideActionRemove(TypedDict):
    id: str
    """
    The id of the pricing override to remove.
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
    The timestamp when the pricing ends.
    """
    type: Literal["timestamp"]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingOverrideActionUpdateStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Literal["timestamp"]
    """
    The type of start time to apply.
    """
