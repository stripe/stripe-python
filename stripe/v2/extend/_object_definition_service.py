# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.extend._object_definition_list_params import (
        ObjectDefinitionListParams,
    )
    from stripe.params.v2.extend._object_definition_retrieve_params import (
        ObjectDefinitionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.extend._object_definition import ObjectDefinition
    from stripe.v2.extend.object_definitions._version_service import (
        VersionService,
    )

_subservices = {
    "versions": [
        "stripe.v2.extend.object_definitions._version_service",
        "VersionService",
    ],
}


class ObjectDefinitionService(StripeService):
    versions: "VersionService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["ObjectDefinitionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ObjectDefinition]":
        """
        Lists a page of object definitions.
        """
        return cast(
            "ListObject[ObjectDefinition]",
            self._request(
                "get",
                "/v2/extend/object_definitions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ObjectDefinitionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ObjectDefinition]":
        """
        Lists a page of object definitions.
        """
        return cast(
            "ListObject[ObjectDefinition]",
            await self._request_async(
                "get",
                "/v2/extend/object_definitions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["ObjectDefinitionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ObjectDefinition":
        """
        Retrieves an object definition.
        """
        return cast(
            "ObjectDefinition",
            self._request(
                "get",
                "/v2/extend/object_definitions/{id}".format(
                    id=sanitize_id(id)
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
        params: Optional["ObjectDefinitionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ObjectDefinition":
        """
        Retrieves an object definition.
        """
        return cast(
            "ObjectDefinition",
            await self._request_async(
                "get",
                "/v2/extend/object_definitions/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
