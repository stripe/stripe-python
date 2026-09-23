# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._provider_connection_list_params import (
        ProviderConnectionListParams,
    )
    from stripe.params.v2.provisioning._provider_connection_unlink_params import (
        ProviderConnectionUnlinkParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.provisioning._provider_connection import ProviderConnection


class ProviderConnectionService(StripeService):
    def list(
        self,
        params: Optional["ProviderConnectionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProviderConnection]":
        """
        Lists the provider connections for the account.
        """
        return cast(
            "ListObject[ProviderConnection]",
            self._request(
                "get",
                "/v2/provisioning/provider_connections",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ProviderConnectionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProviderConnection]":
        """
        Lists the provider connections for the account.
        """
        return cast(
            "ListObject[ProviderConnection]",
            await self._request_async(
                "get",
                "/v2/provisioning/provider_connections",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def unlink(
        self,
        id: str,
        /,
        params: Optional["ProviderConnectionUnlinkParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnection":
        """
        Unlinks a provider connection so it can no longer be used to create resources.
        """
        return cast(
            "ProviderConnection",
            self._request(
                "post",
                "/v2/provisioning/provider_connections/{id}/unlink".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def unlink_async(
        self,
        id: str,
        /,
        params: Optional["ProviderConnectionUnlinkParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnection":
        """
        Unlinks a provider connection so it can no longer be used to create resources.
        """
        return cast(
            "ProviderConnection",
            await self._request_async(
                "post",
                "/v2/provisioning/provider_connections/{id}/unlink".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
