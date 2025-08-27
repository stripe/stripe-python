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


class V2CoreHealthFraudRateIncreasedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.fraud_rate.increased"
    type: Literal["v2.core.health.fraud_rate.increased"]

    class V2CoreHealthFraudRateIncreasedEventData(StripeObject):
        class Impact(StripeObject):
            attack_type: Literal["spike", "sustained_attack"]
            """
            Fraud attack type.
            """
            impacted_requests: int
            """
            The number of impacted requests which are detected.
            """
            realized_fraud_amount: Amount
            """
            Estimated aggregated amount for the impacted requests.
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
        resolved_at: Optional[str]
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

    data: V2CoreHealthFraudRateIncreasedEventData
    """
    Data for the v2.core.health.fraud_rate.increased event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthFraudRateIncreasedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthFraudRateIncreasedEvent.V2CoreHealthFraudRateIncreasedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
