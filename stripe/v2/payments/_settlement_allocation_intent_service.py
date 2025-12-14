# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.payments._settlement_allocation_intent_cancel_params import (
        SettlementAllocationIntentCancelParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_create_params import (
        SettlementAllocationIntentCreateParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_retrieve_params import (
        SettlementAllocationIntentRetrieveParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_submit_params import (
        SettlementAllocationIntentSubmitParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_update_params import (
        SettlementAllocationIntentUpdateParams,
    )
    from stripe.v2.payments._settlement_allocation_intent import (
        SettlementAllocationIntent,
    )
    from stripe.v2.payments.settlement_allocation_intents._split_service import (
        SplitService,
    )

_subservices = {
    "splits": [
        "stripe.v2.payments.settlement_allocation_intents._split_service",
        "SplitService",
    ],
}


class SettlementAllocationIntentService(StripeService):
    splits: "SplitService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def create(
        self,
        params: "SettlementAllocationIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Create a new SettlementAllocationIntent.
        """
        return cast(
            "SettlementAllocationIntent",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "SettlementAllocationIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Create a new SettlementAllocationIntent.
        """
        return cast(
            "SettlementAllocationIntent",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["SettlementAllocationIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Retrieve an existing SettlementAllocationIntent.
        """
        return cast(
            "SettlementAllocationIntent",
            self._request(
                "get",
                "/v2/payments/settlement_allocation_intents/{id}".format(
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
        params: Optional["SettlementAllocationIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Retrieve an existing SettlementAllocationIntent.
        """
        return cast(
            "SettlementAllocationIntent",
            await self._request_async(
                "get",
                "/v2/payments/settlement_allocation_intents/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["SettlementAllocationIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Updates SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending`, `submitted` and `errored` can be updated. Only amount and reference fields can be updated for a SettlementAllocationIntent and at least one must be present. Updating an `amount` moves the SettlementAllocationIntent `pending` status and updating the `reference` for `errored` SettlementAllocationIntent moves it to `submitted`.
        """
        return cast(
            "SettlementAllocationIntent",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["SettlementAllocationIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Updates SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending`, `submitted` and `errored` can be updated. Only amount and reference fields can be updated for a SettlementAllocationIntent and at least one must be present. Updating an `amount` moves the SettlementAllocationIntent `pending` status and updating the `reference` for `errored` SettlementAllocationIntent moves it to `submitted`.
        """
        return cast(
            "SettlementAllocationIntent",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}".format(
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
        params: Optional["SettlementAllocationIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Cancels an existing SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending`, `submitted` and `errored` can be `canceled`.
        """
        return cast(
            "SettlementAllocationIntent",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}/cancel".format(
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
        params: Optional["SettlementAllocationIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Cancels an existing SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending`, `submitted` and `errored` can be `canceled`.
        """
        return cast(
            "SettlementAllocationIntent",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit(
        self,
        id: str,
        params: Optional["SettlementAllocationIntentSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Submits a SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending` can be `submitted`. The net sum of SettlementAllocationIntentSplit amount must be equal to SettlementAllocationIntent amount to be eligible to be submitted.
        """
        return cast(
            "SettlementAllocationIntent",
            self._request(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}/submit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_async(
        self,
        id: str,
        params: Optional["SettlementAllocationIntentSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SettlementAllocationIntent":
        """
        Submits a SettlementAllocationIntent. Only SettlementAllocationIntent with status `pending` can be `submitted`. The net sum of SettlementAllocationIntentSplit amount must be equal to SettlementAllocationIntent amount to be eligible to be submitted.
        """
        return cast(
            "SettlementAllocationIntent",
            await self._request_async(
                "post",
                "/v2/payments/settlement_allocation_intents/{id}/submit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
