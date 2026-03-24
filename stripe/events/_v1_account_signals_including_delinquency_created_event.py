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


class V1AccountSignalsIncludingDelinquencyCreatedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v1.account_signals[delinquency].created"
    type: Literal["v1.account_signals[delinquency].created"]

    @override
    def fetch_event(
        self,
    ) -> "V1AccountSignalsIncludingDelinquencyCreatedEvent":
        return cast(
            "V1AccountSignalsIncludingDelinquencyCreatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1AccountSignalsIncludingDelinquencyCreatedEvent":
        return cast(
            "V1AccountSignalsIncludingDelinquencyCreatedEvent",
            await super().fetch_event_async(),
        )


class V1AccountSignalsIncludingDelinquencyCreatedEvent(Event):
    LOOKUP_TYPE = "v1.account_signals[delinquency].created"
    type: Literal["v1.account_signals[delinquency].created"]

    class V1AccountSignalsIncludingDelinquencyCreatedEventData(StripeObject):
        class Indicator(StripeObject):
            description: str
            """
            A brief explanation of how this indicator contributed to the delinquency probability.
            """
            impact: Literal[
                "decrease", "neutral", "slight_increase", "strong_increase"
            ]
            """
            The effect this indicator had on the overall risk level.
            """
            indicator: Literal[
                "account_balance",
                "aov",
                "charge_concentration",
                "disputes",
                "dispute_window",
                "duplicates",
                "exposure",
                "firmographic",
                "lifetime_metrics",
                "payment_processing",
                "payment_volume",
                "payouts",
                "refunds",
                "tenure",
                "transfers",
            ]
            """
            The name of the specific indicator used in the risk assessment.
            """

        account: str
        """
        The account for which the signals belong to.
        """
        evaluated_at: str
        """
        Time at which the signal was evaluated.
        """
        indicators: List[Indicator]
        """
        Array of objects representing individual factors that contributed to the calculated probability of delinquency.
        """
        probability: Optional[str]
        """
        The probability of delinquency. Can be between 0.00 and 100.00.
        """
        risk_level: Literal[
            "elevated", "highest", "low", "normal", "not_assessed", "unknown"
        ]
        """
        Categorical assessment of the delinquency risk based on probability.
        """
        signal_id: str
        """
        Unique identifier for the delinquency signal.
        """
        _inner_class_types = {"indicators": Indicator}

    data: V1AccountSignalsIncludingDelinquencyCreatedEventData
    """
    Data for the v1.account_signals[delinquency].created event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V1AccountSignalsIncludingDelinquencyCreatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V1AccountSignalsIncludingDelinquencyCreatedEvent.V1AccountSignalsIncludingDelinquencyCreatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
