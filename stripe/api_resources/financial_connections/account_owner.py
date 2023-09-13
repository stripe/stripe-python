# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class AccountOwner(StripeObject):
    """
    Describes an owner of an account.
    """

    OBJECT_NAME = "financial_connections.account_owner"
    email: Optional[str]
    id: str
    name: str
    object: Literal["financial_connections.account_owner"]
    ownership: str
    phone: Optional[str]
    raw_address: Optional[str]
    refreshed_at: Optional[str]
