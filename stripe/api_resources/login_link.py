# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class LoginLink(StripeObject):
    """
    Login Links are single-use login link for an Express account to access their Stripe dashboard.
    """

    OBJECT_NAME = "login_link"
    created: str
    object: Literal["login_link"]
    url: str
