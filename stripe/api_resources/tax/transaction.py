# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource


class Transaction(CreateableAPIResource):
    """
    A Tax `Transaction` records the tax collected from or refunded to your customer.
    """

    OBJECT_NAME = "tax.transaction"

    @classmethod
    def create_reversal(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_reversal",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
