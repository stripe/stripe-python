# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._pricing_plan_version import PricingPlanVersion
from typing import cast
from typing_extensions import NotRequired, TypedDict


class VersionService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        pricing_plan_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlanVersion]:
        """
        List all Pricing Plan Versions of a Pricing Plan.
        """
        return cast(
            ListObject[PricingPlanVersion],
            self._request(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/versions".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        pricing_plan_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlanVersion]:
        """
        List all Pricing Plan Versions of a Pricing Plan.
        """
        return cast(
            ListObject[PricingPlanVersion],
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/versions".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        pricing_plan_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanVersion:
        """
        Retrieve a specific Pricing Plan Version of a Pricing Plan.
        """
        return cast(
            PricingPlanVersion,
            self._request(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/versions/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        pricing_plan_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanVersion:
        """
        Retrieve a specific Pricing Plan Version of a Pricing Plan.
        """
        return cast(
            PricingPlanVersion,
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/versions/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
