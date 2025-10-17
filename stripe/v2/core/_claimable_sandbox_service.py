# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._claimable_sandbox_create_params import (
        ClaimableSandboxCreateParams,
    )
    from stripe.params.v2.core._claimable_sandbox_retrieve_params import (
        ClaimableSandboxRetrieveParams,
    )
    from stripe.v2.core._claimable_sandbox import ClaimableSandbox


class ClaimableSandboxService(StripeService):
    def create(
        self,
        params: "ClaimableSandboxCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ClaimableSandbox":
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            "ClaimableSandbox",
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
        params: "ClaimableSandboxCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ClaimableSandbox":
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            "ClaimableSandbox",
            await self._request_async(
                "post",
                "/v2/core/claimable_sandboxes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ClaimableSandboxRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ClaimableSandbox":
        """
        Retrieves the details of a claimable sandbox that was previously been created.
        Supply the unique claimable sandbox ID that was returned from your creation request,
        and Stripe will return the corresponding sandbox information.
        """
        return cast(
            "ClaimableSandbox",
            self._request(
                "get",
                "/v2/core/claimable_sandboxes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ClaimableSandboxRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ClaimableSandbox":
        """
        Retrieves the details of a claimable sandbox that was previously been created.
        Supply the unique claimable sandbox ID that was returned from your creation request,
        and Stripe will return the corresponding sandbox information.
        """
        return cast(
            "ClaimableSandbox",
            await self._request_async(
                "get",
                "/v2/core/claimable_sandboxes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
