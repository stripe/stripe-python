# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._custom_pricing_unit_create_params import (
        CustomPricingUnitCreateParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_list_params import (
        CustomPricingUnitListParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_retrieve_params import (
        CustomPricingUnitRetrieveParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_update_params import (
        CustomPricingUnitUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._custom_pricing_unit import CustomPricingUnit


class CustomPricingUnitService(StripeService):
    def list(
        self,
        params: Optional["CustomPricingUnitListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomPricingUnit]":
        """
        List all Custom Pricing Unit objects.
        """
        return cast(
            "ListObject[CustomPricingUnit]",
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
        params: Optional["CustomPricingUnitListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomPricingUnit]":
        """
        List all Custom Pricing Unit objects.
        """
        return cast(
            "ListObject[CustomPricingUnit]",
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
        params: "CustomPricingUnitCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Create a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
        params: "CustomPricingUnitCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Create a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
        params: Optional["CustomPricingUnitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Retrieve a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
        params: Optional["CustomPricingUnitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Retrieve a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
        params: Optional["CustomPricingUnitUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Update a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
        params: Optional["CustomPricingUnitUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomPricingUnit":
        """
        Update a Custom Pricing Unit object.
        """
        return cast(
            "CustomPricingUnit",
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
