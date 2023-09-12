# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class Transaction(
    CreateableAPIResource["Transaction"],
    ListableAPIResource["Transaction"],
    UpdateableAPIResource["Transaction"],
):
    """
    A gift card transaction represents a single transaction on a referenced gift card.
    A transaction is in one of three states, `confirmed`, `held` or `canceled`. A `confirmed`
    transaction is one that has added/deducted funds. A `held` transaction has created a
    temporary hold on funds, which can then be cancelled or confirmed. A `held` transaction
    can be confirmed into a `confirmed` transaction, or canceled into a `canceled` transaction.
    A `canceled` transaction has no effect on a gift card's balance.
    """

    OBJECT_NAME = "gift_cards.transaction"
    amount: Optional[int]
    confirmed_at: Optional[str]
    created: Optional[str]
    created_by: Optional[StripeObject]
    currency: Optional[str]
    description: Optional[str]
    gift_card: Optional[str]
    id: str
    metadata: Optional[Dict[str, str]]
    object: Literal["gift_cards.transaction"]
    status: Optional[Literal["canceled", "confirmed", "held", "invalid"]]
    transfer_group: Optional[str]

    @classmethod
    def _cls_cancel(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/transactions/{id}/cancel".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/gift_cards/transactions/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/transactions/{id}/confirm".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/gift_cards/transactions/{id}/confirm".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> "Transaction":
        return cast(
            "Transaction",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["Transaction"]:
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
    def modify(cls, id, **params) -> "Transaction":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Transaction",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "Transaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance