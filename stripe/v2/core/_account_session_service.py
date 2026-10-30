# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._account_session_create_params import (
        AccountSessionCreateParams,
    )
    from stripe.v2.core._account_session import AccountSession


class AccountSessionService(StripeService):
    def create(
        self,
        params: "AccountSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSession":
        """
        Create an Account Session.
        """
        return cast(
            "AccountSession",
            self._request(
                "post",
                "/v2/core/account_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSession":
        """
        Create an Account Session.
        """
        return cast(
            "AccountSession",
            await self._request_async(
                "post",
                "/v2/core/account_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )
