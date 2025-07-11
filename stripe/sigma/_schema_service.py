# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.sigma._schema import Schema
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class SchemaService(StripeService):
    class ListParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        product: NotRequired[Literal["sigma", "stripe_data_pipeline"]]

    def list(
        self,
        params: "SchemaService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Schema]:
        """
        Lists the schemas available to the authorized merchant in Stripe's data products
        """
        return cast(
            ListObject[Schema],
            self._request(
                "get",
                "/v1/sigma/schemas",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "SchemaService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Schema]:
        """
        Lists the schemas available to the authorized merchant in Stripe's data products
        """
        return cast(
            ListObject[Schema],
            await self._request_async(
                "get",
                "/v1/sigma/schemas",
                base_address="api",
                params=params,
                options=options,
            ),
        )
