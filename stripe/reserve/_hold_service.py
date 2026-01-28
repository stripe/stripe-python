# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.reserve._hold_list_params import HoldListParams
    from stripe.params.reserve._hold_retrieve_params import HoldRetrieveParams
    from stripe.reserve._hold import Hold


class HoldService(StripeService):
    def list(
        self,
        params: Optional["HoldListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Hold]":
        """
        Returns a list of ReserveHolds previously created. The ReserveHolds are returned in sorted order, with the most recent ReserveHolds appearing first.
        """
        return cast(
            "ListObject[Hold]",
            self._request(
                "get",
                "/v1/reserve/holds",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["HoldListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Hold]":
        """
        Returns a list of ReserveHolds previously created. The ReserveHolds are returned in sorted order, with the most recent ReserveHolds appearing first.
        """
        return cast(
            "ListObject[Hold]",
            await self._request_async(
                "get",
                "/v1/reserve/holds",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["HoldRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Hold":
        """
        Retrieve a ReserveHold.
        """
        return cast(
            "Hold",
            self._request(
                "get",
                "/v1/reserve/holds/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["HoldRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Hold":
        """
        Retrieve a ReserveHold.
        """
        return cast(
            "Hold",
            await self._request_async(
                "get",
                "/v1/reserve/holds/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
