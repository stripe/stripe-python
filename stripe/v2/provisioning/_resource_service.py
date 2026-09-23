# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._resource_create_params import (
        ResourceCreateParams,
    )
    from stripe.params.v2.provisioning._resource_link_params import (
        ResourceLinkParams,
    )
    from stripe.params.v2.provisioning._resource_remove_params import (
        ResourceRemoveParams,
    )
    from stripe.params.v2.provisioning._resource_retrieve_params import (
        ResourceRetrieveParams,
    )
    from stripe.params.v2.provisioning._resource_rotate_credentials_params import (
        ResourceRotateCredentialsParams,
    )
    from stripe.params.v2.provisioning._resource_submit_information_params import (
        ResourceSubmitInformationParams,
    )
    from stripe.params.v2.provisioning._resource_unlink_params import (
        ResourceUnlinkParams,
    )
    from stripe.params.v2.provisioning._resource_update_params import (
        ResourceUpdateParams,
    )
    from stripe.v2.provisioning._resource import Resource


class ResourceService(StripeService):
    def create(
        self,
        params: "ResourceCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Creates a new provider resource.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ResourceCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Creates a new provider resource.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def link(
        self,
        params: "ResourceLinkParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Links an existing provider resource to a project or account.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/link",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def link_async(
        self,
        params: "ResourceLinkParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Links an existing provider resource to a project or account.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/link",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["ResourceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Retrieves a provider resource.
        """
        return cast(
            "Resource",
            self._request(
                "get",
                "/v2/provisioning/resources/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["ResourceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Retrieves a provider resource.
        """
        return cast(
            "Resource",
            await self._request_async(
                "get",
                "/v2/provisioning/resources/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["ResourceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Updates a resource's configuration or service.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["ResourceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Updates a resource's configuration or service.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def remove(
        self,
        id: str,
        /,
        params: Optional["ResourceRemoveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Removes a resource.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/{id}/remove".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def remove_async(
        self,
        id: str,
        /,
        params: Optional["ResourceRemoveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Removes a resource.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/{id}/remove".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def rotate_credentials(
        self,
        id: str,
        /,
        params: Optional["ResourceRotateCredentialsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Rotates a resource's credentials.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/{id}/rotate_credentials".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def rotate_credentials_async(
        self,
        id: str,
        /,
        params: Optional["ResourceRotateCredentialsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Rotates a resource's credentials.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/{id}/rotate_credentials".format(
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
        params: "ResourceSubmitInformationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Submits additional information requested by the provider for a resource.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/{id}/submit_information".format(
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
        params: "ResourceSubmitInformationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Submits additional information requested by the provider for a resource.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/{id}/submit_information".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def unlink(
        self,
        id: str,
        /,
        params: Optional["ResourceUnlinkParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Unlinks a resource without removing it from the provider.
        """
        return cast(
            "Resource",
            self._request(
                "post",
                "/v2/provisioning/resources/{id}/unlink".format(
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
        params: Optional["ResourceUnlinkParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Resource":
        """
        Unlinks a resource without removing it from the provider.
        """
        return cast(
            "Resource",
            await self._request_async(
                "post",
                "/v2/provisioning/resources/{id}/unlink".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
