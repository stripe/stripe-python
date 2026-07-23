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


class V2CoreHealthElementsErrorResolvedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.elements_error.resolved"
    type: Literal["v2.core.health.elements_error.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthElementsErrorResolvedEvent":
        return cast(
            "V2CoreHealthElementsErrorResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthElementsErrorResolvedEvent":
        return cast(
            "V2CoreHealthElementsErrorResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthElementsErrorResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.elements_error.resolved"
    type: Literal["v2.core.health.elements_error.resolved"]

    class V2CoreHealthElementsErrorResolvedEventData(StripeObject):
        class Impact(StripeObject):
            element_type: Optional[
                Union[Literal["expressCheckout", "payment"], str]
            ]
            """
            The type of the element.
            """
            impacted_sessions: int
            """
            The number of impacted sessions.
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

    data: V2CoreHealthElementsErrorResolvedEventData
    """
    Data for the v2.core.health.elements_error.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthElementsErrorResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthElementsErrorResolvedEvent.V2CoreHealthElementsErrorResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
