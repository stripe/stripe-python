# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class Transaction(ListableAPIResource["Transaction"]):
    """
    A Transaction represents a real transaction that affects a Financial Connections Account balance.
    """

    OBJECT_NAME = "financial_connections.transaction"
    account: str
    amount: int
    currency: str
    description: str
    id: str
    livemode: bool
    object: Literal["financial_connections.transaction"]
    status: str
    status_transitions: StripeObject
    transacted_at: str
    transaction_refresh: str
    updated: str
