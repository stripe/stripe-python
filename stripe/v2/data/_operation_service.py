# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.data._operation_search_params import (
        OperationSearchParams,
    )
    from stripe.v2.data._search_result_list import SearchResultList


class OperationService(StripeService):
    def search(
        self,
        params: "OperationSearchParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SearchResultList":
        """
        Resolve a natural-language query into ranked public analytical resources
        (schemas, reports, and metrics) with execution context.
        """
        return cast(
            "SearchResultList",
            self._request(
                "post",
                "/v2/data/operations/search",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def search_async(
        self,
        params: "OperationSearchParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SearchResultList":
        """
        Resolve a natural-language query into ranked public analytical resources
        (schemas, reports, and metrics) with execution context.
        """
        return cast(
            "SearchResultList",
            await self._request_async(
                "post",
                "/v2/data/operations/search",
                base_address="api",
                params=params,
                options=options,
            ),
        )
