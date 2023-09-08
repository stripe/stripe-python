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


class CreditReversal(
    CreateableAPIResource["CreditReversal"],
    ListableAPIResource["CreditReversal"],
):
    """
    You can reverse some [ReceivedCredits](https://stripe.com/docs/api#received_credits) depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.
    """

    OBJECT_NAME = "treasury.credit_reversal"
    amount: int
    created: str
    currency: str
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    network: str
    object: Literal["treasury.credit_reversal"]
    received_credit: str
    status: str
    status_transitions: StripeObject
    transaction: Optional[ExpandableField["Transaction"]]
