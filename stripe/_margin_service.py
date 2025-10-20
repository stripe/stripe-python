# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._margin import Margin
    from stripe._request_options import RequestOptions
    from stripe.params._margin_create_params import MarginCreateParams
    from stripe.params._margin_list_params import MarginListParams
    from stripe.params._margin_retrieve_params import MarginRetrieveParams
    from stripe.params._margin_update_params import MarginUpdateParams


class MarginService(StripeService):
    def list(
        self,
        params: Optional["MarginListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Margin]":
        """
        Retrieve a list of your margins.
        """
        return cast(
            "ListObject[Margin]",
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
        params: Optional["MarginListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Margin]":
        """
        Retrieve a list of your margins.
        """
        return cast(
            "ListObject[Margin]",
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
        params: "MarginCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            "Margin",
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
        params: "MarginCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            "Margin",
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
        params: Optional["MarginRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Retrieve a margin object with the given ID.
        """
        return cast(
            "Margin",
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
        params: Optional["MarginRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Retrieve a margin object with the given ID.
        """
        return cast(
            "Margin",
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
        params: Optional["MarginUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        return cast(
            "Margin",
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
        params: Optional["MarginUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Margin":
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        return cast(
            "Margin",
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
