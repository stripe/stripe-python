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


class V2CoreHealthSepaDebitDelayedFiringEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.sepa_debit_delayed.firing"
    type: Literal["v2.core.health.sepa_debit_delayed.firing"]

    @override
    def fetch_event(self) -> "V2CoreHealthSepaDebitDelayedFiringEvent":
        return cast(
            "V2CoreHealthSepaDebitDelayedFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthSepaDebitDelayedFiringEvent":
        return cast(
            "V2CoreHealthSepaDebitDelayedFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthSepaDebitDelayedFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.sepa_debit_delayed.firing"
    type: Literal["v2.core.health.sepa_debit_delayed.firing"]

    class V2CoreHealthSepaDebitDelayedFiringEventData(StripeObject):
        class Impact(StripeObject):
            impacted_payments: int
            """
            The number of impacted payments.
            """
            impacted_payments_percentage: str
            """
            The percentage of impacted payments.
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

    data: V2CoreHealthSepaDebitDelayedFiringEventData
    """
    Data for the v2.core.health.sepa_debit_delayed.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthSepaDebitDelayedFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthSepaDebitDelayedFiringEvent.V2CoreHealthSepaDebitDelayedFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
