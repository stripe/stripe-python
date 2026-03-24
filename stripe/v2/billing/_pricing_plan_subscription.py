# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount as V2AmountResource
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._custom_pricing_unit import (
        CustomPricingUnit as V2BillingCustomPricingUnitResource,
    )


class PricingPlanSubscription(StripeObject):
    """
    A Pricing Plan Subscription represents a customer's active subscription to a Pricing Plan. It tracks both the servicing
    status (whether the customer is receiving service) and collection status (whether payments are current). Subscriptions
    are created through Billing Intents and bill according to the associated Billing Cadence.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.pricing_plan_subscription"]] = (
        "v2.billing.pricing_plan_subscription"
    )

    class CancellationDetails(StripeObject):
        comment: Optional[str]
        """
        Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
        """
        feedback: Optional[
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
        reason: Optional[Literal["cancellation_requested"]]
        """
        System-generated reason for cancellation.
        """

    class CollectionStatusTransitions(StripeObject):
        awaiting_customer_action_at: Optional[str]
        """
        When the collection status transitioned to awaiting customer action.
        """
        current_at: Optional[str]
        """
        When the collection status transitioned to current.
        """
        past_due_at: Optional[str]
        """
        When the collection status transitioned to past due.
        """
        paused_at: Optional[str]
        """
        When the collection status transitioned to paused.
        """
        unpaid_at: Optional[str]
        """
        When the collection status transitioned to unpaid.
        """

    class DiscountDetail(StripeObject):
        class Source(StripeObject):
            coupon: Optional[str]
            """
            The ID of the Coupon.
            """
            type: Literal["coupon"]
            """
            Type of the Discount source.
            """

        discount: str
        """
        The ID of the Discount.
        """
        end: Optional[str]
        """
        The time at which the Discount ends, if applicable.
        """
        promotion_code: Optional[str]
        """
        The ID of the PromotionCode, if applicable.
        """
        source: Source
        """
        The source of the Discount.
        """
        start: str
        """
        The time at which the Discount starts.
        """
        _inner_class_types = {"source": Source}

    class PricingPlanComponentDetail(StripeObject):
        class LicenseFeeDetails(StripeObject):
            class ServiceCycle(StripeObject):
                interval: Literal["day", "month", "week", "year"]
                """
                The interval for assessing service.
                """
                interval_count: int
                """
                The length of the interval for assessing service. For example, set this to 3 and `interval` to `"month"` in
                order to specify quarterly service.
                """

            class Tier(StripeObject):
                flat_amount: Optional[str]
                """
                Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
                """
                unit_amount: Optional[str]
                """
                Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
                most 12 decimal places.
                """
                up_to_decimal: Optional[str]
                """
                Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
                be set.
                """
                up_to_inf: Optional[Literal["inf"]]
                """
                No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
                """

            class TransformQuantity(StripeObject):
                divide_by: int
                """
                Divide usage by this number.
                """
                round: Literal["down", "up"]
                """
                After division, round the result up or down.
                """
                _field_encodings = {"divide_by": "int64_string"}

            currency: str
            """
            Three-letter ISO currency code, in lowercase.
            """
            display_name: str
            """
            A customer-facing name for the license fee.
            """
            license_fee: str
            """
            The ID of the License Fee.
            """
            license_fee_version: str
            """
            The ID of the License Fee Version.
            """
            quantity: int
            """
            Quantity of the license fee on the subscription.
            """
            service_cycle: ServiceCycle
            """
            The service cycle configuration.
            """
            tiering_mode: Optional[Literal["graduated", "volume"]]
            """
            Defines whether the tiering price should be graduated or volume-based.
            """
            tiers: List[Tier]
            """
            Each element represents a pricing tier.
            """
            transform_quantity: Optional[TransformQuantity]
            """
            Apply a transformation to the reported usage or set quantity before computing the amount billed.
            """
            unit_amount: Optional[str]
            """
            The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal places.
            """
            unit_label: Optional[str]
            """
            The unit label from the licensed item, used for display purposes (e.g. "seat", "environment").
            """
            _inner_class_types = {
                "service_cycle": ServiceCycle,
                "tiers": Tier,
                "transform_quantity": TransformQuantity,
            }

        class RateCardDetails(StripeObject):
            class ServiceCycle(StripeObject):
                interval: Literal["day", "month", "week", "year"]
                """
                The interval for assessing service.
                """
                interval_count: int
                """
                The length of the interval for assessing service. For example, set this to 3 and `interval` to `"month"` in
                order to specify quarterly service.
                """

            currency: str
            """
            Three-letter ISO currency code, in lowercase.
            """
            display_name: str
            """
            A customer-facing name for the rate card.
            """
            rate_card: str
            """
            The ID of the Rate Card.
            """
            rate_card_version: str
            """
            The ID of the Rate Card Version.
            """
            service_cycle: ServiceCycle
            """
            The service cycle configuration.
            """
            tax_behavior: Literal["exclusive", "inclusive"]
            """
            Whether the rates are inclusive or exclusive of tax.
            """
            _inner_class_types = {"service_cycle": ServiceCycle}

        class RecurringCreditGrantDetails(StripeObject):
            class CreditGrantDetails(StripeObject):
                class Amount(StripeObject):
                    class CustomPricingUnit(StripeObject):
                        custom_pricing_unit_details: Optional[
                            "V2BillingCustomPricingUnitResource"
                        ]
                        """
                        The Custom Pricing Unit object.
                        """
                        id: str
                        """
                        The id of the custom pricing unit.
                        """
                        value: str
                        """
                        The value of the credit grant, decimal value represented as a string.
                        """

                    custom_pricing_unit: Optional[CustomPricingUnit]
                    """
                    The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
                    """
                    monetary: Optional[V2AmountResource]
                    """
                    The monetary amount of the credit grant. Required if `type` is `monetary`.
                    """
                    type: Literal["custom_pricing_unit", "monetary"]
                    """
                    The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
                    """
                    _inner_class_types = {
                        "custom_pricing_unit": CustomPricingUnit,
                    }

                class ApplicabilityConfig(StripeObject):
                    class Scope(StripeObject):
                        billable_items: Optional[List[str]]
                        """
                        The billable items to apply the credit grant to.
                        """
                        price_type: Optional[Literal["metered"]]
                        """
                        The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
                        """

                    scope: Scope
                    """
                    The applicability scope of the credit grant.
                    """
                    _inner_class_types = {"scope": Scope}

                class ExpiryConfig(StripeObject):
                    type: Literal["end_of_service_period"]
                    """
                    The type of the expiry configuration. We currently support `end_of_service_period`.
                    """

                amount: Amount
                """
                The amount of the credit grant.
                """
                applicability_config: ApplicabilityConfig
                """
                Defines the scope where the credit grant is applicable.
                """
                expiry_config: ExpiryConfig
                """
                The expiry configuration for the credit grant.
                """
                _inner_class_types = {
                    "amount": Amount,
                    "applicability_config": ApplicabilityConfig,
                    "expiry_config": ExpiryConfig,
                }

            class CreditGrantPerTenantDetails(StripeObject):
                class Amount(StripeObject):
                    class CustomPricingUnit(StripeObject):
                        custom_pricing_unit_details: Optional[
                            "V2BillingCustomPricingUnitResource"
                        ]
                        """
                        The Custom Pricing Unit object.
                        """
                        id: str
                        """
                        The id of the custom pricing unit.
                        """
                        value: str
                        """
                        The value of the credit grant, decimal value represented as a string.
                        """

                    custom_pricing_unit: Optional[CustomPricingUnit]
                    """
                    The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
                    """
                    monetary: Optional[V2AmountResource]
                    """
                    The monetary amount of the credit grant. Required if `type` is `monetary`.
                    """
                    type: Literal["custom_pricing_unit", "monetary"]
                    """
                    The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
                    """
                    _inner_class_types = {
                        "custom_pricing_unit": CustomPricingUnit,
                    }

                class ApplicabilityConfig(StripeObject):
                    class Scope(StripeObject):
                        billable_items: Optional[List[str]]
                        """
                        The billable items to apply the credit grant to.
                        """
                        price_type: Optional[Literal["metered"]]
                        """
                        The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
                        """

                    scope: Scope
                    """
                    The applicability scope of the credit grant.
                    """
                    _inner_class_types = {"scope": Scope}

                class ExpiryConfig(StripeObject):
                    type: Literal["end_of_service_period"]
                    """
                    The type of the expiry configuration. We currently support `end_of_service_period`.
                    """

                amount: Amount
                """
                The amount of the credit grant.
                """
                applicability_config: ApplicabilityConfig
                """
                Defines the scope where the credit grant is applicable.
                """
                expiry_config: ExpiryConfig
                """
                The expiry configuration for the credit grant.
                """
                _inner_class_types = {
                    "amount": Amount,
                    "applicability_config": ApplicabilityConfig,
                    "expiry_config": ExpiryConfig,
                }

            class ServiceCycle(StripeObject):
                interval: Literal["day", "month", "week", "year"]
                """
                The interval for assessing service.
                """
                interval_count: int
                """
                The length of the interval for assessing service. For example, set this to 3 and `interval` to `"month"` in
                order to specify quarterly service.
                """

            credit_grant_details: Optional[CreditGrantDetails]
            """
            Credit grant details, present when type is CREDIT_GRANT.
            """
            credit_grant_per_tenant_details: Optional[
                CreditGrantPerTenantDetails
            ]
            """
            Credit grant per tenant details, present when type is CREDIT_GRANT_PER_TENANT.
            """
            recurring_credit_grant: str
            """
            The ID of the Recurring Credit Grant.
            """
            service_cycle: ServiceCycle
            """
            The service cycle configuration.
            """
            type: Literal["credit_grant", "credit_grant_per_tenant"]
            """
            The type of the recurring credit grant.
            """
            _inner_class_types = {
                "credit_grant_details": CreditGrantDetails,
                "credit_grant_per_tenant_details": CreditGrantPerTenantDetails,
                "service_cycle": ServiceCycle,
            }

        license_fee_details: Optional[LicenseFeeDetails]
        """
        License fee details, present when type is license_fee_details.
        """
        pricing_plan_component: str
        """
        The ID of the Pricing Plan Component.
        """
        rate_card_details: Optional[RateCardDetails]
        """
        Rate card details, present when type is rate_card_details.
        """
        recurring_credit_grant_details: Optional[RecurringCreditGrantDetails]
        """
        Recurring credit grant details, present when type is recurring_credit_grant_details.
        """
        type: Literal[
            "license_fee_details",
            "rate_card_details",
            "recurring_credit_grant_details",
        ]
        """
        The type of component details included.
        """
        _inner_class_types = {
            "license_fee_details": LicenseFeeDetails,
            "rate_card_details": RateCardDetails,
            "recurring_credit_grant_details": RecurringCreditGrantDetails,
        }

    class ServicingStatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        When the servicing status transitioned to activated.
        """
        canceled_at: Optional[str]
        """
        When the servicing status transitioned to canceled.
        """
        paused_at: Optional[str]
        """
        When the servicing status transitioned to paused.
        """
        will_activate_at: Optional[str]
        """
        When the servicing is scheduled to transition to activate.
        """
        will_cancel_at: Optional[str]
        """
        When the servicing is scheduled to cancel.
        """

    billing_cadence: str
    """
    The ID of the Billing Cadence this subscription is billed on.
    """
    cancellation_details: Optional[CancellationDetails]
    """
    Details about why the subscription was canceled, if applicable. Includes system-generated reason.
    """
    collection_status: Literal[
        "awaiting_customer_action", "current", "past_due", "paused", "unpaid"
    ]
    """
    Current collection status of this subscription.
    """
    collection_status_transitions: CollectionStatusTransitions
    """
    Timestamps for collection status transitions.
    """
    created: str
    """
    Time at which the object was created.
    """
    discount_details: Optional[List[DiscountDetail]]
    """
    Details about Discounts applied to this subscription.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.pricing_plan_subscription"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_plan: str
    """
    The ID of the Pricing Plan for this subscription.
    """
    pricing_plan_component_details: Optional[List[PricingPlanComponentDetail]]
    """
    Pricing plan component details for the subscription, populated when pricing_plan_component_details is included.
    """
    pricing_plan_version: str
    """
    The ID of the Pricing Plan Version for this subscription.
    """
    servicing_status: Literal["active", "canceled", "paused", "pending"]
    """
    Current servicing status of this subscription.
    """
    servicing_status_transitions: ServicingStatusTransitions
    """
    Timestamps for servicing status transitions.
    """
    test_clock: Optional[str]
    """
    The ID of the Test Clock of the associated Billing Cadence, if any.
    """
    _inner_class_types = {
        "cancellation_details": CancellationDetails,
        "collection_status_transitions": CollectionStatusTransitions,
        "discount_details": DiscountDetail,
        "pricing_plan_component_details": PricingPlanComponentDetail,
        "servicing_status_transitions": ServicingStatusTransitions,
    }
