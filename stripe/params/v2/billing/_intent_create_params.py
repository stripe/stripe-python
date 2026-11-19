# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class IntentCreateParams(TypedDict):
    actions: List["IntentCreateParamsAction"]
    """
    Actions to be performed by this Billing Intent.
    """
    billing_group: NotRequired[str]
    """
    ID of an existing Billing Group to use.
    """
    billing_group_data: NotRequired["IntentCreateParamsBillingGroupData"]
    """
    Data for creating a new Billing Group.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """


class IntentCreateParamsAction(TypedDict):
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
    type: Union[
        Literal["apply", "deactivate", "modify", "remove", "subscribe"], str
    ]
    """
    Type of the Billing Intent action.
    """


class IntentCreateParamsActionApply(TypedDict):
    discount: NotRequired["IntentCreateParamsActionApplyDiscount"]
    """
    Details for applying a discount.
    """
    effective_at: NotRequired["IntentCreateParamsActionApplyEffectiveAt"]
    """
    When the apply action takes effect. If not specified, defaults to on_reserve.
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
    type: Union[
        Literal["discount", "invoice_discount_rule", "spend_modifier_rule"],
        str,
    ]
    """
    Type of the apply action details.
    """


class IntentCreateParamsActionApplyDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    The ID of the Coupon to apply.
    """
    promotion_code: NotRequired[str]
    """
    The ID of the PromotionCode to apply.
    """
    type: Literal["coupon", "promotion_code"]
    """
    Type of the discount.
    """


class IntentCreateParamsActionApplyEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the apply action takes effect. Only present if type is timestamp. Only allowed for discount actions.
    """
    type: Literal[
        "current_billing_period_end",
        "current_billing_period_start",
        "next_billing_period_start",
        "on_reserve",
        "timestamp",
    ]
    """
    When the apply action takes effect.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRule(TypedDict):
    applies_to: Union[Literal["cadence", "group"], str]
    """
    The entity that the discount rule applies to, for example, the billing group.
    """
    percent_off: NotRequired[
        "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff"
    ]
    """
    Configuration for percentage off discount.
    """
    type: Union[Literal["percent_off"], str]
    """
    Type of the discount rule.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff(TypedDict):
    maximum_applications: "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications"
    """
    The maximum number of times this discount can be applied for this billing group.
    """
    percent_off: Decimal
    """
    Percent that is taken off the amount. For example, a percent_off of 50.0 reduces a 100 USD amount to 50 USD.
    """


class IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications(
    TypedDict,
):
    type: Union[Literal["indefinite"], str]
    """
    The type of maximum applications configuration.
    """


class IntentCreateParamsActionApplySpendModifierRule(TypedDict):
    applies_to: Literal["cadence"]
    """
    What the spend modifier applies to.
    """
    max_billing_period_spend: NotRequired[
        "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend"
    ]
    """
    Details for max billing period spend modifier. Only present if type is max_billing_period_spend.
    """
    type: Union[Literal["max_billing_period_spend"], str]
    """
    Type of the spend modifier.
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
    The configuration for the overage rate for the custom pricing unit.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount(
    TypedDict,
):
    custom_pricing_unit: NotRequired[
        "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit"
    ]
    """
    The custom pricing unit amount.
    """
    type: Literal["custom_pricing_unit"]
    """
    The type of the amount.
    """


class IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit(
    TypedDict,
):
    id: NotRequired[str]
    """
    The id of the custom pricing unit.
    """
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
    collect_at: NotRequired[
        "Literal['next_billing_date', 'on_effective_at']|str"
    ]
    """
    When the invoice is collected. If not specified, the default behavior is on_effective_at.
    """
    effective_at: NotRequired["IntentCreateParamsActionDeactivateEffectiveAt"]
    """
    When the deactivate action takes effect. If not specified, the default behavior is on_reserve.
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
        "Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']|str"
    ]
    """
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
    """


class IntentCreateParamsActionDeactivateEffectiveAt(TypedDict):
    timestamp: NotRequired[str]
    """
    The timestamp at which the deactivate action takes effect. Only present if type is timestamp.
    """
    type: Union[
        Literal[
            "current_billing_period_end",
            "current_billing_period_start",
            "on_reserve",
            "timestamp",
        ],
        str,
    ]
    """
    When the deactivate action takes effect.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails(
    TypedDict,
):
    overrides: NotRequired[
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides"
    ]
    """
    Configurations for overriding behaviors related to the subscription.
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
    Configurations for behaviors when the action takes effect during the service period.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    license_fee: NotRequired[
        "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Overrides the behavior for license fee components when the action takes effect during the service period.
    """
    type: Union[Literal["license_fee", "recurring_credit_grant"], str]
    """
    The type of behavior to override.
    """


class IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    credit_proration_behavior: Union[Literal["none", "prorated"], str]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is deactivating. If not specified, defaults to none.
    """


class IntentCreateParamsActionModify(TypedDict):
    collect_at: NotRequired[
        "Literal['next_billing_date', 'on_effective_at']|str"
    ]
    """
    When the invoice is collected. If not specified, the default behavior is next_billing_date.
    """
    effective_at: NotRequired["IntentCreateParamsActionModifyEffectiveAt"]
    """
    When the modify action takes effect. If not specified, the default behavior is on_reserve.
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
    The timestamp at which the modify action takes effect. Only present if type is timestamp.
    """
    type: Union[
        Literal["current_billing_period_start", "on_reserve", "timestamp"], str
    ]
    """
    When the modify action takes effect.
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
    Configurations for overriding behaviors related to the subscription.
    """
    pricing_plan_subscription: str
    """
    The ID of the Pricing Plan Subscription to modify.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration(
    TypedDict,
):
    lookup_key: NotRequired[str]
    """
    Lookup key for the pricing plan component.
    """
    pricing_plan_component: NotRequired[str]
    """
    ID of the pricing plan component.
    """
    quantity: NotRequired[int]
    """
    Quantity of the component to be used.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides(
    TypedDict,
):
    partial_period_behaviors: List[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior"
    ]
    """
    Configurations for behaviors when the action takes effect during the service period.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    license_fee: NotRequired[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Overrides the behavior for license fee components when the action takes effect during the service period.
    """
    recurring_credit_grant: NotRequired[
        "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant"
    ]
    """
    Overrides the behavior for recurring credit grant components when the action takes effect during the service period.
    """
    type: Union[Literal["license_fee", "recurring_credit_grant"], str]
    """
    The type of behavior to override.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    credit_proration_behavior: Union[Literal["none", "prorated"], str]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user modifies the subscription. If not specified, defaults to prorated.
    """
    debit_proration_behavior: Union[Literal["none", "prorated"], str]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user modifies the subscription. If not specified, defaults to prorated.
    """


class IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant(
    TypedDict,
):
    create_behavior: Union[Literal["full_credits", "none"], str]
    """
    Controls credit grant creation behavior during partial periods. If not specified, defaults to full_credits.
    """


class IntentCreateParamsActionRemove(TypedDict):
    effective_at: NotRequired["IntentCreateParamsActionRemoveEffectiveAt"]
    """
    When the remove action takes effect. If not specified, defaults to on_reserve.
    """
    invoice_discount_rule: NotRequired[str]
    """
    The ID of the discount rule to remove for future invoices.
    """
    spend_modifier_rule: NotRequired[str]
    """
    The ID of the spend modifier rule to remove.
    """
    type: Union[Literal["invoice_discount_rule", "spend_modifier_rule"], str]
    """
    Type of the remove action.
    """


class IntentCreateParamsActionRemoveEffectiveAt(TypedDict):
    type: Union[Literal["current_billing_period_end", "on_reserve"], str]
    """
    When the remove action takes effect.
    """


class IntentCreateParamsActionSubscribe(TypedDict):
    collect_at: NotRequired[
        "Literal['next_billing_date', 'on_effective_at']|str"
    ]
    """
    When the invoice is collected. If not specified, defaults to on_effective_at.
    """
    effective_at: NotRequired["IntentCreateParamsActionSubscribeEffectiveAt"]
    """
    When the subscribe action takes effect. If not specified, the default behavior is on_reserve.
    """
    pricing_plan_subscription_details: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails"
    ]
    """
    Details for subscribing to a pricing plan.
    """
    type: Literal[
        "pricing_plan_subscription_details", "v1_subscription_details"
    ]
    """
    Type of the action details.
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
    The timestamp at which the subscribe action takes effect. Only present if type is timestamp.
    """
    type: Union[
        Literal["current_billing_period_start", "on_reserve", "timestamp"], str
    ]
    """
    When the subscribe action takes effect.
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
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    overrides: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides"
    ]
    """
    Configurations for overriding behaviors related to the subscription.
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
    lookup_key: NotRequired[str]
    """
    Lookup key for the pricing plan component.
    """
    pricing_plan_component: NotRequired[str]
    """
    ID of the pricing plan component.
    """
    quantity: NotRequired[int]
    """
    Quantity of the component to be used.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides(
    TypedDict,
):
    partial_period_behaviors: List[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior"
    ]
    """
    Configurations for behaviors when the action takes effect during the service period.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior(
    TypedDict,
):
    license_fee: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee"
    ]
    """
    Overrides the behavior for license fee components when the action takes effect during the service period.
    """
    recurring_credit_grant: NotRequired[
        "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant"
    ]
    """
    Overrides the behavior for recurring credit grant components when the action takes effect during the service period.
    """
    type: Union[Literal["license_fee", "recurring_credit_grant"], str]
    """
    The type of behavior to override.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee(
    TypedDict,
):
    debit_proration_behavior: Union[Literal["none", "prorated"], str]
    """
    The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is subscribing. If not specified, defaults to prorated.
    """


class IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant(
    TypedDict,
):
    create_behavior: Union[Literal["full_credits", "none"], str]
    """
    Controls credit grant creation behavior during partial periods. If not specified, defaults to full_credits.
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
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """


class IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem(TypedDict):
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    price: str
    """
    The ID of the price object.
    """
    quantity: NotRequired[int]
    """
    Quantity for this item. If not provided, defaults to 1.
    """


class IntentCreateParamsBillingGroupData(TypedDict):
    billing_settings: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettings"
    ]
    """
    Billing setting overrides for the group. If omitted, the applicable defaults are used.
    """
    customer: str
    """
    The ID of the Customer object whose invoices are grouped.
    """
    default_payment_method: NotRequired[str]
    """
    The ID of the PaymentMethod object used by default. If unset, the customer's default payment method is used.
    """
    grouping_behavior: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehavior"
    ]
    """
    The strategy used to group member invoices.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to find a particular billing group. Maximum length of 200 characters.
    """


class IntentCreateParamsBillingGroupDataBillingSettings(TypedDict):
    collection_method: NotRequired[
        Literal["charge_automatically", "send_invoice"]
    ]
    """
    How Stripe collects payment.
    """
    email_delivery: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsEmailDelivery"
    ]
    """
    Email delivery setting.
    """
    invoice_presentation: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsInvoicePresentation"
    ]
    """
    Settings for invoice presentation.
    """
    invoice_time_until_due: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsInvoiceTimeUntilDue"
    ]
    """
    The amount of time until the invoice is overdue for payment.
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the payment method configuration, which controls which payment methods are displayed to your customers.
    """
    payment_method_options: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptions"
    ]
    """
    Payment Method specific configuration to be stored on the object.
    """
    tax: NotRequired["IntentCreateParamsBillingGroupDataBillingSettingsTax"]
    """
    Settings for calculating tax.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsEmailDelivery(
    TypedDict
):
    payment_due: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsEmailDeliveryPaymentDue"
    ]
    """
    Controls emails for when the payment is due. Omit to use the applicable default.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsEmailDeliveryPaymentDue(
    TypedDict,
):
    enabled: NotRequired[bool]
    """
    If true an email for the invoice would be generated and sent out.
    """
    include_payment_link: NotRequired[bool]
    """
    If true the payment link to hosted invoice page would be included in email and PDF of the invoice.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsInvoicePresentation(
    TypedDict,
):
    invoice_rendering_template: NotRequired[str]
    """
    The ID of the invoice rendering template to be used when generating invoices. Omit to use the applicable default.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsInvoiceTimeUntilDue(
    TypedDict,
):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit for the time until due.
    """
    interval_count: int
    """
    The number of interval units. For example, if interval=day and interval_count=30, the invoice is due in 30 days.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptions(
    TypedDict,
):
    acss_debit: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebit"
    ]
    """
    This sub-hash contains details about the Canadian pre-authorized debit payment method options.
    """
    bancontact: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsBancontact"
    ]
    """
    This sub-hash contains details about the Bancontact payment method.
    """
    card: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains details about the Card payment method options.
    """
    customer_balance: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalance"
    ]
    """
    This sub-hash contains details about the Bank transfer payment method options.
    """
    konbini: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsKonbini"
    ]
    """
    This sub-hash contains details about the Konbini payment method options.
    """
    sepa_debit: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsSepaDebit"
    ]
    """
    This sub-hash contains details about the SEPA Direct Debit payment method options.
    """
    us_bank_account: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccount"
    ]
    """
    This sub-hash contains details about the ACH direct debit payment method options.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebit(
    TypedDict,
):
    mandate_options: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation.
    """
    verification_method: NotRequired[
        "Literal['automatic', 'instant', 'microdeposits']|str"
    ]
    """
    Verification method.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    transaction_type: NotRequired["Literal['business', 'personal']|str"]
    """
    Transaction type of the mandate.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsBancontact(
    TypedDict,
):
    preferred_language: NotRequired["Literal['de', 'en', 'fr', 'nl']|str"]
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCard(
    TypedDict,
):
    mandate_options: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCardMandateOptions"
    ]
    """
    Configuration options for setting up an eMandate for cards issued in India.
    """
    network: NotRequired[str]
    """
    Selected network to process the payment on. Depends on the available networks of the card.
    """
    request_three_d_secure: NotRequired[
        "Literal['any', 'automatic', 'challenge']|str"
    ]
    """
    An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
    for authentication based on risk level and [other requirements](https://docs.stripe.com/strong-customer-authentication).
    However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
    Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCardMandateOptions(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount to be charged for future payments.
    """
    amount_type: NotRequired["Literal['fixed', 'maximum']|str"]
    """
    The AmountType for the mandate. One of `fixed` or `maximum`.
    """
    description: NotRequired[str]
    """
    A description of the mandate that is meant to be displayed to the customer.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalance(
    TypedDict,
):
    bank_transfer: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
    ]
    """
    Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
    """
    funding_type: NotRequired["Literal['bank_transfer']|str"]
    """
    The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
    ]
    """
    Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
    """
    type: NotRequired[
        "Literal['eu_bank_transfer', 'gb_bank_transfer', 'jp_bank_transfer', 'mx_bank_transfer', 'us_bank_transfer']|str"
    ]
    """
    The bank transfer type that can be used for funding.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: Union[Literal["BE", "DE", "ES", "FR", "IE", "NL"], str]
    """
    The desired country code of the bank account information.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsKonbini(
    TypedDict,
):
    pass


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsSepaDebit(
    TypedDict,
):
    pass


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccount(
    TypedDict,
):
    financial_connections: "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
    """
    Additional fields for Financial Connections Session creation.
    """
    verification_method: Union[
        Literal["automatic", "instant", "microdeposits"], str
    ]
    """
    Verification method.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    permissions: NotRequired[
        List[
            Union[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ],
                str,
            ]
        ]
    ]
    """
    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
    """
    prefetch: NotRequired[
        List[Union[Literal["balances", "ownership", "transactions"], str]]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[
        List[Union[Literal["checking", "savings"], str]]
    ]
    """
    The account subcategories to use to filter for selectable accounts.
    """


class IntentCreateParamsBillingGroupDataBillingSettingsTax(TypedDict):
    type: NotRequired["Literal['automatic', 'manual']|str"]
    """
    Determines if tax is calculated automatically based on a product tax code or manually based on rules defined by the business. Omit to use the applicable default.
    """


class IntentCreateParamsBillingGroupDataGroupingBehavior(TypedDict):
    by_cadence: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadence"
    ]
    """
    The cadence configuration when type is `by_cadence`.
    """
    type: Union[Literal["by_cadence"], str]
    """
    The grouping strategy.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadence(TypedDict):
    billing_cycle_anchor: NotRequired[str]
    """
    Timestamp that anchors the recurring grouping cadence.
    """
    day: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDay"
    ]
    """
    Daily cadence details.
    """
    interval_count: NotRequired[int]
    """
    The number of interval units between groups. Defaults to 1.
    """
    month: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonth"
    ]
    """
    Monthly cadence details.
    """
    type: Union[Literal["day", "month", "week", "year"], str]
    """
    The interval unit for the cadence.
    """
    week: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeek"
    ]
    """
    Weekly cadence details.
    """
    year: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYear"
    ]
    """
    Yearly cadence details.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDay(
    TypedDict
):
    time: "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDayTime"
    """
    The time at which the daily grouping interval begins.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDayTime(
    TypedDict,
):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonth(
    TypedDict,
):
    day_of_month: int
    """
    The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
    """
    month_of_year: NotRequired[int]
    """
    The month of year, from 1 through 12, from which occurrences are calculated. Defaults to the month when the billing group was created.
    """
    time: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonthTime"
    ]
    """
    The time at which the monthly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonthTime(
    TypedDict,
):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeek(
    TypedDict,
):
    day_of_week: int
    """
    The ISO-8601 day of week, from 1 for Monday through 7 for Sunday.
    """
    time: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeekTime"
    ]
    """
    The time at which the weekly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeekTime(
    TypedDict,
):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYear(
    TypedDict,
):
    day_of_month: int
    """
    The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
    """
    month_of_year: int
    """
    The month of year, from 1 through 12.
    """
    time: NotRequired[
        "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYearTime"
    ]
    """
    The time at which the yearly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYearTime(
    TypedDict,
):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """
