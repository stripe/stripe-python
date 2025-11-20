# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ServiceActionCreateParams(TypedDict):
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for this service action. Maximum length of 200 characters.
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
    credit_grant: NotRequired["ServiceActionCreateParamsCreditGrant"]
    """
    Details for the credit grant. Required if `type` is `credit_grant`.
    """
    credit_grant_per_tenant: NotRequired[
        "ServiceActionCreateParamsCreditGrantPerTenant"
    ]
    """
    Details for the credit grant per tenant. Required if `type` is `credit_grant_per_tenant`.
    """


class ServiceActionCreateParamsCreditGrant(TypedDict):
    amount: "ServiceActionCreateParamsCreditGrantAmount"
    """
    The amount of the credit grant.
    """
    applicability_config: (
        "ServiceActionCreateParamsCreditGrantApplicabilityConfig"
    )
    """
    Defines the scope where the credit grant is applicable.
    """
    category: NotRequired[Literal["paid", "promotional"]]
    """
    The category of the credit grant.
    """
    expiry_config: "ServiceActionCreateParamsCreditGrantExpiryConfig"
    """
    The expiry configuration for the credit grant.
    """
    name: str
    """
    A descriptive name shown in dashboard.
    """
    priority: NotRequired[int]
    """
    The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
    """


class ServiceActionCreateParamsCreditGrantAmount(TypedDict):
    type: Literal["custom_pricing_unit", "monetary"]
    """
    The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
    """
    custom_pricing_unit: NotRequired[
        "ServiceActionCreateParamsCreditGrantAmountCustomPricingUnit"
    ]
    """
    The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
    """
    monetary: NotRequired["ServiceActionCreateParamsCreditGrantAmountMonetary"]
    """
    The monetary amount of the credit grant. Required if `type` is `monetary`.
    """


class ServiceActionCreateParamsCreditGrantAmountCustomPricingUnit(TypedDict):
    id: str
    """
    The id of the custom pricing unit.
    """
    value: str
    """
    The value of the credit grant, decimal value represented as a string.
    """


class ServiceActionCreateParamsCreditGrantAmountMonetary(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class ServiceActionCreateParamsCreditGrantApplicabilityConfig(TypedDict):
    scope: "ServiceActionCreateParamsCreditGrantApplicabilityConfigScope"
    """
    The applicability scope of the credit grant.
    """


class ServiceActionCreateParamsCreditGrantApplicabilityConfigScope(TypedDict):
    billable_items: NotRequired[List[str]]
    """
    The billable items to apply the credit grant to.
    """
    price_type: NotRequired[Literal["metered"]]
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
    """


class ServiceActionCreateParamsCreditGrantExpiryConfig(TypedDict):
    type: Literal["end_of_service_period"]
    """
    The type of the expiry configuration. We currently support `end_of_service_period`.
    """


class ServiceActionCreateParamsCreditGrantPerTenant(TypedDict):
    amount: "ServiceActionCreateParamsCreditGrantPerTenantAmount"
    """
    The amount of the credit grant.
    """
    applicability_config: (
        "ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfig"
    )
    """
    Defines the scope where the credit grant is applicable.
    """
    category: NotRequired[Literal["paid", "promotional"]]
    """
    The category of the credit grant.
    """
    expiry_config: "ServiceActionCreateParamsCreditGrantPerTenantExpiryConfig"
    """
    The expiry configuration for the credit grant.
    """
    grant_condition: (
        "ServiceActionCreateParamsCreditGrantPerTenantGrantCondition"
    )
    """
    The grant condition for the credit grant.
    """
    name: str
    """
    Customer-facing name for the credit grant.
    """
    priority: NotRequired[int]
    """
    The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
    """


class ServiceActionCreateParamsCreditGrantPerTenantAmount(TypedDict):
    type: Literal["custom_pricing_unit", "monetary"]
    """
    The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
    """
    custom_pricing_unit: NotRequired[
        "ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit"
    ]
    """
    The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
    """
    monetary: NotRequired[
        "ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary"
    ]
    """
    The monetary amount of the credit grant. Required if `type` is `monetary`.
    """


class ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit(
    TypedDict,
):
    id: str
    """
    The id of the custom pricing unit.
    """
    value: str
    """
    The value of the credit grant, decimal value represented as a string.
    """


class ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfig(
    TypedDict,
):
    scope: (
        "ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfigScope"
    )
    """
    The applicability scope of the credit grant.
    """


class ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfigScope(
    TypedDict,
):
    billable_items: NotRequired[List[str]]
    """
    The billable items to apply the credit grant to.
    """
    price_type: NotRequired[Literal["metered"]]
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
    """


class ServiceActionCreateParamsCreditGrantPerTenantExpiryConfig(TypedDict):
    type: Literal["end_of_service_period"]
    """
    The type of the expiry configuration. We currently support `end_of_service_period`.
    """


class ServiceActionCreateParamsCreditGrantPerTenantGrantCondition(TypedDict):
    type: Literal["meter_event_first_per_period"]
    """
    The type of the grant condition. We currently support `meter_event_first_per_period`.
    """
    meter_event_first_per_period: NotRequired[
        "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod"
    ]
    """
    The grant condition for the meter event first per period.
    """


class ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod(
    TypedDict,
):
    meter_segment_conditions: List[
        "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition"
    ]
    """
    The meter segment conditions for the grant condition.
    """


class ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition(
    TypedDict,
):
    type: Literal["dimension"]
    """
    The type of the meter segment condition. We currently support `dimension`.
    """
    dimension: NotRequired[
        "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension"
    ]
    """
    Dimension-based meter segment condition.
    """


class ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension(
    TypedDict,
):
    payload_key: str
    """
    The payload key for the dimension.
    """
    value: str
    """
    The value for the dimension.
    """
