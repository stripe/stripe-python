# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamStripeAccessGrantApprovedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.approved"
    type: Literal["v2.iam.stripe_access_grant.approved"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantApprovedEvent":
        return cast(
            "V2IamStripeAccessGrantApprovedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantApprovedEvent":
        return cast(
            "V2IamStripeAccessGrantApprovedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantApprovedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.approved"
    type: Literal["v2.iam.stripe_access_grant.approved"]
