# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._inbound_transfer_create_params import (
        InboundTransferCreateParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_list_params import (
        InboundTransferListParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_retrieve_params import (
        InboundTransferRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._inbound_transfer import InboundTransfer


class InboundTransferService(StripeService):
    def list(
        self,
        params: Optional["InboundTransferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundTransfer]":
        """
        Retrieves a list of InboundTransfers.
        """
        return cast(
            "ListObject[InboundTransfer]",
            self._request(
                "get",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["InboundTransferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundTransfer]":
        """
        Retrieves a list of InboundTransfers.
        """
        return cast(
            "ListObject[InboundTransfer]",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "InboundTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransfer":
        """
        InboundTransfers APIs are used to create, retrieve or list InboundTransfers.
        """
        return cast(
            "InboundTransfer",
            self._request(
                "post",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "InboundTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransfer":
        """
        InboundTransfers APIs are used to create, retrieve or list InboundTransfers.
        """
        return cast(
            "InboundTransfer",
            await self._request_async(
                "post",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["InboundTransferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransfer":
        """
        Retrieve an InboundTransfer by ID.
        """
        return cast(
            "InboundTransfer",
            self._request(
                "get",
                "/v2/money_management/inbound_transfers/{id}".format(
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
        params: Optional["InboundTransferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransfer":
        """
        Retrieve an InboundTransfer by ID.
        """
        return cast(
            "InboundTransfer",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfers/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
