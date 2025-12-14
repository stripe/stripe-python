# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import get_api_mode
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_client import StripeClient
    from stripe.v2.payments._settlement_allocation_intent_split import (
        SettlementAllocationIntentSplit,
    )


class V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.payments.settlement_allocation_intent_split.created"
    type: Literal["v2.payments.settlement_allocation_intent_split.created"]
    related_object: RelatedObject

    def __init__(
        self, parsed_body: Dict[str, Any], client: "StripeClient"
    ) -> None:
        super().__init__(
            parsed_body,
            client,
        )
        self.related_object = RelatedObject(parsed_body["related_object"])

    @override
    def fetch_event(
        self,
    ) -> "V2PaymentsSettlementAllocationIntentSplitCreatedEvent":
        return cast(
            "V2PaymentsSettlementAllocationIntentSplitCreatedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "SettlementAllocationIntentSplit":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "SettlementAllocationIntentSplit",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2PaymentsSettlementAllocationIntentSplitCreatedEvent":
        return cast(
            "V2PaymentsSettlementAllocationIntentSplitCreatedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(
        self,
    ) -> "SettlementAllocationIntentSplit":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "SettlementAllocationIntentSplit",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2PaymentsSettlementAllocationIntentSplitCreatedEvent(Event):
    LOOKUP_TYPE = "v2.payments.settlement_allocation_intent_split.created"
    type: Literal["v2.payments.settlement_allocation_intent_split.created"]

    class V2PaymentsSettlementAllocationIntentSplitCreatedEventData(
        StripeObject,
    ):
        settlement_allocation_intent_id: str
        """
        The ID of the SettlementAllocationIntent this split belongs to.
        """

    data: V2PaymentsSettlementAllocationIntentSplitCreatedEventData
    """
    Data for the v2.payments.settlement_allocation_intent_split.created event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2PaymentsSettlementAllocationIntentSplitCreatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2PaymentsSettlementAllocationIntentSplitCreatedEvent.V2PaymentsSettlementAllocationIntentSplitCreatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> "SettlementAllocationIntentSplit":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "SettlementAllocationIntentSplit",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_context": self.context},
            ),
        )
