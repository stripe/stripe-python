# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.crypto._customer_payment_token import CustomerPaymentToken
    from stripe.params.crypto._customer_payment_token_list_params import (
        CustomerPaymentTokenListParams,
    )


class CustomerPaymentTokenService(StripeService):
    def list(
        self,
        id: str,
        params: Optional["CustomerPaymentTokenListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerPaymentToken]":
        """
        Lists the Payment Tokens for a Crypto Customer.
        """
        return cast(
            "ListObject[CustomerPaymentToken]",
            self._request(
                "get",
                "/v1/crypto/customers/{id}/payment_tokens".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        params: Optional["CustomerPaymentTokenListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerPaymentToken]":
        """
        Lists the Payment Tokens for a Crypto Customer.
        """
        return cast(
            "ListObject[CustomerPaymentToken]",
            await self._request_async(
                "get",
                "/v1/crypto/customers/{id}/payment_tokens".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
