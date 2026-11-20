# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._dispute_adjustment_list_params import (
        DisputeAdjustmentListParams,
    )
    from stripe.params.v2.money_management._dispute_adjustment_retrieve_params import (
        DisputeAdjustmentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._dispute_adjustment import (
        DisputeAdjustment,
    )


class DisputeAdjustmentService(StripeService):
    def list(
        self,
        params: Optional["DisputeAdjustmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DisputeAdjustment]":
        """
        Retrieves a list of DisputeAdjustments.
        """
        return cast(
            "ListObject[DisputeAdjustment]",
            self._request(
                "get",
                "/v2/money_management/dispute_adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["DisputeAdjustmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DisputeAdjustment]":
        """
        Retrieves a list of DisputeAdjustments.
        """
        return cast(
            "ListObject[DisputeAdjustment]",
            await self._request_async(
                "get",
                "/v2/money_management/dispute_adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["DisputeAdjustmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DisputeAdjustment":
        """
        Retrieves a DisputeAdjustment by ID.
        """
        return cast(
            "DisputeAdjustment",
            self._request(
                "get",
                "/v2/money_management/dispute_adjustments/{id}".format(
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
        /,
        params: Optional["DisputeAdjustmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DisputeAdjustment":
        """
        Retrieves a DisputeAdjustment by ID.
        """
        return cast(
            "DisputeAdjustment",
            await self._request_async(
                "get",
                "/v2/money_management/dispute_adjustments/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
