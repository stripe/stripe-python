# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.billing_portal.configuration import Configuration


class Session(CreateableAPIResource["Session"]):
    """
    The Billing customer portal is a Stripe-hosted UI for subscription and
    billing management.

    A portal configuration describes the functionality and features that you
    want to provide to your customers through the portal.

    A portal session describes the instantiation of the customer portal for
    a particular customer. By visiting the session's URL, the customer
    can manage their subscriptions and billing details. For security reasons,
    sessions are short-lived and will expire if the customer does not visit the URL.
    Create sessions on-demand when customers intend to manage their subscriptions
    and billing details.

    Learn more in the [integration guide](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal).
    """

    OBJECT_NAME = "billing_portal.session"
    configuration: ExpandableField["Configuration"]
    created: str
    customer: str
    flow: Optional[StripeObject]
    id: str
    livemode: bool
    locale: Optional[str]
    object: Literal["billing_portal.session"]
    on_behalf_of: Optional[str]
    return_url: Optional[str]
    url: str
