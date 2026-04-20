# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.shared_payment._issued_token_create_params import (
        IssuedTokenCreateParams,
    )
    from stripe.params.shared_payment._issued_token_retrieve_params import (
        IssuedTokenRetrieveParams,
    )
    from stripe.params.shared_payment._issued_token_revoke_params import (
        IssuedTokenRevokeParams,
    )
    from stripe.shared_payment._issued_token import IssuedToken


class IssuedTokenService(StripeService):
    def retrieve(
        self,
        shared_payment_issued_token: str,
        params: Optional["IssuedTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Retrieves an existing SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            self._request(
                "get",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        shared_payment_issued_token: str,
        params: Optional["IssuedTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Retrieves an existing SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            await self._request_async(
                "get",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "IssuedTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Creates a new SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            self._request(
                "post",
                "/v1/shared_payment/issued_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "IssuedTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Creates a new SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            await self._request_async(
                "post",
                "/v1/shared_payment/issued_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def revoke(
        self,
        shared_payment_issued_token: str,
        params: Optional["IssuedTokenRevokeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            self._request(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def revoke_async(
        self,
        shared_payment_issued_token: str,
        params: Optional["IssuedTokenRevokeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            await self._request_async(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
