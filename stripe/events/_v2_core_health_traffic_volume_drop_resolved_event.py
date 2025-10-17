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


class V2CoreHealthTrafficVolumeDropResolvedEventNotification(
    EventNotification
):
    LOOKUP_TYPE = "v2.core.health.traffic_volume_drop.resolved"
    type: Literal["v2.core.health.traffic_volume_drop.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthTrafficVolumeDropResolvedEvent":
        return cast(
            "V2CoreHealthTrafficVolumeDropResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthTrafficVolumeDropResolvedEvent":
        return cast(
            "V2CoreHealthTrafficVolumeDropResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthTrafficVolumeDropResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.traffic_volume_drop.resolved"
    type: Literal["v2.core.health.traffic_volume_drop.resolved"]

    class V2CoreHealthTrafficVolumeDropResolvedEventData(StripeObject):
        class Impact(StripeObject):
            actual_traffic: int
            """
            The total volume of payment requests within the latest observation time window.
            """
            expected_traffic: Optional[int]
            """
            The expected volume of payment requests within the latest observation time window.
            """
            time_window: str
            """
            The size of the observation time window.
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

    data: V2CoreHealthTrafficVolumeDropResolvedEventData
    """
    Data for the v2.core.health.traffic_volume_drop.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthTrafficVolumeDropResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthTrafficVolumeDropResolvedEvent.V2CoreHealthTrafficVolumeDropResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
