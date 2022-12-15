# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Transaction(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
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
