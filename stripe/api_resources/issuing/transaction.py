# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.authorization import Authorization
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.dispute import Dispute
    from stripe.api_resources.issuing.token import Token


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
    created: int
    currency: str
    dispute: Optional[ExpandableField["Dispute"]]
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: StripeObject
    metadata: Dict[str, str]
    object: Literal["issuing.transaction"]
    purchase_details: Optional[StripeObject]
    token: Optional[ExpandableField["Token"]]
    treasury: Optional[StripeObject]
    type: Literal["capture", "refund"]
    wallet: Optional[Literal["apple_pay", "google_pay", "samsung_pay"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def modify(cls, id, **params: Any) -> "Transaction":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Transaction",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Transaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["Transaction"]):
        _resource_cls: Type["Transaction"]

        @classmethod
        def create_force_capture(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
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
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
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
            transaction: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
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
        def refund(self, idempotency_key: Optional[str] = None, **params: Any):
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
