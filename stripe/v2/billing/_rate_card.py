# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class RateCard(StripeObject):
    """
    A Rate Card represents a versioned set of usage-based prices (rates). Each rate is associated with one Metered Item and
    defines how much to charge for usage of that item. After you've set up a RateCard, you can subscribe customers to it
    by creating a Rate Card Subscription.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.rate_card"]] = (
        "v2.billing.rate_card"
    )
    active: bool
    """
    Whether this RateCard is active. Inactive RateCards cannot be used in new activations or have new rates added.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    display_name: str
    """
    A customer-facing name for the Rate Card.
    This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
    Maximum length of 250 characters.
    """
    id: str
    """
    Unique identifier for the object.
    """
    latest_version: str
    """
    The ID of this rate card's most recently created version.
    """
    live_version: str
    """
    The ID of the Rate Card Version that will be used by all subscriptions when no specific version is specified.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular RateCard. Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.rate_card"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    service_interval: Literal["day", "month", "week", "year"]
    """
    The interval for assessing service. For example, a monthly Rate Card with a rate of $1 for the first 10 "workloads"
    and $2 thereafter means "$1 per workload up to 10 workloads during a month of service." This is similar to but
    distinct from billing interval; the service interval deals with the rate at which the customer accumulates fees,
    while the billing interval in Cadence deals with the rate the customer is billed.
    """
    service_interval_count: int
    """
    The length of the interval for assessing service. For example, set this to 3 and `service_interval` to `"month"` in
    order to specify quarterly service.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The Stripe Tax tax behavior - whether the rates are inclusive or exclusive of tax.
    """
