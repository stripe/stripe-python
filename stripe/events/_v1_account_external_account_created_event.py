# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1AccountExternalAccountCreatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.account.external_account.created"
    type: Literal["v1.account.external_account.created"]

    @override
    def fetch_event(self) -> "V1AccountExternalAccountCreatedEvent":
        return cast(
            "V1AccountExternalAccountCreatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1AccountExternalAccountCreatedEvent":
        return cast(
            "V1AccountExternalAccountCreatedEvent",
            await super().fetch_event_async(),
        )


class V1AccountExternalAccountCreatedEvent(Event):
    LOOKUP_TYPE = "v1.account.external_account.created"
    type: Literal["v1.account.external_account.created"]
