# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1BillingPortalSessionCreatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.billing_portal.session.created"
    type: Literal["v1.billing_portal.session.created"]

    @override
    def fetch_event(self) -> "V1BillingPortalSessionCreatedEvent":
        return cast(
            "V1BillingPortalSessionCreatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V1BillingPortalSessionCreatedEvent":
        return cast(
            "V1BillingPortalSessionCreatedEvent",
            await super().fetch_event_async(),
        )


class V1BillingPortalSessionCreatedEvent(Event):
    LOOKUP_TYPE = "v1.billing_portal.session.created"
    type: Literal["v1.billing_portal.session.created"]
