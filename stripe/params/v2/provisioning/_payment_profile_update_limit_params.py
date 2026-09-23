# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentProfileUpdateLimitParams(TypedDict):
    livemode: NotRequired[bool]
    """
    Whether the billing operation should use Stripe live-mode objects. When omitted, this
    resolves from the authenticated request context.
    """
    provider: NotRequired[str]
    """
    Provider to update the usage limit for.
    """
    usage_limits: "PaymentProfileUpdateLimitParamsUsageLimits"
    """
    New usage limit to apply.
    """


class PaymentProfileUpdateLimitParamsUsageLimits(TypedDict):
    currency: str
    """
    Three-letter ISO currency code for `max_amount`.
    """
    max_amount: int
    """
    Maximum amount that can be charged per recurring interval.
    """
    recurring_interval: Literal["month", "week", "year"]
    """
    Interval over which `max_amount` applies.
    """
