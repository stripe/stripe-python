# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.risk._inquiry_list_params import InquiryListParams
    from stripe.params.v2.risk._inquiry_retrieve_params import (
        InquiryRetrieveParams,
    )
    from stripe.params.v2.risk._inquiry_update_params import (
        InquiryUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.risk._inquiry import Inquiry


class InquiryService(StripeService):
    def list(
        self,
        params: "InquiryListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Inquiry]":
        """
        Lists risk inquiries for a connected account.
        """
        return cast(
            "ListObject[Inquiry]",
            self._request(
                "get",
                "/v2/risk/inquiries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InquiryListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Inquiry]":
        """
        Lists risk inquiries for a connected account.
        """
        return cast(
            "ListObject[Inquiry]",
            await self._request_async(
                "get",
                "/v2/risk/inquiries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["InquiryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Inquiry":
        """
        Retrieves a risk inquiry by ID.
        """
        return cast(
            "Inquiry",
            self._request(
                "get",
                "/v2/risk/inquiries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["InquiryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Inquiry":
        """
        Retrieves a risk inquiry by ID.
        """
        return cast(
            "Inquiry",
            await self._request_async(
                "get",
                "/v2/risk/inquiries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["InquiryUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Inquiry":
        """
        Submits a response to a risk inquiry.
        """
        return cast(
            "Inquiry",
            self._request(
                "post",
                "/v2/risk/inquiries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["InquiryUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Inquiry":
        """
        Submits a response to a risk inquiry.
        """
        return cast(
            "Inquiry",
            await self._request_async(
                "post",
                "/v2/risk/inquiries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
