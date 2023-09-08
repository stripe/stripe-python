# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any
from typing import List
from typing import Optional
from typing_extensions import Literal


class BalanceTransaction(ListableAPIResource["BalanceTransaction"]):
    """
    Balance transactions represent funds moving through your Stripe account.
    They're created for every type of transaction that comes into or flows out of your Stripe account balance.

    Related guide: [Balance transaction types](https://stripe.com/docs/reports/balance-transaction-types)
    """

    OBJECT_NAME = "balance_transaction"
    amount: int
    available_on: str
    created: str
    currency: str
    description: Optional[str]
    exchange_rate: Optional[float]
    fee: int
    fee_details: List[StripeObject]
    id: str
    net: int
    object: Literal["balance_transaction"]
    reporting_category: str
    source: Optional[ExpandableField[Any]]
    status: str
    type: str
