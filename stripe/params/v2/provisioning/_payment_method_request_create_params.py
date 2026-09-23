# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentMethodRequestCreateParams(TypedDict):
    livemode: NotRequired[bool]
    """
    Whether the billing operation should use Stripe live-mode objects. When omitted, this
    resolves from the authenticated request context.
    """
    payment_method_owner: NotRequired[Literal["platform"]]
    """
    Owner of the requested payment method.
    """
    source_account: NotRequired[str]
    """
    Connected account to source the payment method from.
    """
    source_customer: NotRequired[str]
    """
    Customer to source the payment method from.
    """
    source_payment_method: NotRequired[str]
    """
    Existing payment method to reuse instead of collecting a new one.
    """
    usage_limits: NotRequired["PaymentMethodRequestCreateParamsUsageLimits"]
    """
    Usage limit to apply to the requested payment method.
    """


class PaymentMethodRequestCreateParamsUsageLimits(TypedDict):
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
