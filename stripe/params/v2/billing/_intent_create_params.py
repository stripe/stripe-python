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
    type: Literal["invoice_discount_rule"]
    """
    Type of the apply action details.
    """
    invoice_discount_rule: NotRequired[
        "IntentCreateParamsActionApplyInvoiceDiscountRule"
    ]
    """
    Details for applying a discount rule to future invoices.
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


class IntentCreateParamsActionDeactivate(TypedDict):
    billing_details: NotRequired[
        "IntentCreateParamsActionDeactivateBillingDetails"
    ]
    """
    Configuration for the billing details.
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


class IntentCreateParamsActionDeactivateBillingDetails(TypedDict):
    proration_behavior: NotRequired[
        Literal["no_adjustment", "prorated_adjustment"]
    ]
    """
    This controls the proration adjustment for the partial servicing period.
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
    pricing_plan_subscription: str
    """
    ID of the pricing plan subscription to deactivate.
    """


class IntentCreateParamsActionModify(TypedDict):
    billing_details: NotRequired[
        "IntentCreateParamsActionModifyBillingDetails"
    ]
    """
    Configuration for the billing details.
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


class IntentCreateParamsActionModifyBillingDetails(TypedDict):
    proration_behavior: NotRequired[
        Literal["no_adjustment", "prorated_adjustment"]
    ]
    """
    This controls the proration adjustment for the partial servicing period.
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


class IntentCreateParamsActionRemove(TypedDict):
    type: Literal["invoice_discount_rule"]
    """
    Type of the remove action.
    """
    invoice_discount_rule: NotRequired[str]
    """
    The ID of the discount rule to remove for future invoices.
    """


class IntentCreateParamsActionSubscribe(TypedDict):
    billing_details: NotRequired[
        "IntentCreateParamsActionSubscribeBillingDetails"
    ]
    """
    Configuration for the billing details. If not specified, see the default behavior for individual attributes.
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


class IntentCreateParamsActionSubscribeBillingDetails(TypedDict):
    proration_behavior: NotRequired[
        Literal["no_adjustment", "prorated_adjustment"]
    ]
    """
    This controls the proration adjustment for the partial servicing period.
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
