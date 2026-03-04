# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantDeniedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.denied"
    type: Literal["v2.iam.stripe_access_grant.denied"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantDeniedEvent":
        return cast(
            "V2IamStripeAccessGrantDeniedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantDeniedEvent":
        return cast(
            "V2IamStripeAccessGrantDeniedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantDeniedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.denied"
    type: Literal["v2.iam.stripe_access_grant.denied"]
