# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._pricing_plan_create_params import (
        PricingPlanCreateParams,
    )
    from stripe.params.v2.billing._pricing_plan_list_params import (
        PricingPlanListParams,
    )
    from stripe.params.v2.billing._pricing_plan_retrieve_params import (
        PricingPlanRetrieveParams,
    )
    from stripe.params.v2.billing._pricing_plan_update_params import (
        PricingPlanUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._pricing_plan import PricingPlan
    from stripe.v2.billing.pricing_plans._component_service import (
        ComponentService,
    )
    from stripe.v2.billing.pricing_plans._version_service import VersionService

_subservices = {
    "components": [
        "stripe.v2.billing.pricing_plans._component_service",
        "ComponentService",
    ],
    "versions": [
        "stripe.v2.billing.pricing_plans._version_service",
        "VersionService",
    ],
}


class PricingPlanService(StripeService):
    components: "ComponentService"
    versions: "VersionService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["PricingPlanListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlan]":
        """
        List all Pricing Plan objects.
        """
        return cast(
            "ListObject[PricingPlan]",
            self._request(
                "get",
                "/v2/billing/pricing_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["PricingPlanListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PricingPlan]":
        """
        List all Pricing Plan objects.
        """
        return cast(
            "ListObject[PricingPlan]",
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "PricingPlanCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Create a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            self._request(
                "post",
                "/v2/billing/pricing_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "PricingPlanCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Create a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            await self._request_async(
                "post",
                "/v2/billing/pricing_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PricingPlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Retrieve a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            self._request(
                "get",
                "/v2/billing/pricing_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["PricingPlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Retrieve a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            await self._request_async(
                "get",
                "/v2/billing/pricing_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["PricingPlanUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Update a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            self._request(
                "post",
                "/v2/billing/pricing_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["PricingPlanUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlan":
        """
        Update a Pricing Plan object.
        """
        return cast(
            "PricingPlan",
            await self._request_async(
                "post",
                "/v2/billing/pricing_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
