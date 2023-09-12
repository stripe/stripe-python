# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Optional, cast
from typing_extensions import Literal


class Secret(CreateableAPIResource["Secret"], ListableAPIResource["Secret"]):
    """
    Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

    The primary resource in Secret Store is a `secret`. Other apps can't view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

    All Dashboard users and the app backend share `account` scoped secrets. Use the `account` scope for secrets that don't change per-user, like a third-party API key.

    A `user` scoped secret is accessible by the app backend and one specific Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

    Related guide: [Store data between page reloads](https://stripe.com/docs/stripe-apps/store-auth-data-custom-objects)
    """

    OBJECT_NAME = "apps.secret"
    created: int
    deleted: bool
    expires_at: Optional[int]
    id: str
    livemode: bool
    name: str
    object: Literal["apps.secret"]
    payload: Optional[str]
    scope: StripeObject

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> "Secret":
        return cast(
            "Secret",
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
    def delete_where(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "post",
            "/v1/apps/secrets/delete",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def find(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "get",
            "/v1/apps/secrets/find",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["Secret"]:
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
