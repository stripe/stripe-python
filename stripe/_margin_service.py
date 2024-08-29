# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._margin import Margin
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import NotRequired, TypedDict


class MarginService(StripeService):
    class CreateParams(TypedDict):
        active: NotRequired[bool]
        """
        Whether the margin can be applied to invoices, invoice items, or invoice line items or not. Defaults to `true`.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired[str]
        """
        Name of the margin, which is displayed to customers, such as on invoices.
        """
        percent_off: float
        """
        Percent that will be taken off the subtotal before tax (after all other discounts and promotions) of any invoice to which the margin is applied.
        """

    class ListParams(TypedDict):
        active: NotRequired[bool]
        """
        Only return margins that are active or inactive. For example, pass `true` to only list active margins.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        active: NotRequired[bool]
        """
        Whether the margin can be applied to invoices, invoice items, or invoice line items or not.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired[str]
        """
        Name of the margin, which is displayed to customers, such as on invoices.
        """

    def list(
        self,
        params: "MarginService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Margin]:
        """
        Retrieve a list of your margins.
        """
        return cast(
            ListObject[Margin],
            self._request(
                "get",
                "/v1/billing/margins",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "MarginService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Margin]:
        """
        Retrieve a list of your margins.
        """
        return cast(
            ListObject[Margin],
            await self._request_async(
                "get",
                "/v1/billing/margins",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "MarginService.CreateParams",
        options: RequestOptions = {},
    ) -> Margin:
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            Margin,
            self._request(
                "post",
                "/v1/billing/margins",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "MarginService.CreateParams",
        options: RequestOptions = {},
    ) -> Margin:
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            Margin,
            await self._request_async(
                "post",
                "/v1/billing/margins",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        margin: str,
        params: "MarginService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Margin:
        """
        Retrieve a margin object with the given ID.
        """
        return cast(
            Margin,
            self._request(
                "get",
                "/v1/billing/margins/{margin}".format(
                    margin=sanitize_id(margin),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        margin: str,
        params: "MarginService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Margin:
        """
        Retrieve a margin object with the given ID.
        """
        return cast(
            Margin,
            await self._request_async(
                "get",
                "/v1/billing/margins/{margin}".format(
                    margin=sanitize_id(margin),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        margin: str,
        params: "MarginService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Margin:
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        return cast(
            Margin,
            self._request(
                "post",
                "/v1/billing/margins/{margin}".format(
                    margin=sanitize_id(margin),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        margin: str,
        params: "MarginService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Margin:
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        return cast(
            Margin,
            await self._request_async(
                "post",
                "/v1/billing/margins/{margin}".format(
                    margin=sanitize_id(margin),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
