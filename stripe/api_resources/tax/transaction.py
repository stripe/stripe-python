# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResource


class Transaction(APIResource):
    """
    A Tax transaction records the tax collected from or refunded to your customer.
    """

    OBJECT_NAME = "tax.transaction"

    @classmethod
    def create_from_calculation(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_from_calculation",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

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

    @classmethod
    def _cls_list_line_items(
        cls,
        transaction,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(transaction)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
