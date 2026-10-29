# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.data._schema_list_params import SchemaListParams
    from stripe.params.v2.data._schema_retrieve_params import (
        SchemaRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.data._schema import Schema


class SchemaService(StripeService):
    def list(
        self,
        params: Optional["SchemaListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Schema]":
        """
        Returns a list of schemas describing the tables available to query.
        """
        return cast(
            "ListObject[Schema]",
            self._request(
                "get",
                "/v2/data/schemas",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["SchemaListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Schema]":
        """
        Returns a list of schemas describing the tables available to query.
        """
        return cast(
            "ListObject[Schema]",
            await self._request_async(
                "get",
                "/v2/data/schemas",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["SchemaRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Schema":
        """
        Retrieves the schema for a particular table.
        """
        return cast(
            "Schema",
            self._request(
                "get",
                "/v2/data/schemas/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["SchemaRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Schema":
        """
        Retrieves the schema for a particular table.
        """
        return cast(
            "Schema",
            await self._request_async(
                "get",
                "/v2/data/schemas/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
