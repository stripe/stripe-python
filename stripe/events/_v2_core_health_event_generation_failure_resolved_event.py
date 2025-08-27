# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, Optional
from typing_extensions import Literal


class V2CoreHealthEventGenerationFailureResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.event_generation_failure.resolved"
    type: Literal["v2.core.health.event_generation_failure.resolved"]

    class V2CoreHealthEventGenerationFailureResolvedEventData(StripeObject):
        class Impact(StripeObject):
            account: Optional[str]
            """
            The account id the event should have been generated for. Only present when the account is a connected account.
            """
            event_type: str
            """
            The type of event that Stripe failed to generate.
            """
            livemode: bool
            """
            Indicates if the event was for livemode or not.
            """
            missing_delivery_attempts: int
            """
            The number of webhooks that Stripe failed to create and deliver.
            """
            related_object_id: str
            """
            The related object id.
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
