# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._custom_pricing_unit import CustomPricingUnit
from typing import Dict, List, Optional, cast
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitService(StripeService):
    class CreateParams(TypedDict):
        display_name: str
        """
        Description that customers will see in the invoice line item.
        Maximum length of 10 characters.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular custom pricing unit item.
        Must be unique among items.
        Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    class ListParams(TypedDict):
        active: NotRequired[bool]
        """
        Filter for active/inactive custom pricing units. Mutually exclusive with `lookup_keys`.
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
        Whether the Custom Pricing Unit is active.
        """
        display_name: NotRequired[str]
        """
        Description that customers will see in the invoice line item.
        """
        lookup_key: NotRequired[Optional[str]]
        """
        An internal key you can use to search for a particular CustomPricingUnit item.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object.
        """

    def list(
        self,
        params: "CustomPricingUnitService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CustomPricingUnit]:
        """
        List all Custom Pricing Unit objects.
        """
        return cast(
            ListObject[CustomPricingUnit],
            self._request(
                "get",
                "/v2/billing/custom_pricing_units",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CustomPricingUnitService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CustomPricingUnit]:
        """
        List all Custom Pricing Unit objects.
        """
        return cast(
            ListObject[CustomPricingUnit],
            await self._request_async(
                "get",
                "/v2/billing/custom_pricing_units",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CustomPricingUnitService.CreateParams",
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Create a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            self._request(
                "post",
                "/v2/billing/custom_pricing_units",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CustomPricingUnitService.CreateParams",
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Create a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            await self._request_async(
                "post",
                "/v2/billing/custom_pricing_units",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CustomPricingUnitService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Retrieve a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            self._request(
                "get",
                "/v2/billing/custom_pricing_units/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "CustomPricingUnitService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Retrieve a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            await self._request_async(
                "get",
                "/v2/billing/custom_pricing_units/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "CustomPricingUnitService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Update a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            self._request(
                "post",
                "/v2/billing/custom_pricing_units/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "CustomPricingUnitService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CustomPricingUnit:
        """
        Update a Custom Pricing Unit object.
        """
        return cast(
            CustomPricingUnit,
            await self._request_async(
                "post",
                "/v2/billing/custom_pricing_units/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
