# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamApiKeyExpiredEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.expired"
    type: Literal["v2.iam.api_key.expired"]

    @override
    def fetch_event(self) -> "V2IamApiKeyExpiredEvent":
        return cast(
            "V2IamApiKeyExpiredEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyExpiredEvent":
        return cast(
            "V2IamApiKeyExpiredEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyExpiredEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.expired"
    type: Literal["v2.iam.api_key.expired"]
