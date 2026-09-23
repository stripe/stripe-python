# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._provider_connection_request_create_params import (
        ProviderConnectionRequestCreateParams,
    )
    from stripe.params.v2.provisioning._provider_connection_request_retrieve_params import (
        ProviderConnectionRequestRetrieveParams,
    )
    from stripe.params.v2.provisioning._provider_connection_request_submit_information_params import (
        ProviderConnectionRequestSubmitInformationParams,
    )
    from stripe.v2.provisioning._provider_connection_request import (
        ProviderConnectionRequest,
    )


class ProviderConnectionRequestService(StripeService):
    def create(
        self,
        params: "ProviderConnectionRequestCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Creates a new provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            self._request(
                "post",
                "/v2/provisioning/provider_connection_requests",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ProviderConnectionRequestCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Creates a new provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            await self._request_async(
                "post",
                "/v2/provisioning/provider_connection_requests",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["ProviderConnectionRequestRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Retrieves a provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            self._request(
                "get",
                "/v2/provisioning/provider_connection_requests/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["ProviderConnectionRequestRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Retrieves a provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            await self._request_async(
                "get",
                "/v2/provisioning/provider_connection_requests/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit_information(
        self,
        id: str,
        /,
        params: "ProviderConnectionRequestSubmitInformationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Submits additional information requested by the provider for a provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            self._request(
                "post",
                "/v2/provisioning/provider_connection_requests/{id}/submit_information".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_information_async(
        self,
        id: str,
        /,
        params: "ProviderConnectionRequestSubmitInformationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProviderConnectionRequest":
        """
        Submits additional information requested by the provider for a provider connection.
        """
        return cast(
            "ProviderConnectionRequest",
            await self._request_async(
                "post",
                "/v2/provisioning/provider_connection_requests/{id}/submit_information".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
