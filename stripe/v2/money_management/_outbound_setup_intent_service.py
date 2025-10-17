# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._outbound_setup_intent_cancel_params import (
        OutboundSetupIntentCancelParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_create_params import (
        OutboundSetupIntentCreateParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_list_params import (
        OutboundSetupIntentListParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_retrieve_params import (
        OutboundSetupIntentRetrieveParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_update_params import (
        OutboundSetupIntentUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._outbound_setup_intent import (
        OutboundSetupIntent,
    )


class OutboundSetupIntentService(StripeService):
    def list(
        self,
        params: Optional["OutboundSetupIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundSetupIntent]":
        """
        List the OutboundSetupIntent objects.
        """
        return cast(
            "ListObject[OutboundSetupIntent]",
            self._request(
                "get",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OutboundSetupIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundSetupIntent]":
        """
        List the OutboundSetupIntent objects.
        """
        return cast(
            "ListObject[OutboundSetupIntent]",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: Optional["OutboundSetupIntentCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Create an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["OutboundSetupIntentCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Create an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OutboundSetupIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Retrieve an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            self._request(
                "get",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: Optional["OutboundSetupIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Retrieve an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: Optional["OutboundSetupIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Update an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: Optional["OutboundSetupIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Update an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: Optional["OutboundSetupIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Cancel an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}/cancel".format(
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
        params: Optional["OutboundSetupIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundSetupIntent":
        """
        Cancel an OutboundSetupIntent object.
        """
        return cast(
            "OutboundSetupIntent",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
