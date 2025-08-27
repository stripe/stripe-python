# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._pricing_plan_component import PricingPlanComponent
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ComponentService(StripeService):
    class CreateParams(TypedDict):
        lookup_key: NotRequired[str]
        """
        An identifier that can be used to find this component.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        type: Literal["license_fee", "rate_card", "service_action"]
        """
        The type of the PricingPlanComponent.
        """
        license_fee: NotRequired["ComponentService.CreateParamsLicenseFee"]
        """
        Details if this component is a License Fee.
        """
        rate_card: NotRequired["ComponentService.CreateParamsRateCard"]
        """
        Details if this component is a Rate Card.
        """
        service_action: NotRequired[
            "ComponentService.CreateParamsServiceAction"
        ]
        """
        Details if this component is a Service Action.
        """

    class CreateParamsLicenseFee(TypedDict):
        id: str
        """
        The ID of the License Fee.
        """
        version: NotRequired[str]
        """
        The version of the LicenseFee. Defaults to 'latest', if not specified.
        """

    class CreateParamsRateCard(TypedDict):
        id: str
        """
        The ID of the Rate Card.
        """
        version: NotRequired[str]
        """
        The version of the RateCard. Defaults to 'latest', if not specified.
        """

    class CreateParamsServiceAction(TypedDict):
        id: str
        """
        The ID of the service action.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Filter by lookup keys. Mutually exclusive with `pricing_plan_version`.
        You can specify up to 10 lookup keys.
        """
        pricing_plan_version: NotRequired[str]
        """
        The ID of the Pricing Plan Version to list components for. Will use the latest version if not provided.
        Mutually exclusive with `lookup_keys`.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        lookup_key: NotRequired[str]
        """
        An identifier that can be used to find this component. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object.
        """

    def list(
        self,
        pricing_plan_id: str,
        params: "ComponentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlanComponent]:
        """
        List all Pricing Plan Component objects for a Pricing Plan.
        """
        return cast(
            ListObject[PricingPlanComponent],
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
        params: "ComponentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PricingPlanComponent]:
        """
        List all Pricing Plan Component objects for a Pricing Plan.
        """
        return cast(
            ListObject[PricingPlanComponent],
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
        params: "ComponentService.CreateParams",
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Create a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.CreateParams",
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Create a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Remove a Pricing Plan Component from the latest version of a Pricing Plan.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Remove a Pricing Plan Component from the latest version of a Pricing Plan.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Retrieve a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Retrieve a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Update a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
        params: "ComponentService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> PricingPlanComponent:
        """
        Update a Pricing Plan Component object.
        """
        return cast(
            PricingPlanComponent,
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
