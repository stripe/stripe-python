# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.transaction import Transaction


class Authorization(
    ListableAPIResource["Authorization"],
    UpdateableAPIResource["Authorization"],
):
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)
    """

    OBJECT_NAME = "issuing.authorization"
    amount: int
    amount_details: Optional[StripeObject]
    approved: bool
    authorization_method: str
    balance_transactions: List["BalanceTransaction"]
    card: "Card"
    cardholder: Optional[ExpandableField["Cardholder"]]
    created: str
    currency: str
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: StripeObject
    metadata: Dict[str, str]
    network_data: Optional[StripeObject]
    object: Literal["issuing.authorization"]
    pending_request: Optional[StripeObject]
    request_history: List[StripeObject]
    status: str
    transactions: List["Transaction"]
    treasury: Optional[StripeObject]
    verification_data: StripeObject
    wallet: Optional[str]

    @classmethod
    def _cls_approve(
        cls,
        authorization,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_approve")
    def approve(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_decline(
        cls,
        authorization,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_decline")
    def decline(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["Authorization"]:
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
    def modify(cls, id, **params) -> "Authorization":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Authorization",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "Authorization":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
