# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.capital._financing_summary import FinancingSummary
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class FinancingSummaryService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        params: "FinancingSummaryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingSummary:
        """
        Retrieve the financing state for the account that was authenticated in the request.
        """
        return cast(
            FinancingSummary,
            self._request(
                "get",
                "/v1/capital/financing_summary",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: "FinancingSummaryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingSummary:
        """
        Retrieve the financing state for the account that was authenticated in the request.
        """
        return cast(
            FinancingSummary,
            await self._request_async(
                "get",
                "/v1/capital/financing_summary",
                base_address="api",
                params=params,
                options=options,
            ),
        )
