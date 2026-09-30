# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


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
