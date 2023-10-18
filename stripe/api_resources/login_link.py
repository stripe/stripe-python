# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing_extensions import ClassVar, Literal


class LoginLink(StripeObject):
    """
    Login Links are single-use login link for an Express account to access their Stripe dashboard.
    """

    OBJECT_NAME: ClassVar[Literal["login_link"]] = "login_link"
    created: int
    object: Literal["login_link"]
    url: str
