# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.billing._credit_balance_summary import CreditBalanceSummary
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CreditBalanceSummaryService(StripeService):
    class RetrieveParams(TypedDict):
        customer: str
        """
        The customer for which to fetch credit balance summary.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        filter: "CreditBalanceSummaryService.RetrieveParamsFilter"
        """
        The filter criteria for the credit balance summary.
        """

    class RetrieveParamsFilter(TypedDict):
        applicability_scope: NotRequired[
            "CreditBalanceSummaryService.RetrieveParamsFilterApplicabilityScope"
        ]
        """
        The billing credit applicability scope for which to fetch credit balance summary.
        """
        credit_grant: NotRequired[str]
        """
        The credit grant for which to fetch credit balance summary.
        """
        type: Literal["applicability_scope", "credit_grant"]
        """
        Specify the type of this filter.
        """

    class RetrieveParamsFilterApplicabilityScope(TypedDict):
        price_type: Literal["metered"]
        """
        The price type that credit grants can apply to. We currently only support the `metered` price type.
        """

    def retrieve(
        self,
        params: "CreditBalanceSummaryService.RetrieveParams",
        options: RequestOptions = {},
    ) -> CreditBalanceSummary:
        """
        Retrieves the credit balance summary for a customer.
        """
        return cast(
            CreditBalanceSummary,
            self._request(
                "get",
                "/v1/billing/credit_balance_summary",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: "CreditBalanceSummaryService.RetrieveParams",
        options: RequestOptions = {},
    ) -> CreditBalanceSummary:
        """
        Retrieves the credit balance summary for a customer.
        """
        return cast(
            CreditBalanceSummary,
            await self._request_async(
                "get",
                "/v1/billing/credit_balance_summary",
                base_address="api",
                params=params,
                options=options,
            ),
        )
