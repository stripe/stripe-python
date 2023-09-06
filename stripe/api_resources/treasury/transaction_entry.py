# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class TransactionEntry(ListableAPIResource["TransactionEntry"]):
    """
    TransactionEntries represent individual units of money movements within a single [Transaction](https://stripe.com/docs/api#transactions).
    """

    OBJECT_NAME = "treasury.transaction_entry"
    balance_impact: StripeObject
    created: str
    currency: str
    effective_at: str
    financial_account: str
    flow: Optional[str]
    flow_details: Optional[StripeObject]
    flow_type: str
    id: str
    livemode: bool
    object: Literal["treasury.transaction_entry"]
    transaction: ExpandableField["Transaction"]
    type: str

    @classmethod
    def class_url(cls):
        return "/v1/treasury/transaction_entries"
