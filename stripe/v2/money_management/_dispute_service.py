# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._dispute_create_params import (
        DisputeCreateParams,
    )
    from stripe.params.v2.money_management._dispute_list_params import (
        DisputeListParams,
    )
    from stripe.params.v2.money_management._dispute_retrieve_params import (
        DisputeRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._dispute import Dispute


class DisputeService(StripeService):
    def list(
        self,
        params: Optional["DisputeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Dispute]":
        """
        Retrieves a list of Disputes.
        """
        return cast(
            "ListObject[Dispute]",
            self._request(
                "get",
                "/v2/money_management/disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["DisputeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Dispute]":
        """
        Retrieves a list of Disputes.
        """
        return cast(
            "ListObject[Dispute]",
            await self._request_async(
                "get",
                "/v2/money_management/disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "DisputeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Creates a Dispute for the specified money movement.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v2/money_management/disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "DisputeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Creates a Dispute for the specified money movement.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v2/money_management/disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["DisputeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Retrieves a Dispute.
        """
        return cast(
            "Dispute",
            self._request(
                "get",
                "/v2/money_management/disputes/{id}".format(
                    id=sanitize_id(id)
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
        params: Optional["DisputeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Retrieves a Dispute.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "get",
                "/v2/money_management/disputes/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
