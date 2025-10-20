# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._outbound_transfer_cancel_params import (
        OutboundTransferCancelParams,
    )
    from stripe.params.v2.money_management._outbound_transfer_create_params import (
        OutboundTransferCreateParams,
    )
    from stripe.params.v2.money_management._outbound_transfer_list_params import (
        OutboundTransferListParams,
    )
    from stripe.params.v2.money_management._outbound_transfer_retrieve_params import (
        OutboundTransferRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._outbound_transfer import OutboundTransfer


class OutboundTransferService(StripeService):
    def list(
        self,
        params: Optional["OutboundTransferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundTransfer]":
        """
        Returns a list of OutboundTransfers that match the provided filters.
        """
        return cast(
            "ListObject[OutboundTransfer]",
            self._request(
                "get",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OutboundTransferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundTransfer]":
        """
        Returns a list of OutboundTransfers that match the provided filters.
        """
        return cast(
            "ListObject[OutboundTransfer]",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OutboundTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Creates an OutboundTransfer.
        """
        return cast(
            "OutboundTransfer",
            self._request(
                "post",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Creates an OutboundTransfer.
        """
        return cast(
            "OutboundTransfer",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OutboundTransferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundPayment create or list response.
        """
        return cast(
            "OutboundTransfer",
            self._request(
                "get",
                "/v2/money_management/outbound_transfers/{id}".format(
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
        params: Optional["OutboundTransferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundPayment create or list response.
        """
        return cast(
            "OutboundTransfer",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_transfers/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["OutboundTransferCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Cancels an OutboundTransfer. Only processing OutboundTransfers can be canceled.
        """
        return cast(
            "OutboundTransfer",
            self._request(
                "post",
                "/v2/money_management/outbound_transfers/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["OutboundTransferCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundTransfer":
        """
        Cancels an OutboundTransfer. Only processing OutboundTransfers can be canceled.
        """
        return cast(
            "OutboundTransfer",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_transfers/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
