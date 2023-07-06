# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource


class CustomerSession(CreateableAPIResource):
    """
    A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
    control over a customer.
    """

    OBJECT_NAME = "customer_session"
