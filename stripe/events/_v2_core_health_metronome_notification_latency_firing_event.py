# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, Union, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthMetronomeNotificationLatencyFiringEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.core.health.metronome_notification_latency.firing"
    type: Literal["v2.core.health.metronome_notification_latency.firing"]

    @override
    def fetch_event(
        self,
    ) -> "V2CoreHealthMetronomeNotificationLatencyFiringEvent":
        return cast(
            "V2CoreHealthMetronomeNotificationLatencyFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthMetronomeNotificationLatencyFiringEvent":
        return cast(
            "V2CoreHealthMetronomeNotificationLatencyFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthMetronomeNotificationLatencyFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.metronome_notification_latency.firing"
    type: Literal["v2.core.health.metronome_notification_latency.firing"]

    class V2CoreHealthMetronomeNotificationLatencyFiringEventData(
        StripeObject
    ):
        class Impact(StripeObject):
            pipeline: Union[
                Literal[
                    "configuration_triggered",
                    "high_cardinality_usage_triggered",
                    "standard_usage_triggered",
                    "time_triggered",
                ],
                str,
            ]
            """
            The impacted Metronome billing pipeline.
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

    data: V2CoreHealthMetronomeNotificationLatencyFiringEventData
    """
    Data for the v2.core.health.metronome_notification_latency.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthMetronomeNotificationLatencyFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthMetronomeNotificationLatencyFiringEvent.V2CoreHealthMetronomeNotificationLatencyFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
