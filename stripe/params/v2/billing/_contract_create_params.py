# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class ContractCreateParams(TypedDict):
    billing_settings: NotRequired["ContractCreateParamsBillingSettings"]
    """
    The billing settings for the contract.
    """
    contract_number: str
    """
    A unique user-provided contract number e.g. C-2026-0001.
    """
    currency: str
    """
    Currency of the contract.
    """
    include: NotRequired[
        List[Literal["one_time_fees", "pricing_lines", "pricing_overrides"]]
    ]
    """
    Additional fields to include in the response.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    one_time_fees: NotRequired[List["ContractCreateParamsOneTimeFee"]]
    """
    A list of one-time fees to create with the contract. Each fee is billed as individual invoice items per its bill_schedule.
    """
    pricing_lines: List["ContractCreateParamsPricingLine"]
    """
    A list of pricing lines to create with the contract.
    """
    pricing_overrides: NotRequired[List["ContractCreateParamsPricingOverride"]]
    """
    A list of pricing overrides to create with the contract.
    """


class ContractCreateParamsBillingSettings(TypedDict):
    contract_billing_details: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetails"
    ]
    """
    Billing settings details for the contract.
    """


class ContractCreateParamsBillingSettingsContractBillingDetails(TypedDict):
    bill_settings_details: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetails"
    ]
    """
    The bill settings details.
    """
    billing_profile_details: "ContractCreateParamsBillingSettingsContractBillingDetailsBillingProfileDetails"
    """
    The billing profile details.
    """
    collection_settings_details: "ContractCreateParamsBillingSettingsContractBillingDetailsCollectionSettingsDetails"
    """
    The collection settings details.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetails(
    TypedDict,
):
    calculation: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsCalculation"
    ]
    """
    Calculation settings.
    """
    invoice: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsInvoice"
    ]
    """
    Invoice settings.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsCalculation(
    TypedDict,
):
    tax: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsCalculationTax"
    ]
    """
    Tax calculation settings.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsCalculationTax(
    TypedDict,
):
    type: Literal["automatic", "manual"]
    """
    The type of tax calculation.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsInvoice(
    TypedDict,
):
    time_until_due: NotRequired[
        "ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsInvoiceTimeUntilDue"
    ]
    """
    The number of time units before the invoice is past due.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillSettingsDetailsInvoiceTimeUntilDue(
    TypedDict,
):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit.
    """
    interval_count: int
    """
    The number of intervals.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsBillingProfileDetails(
    TypedDict,
):
    customer: str
    """
    The customer who pays for the contract invoice.
    """
    default_payment_method: NotRequired[str]
    """
    The default payment method for the contract.
    """


class ContractCreateParamsBillingSettingsContractBillingDetailsCollectionSettingsDetails(
    TypedDict,
):
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    The collection method.
    """
    payment_method_configuration: NotRequired[str]
    """
    The payment method configuration.
    """


class ContractCreateParamsOneTimeFee(TypedDict):
    bill_schedule: List["ContractCreateParamsOneTimeFeeBillSchedule"]
    """
    The bill schedule for the fee. Each entry produces an individual invoice item billed at `bill_at`.
    """
    billable_item_type: Literal["product"]
    """
    The type of billable item that this fee references.
    """
    product_details: NotRequired[
        "ContractCreateParamsOneTimeFeeProductDetails"
    ]
    """
    Details for a product billable target. Required when `billable_item_type` is `product`.
    """


class ContractCreateParamsOneTimeFeeBillSchedule(TypedDict):
    bill_at: "ContractCreateParamsOneTimeFeeBillScheduleBillAt"
    """
    When this entry should be billed.
    """
    value: int
    """
    The amount to bill for this entry, in the smallest currency unit.
    """


class ContractCreateParamsOneTimeFeeBillScheduleBillAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The datetime at which the entry should be billed. Required if `type` is `datetime`.
    """
    type: Literal["contract_start", "datetime"]
    """
    The type of the bill_at.
    """


class ContractCreateParamsOneTimeFeeProductDetails(TypedDict):
    product: str
    """
    The ID of the v1 Product.
    """


