# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class FinancingTransaction(ListableAPIResource["FinancingTransaction"]):
    """
    This is an object representing the details of a transaction on a Capital financing object.
    """

    OBJECT_NAME = "capital.financing_transaction"
    account: str
    created_at: str
    details: StripeObject
    financing_offer: Optional[str]
    id: str
    legacy_balance_transaction_source: str
    livemode: bool
    object: Literal["capital.financing_transaction"]
    type: Literal["payment", "payout", "reversal"]
    user_facing_description: Optional[str]

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["FinancingTransaction"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "FinancingTransaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance