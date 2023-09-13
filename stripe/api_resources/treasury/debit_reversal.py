# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class DebitReversal(
    CreateableAPIResource["DebitReversal"],
    ListableAPIResource["DebitReversal"],
):
    """
    You can reverse some [ReceivedDebits](https://stripe.com/docs/api#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.
    """

    OBJECT_NAME = "treasury.debit_reversal"
    amount: int
    created: str
    currency: str
    financial_account: Optional[str]
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    linked_flows: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    network: str
    object: Literal["treasury.debit_reversal"]
    received_debit: str
    status: str
    status_transitions: StripeObject
    transaction: Optional[ExpandableField["Transaction"]]
