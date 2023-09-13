# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from typing import Optional, cast
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
    returned to your server to use. You should use our
    [recommended payments integrations](https://stripe.com/docs/payments) to perform this process
    client-side. This ensures that no sensitive card data touches your server,
    and allows your integration to operate in a PCI-compliant way.

    If you cannot use client-side tokenization, you can also create tokens using
    the API with either your publishable or secret API key. Keep in mind that if
    your integration uses this method, you are responsible for any PCI compliance
    that may be required, and you must keep your secret API key safe. Unlike with
    client-side tokenization, your customer's information is not sent directly to
    Stripe, so we cannot determine how it is handled or stored.

    Tokens cannot be stored or used more than once. To store card or bank account
    information for later use, you can create [Customer](https://stripe.com/docs/api#customers)
    objects or [Custom accounts](https://stripe.com/docs/api#external_accounts). Note that
    [Radar](https://stripe.com/docs/radar), our integrated solution for automatic fraud protection,
    performs best with integrations that use client-side tokenization.
    """

    OBJECT_NAME = "token"
    bank_account: "BankAccount"
    card: "Card"
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
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def retrieve(cls, id, api_key=None, **params) -> "Token":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
