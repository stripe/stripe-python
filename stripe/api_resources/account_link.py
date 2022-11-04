# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource


class AccountLink(CreateableAPIResource):
    """
    Account Links are the means by which a Connect platform grants a connected account permission to access
    Stripe-hosted applications, such as Connect Onboarding.

    Related guide: [Connect Onboarding](https://stripe.com/docs/connect/connect-onboarding).
    """

    OBJECT_NAME = "account_link"
