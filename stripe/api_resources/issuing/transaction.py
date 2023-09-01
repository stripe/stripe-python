# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import Optional
from typing_extensions import Literal


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
    authorization: Optional[Any]
    balance_transaction: Optional[Any]
    card: Any
    cardholder: Optional[Any]
    created: str
    currency: str
    dispute: Optional[Any]
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
