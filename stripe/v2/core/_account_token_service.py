# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._account_token_create_params import (
        AccountTokenCreateParams,
    )
    from stripe.params.v2.core._account_token_retrieve_params import (
        AccountTokenRetrieveParams,
    )
    from stripe.v2.core._account_token import AccountToken


class AccountTokenService(StripeService):
    def create(
        self,
        params: Optional["AccountTokenCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountToken":
        """
        Create an account token with a publishable key and pass it to the Accounts v2 API to
        create or update an account without its data touching your server.
        Learn more about [account tokens](https://docs.stripe.com/connect/account-tokens).
        In live mode, you can only create account tokens with your application's publishable key.
        In test mode, you can create account tokens with your secret key or publishable key.
        """
        return cast(
            "AccountToken",
            self._request(
                "post",
                "/v2/core/account_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["AccountTokenCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountToken":
        """
        Create an account token with a publishable key and pass it to the Accounts v2 API to
        create or update an account without its data touching your server.
        Learn more about [account tokens](https://docs.stripe.com/connect/account-tokens).
        In live mode, you can only create account tokens with your application's publishable key.
        In test mode, you can create account tokens with your secret key or publishable key.
        """
        return cast(
            "AccountToken",
            await self._request_async(
                "post",
                "/v2/core/account_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AccountTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountToken":
        """
        Retrieves an Account Token.
        """
        return cast(
            "AccountToken",
            self._request(
                "get",
                "/v2/core/account_tokens/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AccountTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountToken":
        """
        Retrieves an Account Token.
        """
        return cast(
            "AccountToken",
            await self._request_async(
                "get",
                "/v2/core/account_tokens/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
