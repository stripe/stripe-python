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


class V2CoreHealthWebhookLatencyResolvedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.webhook_latency.resolved"
    type: Literal["v2.core.health.webhook_latency.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthWebhookLatencyResolvedEvent":
        return cast(
            "V2CoreHealthWebhookLatencyResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthWebhookLatencyResolvedEvent":
        return cast(
            "V2CoreHealthWebhookLatencyResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthWebhookLatencyResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.webhook_latency.resolved"
    type: Literal["v2.core.health.webhook_latency.resolved"]

    class V2CoreHealthWebhookLatencyResolvedEventData(StripeObject):
        class Impact(StripeObject):
            impacted_requests: int
            """
            The number of impacted requests.
            """

        grouping_key: str
        """
        The grouping key for the alert.
        """
        impact: Impact
        """
        The user impact.
        """
        resolved_at: str
        """
        The time when the user experience has returned to expected levels.
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

    data: V2CoreHealthWebhookLatencyResolvedEventData
    """
    Data for the v2.core.health.webhook_latency.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthWebhookLatencyResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthWebhookLatencyResolvedEvent.V2CoreHealthWebhookLatencyResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
