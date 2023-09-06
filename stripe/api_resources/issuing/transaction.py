# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.issuing.authorization import Authorization
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.dispute import Dispute


class Transaction(
    ListableAPIResource["Transaction"],
    UpdateableAPIResource["Transaction"],
):
    """
    Any use of an [issued card](https://stripe.com/docs/issuing) that results in funds entering or leaving
    your Stripe account, such as a completed purchase or refund, is represented by an Issuing
    `Transaction` object.

    Related guide: [Issued card transactions](https://stripe.com/docs/issuing/purchases/transactions)
    """

    OBJECT_NAME = "issuing.transaction"
    amount: int
    amount_details: Optional[StripeObject]
    authorization: Optional[ExpandableField["Authorization"]]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    card: ExpandableField["Card"]
    cardholder: Optional[ExpandableField["Cardholder"]]
    created: str
    currency: str
    dispute: Optional[ExpandableField["Dispute"]]
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: StripeObject
    metadata: Dict[str, str]
    object: Literal["issuing.transaction"]
    purchase_details: Optional[StripeObject]
    treasury: Optional[StripeObject]
    type: str
    wallet: Optional[str]
