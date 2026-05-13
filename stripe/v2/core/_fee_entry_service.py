# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._fee_entry_list_params import FeeEntryListParams
    from stripe.params.v2.core._fee_entry_retrieve_params import (
        FeeEntryRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core._fee_entry import FeeEntry


class FeeEntryService(StripeService):
    def list(
        self,
        params: Optional["FeeEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeeEntry]":
        """
        List FeeEntries optionally filtered by incurred_by, fee_batch, or collection_record (at most one filter at a time).
        """
        return cast(
            "ListObject[FeeEntry]",
            self._request(
                "get",
                "/v2/core/fee_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FeeEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeeEntry]":
        """
        List FeeEntries optionally filtered by incurred_by, fee_batch, or collection_record (at most one filter at a time).
        """
        return cast(
            "ListObject[FeeEntry]",
            await self._request_async(
                "get",
                "/v2/core/fee_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FeeEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeeEntry":
        """
        Retrieve a FeeEntry by id.
        """
        return cast(
            "FeeEntry",
            self._request(
                "get",
                "/v2/core/fee_entries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["FeeEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeeEntry":
        """
        Retrieve a FeeEntry by id.
        """
        return cast(
            "FeeEntry",
            await self._request_async(
                "get",
                "/v2/core/fee_entries/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
