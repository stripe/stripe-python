# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2.core._account_link import AccountLink
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core._account_link_create_params import (
        AccountLinkCreateParams,
    )


class AccountLinkService(StripeService):
    def create(
        self,
        params: "AccountLinkCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> AccountLink:
        """
        Creates an AccountLink object that includes a single-use Stripe URL that the merchant can redirect their user to in order to take them to a Stripe-hosted application such as Recipient Onboarding.
        """
        return cast(
            AccountLink,
            self._request(
                "post",
                "/v2/core/account_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountLinkCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> AccountLink:
        """
        Creates an AccountLink object that includes a single-use Stripe URL that the merchant can redirect their user to in order to take them to a Stripe-hosted application such as Recipient Onboarding.
        """
        return cast(
            AccountLink,
            await self._request_async(
                "post",
                "/v2/core/account_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )
