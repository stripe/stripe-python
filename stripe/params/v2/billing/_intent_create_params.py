# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class IntentCreateParams(TypedDict):
    actions: List["IntentCreateParamsAction"]
    """
    Actions to be performed by this Billing Intent.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    cadence: NotRequired[str]
    """
    ID of an existing Cadence to use.
    """
    cadence_data: NotRequired["IntentCreateParamsCadenceData"]
    """
    Data for creating a new Cadence.
    """


class IntentCreateParamsAction(TypedDict):
    type: Literal["apply", "deactivate", "modify", "remove", "subscribe"]
    """
    Type of the Billing Intent action.
    """
    apply: NotRequired["IntentCreateParamsActionApply"]
    """
    Details for an apply action.
    """
    deactivate: NotRequired["IntentCreateParamsActionDeactivate"]
    """
    Details for a deactivate action.
    """
    modify: NotRequired["IntentCreateParamsActionModify"]
    """
    Details for a modify action.
    """
    remove: NotRequired["IntentCreateParamsActionRemove"]
    """
    Details for a remove action.
    """
    subscribe: NotRequired["IntentCreateParamsActionSubscribe"]
    """
    Details for a subscribe action.
    """


class IntentCreateParamsActionApply(TypedDict):
    effective_at: NotRequired["IntentCreateParamsActionApplyEffectiveAt"]
    """
    When the apply action will take effect. Defaults to on_reserve if not specified.
    """
    type: Literal["invoice_discount_rule", "spend_modifier_rule"]
    """
    Type of the apply action details.
    """
    invoice_discount_rule: NotRequired[
        "IntentCreateParamsActionApplyInvoiceDiscountRule"
    ]
    """
    Details for applying a discount rule to future invoices.
    """
    spend_modifier_rule: NotRequired[
        "IntentCreateParamsActionApplySpendModifierRule"
    ]
    """
    Details for applying a spend modifier rule. Only present if type is spend_modifier_rule.
    """


class IntentCreateParamsActionApplyEffectiveAt(TypedDict):
    type: Literal["current_billing_period_end", "on_reserve"]
    """
    When the apply action will take effect.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRule(TypedDict):
    applies_to: Literal["cadence"]
    """
    The entity that the discount rule applies to, for example, the cadence.
    """
    type: Literal["percent_off"]
    """
    Type of the discount rule.
    """
    percent_off: NotRequired[
        "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff"
    ]
    """
    Configuration for percentage off discount.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff(TypedDict):
    maximum_applications: "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications"
    """
    The maximum number of times this discount can be applied for this cadence.
    """
    percent_off: str
    """
    Percent that will be taken off of the amount. For example, percent_off of 50.0 will make $100 amount $50 instead.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications(
    TypedDict,
):
    type: Literal["indefinite"]
    """
    The type of maximum applications configuration.
    """


class IntentCreateParamsActionApplySpendModifierRule(TypedDict):
    applies_to: Literal["cadence"]
    """
    What the spend modifier applies to.
    """
    type: Literal["max_billing_period_spend"]
    """
    Type of the spend modifier.
    """
    max_billing_period_spend: NotRequired[
        "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend"
    ]
    """
    Details for max billing period spend modifier. Only present if type is max_billing_period_spend.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend(
    TypedDict,
):
    amount: "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount"
    """
    The maximum amount allowed for the billing period.
    """
    custom_pricing_unit_overage_rate: "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendCustomPricingUnitOverageRate"
    """
    The configration for the overage rate for the custom pricing unit.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount(
    TypedDict,
):
    type: Literal["custom_pricing_unit"]
    """
    The type of the amount.
    """
    custom_pricing_unit: NotRequired[
        "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit"
    ]
    """
    The custom pricing unit amount.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit(
    TypedDict,
):
    value: str
    """
    The value of the custom pricing unit.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendCustomPricingUnitOverageRate(
    TypedDict,
):
    id: str
    """
    ID of the custom pricing unit overage rate.
    """


class IntentCreateParamsActionDeactivate(TypedDict):
    cancellation_details: NotRequired[
        "IntentCreateParamsActionDeactivateCancellationDetails"
    ]
    """
    Details about why the cancellation is being requested.
    """
    collect_at: NotRequired[Literal["next_billing_date", "on_effective_at"]]
    """
    Allows users to override the collect at behavior.
    """
    effective_at: NotRequired["IntentCreateParamsActionDeactivateEffectiveAt"]
    """
    When the deactivate action will take effect. If not specified, the default behavior is on_reserve.
    """
    pricing_plan_subscription_details: (
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails"
    )
    """
    Details for deactivating a pricing plan subscription.
    """
    type: Literal[
        "pricing_plan_subscription_details", "v1_subscription_details"
    ]
    """
    Type of the action details.
    """


class IntentCreateParamsActionDeactivateCancellationDetails(TypedDict):
    comment: NotRequired[str]
    """
    Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
    """
    feedback: NotRequired[
        Literal[
            "customer_service",
            "low_quality",
            "missing_features",
            "other",
            "switched_service",
            "too_complex",
            "too_expensive",
            "unused",
        ]
    ]
    """
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
    """


class IntentCreateParamsActionDeactivateEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the deactivate action will take effect. Only present if type is timestamp.
    """
    type: Literal[
        "current_billing_period_end",
        "current_billing_period_start",
        "on_reserve",
        "timestamp",
    ]
    """
    When the deactivate action will take effect.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails(
    TypedDict,
):
    overrides: NotRequired[
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides"
    ]
    """
    Allows users to override the partial period behavior.
    """
    pricing_plan_subscription: str
    """
    ID of the pricing plan subscription to deactivate.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides(
    TypedDict,
):
    partial_period_behaviors: List[
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior"
    ]
    """
    Override for the partial period behavior.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    type: Literal["license_fee"]
    """
    Type of the partial period behavior override.
    """
    license_fee: NotRequired[
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Override for the license fee.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    credit_proration_behavior: Literal["none", "prorated"]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is deactivating.
    """


class IntentCreateParamsActionModify(TypedDict):
    collect_at: NotRequired[Literal["next_billing_date", "on_effective_at"]]
    """
    Allows users to override the collect at behavior.
    """
    effective_at: NotRequired["IntentCreateParamsActionModifyEffectiveAt"]
    """
    When the modify action will take effect. If not specified, the default behavior is on_reserve.
    """
    pricing_plan_subscription_details: (
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetails"
    )
    """
    Details for modifying a pricing plan subscription.
    """
    type: Literal[
        "pricing_plan_subscription_details", "v1_subscription_details"
    ]
    """
    Type of the action details.
    """


class IntentCreateParamsActionModifyEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the modify action will take effect. Only present if type is timestamp.
    """
    type: Literal["current_billing_period_start", "on_reserve", "timestamp"]
    """
    When the modify action will take effect.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetails(TypedDict):
    component_configurations: NotRequired[
        List[
            "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration"
        ]
    ]
    """
    New configurations for the components of the pricing plan.
    """
    new_pricing_plan: NotRequired[str]
    """
    The ID of the new Pricing Plan, if changing plans.
    """
    new_pricing_plan_version: NotRequired[str]
    """
    The ID of the new Pricing Plan Version to use.
    """
    overrides: NotRequired[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides"
    ]
    """
    Allows users to override the partial period behavior.
    """
    pricing_plan_subscription: str
    """
    The ID of the Pricing Plan Subscription to modify.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration(
    TypedDict,
):
    quantity: NotRequired[int]
    """
    Quantity of the component to be used.
    """
    lookup_key: NotRequired[str]
    """
    Lookup key for the pricing plan component.
    """
    pricing_plan_component: NotRequired[str]
    """
    ID of the pricing plan component.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides(
    TypedDict,
):
    partial_period_behaviors: List[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior"
    ]
    """
    Override for the partial period behavior.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    type: Literal["license_fee"]
    """
    Type of the partial period behavior override.
    """
    license_fee: NotRequired[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Override for the license fee.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    credit_proration_behavior: Literal["none", "prorated"]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is upgrading.
    """
    debit_proration_behavior: Literal["none", "prorated"]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is downgrading.
    """


class IntentCreateParamsActionRemove(TypedDict):
    effective_at: NotRequired["IntentCreateParamsActionRemoveEffectiveAt"]
    """
    When the remove action will take effect. Defaults to on_reserve if not specified.
    """
    type: Literal["invoice_discount_rule", "spend_modifier_rule"]
    """
    Type of the remove action.
    """
    invoice_discount_rule: NotRequired[str]
    """
    The ID of the discount rule to remove for future invoices.
    """
    spend_modifier_rule: NotRequired[str]
    """
    The ID of the spend modifier rule to remove.
    """


class IntentCreateParamsActionRemoveEffectiveAt(TypedDict):
    type: Literal["current_billing_period_end", "on_reserve"]
    """
    When the remove action will take effect.
    """


class IntentCreateParamsActionSubscribe(TypedDict):
    collect_at: NotRequired[Literal["next_billing_date", "on_effective_at"]]
    """
    Allows users to override the collect at behavior.
    """
    effective_at: NotRequired["IntentCreateParamsActionSubscribeEffectiveAt"]
    """
    When the subscribe action will take effect. If not specified, the default behavior is on_reserve.
    """
    type: Literal[
        "pricing_plan_subscription_details", "v1_subscription_details"
    ]
    """
    Type of the action details.
    """
    pricing_plan_subscription_details: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails"
    ]
    """
    Details for subscribing to a pricing plan.
    """
    v1_subscription_details: NotRequired[
        "IntentCreateParamsActionSubscribeV1SubscriptionDetails"
    ]
    """
    Details for subscribing to a v1 subscription.
    """


class IntentCreateParamsActionSubscribeEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the subscribe action will take effect. Only present if type is timestamp.
    """
    type: Literal["current_billing_period_start", "on_reserve", "timestamp"]
    """
    When the subscribe action will take effect.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails(
    TypedDict,
):
    component_configurations: NotRequired[
        List[
            "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration"
        ]
    ]
    """
    Configurations for the components of the pricing plan.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    overrides: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides"
    ]
    """
    Allows users to override the partial period behavior.
    """
    pricing_plan: str
    """
    ID of the Pricing Plan to subscribe to.
    """
    pricing_plan_version: str
    """
    Version of the Pricing Plan to use.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration(
    TypedDict,
):
    quantity: NotRequired[int]
    """
    Quantity of the component to be used.
    """
    lookup_key: NotRequired[str]
    """
    Lookup key for the pricing plan component.
    """
    pricing_plan_component: NotRequired[str]
    """
    ID of the pricing plan component.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides(
    TypedDict,
):
    partial_period_behaviors: List[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior"
    ]
    """
    Override for the partial period behavior.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    type: Literal["license_fee"]
    """
    Type of the partial period behavior override.
    """
    license_fee: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Override for the license fee.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    debit_proration_behavior: Literal["none", "prorated"]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is subscribing.
    """


class IntentCreateParamsActionSubscribeV1SubscriptionDetails(TypedDict):
    description: NotRequired[str]
    """
    The subscription's description, meant to be displayable to the customer.
    Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """
    items: List["IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem"]
    """
    A list of up to 20 subscription items, each with an attached price.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """


class IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem(TypedDict):
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    price: str
    """
    The ID of the price object.
    """
    quantity: NotRequired[int]
    """
    Quantity for this item. If not provided, will default to 1.
    """


class IntentCreateParamsCadenceData(TypedDict):
    billing_cycle: "IntentCreateParamsCadenceDataBillingCycle"
    """
    The billing cycle configuration for this Cadence.
    """
    payer: "IntentCreateParamsCadenceDataPayer"
    """
    Information about the payer for this Cadence.
    """
    settings: NotRequired["IntentCreateParamsCadenceDataSettings"]
    """
    Settings for creating the Cadence.
    """


class IntentCreateParamsCadenceDataBillingCycle(TypedDict):
    interval_count: NotRequired[int]
    """
    The number of intervals (specified in the interval attribute) between
    cadence billings. For example, type=month and interval_count=3 bills every
    3 months. If this is not provided, it will default to 1.
    """
    type: Literal["day", "month", "week", "year"]
    """
    The frequency at which a cadence bills.
    """
    day: NotRequired["IntentCreateParamsCadenceDataBillingCycleDay"]
    """
    Specific configuration for determining billing dates when type=day.
    """
    month: NotRequired["IntentCreateParamsCadenceDataBillingCycleMonth"]
    """
    Specific configuration for determining billing dates when type=month.
    """
    week: NotRequired["IntentCreateParamsCadenceDataBillingCycleWeek"]
    """
    Specific configuration for determining billing dates when type=week.
    """
    year: NotRequired["IntentCreateParamsCadenceDataBillingCycleYear"]
    """
    Specific configuration for determining billing dates when type=year.
    """


class IntentCreateParamsCadenceDataBillingCycleDay(TypedDict):
    time: NotRequired["IntentCreateParamsCadenceDataBillingCycleDayTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class IntentCreateParamsCadenceDataBillingCycleDayTime(TypedDict):
    hour: int
    """
    The hour at which the billing cycle ends.
    This must be an integer between 0 and 23, inclusive.
    0 represents midnight, and 23 represents 11 PM.
    """
    minute: int
    """
    The minute at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class IntentCreateParamsCadenceDataBillingCycleMonth(TypedDict):
    day_of_month: int
    """
    The day to anchor the billing on for a type="month" billing cycle from
    1-31. If this number is greater than the number of days in the month being
    billed, this will anchor to the last day of the month. If not provided,
    this will default to the day the cadence was created.
    """
    month_of_year: NotRequired[int]
    """
    The month to anchor the billing on for a type="month" billing cycle from
    1-12. If not provided, this will default to the month the cadence was created.
    This setting can only be used for monthly billing cycles with `interval_count` of 2, 3, 4 or 6.
    All occurrences will be calculated from month provided.
    """
    time: NotRequired["IntentCreateParamsCadenceDataBillingCycleMonthTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class IntentCreateParamsCadenceDataBillingCycleMonthTime(TypedDict):
    hour: int
    """
    The hour at which the billing cycle ends.
    This must be an integer between 0 and 23, inclusive.
    0 represents midnight, and 23 represents 11 PM.
    """
    minute: int
    """
    The minute at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class IntentCreateParamsCadenceDataBillingCycleWeek(TypedDict):
    day_of_week: int
    """
    The day of the week to bill the type=week billing cycle on.
    Numbered from 1-7 for Monday to Sunday respectively, based on the ISO-8601
    week day numbering. If not provided, this will default to the day the
    cadence was created.
    """
    time: NotRequired["IntentCreateParamsCadenceDataBillingCycleWeekTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class IntentCreateParamsCadenceDataBillingCycleWeekTime(TypedDict):
    hour: int
    """
    The hour at which the billing cycle ends.
    This must be an integer between 0 and 23, inclusive.
    0 represents midnight, and 23 represents 11 PM.
    """
    minute: int
    """
    The minute at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class IntentCreateParamsCadenceDataBillingCycleYear(TypedDict):
    day_of_month: NotRequired[int]
    """
    The day to anchor the billing on for a type="month" billing cycle from
    1-31. If this number is greater than the number of days in the month being
    billed, this will anchor to the last day of the month. If not provided,
    this will default to the day the cadence was created.
    """
    month_of_year: NotRequired[int]
    """
    The month to bill on from 1-12. If not provided, this will default to the
    month the cadence was created.
    """
    time: NotRequired["IntentCreateParamsCadenceDataBillingCycleYearTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class IntentCreateParamsCadenceDataBillingCycleYearTime(TypedDict):
    hour: int
    """
    The hour at which the billing cycle ends.
    This must be an integer between 0 and 23, inclusive.
    0 represents midnight, and 23 represents 11 PM.
    """
    minute: int
    """
    The minute at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class IntentCreateParamsCadenceDataPayer(TypedDict):
    billing_profile: NotRequired[str]
    """
    The ID of the Billing Profile object which determines how a bill will be paid.
    """
    billing_profile_data: NotRequired[
        "IntentCreateParamsCadenceDataPayerBillingProfileData"
    ]
    """
    Data for creating a new profile.
    """


class IntentCreateParamsCadenceDataPayerBillingProfileData(TypedDict):
    customer: str
    """
    The customer to associate with the profile.
    """
    default_payment_method: NotRequired[str]
    """
    The default payment method to use when billing this profile.
    If left blank, the `PaymentMethod` from the `PaymentIntent` provided
    on commit will be used to create the profile.
    """


class IntentCreateParamsCadenceDataSettings(TypedDict):
    bill: NotRequired["IntentCreateParamsCadenceDataSettingsBill"]
    """
    Settings that configure bill generation, which includes calculating totals, tax, and presenting invoices.
    If no setting is provided here, the settings from the customer referenced on the payer will be used.
    If no customer settings are present, the merchant default settings will be used.
    """
    collection: NotRequired["IntentCreateParamsCadenceDataSettingsCollection"]
    """
    Settings that configure and manage the behavior of collecting payments.
    If no setting is provided here, the settings from the customer referenced from the payer will be used if they exist.
    If no customer settings are present, the merchant default settings will be used.
    """


class IntentCreateParamsCadenceDataSettingsBill(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of the Settings to use.
    If not provided, this will always default to the live version any time the settings are used.
    """


class IntentCreateParamsCadenceDataSettingsCollection(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of the Settings to use.
    If not provided, this will always default to the live version any time the settings are used.
    """
