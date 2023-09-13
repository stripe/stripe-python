# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal
from typing_extensions import Type

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
    network_data: Optional[StripeObject]
    object: Literal["issuing.transaction"]
    purchase_details: Optional[StripeObject]
    treasury: Optional[StripeObject]
    type: str
    wallet: Optional[str]

    class TestHelpers(APIResourceTestHelpers["Transaction"]):
        _resource_cls: Type["Transaction"]

        @classmethod
        def create_force_capture(
            cls,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/create_force_capture",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def create_unlinked_refund(
            cls,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/create_unlinked_refund",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def _cls_refund(
            cls,
            transaction,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/{transaction}/refund".format(
                    transaction=util.sanitize_id(transaction)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_refund")
        def refund(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/transactions/{transaction}/refund".format(
                    transaction=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Transaction.TestHelpers._resource_cls = Transaction
