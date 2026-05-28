# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing_extensions import Literal, NotRequired


class SubscriptionItemDeleteParams(RequestOptions):
    clear_usage: NotRequired[bool]
    """
    Delete all usage for the given subscription item. Allowed only when the current plan's `usage_type` is `metered`.
    """
    payment_behavior: NotRequired[
        Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ]
    """
    Controls how Stripe handles payment when a subscription update requires payment and `collection_method=charge_automatically`.
    """
    proration_behavior: NotRequired[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://docs.stripe.com/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """
    proration_date: NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://docs.stripe.com/api/invoices/create_preview) endpoint.
    """
