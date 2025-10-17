# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._adjustment_list_params import (
        AdjustmentListParams,
    )
    from stripe.params.v2.money_management._adjustment_retrieve_params import (
        AdjustmentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._adjustment import Adjustment


class AdjustmentService(StripeService):
    def list(
        self,
        params: Optional["AdjustmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Adjustment]":
        """
        Returns a list of Adjustments that match the provided filters.
        """
        return cast(
            "ListObject[Adjustment]",
            self._request(
                "get",
                "/v2/money_management/adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["AdjustmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Adjustment]":
        """
        Returns a list of Adjustments that match the provided filters.
        """
        return cast(
            "ListObject[Adjustment]",
            await self._request_async(
                "get",
                "/v2/money_management/adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AdjustmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Adjustment":
        """
        Retrieves the details of an Adjustment by ID.
        """
        return cast(
            "Adjustment",
            self._request(
                "get",
                "/v2/money_management/adjustments/{id}".format(
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
        params: Optional["AdjustmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Adjustment":
        """
        Retrieves the details of an Adjustment by ID.
        """
        return cast(
            "Adjustment",
            await self._request_async(
                "get",
                "/v2/money_management/adjustments/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
