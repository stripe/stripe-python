# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, Optional
from typing_extensions import Literal


class V2CoreHealthApiErrorFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.api_error.firing"
    type: Literal["v2.core.health.api_error.firing"]

    class V2CoreHealthApiErrorFiringEventData(StripeObject):
        class Impact(StripeObject):
            canonical_path: str
            """
            The canonical path.
            """
            error_code: Optional[str]
            """
            The error code.
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

    data: V2CoreHealthApiErrorFiringEventData
    """
    Data for the v2.core.health.api_error.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthApiErrorFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthApiErrorFiringEvent.V2CoreHealthApiErrorFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
