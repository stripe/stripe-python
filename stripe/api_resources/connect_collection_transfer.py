# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Any
from typing_extensions import Literal


class ConnectCollectionTransfer(StripeObject):
    OBJECT_NAME = "connect_collection_transfer"
    amount: int
    currency: str
    destination: Any
    id: str
    livemode: bool
    object: Literal["connect_collection_transfer"]
