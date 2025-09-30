# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AlertCreateParams(RequestOptions):
    alert_type: Literal["credit_balance_threshold", "usage_threshold"]
    """
    The type of alert to create.
    """
    credit_balance_threshold: NotRequired[
        "AlertCreateParamsCreditBalanceThreshold"
    ]
    """
    The configuration of the credit balance threshold.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    title: str
    """
    The title of the alert.
    """
    usage_threshold: NotRequired["AlertCreateParamsUsageThreshold"]
    """
    The configuration of the usage threshold.
    """


class AlertCreateParamsCreditBalanceThreshold(TypedDict):
    filters: NotRequired[List["AlertCreateParamsCreditBalanceThresholdFilter"]]
    """
    The filters allows limiting the scope of this credit balance alert. You must specify a customer filter at this time.
    """
    lte: "AlertCreateParamsCreditBalanceThresholdLte"
    """
    Defines at which value the alert will fire.
    """


class AlertCreateParamsCreditBalanceThresholdFilter(TypedDict):
    credit_grants: NotRequired[
        "AlertCreateParamsCreditBalanceThresholdFilterCreditGrants"
    ]
    """
    The credit grants for which to configure the credit balance alert.
    """
    customer: NotRequired[str]
    """
    Limit the scope to this credit balance alert only to this customer.
    """
    type: Literal["customer", "tenant"]
    """
    What type of filter is being applied to this credit balance alert.
    """


class AlertCreateParamsCreditBalanceThresholdFilterCreditGrants(TypedDict):
    applicability_config: "AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfig"
    """
    The applicability configuration for this credit grants filter.
    """


class AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfig(
    TypedDict,
):
    scope: "AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScope"
    """
    Specify the scope of this applicability config.
    """


class AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScope(
    TypedDict,
):
    billable_items: NotRequired[
        List[
            "AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScopeBillableItem"
        ]
    ]
    """
    A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.
    """
    price_type: NotRequired[Literal["metered"]]
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
    """
    prices: NotRequired[
        List[
            "AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScopePrice"
        ]
    ]
    """
    A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.
    """


class AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScopeBillableItem(
    TypedDict,
):
    id: str
    """
    The billable item ID this credit grant should apply to.
    """


class AlertCreateParamsCreditBalanceThresholdFilterCreditGrantsApplicabilityConfigScopePrice(
    TypedDict,
):
    id: str
    """
    The price ID this credit grant should apply to.
    """


class AlertCreateParamsCreditBalanceThresholdLte(TypedDict):
    balance_type: Literal["custom_pricing_unit", "monetary"]
    """
    Specify the type of this balance. We currently only support `monetary` billing credits.
    """
    custom_pricing_unit: NotRequired[
        "AlertCreateParamsCreditBalanceThresholdLteCustomPricingUnit"
    ]
    """
    The custom pricing unit amount.
    """
    monetary: NotRequired["AlertCreateParamsCreditBalanceThresholdLteMonetary"]
    """
    The monetary amount.
    """


class AlertCreateParamsCreditBalanceThresholdLteCustomPricingUnit(TypedDict):
    id: str
    """
    The ID of the custom pricing unit.
    """
    value: str
    """
    A positive decimal string representing the amount of the custom pricing unit threshold.
    """


class AlertCreateParamsCreditBalanceThresholdLteMonetary(TypedDict):
    currency: str
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `value` parameter.
    """
    value: int
    """
    An integer representing the amount of the threshold.
    """


class AlertCreateParamsUsageThreshold(TypedDict):
    filters: NotRequired[List["AlertCreateParamsUsageThresholdFilter"]]
    """
    The filters allows limiting the scope of this usage alert. You can only specify up to one filter at this time.
    """
    gte: int
    """
    Defines at which value the alert will fire.
    """
    meter: str
    """
    The [Billing Meter](https://docs.stripe.com/api/billing/meter) ID whose usage is monitored.
    """
    recurrence: Literal["one_time"]
    """
    Defines how the alert will behave.
    """


class AlertCreateParamsUsageThresholdFilter(TypedDict):
    customer: NotRequired[str]
    """
    Limit the scope to this usage alert only to this customer.
    """
    type: Literal["customer"]
    """
    What type of filter is being applied to this usage alert.
    """
