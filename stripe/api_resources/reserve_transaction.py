# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class ReserveTransaction(StripeObject):
    OBJECT_NAME = "reserve_transaction"
    amount: int
    currency: str
    description: Optional[str]
    id: str
    object: Literal["reserve_transaction"]
