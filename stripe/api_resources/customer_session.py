# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer


class CustomerSession(CreateableAPIResource["CustomerSession"]):
    """
    A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
    control over a customer.
    """

    OBJECT_NAME = "customer_session"
    client_secret: str
    customer: ExpandableField["Customer"]
    expires_at: str
    livemode: bool
    object: Literal["customer_session"]
