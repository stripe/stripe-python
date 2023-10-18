# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class AccountOwner(StripeObject):
    """
    Describes an owner of an account.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account_owner"]
    ] = "financial_connections.account_owner"
    email: Optional[str]
    id: str
    name: str
    object: Literal["financial_connections.account_owner"]
    ownership: str
    phone: Optional[str]
    raw_address: Optional[str]
    refreshed_at: Optional[int]
