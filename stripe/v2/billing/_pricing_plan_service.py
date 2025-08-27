# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._pricing_plan import PricingPlan
from stripe.v2.billing.pricing_plans._component_service import ComponentService
from stripe.v2.billing.pricing_plans._version_service import VersionService
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.components = ComponentService(self._requestor)
        self.versions = VersionService(self._requestor)

    class CreateParams(TypedDict):
        currency: str
        """
        The currency of the PricingPlan.
        """
        description: NotRequired[str]
        """
        Description of pricing plan subscription.
        """
        display_name: str
        """
        Display name of the PricingPlan. Maximum 250 characters.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular PricingPlan. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        tax_behavior: Literal["exclusive", "inclusive"]
        """
        The Stripe Tax tax behavior - whether the PricingPlan is inclusive or exclusive of tax.
        """

    class ListParams(TypedDict):
        active: NotRequired[bool]
        """
        Filter for active/inactive PricingPlans. Mutually exclusive with `lookup_keys`.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Filter by lookup keys. Mutually exclusive with `active`.
        You can specify up to 10 lookup keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        active: NotRequired[bool]
        """
        Whether the PricingPlan is active.
        """
        description: NotRequired[str]
        """
        Description of pricing plan subscription.
        """
        display_name: NotRequired[str]
        """
        Display name of the PricingPlan. Maximum 250 characters.
        """
        live_version: NotRequired[str]
        """
        The ID of the live version of the PricingPlan.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular PricingPlan. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object.
        """

    def list(
        self,
        params: "PricingPlanService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlan]:
        """
        List all Pricing Plan objects.
        """
        return cast(
            ListObject[PricingPlan],
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
        params: "PricingPlanService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlan]:
        """
        List all Pricing Plan objects.
        """
        return cast(
            ListObject[PricingPlan],
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
        params: "PricingPlanService.CreateParams",
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Create a Pricing Plan object.
        """
        return cast(
            PricingPlan,
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
        params: "PricingPlanService.CreateParams",
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Create a Pricing Plan object.
        """
        return cast(
            PricingPlan,
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
        params: "PricingPlanService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Retrieve a Pricing Plan object.
        """
        return cast(
            PricingPlan,
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
        params: "PricingPlanService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Retrieve a Pricing Plan object.
        """
        return cast(
            PricingPlan,
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
        params: "PricingPlanService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Update a Pricing Plan object.
        """
        return cast(
            PricingPlan,
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
        params: "PricingPlanService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlan:
        """
        Update a Pricing Plan object.
        """
        return cast(
            PricingPlan,
            await self._request_async(
                "post",
                "/v2/billing/pricing_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
