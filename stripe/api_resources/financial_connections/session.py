# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.financial_connections.account import Account


class Session(CreateableAPIResource["Session"]):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    OBJECT_NAME = "financial_connections.session"
    account_holder: Optional[StripeObject]
    accounts: ListObject["Account"]
    client_secret: str
    filters: Optional[StripeObject]
    id: str
    livemode: bool
    object: Literal["financial_connections.session"]
    permissions: List[
        Literal["balances", "ownership", "payment_method", "transactions"]
    ]
    prefetch: Optional[List[Literal["balances", "ownership"]]]
    return_url: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Session":
        return cast(
            "Session",
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
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Session":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
