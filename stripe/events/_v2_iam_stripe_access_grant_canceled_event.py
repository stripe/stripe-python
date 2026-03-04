# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantCanceledEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.canceled"
    type: Literal["v2.iam.stripe_access_grant.canceled"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantCanceledEvent":
        return cast(
            "V2IamStripeAccessGrantCanceledEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantCanceledEvent":
        return cast(
            "V2IamStripeAccessGrantCanceledEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantCanceledEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.canceled"
    type: Literal["v2.iam.stripe_access_grant.canceled"]
