# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._payout_intent_cancel_params import (
        PayoutIntentCancelParams,
    )
    from stripe.params.v2.money_management._payout_intent_create_params import (
        PayoutIntentCreateParams,
    )
    from stripe.params.v2.money_management._payout_intent_list_params import (
        PayoutIntentListParams,
    )
    from stripe.params.v2.money_management._payout_intent_retrieve_params import (
        PayoutIntentRetrieveParams,
    )
    from stripe.params.v2.money_management._payout_intent_update_params import (
        PayoutIntentUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._payout_intent import PayoutIntent


class PayoutIntentService(StripeService):
    def list(
        self,
        params: Optional["PayoutIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PayoutIntent]":
        """
        Returns a list of PayoutIntents.
        """
        return cast(
            "ListObject[PayoutIntent]",
            self._request(
                "get",
                "/v2/money_management/payout_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["PayoutIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PayoutIntent]":
        """
        Returns a list of PayoutIntents.
        """
        return cast(
            "ListObject[PayoutIntent]",
            await self._request_async(
                "get",
                "/v2/money_management/payout_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "PayoutIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Creates a PayoutIntent.
        """
        return cast(
            "PayoutIntent",
            self._request(
                "post",
                "/v2/money_management/payout_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "PayoutIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Creates a PayoutIntent.
        """
        return cast(
            "PayoutIntent",
            await self._request_async(
                "post",
                "/v2/money_management/payout_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PayoutIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Retrieves the details of an existing PayoutIntent by passing the unique PayoutIntent ID.
        """
        return cast(
            "PayoutIntent",
            self._request(
                "get",
                "/v2/money_management/payout_intents/{id}".format(
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
        params: Optional["PayoutIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Retrieves the details of an existing PayoutIntent by passing the unique PayoutIntent ID.
        """
        return cast(
            "PayoutIntent",
            await self._request_async(
                "get",
                "/v2/money_management/payout_intents/{id}".format(
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
        params: Optional["PayoutIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Updates a PayoutIntent. Only pending or requires_action PayoutIntents that are editable can be updated.
        """
        return cast(
            "PayoutIntent",
            self._request(
                "post",
                "/v2/money_management/payout_intents/{id}".format(
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
        params: Optional["PayoutIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Updates a PayoutIntent. Only pending or requires_action PayoutIntents that are editable can be updated.
        """
        return cast(
            "PayoutIntent",
            await self._request_async(
                "post",
                "/v2/money_management/payout_intents/{id}".format(
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
        params: Optional["PayoutIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Cancels a PayoutIntent. Only pending PayoutIntents or processing PayoutIntents with cancelable OutboundPayment/Transfer can be canceled.
        """
        return cast(
            "PayoutIntent",
            self._request(
                "post",
                "/v2/money_management/payout_intents/{id}/cancel".format(
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
        params: Optional["PayoutIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutIntent":
        """
        Cancels a PayoutIntent. Only pending PayoutIntents or processing PayoutIntents with cancelable OutboundPayment/Transfer can be canceled.
        """
        return cast(
            "PayoutIntent",
            await self._request_async(
                "post",
                "/v2/money_management/payout_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
