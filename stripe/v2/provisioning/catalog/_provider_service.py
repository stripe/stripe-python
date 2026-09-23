# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning.catalog._provider_list_params import (
        ProviderListParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.provisioning._provider import Provider


class ProviderService(StripeService):
    def list(
        self,
        params: Optional["ProviderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Provider]":
        """
        Lists providers available in the catalog.
        """
        return cast(
            "ListObject[Provider]",
            self._request(
                "get",
                "/v2/provisioning/catalog/providers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ProviderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Provider]":
        """
        Lists providers available in the catalog.
        """
        return cast(
            "ListObject[Provider]",
            await self._request_async(
                "get",
                "/v2/provisioning/catalog/providers",
                base_address="api",
                params=params,
                options=options,
            ),
        )
