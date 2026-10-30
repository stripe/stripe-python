# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._inbound_funding_list_params import (
        InboundFundingListParams,
    )
    from stripe.params.v2.money_management._inbound_funding_retrieve_params import (
        InboundFundingRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._inbound_funding import InboundFunding


class InboundFundingService(StripeService):
    def list(
        self,
        params: Optional["InboundFundingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundFunding]":
        """
        Lists InboundFundings.
        """
        return cast(
            "ListObject[InboundFunding]",
            self._request(
                "get",
                "/v2/money_management/inbound_fundings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["InboundFundingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InboundFunding]":
        """
        Lists InboundFundings.
        """
        return cast(
            "ListObject[InboundFunding]",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_fundings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["InboundFundingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundFunding":
        """
        Retrieves an InboundFunding by ID.
        """
        return cast(
            "InboundFunding",
            self._request(
                "get",
                "/v2/money_management/inbound_fundings/{id}".format(
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
        params: Optional["InboundFundingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "InboundFunding":
        """
        Retrieves an InboundFunding by ID.
        """
        return cast(
            "InboundFunding",
            await self._request_async(
                "get",
                "/v2/money_management/inbound_fundings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
