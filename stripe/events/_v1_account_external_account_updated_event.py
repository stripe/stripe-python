# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1AccountExternalAccountUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.account.external_account.updated"
    type: Literal["v1.account.external_account.updated"]

    @override
    def fetch_event(self) -> "V1AccountExternalAccountUpdatedEvent":
        return cast(
            "V1AccountExternalAccountUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1AccountExternalAccountUpdatedEvent":
        return cast(
            "V1AccountExternalAccountUpdatedEvent",
            await super().fetch_event_async(),
        )


class V1AccountExternalAccountUpdatedEvent(Event):
    LOOKUP_TYPE = "v1.account.external_account.updated"
    type: Literal["v1.account.external_account.updated"]
