# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.pricing_plans._component_create_params import (
        ComponentCreateParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_delete_params import (
        ComponentDeleteParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_list_params import (
        ComponentListParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_retrieve_params import (
        ComponentRetrieveParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_update_params import (
        ComponentUpdateParams,
    )
    from stripe.v2._deleted_object import DeletedObject
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._pricing_plan_component import PricingPlanComponent


class ComponentService(StripeService):
    def list(
        self,
        pricing_plan_id: str,
        params: Optional["ComponentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlanComponent]":
        """
        List all Pricing Plan Component objects for a Pricing Plan.
        """
        return cast(
            "ListObject[PricingPlanComponent]",
            self._request(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components".format(
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
        params: Optional["ComponentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlanComponent]":
        """
        List all Pricing Plan Component objects for a Pricing Plan.
        """
        return cast(
            "ListObject[PricingPlanComponent]",
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        pricing_plan_id: str,
        params: "ComponentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Create a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            self._request(
                "post",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        pricing_plan_id: str,
        params: "ComponentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Create a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            await self._request_async(
                "post",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def delete(
        self,
        pricing_plan_id: str,
        id: str,
        params: Optional["ComponentDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Remove a Pricing Plan Component from the latest version of a Pricing Plan.
        """
        return cast(
            "DeletedObject",
            self._request(
                "delete",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        pricing_plan_id: str,
        id: str,
        params: Optional["ComponentDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Remove a Pricing Plan Component from the latest version of a Pricing Plan.
        """
        return cast(
            "DeletedObject",
            await self._request_async(
                "delete",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
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
        params: Optional["ComponentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Retrieve a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            self._request(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
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
        params: Optional["ComponentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Retrieve a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        pricing_plan_id: str,
        id: str,
        params: Optional["ComponentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Update a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            self._request(
                "post",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        pricing_plan_id: str,
        id: str,
        params: Optional["ComponentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanComponent":
        """
        Update a Pricing Plan Component object.
        """
        return cast(
            "PricingPlanComponent",
            await self._request_async(
                "post",
                "/v2/billing/pricing_plans/{pricing_plan_id}/components/{id}".format(
                    pricing_plan_id=sanitize_id(pricing_plan_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
