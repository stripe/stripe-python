# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamApiKeyUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.updated"
    type: Literal["v2.iam.api_key.updated"]

    @override
    def fetch_event(self) -> "V2IamApiKeyUpdatedEvent":
        return cast(
            "V2IamApiKeyUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyUpdatedEvent":
        return cast(
            "V2IamApiKeyUpdatedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.updated"
    type: Literal["v2.iam.api_key.updated"]
