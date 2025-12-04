# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V2IamApiKeyPermissionsUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.permissions_updated"
    type: Literal["v2.iam.api_key.permissions_updated"]

    @override
    def fetch_event(self) -> "V2IamApiKeyPermissionsUpdatedEvent":
        return cast(
            "V2IamApiKeyPermissionsUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyPermissionsUpdatedEvent":
        return cast(
            "V2IamApiKeyPermissionsUpdatedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyPermissionsUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.permissions_updated"
    type: Literal["v2.iam.api_key.permissions_updated"]
