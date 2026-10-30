# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractUpdateParams(TypedDict):
    actions: NotRequired[List["ContractUpdateParamsAction"]]
    """
    Apply all actions atomically. Cannot be combined with the legacy child action arrays.
    """
    billing_settings: NotRequired["ContractUpdateParamsBillingSettings"]
    """
    The billing settings to update on the contract.
    """
    include: NotRequired[
        List[
            Union[
                Literal[
                    "billing_settings",
                    "one_time_fees",
                    "pricing_lines",
                    "pricing_overrides",
                    "terms",
                ],
                str,
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs.
    """
    one_time_fee_actions: NotRequired[
        List["ContractUpdateParamsOneTimeFeeAction"]
    ]
    """
    One-time fee actions to apply.
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


class ContractUpdateParamsAction(TypedDict):
    add_term: NotRequired["ContractUpdateParamsActionAddTerm"]
    """
    Prepend a term, preserving relative order among additions in this request.
    """
    remove_term: NotRequired["ContractUpdateParamsActionRemoveTerm"]
    """
    Remove a term that has not started.
    """
    type: Union[Literal["add_term", "remove_term", "update_term"], str]
    """
    The action type. Exactly one matching payload is required.
    """
    update_term: NotRequired["ContractUpdateParamsActionUpdateTerm"]
    """
    Edit a term without changing its display position.
    """


class ContractUpdateParamsActionAddTerm(TypedDict):
    ad_hoc_product: NotRequired[
        "ContractUpdateParamsActionAddTermAdHocProduct"
    ]
    """
    Required when type is ad_hoc_product.
    """
    lookup_key: NotRequired[str]
    """
    Lookup key unique across all term types on the contract.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs attached to the term.
    """
    pricing_override: NotRequired[
        "ContractUpdateParamsActionAddTermPricingOverride"
    ]
    """
    Required when type is pricing_override.
    """
    recurring_price: NotRequired[
        "ContractUpdateParamsActionAddTermRecurringPrice"
    ]
    """
    Required when type is recurring_price.
    """
    type: Union[
        Literal["ad_hoc_product", "pricing_override", "recurring_price"], str
    ]
    """
    The term type. Production types require exactly one matching payload.
    """


class ContractUpdateParamsActionAddTermAdHocProduct(TypedDict):
    bill_schedule: "ContractUpdateParamsActionAddTermAdHocProductBillSchedule"
    """
    Explicit bill dates and amounts.
    """
    product: str
    """
    The V1 Product being billed.
    """
    service_period: NotRequired[
        "ContractUpdateParamsActionAddTermAdHocProductServicePeriod"
    ]
    """
    Informational service period, independent of bill dates.
    """


class ContractUpdateParamsActionAddTermAdHocProductBillSchedule(TypedDict):
    custom: NotRequired[
        List["ContractUpdateParamsActionAddTermAdHocProductBillScheduleCustom"]
    ]
    """
    Between one and ten installments. Empty schedules are allowed only on update.
    """
    type: Union[Literal["custom"], str]
    """
    The type of schedule.
    """


class ContractUpdateParamsActionAddTermAdHocProductBillScheduleCustom(
    TypedDict,
):
    amount: AmountParam
    """
    Non-negative amount with an explicit currency that must match the contract's currency.
    """
    bill_at: (
        "ContractUpdateParamsActionAddTermAdHocProductBillScheduleCustomBillAt"
    )
    """
    A finite bill date. Resolved once per request, including on idempotent retries.
    """


class ContractUpdateParamsActionAddTermAdHocProductBillScheduleCustomBillAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp at which the entry should be billed. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the bill_at.
    """


class ContractUpdateParamsActionAddTermAdHocProductServicePeriod(TypedDict):
    ends_at: "ContractUpdateParamsActionAddTermAdHocProductServicePeriodEndsAt"
    """
    The finite exclusive end; must be after starts_at. Never is not supported.
    """
    starts_at: (
        "ContractUpdateParamsActionAddTermAdHocProductServicePeriodStartsAt"
    )
    """
    The finite inclusive start of the service period.
    """


class ContractUpdateParamsActionAddTermAdHocProductServicePeriodEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionAddTermAdHocProductServicePeriodStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionAddTermPricingOverride(TypedDict):
    criteria: NotRequired[
        List["ContractUpdateParamsActionAddTermPricingOverrideCriterion"]
    ]
    """
    Optional criteria selecting recurring or ad_hoc_product terms. If omitted, the override applies to all recurring and ad_hoc_product terms.
    """
    ends_at: NotRequired[
        "ContractUpdateParamsActionAddTermPricingOverrideEndsAt"
    ]
    """
    The exclusive end. Omitted means open-ended.
    """
    multiply: NotRequired[
        "ContractUpdateParamsActionAddTermPricingOverrideMultiply"
    ]
    """
    Required when type is multiply.
    """
    overwrite: NotRequired[
        "ContractUpdateParamsActionAddTermPricingOverrideOverwrite"
    ]
    """
    Required when type is overwrite.
    """
    priority: NotRequired[int]
    """
    Lower numbers win; defaults to 50.
    """
    starts_at: "ContractUpdateParamsActionAddTermPricingOverrideStartsAt"
    """
    The inclusive start of the validity window.
    """
    type: Union[Literal["multiply", "overwrite"], str]
    """
    The pricing operation. Exactly one matching pricing payload is required.
    """


class ContractUpdateParamsActionAddTermPricingOverrideCriterion(TypedDict):
    terms: NotRequired[
        List["ContractUpdateParamsActionAddTermPricingOverrideCriterionTerm"]
    ]
    """
    Term selectors. Each ID or lookup key resolves to one fixed term ID.
    Omitted or empty selects all charge-bearing terms. Override terms cannot be targets.
    """
    type: Union[Literal["exclude", "include"], str]
    """
    Whether to include or exclude the selected recurring or ad_hoc_product terms.
    """


class ContractUpdateParamsActionAddTermPricingOverrideCriterionTerm(TypedDict):
    id: NotRequired[str]
    """
    Select this term by its stable ID.
    """
    lookup_key: NotRequired[str]
    """
    Select this term by its unique lookup key.
    """
    type: Literal["id", "lookup_key"]
    """
    Whether the selector uses a term ID or lookup key.
    """


class ContractUpdateParamsActionAddTermPricingOverrideEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionAddTermPricingOverrideMultiply(TypedDict):
    factor: Decimal
    """
    The multiplier, for example 0.85 for a 15% discount.
    """


class ContractUpdateParamsActionAddTermPricingOverrideOverwrite(TypedDict):
    unit_amount_decimal: NotRequired[Decimal]
    """
    The replacement per-unit amount in minor currency units.
    """


class ContractUpdateParamsActionAddTermPricingOverrideStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionAddTermRecurringPrice(TypedDict):
    ends_at: NotRequired[
        "ContractUpdateParamsActionAddTermRecurringPriceEndsAt"
    ]
    """
    The exclusive end. Omitted means open-ended.
    """
    price: str
    """
    The V1 recurring Price.
    """
    quantity: NotRequired[Decimal]
    """
    Initial licensed quantity. Defaults to 1; must be omitted for metered Prices.
    """
    starts_at: "ContractUpdateParamsActionAddTermRecurringPriceStartsAt"
    """
    The inclusive start of the term.
    """


class ContractUpdateParamsActionAddTermRecurringPriceEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionAddTermRecurringPriceStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionRemoveTerm(TypedDict):
    term: "ContractUpdateParamsActionRemoveTermTerm"
    """
    Select a term by ID or its unique lookup key.
    """


class ContractUpdateParamsActionRemoveTermTerm(TypedDict):
    id: NotRequired[str]
    """
    Select this term by its stable ID.
    """
    lookup_key: NotRequired[str]
    """
    Select this term by its unique lookup key.
    """
    type: Literal["id", "lookup_key"]
    """
    Whether the selector uses a term ID or lookup key.
    """


class ContractUpdateParamsActionUpdateTerm(TypedDict):
    ad_hoc_product: NotRequired[
        "ContractUpdateParamsActionUpdateTermAdHocProduct"
    ]
    """
    Must match the existing term's type.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata changes to apply immediately.
    """
    pricing_override: NotRequired[
        "ContractUpdateParamsActionUpdateTermPricingOverride"
    ]
    """
    Only validity dates can change; pricing, criteria, and priority are immutable.
    """
    recurring_price: NotRequired[
        "ContractUpdateParamsActionUpdateTermRecurringPrice"
    ]
    """
    Must match the existing term's type.
    """
    term: "ContractUpdateParamsActionUpdateTermTerm"
    """
    Select a term by ID or its unique lookup key.
    """


class ContractUpdateParamsActionUpdateTermAdHocProduct(TypedDict):
    bill_schedule: NotRequired[
        "ContractUpdateParamsActionUpdateTermAdHocProductBillSchedule"
    ]
    """
    Replace remaining unbilled installments. Billed entries remain immutable.
    """
    service_period: NotRequired[
        "ContractUpdateParamsActionUpdateTermAdHocProductServicePeriod"
    ]
    """
    Informational service period; cannot change historical billing.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductBillSchedule(TypedDict):
    custom: NotRequired[
        List[
            "ContractUpdateParamsActionUpdateTermAdHocProductBillScheduleCustom"
        ]
    ]
    """
    Full replacement of up to ten unbilled installments. An explicit empty array cancels all of them.
    """
    type: Union[Literal["custom"], str]
    """
    The type of schedule.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductBillScheduleCustom(
    TypedDict,
):
    amount: AmountParam
    """
    Non-negative amount with an explicit currency that must match the contract's currency.
    """
    bill_at: "ContractUpdateParamsActionUpdateTermAdHocProductBillScheduleCustomBillAt"
    """
    A finite bill date. Resolved once per request, including on idempotent retries.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductBillScheduleCustomBillAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp at which the entry should be billed. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the bill_at.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductServicePeriod(TypedDict):
    ends_at: (
        "ContractUpdateParamsActionUpdateTermAdHocProductServicePeriodEndsAt"
    )
    """
    The finite exclusive end; must be after starts_at. Never is not supported.
    """
    starts_at: (
        "ContractUpdateParamsActionUpdateTermAdHocProductServicePeriodStartsAt"
    )
    """
    The finite inclusive start of the service period.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductServicePeriodEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermAdHocProductServicePeriodStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermPricingOverride(TypedDict):
    ends_at: NotRequired[
        "ContractUpdateParamsActionUpdateTermPricingOverrideEndsAt"
    ]
    """
    Omission leaves the end unchanged; never requests an open end.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt"
    ]
    """
    Can change only before the override starts. Accepts timestamp or now.
    """


class ContractUpdateParamsActionUpdateTermPricingOverrideEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermRecurringPrice(TypedDict):
    ends_at: NotRequired[
        "ContractUpdateParamsActionUpdateTermRecurringPriceEndsAt"
    ]
    """
    Omission leaves the end unchanged; never requests an open end.
    """
    quantity: NotRequired[Decimal]
    """
    Update an active term's licensed quantity at the contract's current clock time,
    or an unstarted term's initial quantity, preserving its ID. Ended terms cannot change quantity.
    """
    starts_at: NotRequired[
        "ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt"
    ]
    """
    Reschedule an unstarted term in place.
    """


class ContractUpdateParamsActionUpdateTermRecurringPriceEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermTerm(TypedDict):
    id: NotRequired[str]
    """
    Select this term by its stable ID.
    """
    lookup_key: NotRequired[str]
    """
    Select this term by its unique lookup key.
    """
    type: Literal["id", "lookup_key"]
    """
    Whether the selector uses a term ID or lookup key.
    """


class ContractUpdateParamsBillingSettings(TypedDict):
    bill_settings_details: NotRequired[
        "ContractUpdateParamsBillingSettingsBillSettingsDetails"
    ]
    """
    The bill settings to update (tax calculation type and/or invoice time until due).
    """
    billing_profile_details: NotRequired[
        "ContractUpdateParamsBillingSettingsBillingProfileDetails"
    ]
    """
    The billing profile details to update.
    """
    collection_settings_details: NotRequired[
        "ContractUpdateParamsBillingSettingsCollectionSettingsDetails"
    ]
    """
    The collection settings details to update on the contract.
    """


class ContractUpdateParamsBillingSettingsBillSettingsDetails(TypedDict):
    calculation: NotRequired[
        "ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculation"
    ]
    """
    The tax calculation settings to update.
    """
    invoice: NotRequired[
        "ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoice"
    ]
    """
    The invoice settings to update.
    """


class ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculation(
    TypedDict,
):
    tax: NotRequired[
        "ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculationTax"
    ]
    """
    Tax calculation settings.
    """


class ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculationTax(
    TypedDict,
):
    type: Literal["automatic", "manual"]
    """
    The type of tax calculation.
    """


class ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoice(TypedDict):
    time_until_due: NotRequired[
        "ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue"
    ]
    """
    How long the customer has to pay the invoice before it's past due.
    """


class ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue(
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


class ContractUpdateParamsBillingSettingsBillingProfileDetails(TypedDict):
    default_payment_method: NotRequired[str]
    """
    The default payment method to charge for the contract.
    """


class ContractUpdateParamsBillingSettingsCollectionSettingsDetails(TypedDict):
    collection_method: NotRequired[
        Literal["charge_automatically", "send_invoice"]
    ]
    """
    How payment is collected for the contract. An omitted value leaves the
    collection method unchanged.
    """
    payment_method_configuration: NotRequired[str]
    """
    The payment method configuration.
    """


class ContractUpdateParamsOneTimeFeeAction(TypedDict):
    add: NotRequired["ContractUpdateParamsOneTimeFeeActionAdd"]
    """
    Parameters for adding a one-time fee.
    """
    remove: NotRequired["ContractUpdateParamsOneTimeFeeActionRemove"]
    """
    Parameters for removing a one-time fee.
    """
    type: Literal["add", "remove", "update"]
    """
    The type of one-time fee action.
    """
    update: NotRequired["ContractUpdateParamsOneTimeFeeActionUpdate"]
    """
    Parameters for updating a one-time fee.
    """


class ContractUpdateParamsOneTimeFeeActionAdd(TypedDict):
    amount: AmountParam
    """
    The amount to bill.
    """
    bill_at: "ContractUpdateParamsOneTimeFeeActionAddBillAt"
    """
    When this fee should be billed.
    """
    lookup_key: NotRequired[str]
    """
    A user-provided lookup key.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata for the one-time fee.
    """
    product: str
    """
    The id of the product for this fee.
    """


class ContractUpdateParamsOneTimeFeeActionAddBillAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the entry should be billed. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the bill_at.
    """


class ContractUpdateParamsOneTimeFeeActionRemove(TypedDict):
    id: NotRequired[str]
    """
    The id of the one-time fee to remove.
    """
    lookup_key: NotRequired[str]
    """
    The lookup key of the one-time fee to remove.
    """


class ContractUpdateParamsOneTimeFeeActionUpdate(TypedDict):
    amount: NotRequired[AmountParam]
    """
    The updated amount to bill.
    """
    bill_at: NotRequired["ContractUpdateParamsOneTimeFeeActionUpdateBillAt"]
    """
    The updated bill_at schedule.
    """
    id: NotRequired[str]
    """
    The id of the one-time fee to update.
    """
    lookup_key: NotRequired[str]
    """
    The lookup key of the one-time fee to update.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata mutations to apply to the one-time fee.
    """


class ContractUpdateParamsOneTimeFeeActionUpdateBillAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the entry should be billed. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the bill_at.
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
    ends_at: NotRequired["ContractUpdateParamsPricingLineActionAddEndsAt"]
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
    type: Union[Literal["never", "now", "timestamp"], str]
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
    type: Union[Literal["price"], str]
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
    type: Union[Literal["overwrite_price"], str]
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
    type: Union[Literal["never", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideOverwritePrice(
    TypedDict,
):
    unit_amount: NotRequired[Decimal]
    """
    The per-unit amount to be charged in minor currency units.
    """


class ContractUpdateParamsPricingLineActionAddPricingPriceDetailsPricingOverrideStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["timestamp"], str]
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
    type: Union[Literal["timestamp"], str]
    """
    The type of the effective at.
    """


class ContractUpdateParamsPricingLineActionAddStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Union[Literal["timestamp"], str]
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
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata mutations to apply to the pricing line.
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
    type: Union[Literal["never", "now", "timestamp"], str]
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
    ends_at: NotRequired[
        "ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddEndsAt"
    ]
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
    type: Union[Literal["overwrite_price"], str]
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
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddOverwritePrice(
    TypedDict,
):
    unit_amount: NotRequired[Decimal]
    """
    The per-unit amount to be charged in minor currency units.
    """


class ContractUpdateParamsPricingLineActionUpdatePricingPriceDetailsPricingOverrideActionAddStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Union[Literal["timestamp"], str]
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
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata mutations to apply to the pricing override.
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
    type: Union[Literal["never", "now", "timestamp"], str]
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
    type: Union[Literal["timestamp"], str]
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
    type: Union[Literal["timestamp"], str]
    """
    The type of the effective at.
    """


class ContractUpdateParamsPricingLineActionUpdateStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Union[Literal["timestamp"], str]
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
    ends_at: NotRequired["ContractUpdateParamsPricingOverrideActionAddEndsAt"]
    """
    The end time for the pricing override.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key for the pricing override.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata for the pricing override.
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
    type: Union[Literal["multiply_pricing"], str]
    """
    The type of pricing override to add.
    """


class ContractUpdateParamsPricingOverrideActionAddEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing ends.
    """
    type: Union[Literal["never", "now", "timestamp"], str]
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
    type: Union[Literal["timestamp"], str]
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
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata mutations to apply to the pricing override.
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
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of end time to apply.
    """


class ContractUpdateParamsPricingOverrideActionUpdateStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the pricing starts.
    """
    type: Union[Literal["timestamp"], str]
    """
    The type of start time to apply.
    """
