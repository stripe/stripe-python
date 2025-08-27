# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._amount import Amount
from stripe.v2._event import Event
from typing import Any, Dict, Optional
from typing_extensions import Literal


class V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent(Event):
    LOOKUP_TYPE = (
        "v2.core.health.issuing_authorization_request_timeout.resolved"
    )
    type: Literal[
        "v2.core.health.issuing_authorization_request_timeout.resolved"
    ]

    class V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventData(
        StripeObject,
    ):
        class Impact(StripeObject):
            approved_amount: Optional[Amount]
            """
            Estimated aggregated amount for the approved requests.
            """
            approved_impacted_requests: Optional[int]
            """
            The number of approved requests which are impacted.
            """
            declined_amount: Optional[Amount]
            """
            Estimated aggregated amount for the declined requests.
            """
            declined_impacted_requests: Optional[int]
            """
            The number of declined requests which are impacted.
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

    data: V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventData
    """
    Data for the v2.core.health.issuing_authorization_request_timeout.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
