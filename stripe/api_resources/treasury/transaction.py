# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction_entry import (
        TransactionEntry,
    )


class Transaction(ListableAPIResource["Transaction"]):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME = "treasury.transaction"
    amount: int
    balance_impact: StripeObject
    created: str
    currency: str
    description: str
    entries: Optional[ListObject["TransactionEntry"]]
    financial_account: str
    flow: Optional[str]
    flow_details: Optional[StripeObject]
    flow_type: str
    id: str
    livemode: bool
    object: Literal["treasury.transaction"]
    status: str
    status_transitions: StripeObject
