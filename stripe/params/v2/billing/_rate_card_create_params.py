# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class RateCardCreateParams(TypedDict):
    currency: str
    """
    The currency of this RateCard.
    """
    display_name: str
    """
    A customer-facing name for the RateCard.
    This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular RateCard. Maximum length of 200 characters.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    service_interval: Literal["day", "month", "week", "year"]
    """
    The interval for assessing service. For example, a monthly RateCard with a rate of 1 USD for the first 10 "workloads"
    and 2 USD thereafter means "1 USD per workload up to 10 workloads during a month of service." This is similar to but
    distinct from billing interval; the service interval deals with the rate at which the customer accumulates fees,
    while the billing interval in Cadence deals with the rate the customer is billed.
    """
    service_interval_count: int
    """
    The length of the interval for assessing service. For example, set this to 3 and `service_interval` to `"month"`
    to specify quarterly service.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The tax behavior for Stripe Tax — whether the rate card price includes or excludes tax.
    """
