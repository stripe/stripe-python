# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantRequestedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.requested"
    type: Literal["v2.iam.stripe_access_grant.requested"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantRequestedEvent":
        return cast(
            "V2IamStripeAccessGrantRequestedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2IamStripeAccessGrantRequestedEvent":
        return cast(
            "V2IamStripeAccessGrantRequestedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantRequestedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.requested"
    type: Literal["v2.iam.stripe_access_grant.requested"]
