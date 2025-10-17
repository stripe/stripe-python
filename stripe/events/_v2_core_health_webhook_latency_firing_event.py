# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthWebhookLatencyFiringEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.webhook_latency.firing"
    type: Literal["v2.core.health.webhook_latency.firing"]

    @override
    def fetch_event(self) -> "V2CoreHealthWebhookLatencyFiringEvent":
        return cast(
            "V2CoreHealthWebhookLatencyFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthWebhookLatencyFiringEvent":
        return cast(
            "V2CoreHealthWebhookLatencyFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthWebhookLatencyFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.webhook_latency.firing"
    type: Literal["v2.core.health.webhook_latency.firing"]

    class V2CoreHealthWebhookLatencyFiringEventData(StripeObject):
        class Impact(StripeObject):
            impacted_requests: int
            """
            The number of impacted requests.
            """

        alert_id: str
        """
        The alert ID.
        """
        grouping_key: str
        """
        The grouping key for the alert.
        """
        impact: Impact
        """
        The user impact.
        """
        started_at: str
        """
        The time when impact on the user experience was first detected.
        """
        summary: str
        """
        A short description of the alert.
        """
        _inner_class_types = {"impact": Impact}

    data: V2CoreHealthWebhookLatencyFiringEventData
    """
    Data for the v2.core.health.webhook_latency.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthWebhookLatencyFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthWebhookLatencyFiringEvent.V2CoreHealthWebhookLatencyFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
