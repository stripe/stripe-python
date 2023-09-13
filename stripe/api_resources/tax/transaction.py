# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax.transaction_line_item import (
        TransactionLineItem,
    )


class Transaction(APIResource["Transaction"]):
    """
    A Tax Transaction records the tax collected from or refunded to your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom#tax-transaction)
    """

    OBJECT_NAME = "tax.transaction"
    created: str
    currency: str
    customer: Optional[str]
    customer_details: StripeObject
    id: str
    line_items: Optional[ListObject["TransactionLineItem"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax.transaction"]
    reference: str
    reversal: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    tax_date: str
    type: str

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
