# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.capital._financing_summary import FinancingSummary
    from stripe.params.capital._financing_summary_retrieve_params import (
        FinancingSummaryRetrieveParams,
    )


class FinancingSummaryService(StripeService):
    def retrieve(
        self,
        params: Optional["FinancingSummaryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingSummary":
        """
        Retrieve the financing summary object for the account.
        """
        return cast(
            "FinancingSummary",
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
        params: Optional["FinancingSummaryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingSummary":
        """
        Retrieve the financing summary object for the account.
        """
        return cast(
            "FinancingSummary",
            await self._request_async(
                "get",
                "/v1/capital/financing_summary",
                base_address="api",
                params=params,
                options=options,
            ),
        )
