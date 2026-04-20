# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.test_helpers.shared_payment._granted_token_create_params import (
        GrantedTokenCreateParams,
    )
    from stripe.params.test_helpers.shared_payment._granted_token_revoke_params import (
        GrantedTokenRevokeParams,
    )
    from stripe.shared_payment._granted_token import GrantedToken


class GrantedTokenService(StripeService):
    def create(
        self,
        params: "GrantedTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Creates a new test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to create SharedPaymentGrantedTokens for testing their integration
        """
        return cast(
            "GrantedToken",
            self._request(
                "post",
                "/v1/test_helpers/shared_payment/granted_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "GrantedTokenCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Creates a new test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to create SharedPaymentGrantedTokens for testing their integration
        """
        return cast(
            "GrantedToken",
            await self._request_async(
                "post",
                "/v1/test_helpers/shared_payment/granted_tokens",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def revoke(
        self,
        shared_payment_granted_token: str,
        params: Optional["GrantedTokenRevokeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
        """
        return cast(
            "GrantedToken",
            self._request(
                "post",
                "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                    shared_payment_granted_token=sanitize_id(
                        shared_payment_granted_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def revoke_async(
        self,
        shared_payment_granted_token: str,
        params: Optional["GrantedTokenRevokeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
        """
        return cast(
            "GrantedToken",
            await self._request_async(
                "post",
                "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                    shared_payment_granted_token=sanitize_id(
                        shared_payment_granted_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
