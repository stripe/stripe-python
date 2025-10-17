# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.pricing_plans._version_list_params import (
        VersionListParams,
    )
    from stripe.params.v2.billing.pricing_plans._version_retrieve_params import (
        VersionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._pricing_plan_version import PricingPlanVersion


class VersionService(StripeService):
    def list(
        self,
        pricing_plan_id: str,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlanVersion]":
        """
        List all Pricing Plan Versions of a Pricing Plan.
        """
        return cast(
            "ListObject[PricingPlanVersion]",
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
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlanVersion]":
        """
        List all Pricing Plan Versions of a Pricing Plan.
        """
        return cast(
            "ListObject[PricingPlanVersion]",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanVersion":
        """
        Retrieve a specific Pricing Plan Version of a Pricing Plan.
        """
        return cast(
            "PricingPlanVersion",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanVersion":
        """
        Retrieve a specific Pricing Plan Version of a Pricing Plan.
        """
        return cast(
            "PricingPlanVersion",
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