class ContractCreateParamsPricingLine(TypedDict):
    ends_at: "ContractCreateParamsPricingLineEndsAt"
    """
    When the pricing line ends.
    """
    lookup_key: NotRequired[str]
    """
    A user-provided lookup key to reference this pricing line.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    pricing: "ContractCreateParamsPricingLinePricing"
    """
    The pricing configuration for the pricing line.
    """
    starts_at: "ContractCreateParamsPricingLineStartsAt"
    """
    When the pricing line starts.
    """


class ContractCreateParamsPricingLineEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Literal["contract_end", "timestamp"]
    """
    The type of the ends_at.
    """


class ContractCreateParamsPricingLinePricing(TypedDict):
    price_details: NotRequired[
        "ContractCreateParamsPricingLinePricingPriceDetails"
    ]
    """
    V1 price details. Required if `type` is `price`.
    """
    type: Literal["price"]
    """
    The type of pricing.
    """


class ContractCreateParamsPricingLinePricingPriceDetails(TypedDict):
    price: str
    """
    The ID of the V1 price.
    """
    pricing_overrides: NotRequired[
        List[
            "ContractCreateParamsPricingLinePricingPriceDetailsPricingOverride"
        ]
    ]
    """
    Pricing overrides embedded directly on this pricing line.
    """
    quantity_changes: NotRequired[
        List[
            "ContractCreateParamsPricingLinePricingPriceDetailsQuantityChange"
        ]
    ]
    """
    Quantity changes for the pricing line. For now, at most one entry is allowed.
    A quantity change clears all future quantity changes on this pricing line.
    """


class ContractCreateParamsPricingLinePricingPriceDetailsPricingOverride(
    TypedDict,
):
    ends_at: NotRequired[
        "ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideEndsAt"
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
        "ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideOverwritePrice"
    ]
    """
    Parameters for the overwrite_price override. Required if `type` is `overwrite_price`.
    """
    priority: NotRequired[int]
    """
    The priority of this override relative to others. 0 is highest, 100 is lowest. Defaults to 50.
    """
    starts_at: NotRequired[
        "ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideStartsAt"
    ]
    """
    When the override starts. Defaults to the pricing line's start if not specified.
    """
    type: Literal["overwrite_price"]
    """
    The type of override. Currently only `overwrite_price` is supported.
    """


class ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideEndsAt(
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


class ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideOverwritePrice(
    TypedDict,
):
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based.
    """
    tiers: NotRequired[
        List[
            "ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideOverwritePriceTier"
        ]
    ]
    """
    Each element represents a pricing tier.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units.
    """


class ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideOverwritePriceTier(
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


class ContractCreateParamsPricingLinePricingPriceDetailsPricingOverrideStartsAt(
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


class ContractCreateParamsPricingLinePricingPriceDetailsQuantityChange(
    TypedDict,
):
    effective_at: "ContractCreateParamsPricingLinePricingPriceDetailsQuantityChangeEffectiveAt"
    """
    When this quantity change takes effect.
    """
    set: Decimal
    """
    The quantity to set.
    """


class ContractCreateParamsPricingLinePricingPriceDetailsQuantityChangeEffectiveAt(
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


class ContractCreateParamsPricingLineStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Literal["contract_start", "timestamp"]
    """
    The type of the starts_at.
    """


class ContractCreateParamsPricingOverride(TypedDict):
    ends_at: "ContractCreateParamsPricingOverrideEndsAt"
    """
    When the pricing override ends.
    """
    lookup_key: NotRequired[str]
    """
    A user-provided lookup key to reference this pricing override.
    """
    multiplier: NotRequired["ContractCreateParamsPricingOverrideMultiplier"]
    """
    Parameters for a multiplier override. Required if `type` is `multiplier`.
    """
    priority: int
    """
    The priority of this override relative to others. The highest priority is 0 and the lowest is 100.
    """
    starts_at: "ContractCreateParamsPricingOverrideStartsAt"
    """
    When the pricing override starts.
    """
    type: Literal["multiplier"]
    """
    The type of pricing override.
    """


class ContractCreateParamsPricingOverrideEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Literal["contract_end", "timestamp"]
    """
    The type of the ends_at.
    """


class ContractCreateParamsPricingOverrideMultiplier(TypedDict):
    criteria: NotRequired[
        List["ContractCreateParamsPricingOverrideMultiplierCriterion"]
    ]
    """
    Criteria determining which rates the multiplier applies to.
    """
    factor: str
    """
    The multiplier factor, represented as a decimal string. e.g. "0.8" for a 20% reduction.
    """


class ContractCreateParamsPricingOverrideMultiplierCriterion(TypedDict):
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
        "ContractCreateParamsPricingOverrideMultiplierCriterionMetadataCondition"
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


class ContractCreateParamsPricingOverrideMultiplierCriterionMetadataCondition(
    TypedDict,
):
    all_of: List[
        "ContractCreateParamsPricingOverrideMultiplierCriterionMetadataConditionAllOf"
    ]
    """
    All of these key-value conditions must match.
    """


class ContractCreateParamsPricingOverrideMultiplierCriterionMetadataConditionAllOf(
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


class ContractCreateParamsPricingOverrideStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Literal["contract_start", "timestamp"]
    """
    The type of the starts_at.
    """
