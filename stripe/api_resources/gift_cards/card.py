# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Card(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    """
    A gift card represents a single gift card owned by a customer, including the
    remaining balance, gift card code, and whether or not it is active.
    """

    OBJECT_NAME = "gift_cards.card"

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
