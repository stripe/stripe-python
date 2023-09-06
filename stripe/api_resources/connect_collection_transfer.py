# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account


class ConnectCollectionTransfer(StripeObject):
    OBJECT_NAME = "connect_collection_transfer"
    amount: int
    currency: str
    destination: ExpandableField["Account"]
    id: str
    livemode: bool
    object: Literal["connect_collection_transfer"]
