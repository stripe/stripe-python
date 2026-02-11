# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._one_time_item_create_params import (
        OneTimeItemCreateParams,
    )
    from stripe.params.v2.billing._one_time_item_list_params import (
        OneTimeItemListParams,
    )
    from stripe.params.v2.billing._one_time_item_retrieve_params import (
        OneTimeItemRetrieveParams,
    )
    from stripe.params.v2.billing._one_time_item_update_params import (
        OneTimeItemUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._one_time_item import OneTimeItem


class OneTimeItemService(StripeService):
    def list(
        self,
        params: Optional["OneTimeItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OneTimeItem]":
        """
        List all One-Time Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[OneTimeItem]",
            self._request(
                "get",
                "/v2/billing/one_time_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OneTimeItemListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OneTimeItem]":
        """
        List all One-Time Item objects in reverse chronological order of creation.
        """
        return cast(
            "ListObject[OneTimeItem]",
            await self._request_async(
                "get",
                "/v2/billing/one_time_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OneTimeItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Create a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            self._request(
                "post",
                "/v2/billing/one_time_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OneTimeItemCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Create a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            await self._request_async(
                "post",
                "/v2/billing/one_time_items",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OneTimeItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Retrieve a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            self._request(
                "get",
                "/v2/billing/one_time_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["OneTimeItemRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Retrieve a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            await self._request_async(
                "get",
                "/v2/billing/one_time_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["OneTimeItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Update a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            self._request(
                "post",
                "/v2/billing/one_time_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["OneTimeItemUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OneTimeItem":
        """
        Update a One-Time Item object.
        """
        return cast(
            "OneTimeItem",
            await self._request_async(
                "post",
                "/v2/billing/one_time_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
