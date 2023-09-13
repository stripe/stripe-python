# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.financial_connections.account_owner import (
        AccountOwner,
    )


class AccountOwnership(StripeObject):
    """
    Describes a snapshot of the owners of an account at a particular point in time.
    """

    OBJECT_NAME = "financial_connections.account_ownership"
    created: str
    id: str
    object: Literal["financial_connections.account_ownership"]
    owners: ListObject["AccountOwner"]
