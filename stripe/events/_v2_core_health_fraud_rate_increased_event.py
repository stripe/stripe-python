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


class V2CoreHealthFraudRateIncreasedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.fraud_rate.increased"
    type: Literal["v2.core.health.fraud_rate.increased"]

    @override
    def fetch_event(self) -> "V2CoreHealthFraudRateIncreasedEvent":
        return cast(
            "V2CoreHealthFraudRateIncreasedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2CoreHealthFraudRateIncreasedEvent":
        return cast(
            "V2CoreHealthFraudRateIncreasedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthFraudRateIncreasedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.fraud_rate.increased"
    type: Literal["v2.core.health.fraud_rate.increased"]

    class V2CoreHealthFraudRateIncreasedEventData(StripeObject):
        class Impact(StripeObject):
            class RealizedFraudAmount(StripeObject):
                currency: Optional[str]
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: Optional[int]
                """
                A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
                """

            attack_type: Literal["spike", "sustained_attack"]
            """
            Fraud attack type.
            """
            impacted_requests: int
            """
            The number of impacted requests which are detected.
            """
            realized_fraud_amount: RealizedFraudAmount
            """
            Estimated aggregated amount for the impacted requests.
            """
            _inner_class_types = {"realized_fraud_amount": RealizedFraudAmount}

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
