# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject


class AccountOwnership(StripeObject):
    """
    Describes a snapshot of the owners of an account at a particular point in time.
    """

    OBJECT_NAME = "financial_connections.account_ownership"
