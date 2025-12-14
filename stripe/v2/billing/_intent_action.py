# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class IntentAction(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.intent_action"]] = (
        "v2.billing.intent_action"
    )

    class Apply(StripeObject):
        class InvoiceDiscountRule(StripeObject):
            class PercentOff(StripeObject):
                class MaximumApplications(StripeObject):
                    type: Literal["indefinite"]
                    """
                    The type of maximum applications configuration.
                    """

                maximum_applications: MaximumApplications
                """
                The maximum number of times this discount can be applied for this Billing Cadence.
                """
                percent_off: str
                """
                Percent that will be taken off of the amount. For example, percent_off of 50.0 will make $100 amount $50 instead.
                """
                _inner_class_types = {
                    "maximum_applications": MaximumApplications,
                }

            applies_to: Literal["cadence"]
            """
            The entity that the discount rule applies to, for example, the Billing Cadence.
            """
            invoice_discount_rule: Optional[str]
            """
            The ID of the created discount rule. This is only present once the Billing Intent is committed and the discount rule is created.
            """
            percent_off: Optional[PercentOff]
            """
            Configuration for percentage off discount.
            """
            type: Literal["percent_off"]
            """
            Type of the discount rule.
            """
            _inner_class_types = {"percent_off": PercentOff}

        invoice_discount_rule: Optional[InvoiceDiscountRule]
        """
        Details for applying a discount rule to future invoices.
        """
        type: Literal["invoice_discount_rule"]
        """
        Type of the apply action details.
        """
        _inner_class_types = {"invoice_discount_rule": InvoiceDiscountRule}

    class Deactivate(StripeObject):
        class EffectiveAt(StripeObject):
            timestamp: Optional[str]
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

        class PricingPlanSubscriptionDetails(StripeObject):
            class Overrides(StripeObject):
                class PartialPeriodBehavior(StripeObject):
                    class LicenseFee(StripeObject):
                        credit_proration_behavior: Literal["none", "prorated"]
                        """
                        The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is deactivating.
                        """

                    license_fee: Optional[LicenseFee]
                    """
                    Override for the license fee.
                    """
                    type: Literal["license_fee"]
                    """
                    Type of the partial period behavior override.
                    """
                    _inner_class_types = {"license_fee": LicenseFee}

                partial_period_behaviors: List[PartialPeriodBehavior]
                """
                Override for the partial period behavior.
                """
                _inner_class_types = {
                    "partial_period_behaviors": PartialPeriodBehavior,
                }

            overrides: Optional[Overrides]
            """
            Allows users to override the partial period behavior.
            """
            pricing_plan_subscription: str
            """
            ID of the Pricing Plan Subscription to deactivate.
            """
            _inner_class_types = {"overrides": Overrides}

        collect_at: Literal["next_billing_date", "on_effective_at"]
        """
        Allows users to override the collect at behavior.
        """
        effective_at: EffectiveAt
        """
        When the deactivate action will take effect. If not specified, the default behavior is on_reserve.
        """
        pricing_plan_subscription_details: Optional[
            PricingPlanSubscriptionDetails
        ]
        """
        Details for deactivating a Pricing Plan Subscription.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """
        _inner_class_types = {
            "effective_at": EffectiveAt,
            "pricing_plan_subscription_details": PricingPlanSubscriptionDetails,
        }

    class Modify(StripeObject):
        class EffectiveAt(StripeObject):
            timestamp: Optional[str]
            """
            The timestamp at which the modify action will take effect. Only present if type is timestamp.
            """
            type: Literal[
                "current_billing_period_start", "on_reserve", "timestamp"
            ]
            """
            When the modify action will take effect.
            """

        class PricingPlanSubscriptionDetails(StripeObject):
            class ComponentConfiguration(StripeObject):
                lookup_key: Optional[str]
                """
                Lookup key for the pricing plan component.
                """
                pricing_plan_component: Optional[str]
                """
                ID of the pricing plan component.
                """
                quantity: Optional[int]
                """
                Quantity of the component to be used.
                """

            class Overrides(StripeObject):
                class PartialPeriodBehavior(StripeObject):
                    class LicenseFee(StripeObject):
                        credit_proration_behavior: Literal["none", "prorated"]
                        """
                        The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is upgrading.
                        """
                        debit_proration_behavior: Literal["none", "prorated"]
                        """
                        The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is downgrading.
                        """

                    license_fee: Optional[LicenseFee]
                    """
                    Override for the license fee.
                    """
                    type: Literal["license_fee"]
                    """
                    Type of the partial period behavior override.
                    """
                    _inner_class_types = {"license_fee": LicenseFee}

                partial_period_behaviors: List[PartialPeriodBehavior]
                """
                Override for the partial period behavior.
                """
                _inner_class_types = {
                    "partial_period_behaviors": PartialPeriodBehavior,
                }

            component_configurations: List[ComponentConfiguration]
            """
            New configurations for the components of the Pricing Plan.
            """
            new_pricing_plan: str
            """
            ID of the new Pricing Plan.
            """
            new_pricing_plan_version: str
            """
            Version of the Pricing Plan to use.
            """
            overrides: Optional[Overrides]
            """
            Allows users to override the partial period behavior.
            """
            pricing_plan_subscription: str
            """
            ID of the Pricing Plan Subscription to modify.
            """
            _inner_class_types = {
                "component_configurations": ComponentConfiguration,
                "overrides": Overrides,
            }

        collect_at: Literal["next_billing_date", "on_effective_at"]
        """
        Allows users to override the collect at behavior.
        """
        effective_at: EffectiveAt
        """
        When the modify action will take effect. If not specified, the default behavior is on_reserve.
        """
        pricing_plan_subscription_details: Optional[
            PricingPlanSubscriptionDetails
        ]
        """
        Details for modifying a Pricing Plan Subscription.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """
        _inner_class_types = {
            "effective_at": EffectiveAt,
            "pricing_plan_subscription_details": PricingPlanSubscriptionDetails,
        }

    class Remove(StripeObject):
        invoice_discount_rule: Optional[str]
        """
        The ID of the discount rule to remove for future invoices.
        """
        type: Literal["invoice_discount_rule"]
        """
        Type of the remove action.
        """

    class Subscribe(StripeObject):
        class EffectiveAt(StripeObject):
            timestamp: Optional[str]
            """
            The timestamp at which the subscribe action will take effect. Only present if type is timestamp.
            """
            type: Literal[
                "current_billing_period_start", "on_reserve", "timestamp"
            ]
            """
            When the subscribe action will take effect.
            """

        class PricingPlanSubscriptionDetails(StripeObject):
            class ComponentConfiguration(StripeObject):
                lookup_key: Optional[str]
                """
                Lookup key for the pricing plan component.
                """
                pricing_plan_component: Optional[str]
                """
                ID of the pricing plan component.
                """
                quantity: Optional[int]
                """
                Quantity of the component to be used.
                """

            class Overrides(StripeObject):
                class PartialPeriodBehavior(StripeObject):
                    class LicenseFee(StripeObject):
                        debit_proration_behavior: Literal["none", "prorated"]
                        """
                        The proration behavior for the partial servicing period. Defines how we prorate the license fee when the user is subscribing.
                        """

                    license_fee: Optional[LicenseFee]
                    """
                    Override for the license fee.
                    """
                    type: Literal["license_fee"]
                    """
                    Type of the partial period behavior override.
                    """
                    _inner_class_types = {"license_fee": LicenseFee}

                partial_period_behaviors: List[PartialPeriodBehavior]
                """
                Override for the partial period behavior.
                """
                _inner_class_types = {
                    "partial_period_behaviors": PartialPeriodBehavior,
                }

            component_configurations: List[ComponentConfiguration]
            """
            Configurations for the components of the Pricing Plan.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            overrides: Optional[Overrides]
            """
            Allows users to override the partial period behavior.
            """
            pricing_plan: str
            """
            ID of the Pricing Plan to subscribe to.
            """
            pricing_plan_subscription: Optional[str]
            """
            ID of the created Pricing Plan Subscription. This is only present once the Billing Intent is committed and the Pricing Plan Subscription is created.
            """
            pricing_plan_version: str
            """
            Version of the Pricing Plan to use.
            """
            _inner_class_types = {
                "component_configurations": ComponentConfiguration,
                "overrides": Overrides,
            }

        class V1SubscriptionDetails(StripeObject):
            class Item(StripeObject):
                metadata: Optional[Dict[str, str]]
                """
                Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
                """
                price: str
                """
                The ID of the price object.
                """
                quantity: Optional[int]
                """
                Quantity for this item. If not provided, will default to 1.
                """

            description: Optional[str]
            """
            The subscription's description, meant to be displayable to the customer.
            Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
            """
            items: List[Item]
            """
            A list of up to 20 subscription items, each with an attached price.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            _inner_class_types = {"items": Item}

        collect_at: Literal["next_billing_date", "on_effective_at"]
        """
        Allows users to override the collect at behavior.
        """
        effective_at: EffectiveAt
        """
        When the subscribe action will take effect. If not specified, the default behavior is on_reserve.
        """
        pricing_plan_subscription_details: Optional[
            PricingPlanSubscriptionDetails
        ]
        """
        Details for subscribing to a Pricing Plan.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """
        v1_subscription_details: Optional[V1SubscriptionDetails]
        """
        Details for subscribing to a V1 subscription.
        """
        _inner_class_types = {
            "effective_at": EffectiveAt,
            "pricing_plan_subscription_details": PricingPlanSubscriptionDetails,
            "v1_subscription_details": V1SubscriptionDetails,
        }

    apply: Optional[Apply]
    """
    Details for an apply action.
    """
    created: str
    """
    Time at which the object was created.
    """
    deactivate: Optional[Deactivate]
    """
    Details for a deactivate action.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    modify: Optional[Modify]
    """
    Details for a modify action.
    """
    object: Literal["v2.billing.intent_action"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    remove: Optional[Remove]
    """
    Details for a remove action.
    """
    subscribe: Optional[Subscribe]
    """
    Details for a subscribe action.
    """
    type: Literal["apply", "deactivate", "modify", "remove", "subscribe"]
    """
    Type of the Billing Intent Action.
    """
    _inner_class_types = {
        "apply": Apply,
        "deactivate": Deactivate,
        "modify": Modify,
        "remove": Remove,
        "subscribe": Subscribe,
    }
