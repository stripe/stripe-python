# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._customer_entitlement_summary import CustomerEntitlementSummary
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class CustomerEntitlementSummaryService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        customer: str,
        params: "CustomerEntitlementSummaryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CustomerEntitlementSummary:
        """
        Retrieve the entitlement summary for a customer
        """
        return cast(
            CustomerEntitlementSummary,
            self._request(
                "get",
                "/v1/customers/{customer}/entitlement_summary".format(
                    customer=sanitize_id(customer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        customer: str,
        params: "CustomerEntitlementSummaryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CustomerEntitlementSummary:
        """
        Retrieve the entitlement summary for a customer
        """
        return cast(
            CustomerEntitlementSummary,
            await self._request_async(
                "get",
                "/v1/customers/{customer}/entitlement_summary".format(
                    customer=sanitize_id(customer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
