# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanSubscriptionListParams(TypedDict):
    billing_cadence: NotRequired[str]
    """
    Filter by Billing Cadence ID. Mutually exclusive with `payer`, `pricing_plan`, and `pricing_plan_version`.
    """
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    payer: NotRequired["PricingPlanSubscriptionListParamsPayer"]
    """
    Filter by payer. Mutually exclusive with `billing_cadence`, `pricing_plan`, and `pricing_plan_version`.
    """
    pricing_plan: NotRequired[str]
    """
    Filter by PricingPlan ID. Mutually exlcusive with `billing_cadence`, `payer`, and `pricing_plan_version`.
    """
    pricing_plan_version: NotRequired[str]
    """
    Filter by Pricing Plan Version ID. Mutually exlcusive with `billing_cadence`, `payer`, and `pricing_plan`.
    """
    servicing_status: NotRequired[
        Literal["active", "canceled", "paused", "pending"]
    ]
    """
    Filter by servicing status.
    """


class PricingPlanSubscriptionListParamsPayer(TypedDict):
    customer: NotRequired[str]
    """
    The ID of the Customer object. If provided, only Pricing Plan Subscriptions that are subscribed on the cadences with the specified payer will be returned.
    """
    type: Literal["customer"]
    """
    A string identifying the type of the payer. Currently the only supported value is `customer`.
    """
