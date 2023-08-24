# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import SingletonAPIResource
from typing import Any
from typing import List
from typing_extensions import Literal


class Balance(SingletonAPIResource["Balance"]):
    """
    This is an object representing your Stripe balance. You can retrieve it to see
    the balance currently on your Stripe account.

    You can also retrieve the balance history, which contains a list of
    [transactions](https://stripe.com/docs/reporting/balance-transaction-types) that contributed to the balance
    (charges, payouts, and so forth).

    The available and pending amounts for each currency are broken down further by
    payment source types.

    Related guide: [Understanding Connect account balances](https://stripe.com/docs/connect/account-balances)
    """

    OBJECT_NAME = "balance"
    available: List[Any]
    connect_reserved: List[Any]
    instant_available: List[Any]
    issuing: Any
    livemode: bool
    object: Literal["balance"]
    pending: List[Any]

    @classmethod
    def class_url(cls):
        return "/v1/balance"
