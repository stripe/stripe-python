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


class V2SignalsPaymentRetryEvaluationsRetryRecommendedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.signals.payment_retry_evaluations.retry_recommended"
    type: Literal["v2.signals.payment_retry_evaluations.retry_recommended"]

    @override
    def fetch_event(
        self,
    ) -> "V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent":
        return cast(
            "V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent":
        return cast(
            "V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent",
            await super().fetch_event_async(),
        )


class V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent(Event):
    LOOKUP_TYPE = "v2.signals.payment_retry_evaluations.retry_recommended"
    type: Literal["v2.signals.payment_retry_evaluations.retry_recommended"]

    class V2SignalsPaymentRetryEvaluationsRetryRecommendedEventData(
        StripeObject,
    ):
        id: str
        """
        Unique identifier for the payment retry evaluation.
        """
        livemode: bool
        """
        Whether the event was created in livemode.
        """
        payment_intent: Optional[str]
        """
        The PaymentIntent ID. Present when the evaluation is for a PaymentIntent.
        """
        payment_record: Optional[str]
        """
        The PaymentRecord ID. Present when the evaluation is for a PaymentRecord.
        """

    data: V2SignalsPaymentRetryEvaluationsRetryRecommendedEventData
    """
    Data for the v2.signals.payment_retry_evaluations.retry_recommended event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent.V2SignalsPaymentRetryEvaluationsRetryRecommendedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
