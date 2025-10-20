# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._licensed_item_create_params import (
        LicensedItemCreateParams,
    )
    from stripe.params.v2.billing._licensed_item_list_params import (
        LicensedItemListParams,
    )
    from stripe.params.v2.billing._licensed_item_retrieve_params import (
        LicensedItemRetrieveParams,
    )
    from stripe.params.v2.billing._licensed_item_update_params import (
        LicensedItemUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._licensed_item import LicensedItem


class LicensedItemService(StripeService):
    def list(
        self,
        params: Optional["LicensedItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicensedItem]":
        """
        List all Licensed Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[LicensedItem]",
            self._request(
                "get",
                "/v2/billing/licensed_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["LicensedItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicensedItem]":
        """
        List all Licensed Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[LicensedItem]",
            await self._request_async(
                "get",
                "/v2/billing/licensed_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "LicensedItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Create a Licensed Item object.
        """
        return cast(
            "LicensedItem",
            self._request(
                "post",
                "/v2/billing/licensed_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "LicensedItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Create a Licensed Item object.
        """
        return cast(
            "LicensedItem",
            await self._request_async(
                "post",
                "/v2/billing/licensed_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["LicensedItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Retrieve a Licensed Item object.
        """
        return cast(
            "LicensedItem",
            self._request(
                "get",
                "/v2/billing/licensed_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["LicensedItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Retrieve a Licensed Item object.
        """
        return cast(
            "LicensedItem",
            await self._request_async(
                "get",
                "/v2/billing/licensed_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["LicensedItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Update a Licensed Item object. At least one of the fields is required.
        """
        return cast(
            "LicensedItem",
            self._request(
                "post",
                "/v2/billing/licensed_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["LicensedItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicensedItem":
        """
        Update a Licensed Item object. At least one of the fields is required.
        """
        return cast(
            "LicensedItem",
            await self._request_async(
                "post",
                "/v2/billing/licensed_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
