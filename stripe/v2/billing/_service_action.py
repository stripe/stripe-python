# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._custom_pricing_unit import (
        CustomPricingUnit as V2BillingCustomPricingUnitResource,
    )


class ServiceAction(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.service_action"]] = (
        "v2.billing.service_action"
    )

    class CreditGrant(StripeObject):
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

            class Monetary(StripeObject):
                currency: Optional[str]
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: Optional[int]
                """
                A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
                """

            custom_pricing_unit: Optional[CustomPricingUnit]
            """
            The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
            """
            monetary: Optional[Monetary]
            """
            The monetary amount of the credit grant. Required if `type` is `monetary`.
            """
            type: Literal["custom_pricing_unit", "monetary"]
            """
            The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
            """
            _inner_class_types = {
                "custom_pricing_unit": CustomPricingUnit,
                "monetary": Monetary,
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
        category: Optional[Literal["paid", "promotional"]]
        """
        The category of the credit grant.
        """
        expiry_config: ExpiryConfig
        """
        The expiry configuration for the credit grant.
        """
        name: str
        """
        A descriptive name shown in dashboard.
        """
        priority: Optional[int]
        """
        The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
        """
        _inner_class_types = {
            "amount": Amount,
            "applicability_config": ApplicabilityConfig,
            "expiry_config": ExpiryConfig,
        }

    class CreditGrantPerTenant(StripeObject):
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

            class Monetary(StripeObject):
                currency: Optional[str]
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: Optional[int]
                """
                A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
                """

            custom_pricing_unit: Optional[CustomPricingUnit]
            """
            The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
            """
            monetary: Optional[Monetary]
            """
            The monetary amount of the credit grant. Required if `type` is `monetary`.
            """
            type: Literal["custom_pricing_unit", "monetary"]
            """
            The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
            """
            _inner_class_types = {
                "custom_pricing_unit": CustomPricingUnit,
                "monetary": Monetary,
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
        category: Optional[Literal["paid", "promotional"]]
        """
        The category of the credit grant.
        """
        expiry_config: ExpiryConfig
        """
        The expiry configuration for the credit grant.
        """
        name: str
        """
        Customer-facing name for the credit grant.
        """
        priority: Optional[int]
        """
        The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
        """
        _inner_class_types = {
            "amount": Amount,
            "applicability_config": ApplicabilityConfig,
            "expiry_config": ExpiryConfig,
        }

    created: str
    """
    Timestamp of when the object was created.
    """
    credit_grant: Optional[CreditGrant]
    """
    Details for the credit grant. Provided only if `type` is "credit_grant".
    """
    credit_grant_per_tenant: Optional[CreditGrantPerTenant]
    """
    Details for the credit grant per tenant. Provided only if `type` is "credit_grant_per_tenant".
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for this service action.
    """
    object: Literal["v2.billing.service_action"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    service_interval: Literal["day", "month", "week", "year"]
    """
    The interval for assessing service.
    """
    service_interval_count: int
    """
    The length of the interval for assessing service.
    """
    type: Literal["credit_grant", "credit_grant_per_tenant"]
    """
    The type of the service action.
    """
    _inner_class_types = {
        "credit_grant": CreditGrant,
        "credit_grant_per_tenant": CreditGrantPerTenant,
    }
