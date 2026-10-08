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


class V1InvoiceUpcomingEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.invoice.upcoming"
    type: Literal["v1.invoice.upcoming"]

    @override
    def fetch_event(self) -> "V1InvoiceUpcomingEvent":
        return cast(
            "V1InvoiceUpcomingEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V1InvoiceUpcomingEvent":
        return cast(
            "V1InvoiceUpcomingEvent",
            await super().fetch_event_async(),
        )


class V1InvoiceUpcomingEvent(Event):
    LOOKUP_TYPE = "v1.invoice.upcoming"
    type: Literal["v1.invoice.upcoming"]

    class V1InvoiceUpcomingEventData(StripeObject):
        customer: str
        """
        The ID of the customer this upcoming invoice is associated with.
        """
        subscription: Optional[str]
        """
        The ID of the subscription, if any.
        """

    data: V1InvoiceUpcomingEventData
    """
    Data for the v1.invoice.upcoming event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V1InvoiceUpcomingEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V1InvoiceUpcomingEvent.V1InvoiceUpcomingEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
