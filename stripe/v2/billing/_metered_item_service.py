# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._metered_item_create_params import (
        MeteredItemCreateParams,
    )
    from stripe.params.v2.billing._metered_item_list_params import (
        MeteredItemListParams,
    )
    from stripe.params.v2.billing._metered_item_retrieve_params import (
        MeteredItemRetrieveParams,
    )
    from stripe.params.v2.billing._metered_item_update_params import (
        MeteredItemUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._metered_item import MeteredItem


class MeteredItemService(StripeService):
    def list(
        self,
        params: Optional["MeteredItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[MeteredItem]":
        """
        List all Metered Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[MeteredItem]",
            self._request(
                "get",
                "/v2/billing/metered_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["MeteredItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[MeteredItem]":
        """
        List all Metered Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[MeteredItem]",
            await self._request_async(
                "get",
                "/v2/billing/metered_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "MeteredItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Create a Metered Item object.
        """
        return cast(
            "MeteredItem",
            self._request(
                "post",
                "/v2/billing/metered_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "MeteredItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Create a Metered Item object.
        """
        return cast(
            "MeteredItem",
            await self._request_async(
                "post",
                "/v2/billing/metered_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["MeteredItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Retrieve a Metered Item object.
        """
        return cast(
            "MeteredItem",
            self._request(
                "get",
                "/v2/billing/metered_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["MeteredItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Retrieve a Metered Item object.
        """
        return cast(
            "MeteredItem",
            await self._request_async(
                "get",
                "/v2/billing/metered_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["MeteredItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Update a Metered Item object. At least one of the fields is required.
        """
        return cast(
            "MeteredItem",
            self._request(
                "post",
                "/v2/billing/metered_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["MeteredItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "MeteredItem":
        """
        Update a Metered Item object. At least one of the fields is required.
        """
        return cast(
            "MeteredItem",
            await self._request_async(
                "post",
                "/v2/billing/metered_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
