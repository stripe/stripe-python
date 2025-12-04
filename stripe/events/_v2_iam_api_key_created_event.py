# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamApiKeyCreatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.created"
    type: Literal["v2.iam.api_key.created"]

    @override
    def fetch_event(self) -> "V2IamApiKeyCreatedEvent":
        return cast(
            "V2IamApiKeyCreatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyCreatedEvent":
        return cast(
            "V2IamApiKeyCreatedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyCreatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.created"
    type: Literal["v2.iam.api_key.created"]
