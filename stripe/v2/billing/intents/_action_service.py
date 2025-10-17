# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.intents._action_list_params import (
        ActionListParams,
    )
    from stripe.params.v2.billing.intents._action_retrieve_params import (
        ActionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._intent_action import IntentAction


class ActionService(StripeService):
    def list(
        self,
        intent_id: str,
        params: Optional["ActionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[IntentAction]":
        """
        List Billing Intent Actions.
        """
        return cast(
            "ListObject[IntentAction]",
            self._request(
                "get",
                "/v2/billing/intents/{intent_id}/actions".format(
                    intent_id=sanitize_id(intent_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        intent_id: str,
        params: Optional["ActionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[IntentAction]":
        """
        List Billing Intent Actions.
        """
        return cast(
            "ListObject[IntentAction]",
            await self._request_async(
                "get",
                "/v2/billing/intents/{intent_id}/actions".format(
                    intent_id=sanitize_id(intent_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        intent_id: str,
        id: str,
        params: Optional["ActionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntentAction":
        """
        Retrieve a Billing Intent Action.
        """
        return cast(
            "IntentAction",
            self._request(
                "get",
                "/v2/billing/intents/{intent_id}/actions/{id}".format(
                    intent_id=sanitize_id(intent_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        intent_id: str,
        id: str,
        params: Optional["ActionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntentAction":
        """
        Retrieve a Billing Intent Action.
        """
        return cast(
            "IntentAction",
            await self._request_async(
                "get",
                "/v2/billing/intents/{intent_id}/actions/{id}".format(
                    intent_id=sanitize_id(intent_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
