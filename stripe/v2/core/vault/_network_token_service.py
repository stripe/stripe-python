# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core.vault._network_token_create_from_credential_params import (
        NetworkTokenCreateFromCredentialParams,
    )
    from stripe.params.v2.core.vault._network_token_create_params import (
        NetworkTokenCreateParams,
    )
    from stripe.params.v2.core.vault._network_token_generate_cryptogram_params import (
        NetworkTokenGenerateCryptogramParams,
    )
    from stripe.params.v2.core.vault._network_token_retrieve_params import (
        NetworkTokenRetrieveParams,
    )
    from stripe.v2.core.vault._network_token import NetworkToken


class NetworkTokenService(StripeService):
    def create(
        self,
        params: "NetworkTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Creates or returns a NetworkToken from raw card data for POST /v2/core/vault/network_tokens.
        """
        return cast(
            "NetworkToken",
            self._request(
                "post",
                "/v2/core/vault/network_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "NetworkTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Creates or returns a NetworkToken from raw card data for POST /v2/core/vault/network_tokens.
        """
        return cast(
            "NetworkToken",
            await self._request_async(
                "post",
                "/v2/core/vault/network_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_credential(
        self,
        params: "NetworkTokenCreateFromCredentialParams",
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Creates or returns a NetworkToken from an existing card reference for POST /v2/core/vault/network_tokens/create_from_credential.
        """
        return cast(
            "NetworkToken",
            self._request(
                "post",
                "/v2/core/vault/network_tokens/create_from_credential",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_credential_async(
        self,
        params: "NetworkTokenCreateFromCredentialParams",
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Creates or returns a NetworkToken from an existing card reference for POST /v2/core/vault/network_tokens/create_from_credential.
        """
        return cast(
            "NetworkToken",
            await self._request_async(
                "post",
                "/v2/core/vault/network_tokens/create_from_credential",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["NetworkTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Retrieves the persisted NetworkToken projection for GET /v2/core/vault/network_tokens/:id.
        """
        return cast(
            "NetworkToken",
            self._request(
                "get",
                "/v2/core/vault/network_tokens/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["NetworkTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Retrieves the persisted NetworkToken projection for GET /v2/core/vault/network_tokens/:id.
        """
        return cast(
            "NetworkToken",
            await self._request_async(
                "get",
                "/v2/core/vault/network_tokens/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def generate_cryptogram(
        self,
        id: str,
        /,
        params: Optional["NetworkTokenGenerateCryptogramParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Generates a single-use cryptogram for POST /v2/core/vault/network_tokens/:id/generate_cryptogram.
        Every successful call generates a new cryptogram, and retrying can generate another cryptogram.
        The cryptogram is returned only in this response and is never persisted.
        """
        return cast(
            "NetworkToken",
            self._request(
                "post",
                "/v2/core/vault/network_tokens/{id}/generate_cryptogram".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def generate_cryptogram_async(
        self,
        id: str,
        /,
        params: Optional["NetworkTokenGenerateCryptogramParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "NetworkToken":
        """
        Generates a single-use cryptogram for POST /v2/core/vault/network_tokens/:id/generate_cryptogram.
        Every successful call generates a new cryptogram, and retrying can generate another cryptogram.
        The cryptogram is returned only in this response and is never persisted.
        """
        return cast(
            "NetworkToken",
            await self._request_async(
                "post",
                "/v2/core/vault/network_tokens/{id}/generate_cryptogram".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
