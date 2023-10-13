# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.financial_connections.account import Account


class Session(CreateableAPIResource["Session"]):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    OBJECT_NAME = "financial_connections.session"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_holder: "Session.CreateParamsAccountHolder"
            expand: NotRequired["List[str]|None"]
            filters: NotRequired["Session.CreateParamsFilters|None"]
            permissions: List[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ]
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'ownership']]|None"
            ]
            return_url: NotRequired["str|None"]

        class CreateParamsFilters(TypedDict):
            countries: List[str]

        class CreateParamsAccountHolder(TypedDict):
            account: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            type: Literal["account", "customer"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
        **params: Unpack["Session.CreateParams"]
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
        cls, id: str, **params: Unpack["Session.RetrieveParams"]
    ) -> "Session":
        instance = cls(id, **params)
        instance.refresh()
        return instance
