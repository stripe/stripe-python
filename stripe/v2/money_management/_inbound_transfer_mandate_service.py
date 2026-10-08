# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._inbound_transfer_mandate_cancel_params import (
        InboundTransferMandateCancelParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_mandate_create_params import (
        InboundTransferMandateCreateParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_mandate_list_params import (
        InboundTransferMandateListParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_mandate_retrieve_params import (
        InboundTransferMandateRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._inbound_transfer_mandate import (
        InboundTransferMandate,
    )


class InboundTransferMandateService(StripeService):
    def list(
        self,
        params: Optional["InboundTransferMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundTransferMandate]":
        """
        Retrieve a list of InboundTransferMandates for the authenticated compartment.
        """
        return cast(
            "ListObject[InboundTransferMandate]",
            self._request(
                "get",
                "/v2/money_management/inbound_transfer_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["InboundTransferMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundTransferMandate]":
        """
        Retrieve a list of InboundTransferMandates for the authenticated compartment.
        """
        return cast(
            "ListObject[InboundTransferMandate]",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfer_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "InboundTransferMandateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Create an InboundTransferMandate for a v2 credential. If a pending or
        active mandate already exists for the same user and credential, that
        mandate is returned instead of creating a new one.
        """
        return cast(
            "InboundTransferMandate",
            self._request(
                "post",
                "/v2/money_management/inbound_transfer_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "InboundTransferMandateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Create an InboundTransferMandate for a v2 credential. If a pending or
        active mandate already exists for the same user and credential, that
        mandate is returned instead of creating a new one.
        """
        return cast(
            "InboundTransferMandate",
            await self._request_async(
                "post",
                "/v2/money_management/inbound_transfer_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["InboundTransferMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Retrieve an InboundTransferMandate by ID.
        """
        return cast(
            "InboundTransferMandate",
            self._request(
                "get",
                "/v2/money_management/inbound_transfer_mandates/{id}".format(
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
        params: Optional["InboundTransferMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Retrieve an InboundTransferMandate by ID.
        """
        return cast(
            "InboundTransferMandate",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfer_mandates/{id}".format(
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
        /,
        params: Optional["InboundTransferMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Cancel a pending or active InboundTransferMandate.
        """
        return cast(
            "InboundTransferMandate",
            self._request(
                "post",
                "/v2/money_management/inbound_transfer_mandates/{id}/cancel".format(
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
        /,
        params: Optional["InboundTransferMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundTransferMandate":
        """
        Cancel a pending or active InboundTransferMandate.
        """
        return cast(
            "InboundTransferMandate",
            await self._request_async(
                "post",
                "/v2/money_management/inbound_transfer_mandates/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
