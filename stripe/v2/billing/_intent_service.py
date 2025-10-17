# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._intent_cancel_params import (
        IntentCancelParams,
    )
    from stripe.params.v2.billing._intent_commit_params import (
        IntentCommitParams,
    )
    from stripe.params.v2.billing._intent_create_params import (
        IntentCreateParams,
    )
    from stripe.params.v2.billing._intent_list_params import IntentListParams
    from stripe.params.v2.billing._intent_release_reservation_params import (
        IntentReleaseReservationParams,
    )
    from stripe.params.v2.billing._intent_reserve_params import (
        IntentReserveParams,
    )
    from stripe.params.v2.billing._intent_retrieve_params import (
        IntentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._intent import Intent
    from stripe.v2.billing.intents._action_service import ActionService

_subservices = {
    "actions": ["stripe.v2.billing.intents._action_service", "ActionService"],
}


class IntentService(StripeService):
    actions: "ActionService"

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

    def list(
        self,
        params: Optional["IntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Intent]":
        """
        List Billing Intents.
        """
        return cast(
            "ListObject[Intent]",
            self._request(
                "get",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["IntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Intent]":
        """
        List Billing Intents.
        """
        return cast(
            "ListObject[Intent]",
            await self._request_async(
                "get",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "IntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Create a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "post",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "IntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Create a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "post",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["IntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Retrieve a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "get",
                "/v2/billing/intents/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["IntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Retrieve a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "get",
                "/v2/billing/intents/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["IntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Cancel a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "post",
                "/v2/billing/intents/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["IntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Cancel a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def commit(
        self,
        id: str,
        params: Optional["IntentCommitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Commit a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "post",
                "/v2/billing/intents/{id}/commit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def commit_async(
        self,
        id: str,
        params: Optional["IntentCommitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Commit a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/commit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def release_reservation(
        self,
        id: str,
        params: Optional["IntentReleaseReservationParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Release a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "post",
                "/v2/billing/intents/{id}/release_reservation".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def release_reservation_async(
        self,
        id: str,
        params: Optional["IntentReleaseReservationParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Release a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/release_reservation".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reserve(
        self,
        id: str,
        params: Optional["IntentReserveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Reserve a Billing Intent.
        """
        return cast(
            "Intent",
            self._request(
                "post",
                "/v2/billing/intents/{id}/reserve".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reserve_async(
        self,
        id: str,
        params: Optional["IntentReserveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Intent":
        """
        Reserve a Billing Intent.
        """
        return cast(
            "Intent",
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/reserve".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
