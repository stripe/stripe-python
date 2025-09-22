# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2.core._claimable_sandbox import ClaimableSandbox
from typing import Optional, cast
from typing_extensions import NotRequired, TypedDict


class ClaimableSandboxService(StripeService):
    class CreateParams(TypedDict):
        enable_mcp_access: bool
        """
        If true, returns a key that can be used with [Stripe's MCP server](https://docs.stripe.com/mcp).
        """
        prefill: "ClaimableSandboxService.CreateParamsPrefill"
        """
        Values that are prefilled when a user claims the sandbox.
        """

    class CreateParamsPrefill(TypedDict):
        country: str
        """
        Country in which the account holder resides, or in which the business is legally established.
        Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        email: str
        """
        Email that this sandbox is meant to be claimed by. Stripe will
        notify this email address before the sandbox expires.
        """
        name: NotRequired[str]
        """
        Name for the sandbox. If not provided, this will be generated.
        """

    def create(
        self,
        params: "ClaimableSandboxService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> ClaimableSandbox:
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            ClaimableSandbox,
            self._request(
                "post",
                "/v2/core/claimable_sandboxes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ClaimableSandboxService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> ClaimableSandbox:
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            ClaimableSandbox,
            await self._request_async(
                "post",
                "/v2/core/claimable_sandboxes",
                base_address="api",
                params=params,
                options=options,
            ),
        )
