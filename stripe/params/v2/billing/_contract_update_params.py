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
    Apply all term actions atomically.
    """
    billing_settings: NotRequired["ContractUpdateParamsBillingSettings"]
    """
    The billing settings to update on the contract.
    """
    contract_number: NotRequired[str]
    """
    The unique user-provided contract number. This can only be changed while the contract is in draft.
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
    scheduled_fee: NotRequired["ContractUpdateParamsActionAddTermScheduledFee"]
    """
    Required when type is scheduled_fee.
    """
    type: Union[
        Literal["pricing_override", "recurring_price", "scheduled_fee"], str
    ]
    """
    The term type. Production types require exactly one matching payload.
    """


class ContractUpdateParamsActionAddTermPricingOverride(TypedDict):
    criteria: NotRequired[
        List["ContractUpdateParamsActionAddTermPricingOverrideCriterion"]
    ]
    """
    Optional criteria selecting recurring or scheduled_fee terms. If omitted, the override applies to all recurring and scheduled_fee terms.
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
    Whether to include or exclude the selected recurring or scheduled_fee terms.
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
    type: Union[Literal["never", "now", "timestamp"], str]
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
    type: Union[Literal["now", "timestamp"], str]
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
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionAddTermRecurringPriceStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionAddTermScheduledFee(TypedDict):
    bill_schedule: "ContractUpdateParamsActionAddTermScheduledFeeBillSchedule"
    """
    Explicit bill dates and amounts.
    """
    product: str
    """
    The V1 Product being billed.
    """
    service_period: NotRequired[
        "ContractUpdateParamsActionAddTermScheduledFeeServicePeriod"
    ]
    """
    Informational service period, independent of bill dates.
    """


class ContractUpdateParamsActionAddTermScheduledFeeBillSchedule(TypedDict):
    custom: NotRequired[
        List["ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustom"]
    ]
    """
    Between one and ten installments. Empty schedules are allowed only on update.
    """
    type: Union[Literal["custom"], str]
    """
    The type of schedule.
    """


class ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustom(
    TypedDict,
):
    amount: AmountParam
    """
    Non-negative amount with an explicit currency that must match the contract's currency.
    """
    bill_at: (
        "ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustomBillAt"
    )
    """
    A finite bill date. Resolved once per request, including on idempotent retries.
    """


class ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustomBillAt(
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


class ContractUpdateParamsActionAddTermScheduledFeeServicePeriod(TypedDict):
    ends_at: "ContractUpdateParamsActionAddTermScheduledFeeServicePeriodEndsAt"
    """
    The finite exclusive end; must be after starts_at. Never is not supported.
    """
    starts_at: (
        "ContractUpdateParamsActionAddTermScheduledFeeServicePeriodStartsAt"
    )
    """
    The finite inclusive start of the service period.
    """


class ContractUpdateParamsActionAddTermScheduledFeeServicePeriodEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionAddTermScheduledFeeServicePeriodStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
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
    scheduled_fee: NotRequired[
        "ContractUpdateParamsActionUpdateTermScheduledFee"
    ]
    """
    Must match the existing term's type.
    """
    term: "ContractUpdateParamsActionUpdateTermTerm"
    """
    Select a term by ID or its unique lookup key.
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
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
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
    type: Union[Literal["never", "now", "timestamp"], str]
    """
    The type of the ends_at.
    """


class ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermScheduledFee(TypedDict):
    bill_schedule: NotRequired[
        "ContractUpdateParamsActionUpdateTermScheduledFeeBillSchedule"
    ]
    """
    Replace remaining unbilled installments. Billed entries remain immutable.
    """
    service_period: NotRequired[
        "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriod"
    ]
    """
    Informational service period; cannot change historical billing.
    """


class ContractUpdateParamsActionUpdateTermScheduledFeeBillSchedule(TypedDict):
    custom: NotRequired[
        List[
            "ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustom"
        ]
    ]
    """
    Full replacement of up to ten unbilled installments. An explicit empty array cancels all of them.
    """
    type: Union[Literal["custom"], str]
    """
    The type of schedule.
    """


class ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustom(
    TypedDict,
):
    amount: AmountParam
    """
    Non-negative amount with an explicit currency that must match the contract's currency.
    """
    bill_at: "ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustomBillAt"
    """
    A finite bill date. Resolved once per request, including on idempotent retries.
    """


class ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustomBillAt(
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


class ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriod(TypedDict):
    ends_at: (
        "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodEndsAt"
    )
    """
    The finite exclusive end; must be after starts_at. Never is not supported.
    """
    starts_at: (
        "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodStartsAt"
    )
    """
    The finite inclusive start of the service period.
    """


class ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodEndsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
    """
    The type of the starts_at.
    """


class ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodStartsAt(
    TypedDict,
):
    timestamp: NotRequired[str]
    """
    The timestamp when the item starts. Required if `type` is `timestamp`.
    """
    type: Union[Literal["now", "timestamp"], str]
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
