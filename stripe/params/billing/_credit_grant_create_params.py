# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class CreditGrantCreateParams(RequestOptions):
    amount: "CreditGrantCreateParamsAmount"
    """
    Amount of this credit grant.
    """
    applicability_config: "CreditGrantCreateParamsApplicabilityConfig"
    """
    Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
    """
    category: Literal["paid", "promotional"]
    """
    The category of this credit grant.
    """
    customer: NotRequired[str]
    """
    ID of the customer to receive the billing credits.
    """
    customer_account: NotRequired[str]
    """
    ID of the account to receive the billing credits.
    """
    effective_at: NotRequired[int]
    """
    The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    expires_at: NotRequired[int]
    """
    The time when the billing credits expire. If not specified, the billing credits don't expire.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
    """
    name: NotRequired[str]
    """
    A descriptive name shown in the Dashboard.
    """
    priority: NotRequired[int]
    """
    The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
    """


class CreditGrantCreateParamsAmount(TypedDict):
    custom_pricing_unit: NotRequired[
        "CreditGrantCreateParamsAmountCustomPricingUnit"
    ]
    """
    The custom pricing unit amount.
    """
    monetary: NotRequired["CreditGrantCreateParamsAmountMonetary"]
    """
    The monetary amount.
    """
    type: Literal["custom_pricing_unit", "monetary"]
    """
    The type of this amount. We currently only support `monetary` billing credits.
    """


class CreditGrantCreateParamsAmountCustomPricingUnit(TypedDict):
    id: str
    """
    The ID of the custom pricing unit.
    """
    value: str
    """
    A positive integer representing the amount of the credit grant.
    """


class CreditGrantCreateParamsAmountMonetary(TypedDict):
    currency: str
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `value` parameter.
    """
    value: int
    """
    A positive integer representing the amount of the credit grant.
    """


class CreditGrantCreateParamsApplicabilityConfig(TypedDict):
    scope: "CreditGrantCreateParamsApplicabilityConfigScope"
    """
    Specify the scope of this applicability config.
    """


class CreditGrantCreateParamsApplicabilityConfigScope(TypedDict):
    billable_items: NotRequired[
        List["CreditGrantCreateParamsApplicabilityConfigScopeBillableItem"]
    ]
    """
    A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.
    """
    price_type: NotRequired[Literal["metered"]]
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
    """
    prices: NotRequired[
        List["CreditGrantCreateParamsApplicabilityConfigScopePrice"]
    ]
    """
    A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.
    """


class CreditGrantCreateParamsApplicabilityConfigScopeBillableItem(TypedDict):
    id: str
    """
    The billable item ID this credit grant should apply to.
    """


class CreditGrantCreateParamsApplicabilityConfigScopePrice(TypedDict):
    id: str
    """
    The price ID this credit grant should apply to.
    """
