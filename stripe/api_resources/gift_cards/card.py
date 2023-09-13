# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.gift_cards.transaction import Transaction


class Card(
    CreateableAPIResource["Card"],
    ListableAPIResource["Card"],
    UpdateableAPIResource["Card"],
):
    """
    A gift card represents a single gift card owned by a customer, including the
    remaining balance, gift card code, and whether or not it is active.
    """

    OBJECT_NAME = "gift_cards.card"
    active: bool
    amount_available: int
    amount_held: int
    code: Optional[str]
    created: str
    created_by: Optional[StripeObject]
    currency: str
    id: str
    metadata: Optional[Dict[str, str]]
    object: Literal["gift_cards.card"]
    transactions: ListObject["Transaction"]

    @classmethod
    def validate(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/cards/validate",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
