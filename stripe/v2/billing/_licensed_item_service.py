# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._licensed_item import LicensedItem
from typing import Dict, List, Optional, cast
from typing_extensions import NotRequired, TypedDict


class LicensedItemService(StripeService):
    class CreateParams(TypedDict):
        display_name: str
        """
        Description that customers will see in the invoice line item.
        Maximum length of 250 characters.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular billable item.
        Must be unique among billable items.
        Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        tax_details: NotRequired["LicensedItemService.CreateParamsTaxDetails"]
        """
        Stripe Tax details.
        """
        unit_label: NotRequired[str]
        """
        The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
        to "seat" for Checkout to display "(price) per seat", or "environment" to display "(price) per environment".
        Maximum length of 100 characters.
        """

    class CreateParamsTaxDetails(TypedDict):
        tax_code: str
        """
        Product tax code (PTC).
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Filter by lookup keys.
        You can specify up to 10 lookup keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        display_name: NotRequired[str]
        """
        Description that customers will see in the invoice line item.
        Maximum length of 250 characters.
        """
        lookup_key: NotRequired[Optional[str]]
        """
        An internal key you can use to search for a particular billable item.
        Maximum length of 200 characters.
        To remove the lookup_key from the object, set it to null in the request.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        tax_details: NotRequired["LicensedItemService.UpdateParamsTaxDetails"]
        """
        Stripe Tax details.
        """
        unit_label: NotRequired[Optional[str]]
        """
        The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
        to "seat" for Checkout to display "(price) per seat", or "environment" to display "(price) per environment".
        Maximum length of 100 characters.
        """

    class UpdateParamsTaxDetails(TypedDict):
        tax_code: str
        """
        Product tax code (PTC).
        """

    def list(
        self,
        params: "LicensedItemService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[LicensedItem]:
        """
        List all Licensed Item objects in reverse chronological order of creation.
        """
        return cast(
            ListObject[LicensedItem],
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
        params: "LicensedItemService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[LicensedItem]:
        """
        List all Licensed Item objects in reverse chronological order of creation.
        """
        return cast(
            ListObject[LicensedItem],
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
        params: "LicensedItemService.CreateParams",
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Create a Licensed Item object.
        """
        return cast(
            LicensedItem,
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
        params: "LicensedItemService.CreateParams",
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Create a Licensed Item object.
        """
        return cast(
            LicensedItem,
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
        params: "LicensedItemService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Retrieve a Licensed Item object.
        """
        return cast(
            LicensedItem,
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
        params: "LicensedItemService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Retrieve a Licensed Item object.
        """
        return cast(
            LicensedItem,
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
        params: "LicensedItemService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Update a Licensed Item object. At least one of the fields is required.
        """
        return cast(
            LicensedItem,
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
        params: "LicensedItemService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> LicensedItem:
        """
        Update a Licensed Item object. At least one of the fields is required.
        """
        return cast(
            LicensedItem,
            await self._request_async(
                "post",
                "/v2/billing/licensed_items/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
