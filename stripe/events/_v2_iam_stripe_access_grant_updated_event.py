# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.updated"
    type: Literal["v2.iam.stripe_access_grant.updated"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantUpdatedEvent":
        return cast(
            "V2IamStripeAccessGrantUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantUpdatedEvent":
        return cast(
            "V2IamStripeAccessGrantUpdatedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.updated"
    type: Literal["v2.iam.stripe_access_grant.updated"]
