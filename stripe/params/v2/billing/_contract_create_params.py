# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractCreateParams(TypedDict):
    billing_cycle_anchor: NotRequired["ContractCreateParamsBillingCycleAnchor"]
    """
    The billing cycle anchor for the contract. If not provided, defaults to the pricing line start time.
    It is only at the top-level of the contract with no option to override at the pricing line level.
    """
    billing_settings: NotRequired["ContractCreateParamsBillingSettings"]
    """
    The billing settings for the contract.
    """
    contract_number: str
    """
    A unique user-provided contract number e.g. C-2026-0001.
    Maximum length of 200 characters.
    """
    currency: str
    """
    Currency of the contract.
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
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object.
    """
    terms: NotRequired[List["ContractCreateParamsTerm"]]
    """
    Terms to create with the contract.
    """


class ContractCreateParamsBillingCycleAnchor(TypedDict):
    config: NotRequired["ContractCreateParamsBillingCycleAnchorConfig"]
    """
    Configuration for determining the billing cycle anchor by calendar fields.
    """
    timestamp: NotRequired[str]
    """
    A specific timestamp to use as the billing cycle anchor.
    """
    type: Literal["config", "timestamp"]
    """
    The type of billing cycle anchor.
    """


class ContractCreateParamsBillingCycleAnchorConfig(TypedDict):
    day_of_month: int
    """
    Day of month (1-31).
    """
    hour: NotRequired[int]
    """
    Hour of day in UTC (0-23).
    """
    minute: NotRequired[int]
    """
    Minute of hour (0-59).
    """
    month_of_year: NotRequired[int]
    """
    Month of year (1-12).
    """
    second: NotRequired[int]
    """
    Second of minute (0-59).
    """


class ContractCreateParamsBillingSettings(TypedDict):
    bill_settings_details: NotRequired[
        "ContractCreateParamsBillingSettingsBillSettingsDetails"
    ]
    """
    The bill settings details configures invoice and tax settings for the contract.
    """
    billing_profile_details: (
        "ContractCreateParamsBillingSettingsBillingProfileDetails"
    )
    """
    The billing profile details configures who is charged for the contract.
    """
    collection_settings_details: (
        "ContractCreateParamsBillingSettingsCollectionSettingsDetails"
    )
    """
    The collection settings details configures how payments are collected on the contract.
    """


class ContractCreateParamsBillingSettingsBillSettingsDetails(TypedDict):
    calculation: NotRequired[
        "ContractCreateParamsBillingSettingsBillSettingsDetailsCalculation"
    ]
    """
    Calculation settings.
    """
    invoice: NotRequired[
        "ContractCreateParamsBillingSettingsBillSettingsDetailsInvoice"
    ]
    """
    Invoice settings.
    """


class ContractCreateParamsBillingSettingsBillSettingsDetailsCalculation(
    TypedDict,
):
    tax: NotRequired[
        "ContractCreateParamsBillingSettingsBillSettingsDetailsCalculationTax"
    ]
    """
    Tax calculation settings.
    """


class ContractCreateParamsBillingSettingsBillSettingsDetailsCalculationTax(
    TypedDict,
):
    type: Literal["automatic", "manual"]
    """
    The type of tax calculation.
    """


class ContractCreateParamsBillingSettingsBillSettingsDetailsInvoice(TypedDict):
    time_until_due: NotRequired[
        "ContractCreateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue"
    ]
    """
    How long the customer has to pay the invoice before it's past due.
    """


class ContractCreateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue(
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


class ContractCreateParamsBillingSettingsBillingProfileDetails(TypedDict):
    customer: str
    """
    The customer who pays for the contract invoice.
    """
    default_payment_method: NotRequired[str]
    """
    The default payment method for the contract.
    """


class ContractCreateParamsBillingSettingsCollectionSettingsDetails(TypedDict):
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    How payment is collected for the contract.
    """
    payment_method_configuration: NotRequired[str]
    """
    The payment method configuration.
    """


class ContractCreateParamsTerm(TypedDict):
    lookup_key: NotRequired[str]
    """
    Lookup key unique across all term types on the contract.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs attached to the term.
    """
    pricing_override: NotRequired["ContractCreateParamsTermPricingOverride"]
    """
    Required when type is pricing_override.
    """
    recurring_price: NotRequired["ContractCreateParamsTermRecurringPrice"]
    """
    Required when type is recurring_price.
    """
    scheduled_fee: NotRequired["ContractCreateParamsTermScheduledFee"]
    """
    Required when type is scheduled_fee.
    """
    type: Union[
        Literal["pricing_override", "recurring_price", "scheduled_fee"], str
    ]
    """
    The term type. Production types require exactly one matching payload.
    """


class ContractCreateParamsTermPricingOverride(TypedDict):
    criteria: NotRequired[
        List["ContractCreateParamsTermPricingOverrideCriterion"]
    ]
    """
    Optional criteria selecting recurring or scheduled_fee terms. If omitted, the override applies to all recurring and scheduled_fee terms.
    """
    ends_at: NotRequired["ContractCreateParamsTermPricingOverrideEndsAt"]
    """
    The exclusive end. Omitted means open-ended.
    """
    multiply: NotRequired["ContractCreateParamsTermPricingOverrideMultiply"]
    """
    Required when type is multiply.
    """
    overwrite: NotRequired["ContractCreateParamsTermPricingOverrideOverwrite"]
    """
    Required when type is overwrite.
    """
    priority: NotRequired[int]
    """
    Lower numbers win; defaults to 50.
    """
    starts_at: "ContractCreateParamsTermPricingOverrideStartsAt"
    """
    The inclusive start of the validity window.
    """
    type: Union[Literal["multiply", "overwrite"], str]
    """
    The pricing operation. Exactly one matching pricing payload is required.
    """


class ContractCreateParamsTermPricingOverrideCriterion(TypedDict):
    terms: NotRequired[
        List["ContractCreateParamsTermPricingOverrideCriterionTerm"]
    ]
    """
    Term selectors. Each ID or lookup key resolves to one fixed term ID.
    Omitted or empty selects all charge-bearing terms. Override terms cannot be targets.
    """
    type: Union[Literal["exclude", "include"], str]
    """
    Whether to include or exclude the selected recurring or scheduled_fee terms.
    """


class ContractCreateParamsTermPricingOverrideCriterionTerm(TypedDict):
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


class ContractCreateParamsTermPricingOverrideEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractCreateParamsTermPricingOverrideMultiply(TypedDict):
    factor: Decimal
    """
    The multiplier, for example 0.85 for a 15% discount.
    """


class ContractCreateParamsTermPricingOverrideOverwrite(TypedDict):
    billing_scheme: NotRequired[Literal["per_unit", "tiered"]]
    """
    Whether the replacement pricing is per unit or tiered.
    """
    tiers: NotRequired[
        List["ContractCreateParamsTermPricingOverrideOverwriteTier"]
    ]
    """
    Replacement pricing tiers.
    """
    tiers_mode: NotRequired[Literal["graduated", "volume"]]
    """
    How the pricing tiers are applied.
    """
    unit_amount_decimal: NotRequired[Decimal]
    """
    The replacement per-unit amount in minor currency units.
    """


class ContractCreateParamsTermPricingOverrideOverwriteTier(TypedDict):
    flat_amount_decimal: NotRequired[Decimal]
    """
    Flat amount in minor currency units.
    """
    unit_amount_decimal: NotRequired[Decimal]
    """
    Per-unit amount in minor currency units.
    """
    up_to: NotRequired[int]
    """
    Inclusive whole-number upper bound. Omitted for an unbounded final tier.
    """


class ContractCreateParamsTermPricingOverrideStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractCreateParamsTermRecurringPrice(TypedDict):
    ends_at: NotRequired["ContractCreateParamsTermRecurringPriceEndsAt"]
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
    starts_at: "ContractCreateParamsTermRecurringPriceStartsAt"
    """
    The inclusive start of the term.
    """


class ContractCreateParamsTermRecurringPriceEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item ends. Required if `type` is `timestamp`.
    """
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractCreateParamsTermRecurringPriceStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractCreateParamsTermScheduledFee(TypedDict):
    bill_schedule: "ContractCreateParamsTermScheduledFeeBillSchedule"
    """
    Explicit bill dates and amounts.
    """
    product: str
    """
    The V1 Product being billed.
    """
    service_period: NotRequired[
        "ContractCreateParamsTermScheduledFeeServicePeriod"
    ]
    """
    Informational service period, independent of bill dates.
    """


class ContractCreateParamsTermScheduledFeeBillSchedule(TypedDict):
    custom: NotRequired[
        List["ContractCreateParamsTermScheduledFeeBillScheduleCustom"]
    ]
    """
    Between one and ten installments. Empty schedules are allowed only on update.
    """
    type: Union[Literal["custom"], str]
    """
    The type of schedule.
    """


class ContractCreateParamsTermScheduledFeeBillScheduleCustom(TypedDict):
    bill_at: "ContractCreateParamsTermScheduledFeeBillScheduleCustomBillAt"
    """
    A finite bill date. Resolved once per request, including on idempotent retries.
    """
    quantity: NotRequired[Decimal]
    """
    Positive installment quantity. Defaults to 1 when omitted.
    """
    unit_amount_decimal: Decimal
    """
    Positive unit price in minor units of the contract's currency, before multiplying by quantity.
    """


class ContractCreateParamsTermScheduledFeeBillScheduleCustomBillAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the entry should be billed. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the bill_at.
    """


class ContractCreateParamsTermScheduledFeeServicePeriod(TypedDict):
    ends_at: "ContractCreateParamsTermScheduledFeeServicePeriodEndsAt"
    """
    The finite exclusive end; must be after starts_at. Never is not supported.
    """
    starts_at: "ContractCreateParamsTermScheduledFeeServicePeriodStartsAt"
    """
    The finite inclusive start of the service period.
    """


class ContractCreateParamsTermScheduledFeeServicePeriodEndsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractCreateParamsTermScheduledFeeServicePeriodStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """
