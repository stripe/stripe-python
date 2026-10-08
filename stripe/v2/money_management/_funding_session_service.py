# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._funding_session_create_params import (
        FundingSessionCreateParams,
    )
    from stripe.v2.money_management._funding_session import FundingSession


class FundingSessionService(StripeService):
    def create(
        self,
        params: "FundingSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingSession":
        """
        Create a FundingSession: a hosted funding surface for a customer to fund a FinancialAccount.
        """
        return cast(
            "FundingSession",
            self._request(
                "post",
                "/v2/money_management/funding_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FundingSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingSession":
        """
        Create a FundingSession: a hosted funding surface for a customer to fund a FinancialAccount.
        """
        return cast(
            "FundingSession",
            await self._request_async(
                "post",
                "/v2/money_management/funding_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )
