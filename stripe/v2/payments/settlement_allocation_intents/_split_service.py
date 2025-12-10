# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.payments.settlement_allocation_intents._split_cancel_params import (
        SplitCancelParams,
    )
    from stripe.params.v2.payments.settlement_allocation_intents._split_create_params import (
        SplitCreateParams,
    )
    from stripe.params.v2.payments.settlement_allocation_intents._split_retrieve_params import (
        SplitRetrieveParams,
    )
    from stripe.v2.payments._settlement_allocation_intent_split import (
        SettlementAllocationIntentSplit,
    )


class SplitService(StripeService):
    def create(
        self,
        settlement_allocation_intent_id: str,
        params: "SplitCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Create SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        settlement_allocation_intent_id: str,
        params: "SplitCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Create SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        settlement_allocation_intent_id: str,
        id: str,
        params: Optional["SplitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Retrieve SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            self._request(
                "get",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits/{id}".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        settlement_allocation_intent_id: str,
        id: str,
        params: Optional["SplitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Retrieve SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            await self._request_async(
                "get",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits/{id}".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        settlement_allocation_intent_id: str,
        id: str,
        params: Optional["SplitCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Cancel SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits/{id}/cancel".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        settlement_allocation_intent_id: str,
        id: str,
        params: Optional["SplitCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntentSplit":
        """
        Cancel SettlementAllocationIntentSplit API.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents/{settlement_allocation_intent_id}/splits/{id}/cancel".format(
                    settlement_allocation_intent_id=sanitize_id(
                        settlement_allocation_intent_id
                    ),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
