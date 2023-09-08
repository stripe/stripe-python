# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class FinancingTransaction(ListableAPIResource["FinancingTransaction"]):
    """
    This is an object representing the details of a transaction on a Capital financing object.
    """

    OBJECT_NAME = "capital.financing_transaction"
    account: str
    created_at: str
    details: StripeObject
    financing_offer: Optional[str]
    id: str
    legacy_balance_transaction_source: str
    livemode: bool
    object: Literal["capital.financing_transaction"]
    type: str
    user_facing_description: Optional[str]
