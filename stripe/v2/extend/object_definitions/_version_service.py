# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.extend.object_definitions._version_list_params import (
        VersionListParams,
    )
    from stripe.params.v2.extend.object_definitions._version_retrieve_params import (
        VersionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.extend._object_definition_version import (
        ObjectDefinitionVersion,
    )


class VersionService(StripeService):
    def list(
        self,
        object_definition_id: str,
        /,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ObjectDefinitionVersion]":
        """
        Lists a page of object definition versions in descending semantic version order.
        """
        return cast(
            "ListObject[ObjectDefinitionVersion]",
            self._request(
                "get",
                "/v2/extend/object_definitions/{object_definition_id}/versions".format(
                    object_definition_id=sanitize_id(object_definition_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        object_definition_id: str,
        /,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ObjectDefinitionVersion]":
        """
        Lists a page of object definition versions in descending semantic version order.
        """
        return cast(
            "ListObject[ObjectDefinitionVersion]",
            await self._request_async(
                "get",
                "/v2/extend/object_definitions/{object_definition_id}/versions".format(
                    object_definition_id=sanitize_id(object_definition_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        object_definition_id: str,
        id: str,
        /,
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ObjectDefinitionVersion":
        """
        Retrieves an object definition version.
        """
        return cast(
            "ObjectDefinitionVersion",
            self._request(
                "get",
                "/v2/extend/object_definitions/{object_definition_id}/versions/{id}".format(
                    object_definition_id=sanitize_id(object_definition_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        object_definition_id: str,
        id: str,
        /,
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ObjectDefinitionVersion":
        """
        Retrieves an object definition version.
        """
        return cast(
            "ObjectDefinitionVersion",
            await self._request_async(
                "get",
                "/v2/extend/object_definitions/{object_definition_id}/versions/{id}".format(
                    object_definition_id=sanitize_id(object_definition_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
