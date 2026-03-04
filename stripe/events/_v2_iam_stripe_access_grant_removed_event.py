# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantRemovedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.removed"
    type: Literal["v2.iam.stripe_access_grant.removed"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantRemovedEvent":
        return cast(
            "V2IamStripeAccessGrantRemovedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantRemovedEvent":
        return cast(
            "V2IamStripeAccessGrantRemovedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantRemovedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.removed"
    type: Literal["v2.iam.stripe_access_grant.removed"]
