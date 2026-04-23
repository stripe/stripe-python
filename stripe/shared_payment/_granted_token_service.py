# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.shared_payment._granted_token_retrieve_params import (
        GrantedTokenRetrieveParams,
    )
    from stripe.shared_payment._granted_token import GrantedToken


class GrantedTokenService(StripeService):
    def retrieve(
        self,
        shared_payment_granted_token: str,
        params: Optional["GrantedTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Retrieves an existing SharedPaymentGrantedToken object
        """
        return cast(
            "GrantedToken",
            self._request(
                "get",
                "/v1/shared_payment/granted_tokens/{shared_payment_granted_token}".format(
                    shared_payment_granted_token=sanitize_id(
                        shared_payment_granted_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        shared_payment_granted_token: str,
        params: Optional["GrantedTokenRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GrantedToken":
        """
        Retrieves an existing SharedPaymentGrantedToken object
        """
        return cast(
            "GrantedToken",
            await self._request_async(
                "get",
                "/v1/shared_payment/granted_tokens/{shared_payment_granted_token}".format(
                    shared_payment_granted_token=sanitize_id(
                        shared_payment_granted_token
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
