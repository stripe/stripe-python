# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from typing import Any, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card


class Token(CreateableAPIResource["Token"]):
    """
    Tokenization is the process Stripe uses to collect sensitive card or bank
    account details, or personally identifiable information (PII), directly from
    your customers in a secure manner. A token representing this information is
    returned to your server to use. Use our
    [recommended payments integrations](https://stripe.com/docs/payments) to perform this process
    on the client-side. This guarantees that no sensitive card data touches your server,
    and allows your integration to operate in a PCI-compliant way.

    If you can't use client-side tokenization, you can also create tokens using
    the API with either your publishable or secret API key. If
    your integration uses this method, you're responsible for any PCI compliance
    that it might require, and you must keep your secret API key safe. Unlike with
    client-side tokenization, your customer's information isn't sent directly to
    Stripe, so we can't determine how it's handled or stored.

    You can't store or use tokens more than once. To store card or bank account
    information for later use, create [Customer](https://stripe.com/docs/api#customers)
    objects or [Custom accounts](https://stripe.com/docs/api#external_accounts).
    [Radar](https://stripe.com/docs/radar), our integrated solution for automatic fraud protection,
    performs best with integrations that use client-side tokenization.
    """

    OBJECT_NAME = "token"
    bank_account: Optional["BankAccount"]
    card: Optional["Card"]
    client_ip: Optional[str]
    created: int
    id: str
    livemode: bool
    object: Literal["token"]
    type: str
    used: bool

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Token":
        return cast(
            "Token",
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
    ) -> "Token":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
