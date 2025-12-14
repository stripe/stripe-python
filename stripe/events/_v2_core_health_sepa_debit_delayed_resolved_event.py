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


class V2CoreHealthSepaDebitDelayedResolvedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.sepa_debit_delayed.resolved"
    type: Literal["v2.core.health.sepa_debit_delayed.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthSepaDebitDelayedResolvedEvent":
        return cast(
            "V2CoreHealthSepaDebitDelayedResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthSepaDebitDelayedResolvedEvent":
        return cast(
            "V2CoreHealthSepaDebitDelayedResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthSepaDebitDelayedResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.sepa_debit_delayed.resolved"
    type: Literal["v2.core.health.sepa_debit_delayed.resolved"]

    class V2CoreHealthSepaDebitDelayedResolvedEventData(StripeObject):
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

    data: V2CoreHealthSepaDebitDelayedResolvedEventData
    """
    Data for the v2.core.health.sepa_debit_delayed.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthSepaDebitDelayedResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthSepaDebitDelayedResolvedEvent.V2CoreHealthSepaDebitDelayedResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
