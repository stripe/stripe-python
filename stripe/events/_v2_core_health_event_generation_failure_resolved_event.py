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


class V2CoreHealthEventGenerationFailureResolvedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.core.health.event_generation_failure.resolved"
    type: Literal["v2.core.health.event_generation_failure.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthEventGenerationFailureResolvedEvent":
        return cast(
            "V2CoreHealthEventGenerationFailureResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthEventGenerationFailureResolvedEvent":
        return cast(
            "V2CoreHealthEventGenerationFailureResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthEventGenerationFailureResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.event_generation_failure.resolved"
    type: Literal["v2.core.health.event_generation_failure.resolved"]

    class V2CoreHealthEventGenerationFailureResolvedEventData(StripeObject):
        class Impact(StripeObject):
            class RelatedObject(StripeObject):
                id: str
                """
                The ID of the related object (e.g., "pi_...").
                """
                type: str
                """
                The type of the related object (e.g., "payment_intent").
                """
                url: str
                """
                The API URL for the related object (e.g., "/v1/payment_intents/pi_...").
                """

            context: Optional[str]
            """
            The context the event should have been generated for. Only present when the account is a connected account.
            """
            event_type: str
            """
            The type of event that Stripe failed to generate.
            """
            related_object: RelatedObject
            """
            The related object details.
            """
            _inner_class_types = {"related_object": RelatedObject}

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
        summary: str
        """
        A short description of the alert.
        """
        _inner_class_types = {"impact": Impact}

    data: V2CoreHealthEventGenerationFailureResolvedEventData
    """
    Data for the v2.core.health.event_generation_failure.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthEventGenerationFailureResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthEventGenerationFailureResolvedEvent.V2CoreHealthEventGenerationFailureResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
