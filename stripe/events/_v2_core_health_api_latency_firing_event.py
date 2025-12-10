# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthApiLatencyFiringEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.api_latency.firing"
    type: Literal["v2.core.health.api_latency.firing"]

    @override
    def fetch_event(self) -> "V2CoreHealthApiLatencyFiringEvent":
        return cast(
            "V2CoreHealthApiLatencyFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2CoreHealthApiLatencyFiringEvent":
        return cast(
            "V2CoreHealthApiLatencyFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthApiLatencyFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.api_latency.firing"
    type: Literal["v2.core.health.api_latency.firing"]

    class V2CoreHealthApiLatencyFiringEventData(StripeObject):
        class Impact(StripeObject):
            class TopImpactedAccount(StripeObject):
                account: str
                """
                The account ID of the impacted connected account.
                """
                impacted_requests: int
                """
                The number of impacted requests.
                """
                impacted_requests_percentage: Optional[str]
                """
                The percentage of impacted requests.
                """

            canonical_path: str
            """
            The canonical path.
            """
            http_method: Literal["DELETE", "GET", "POST", "PUT"]
            """
            The HTTP method.
            """
            http_status: str
            """
            The HTTP status.
            """
            impacted_requests: int
            """
            The number of impacted requests.
            """
            impacted_requests_percentage: Optional[str]
            """
            The percentage of impacted requests.
            """
            top_impacted_accounts: Optional[List[TopImpactedAccount]]
            """
            The top impacted connected accounts (only for platforms).
            """
            _inner_class_types = {"top_impacted_accounts": TopImpactedAccount}

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

    data: V2CoreHealthApiLatencyFiringEventData
    """
    Data for the v2.core.health.api_latency.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthApiLatencyFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthApiLatencyFiringEvent.V2CoreHealthApiLatencyFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
