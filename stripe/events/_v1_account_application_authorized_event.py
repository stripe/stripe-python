# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1AccountApplicationAuthorizedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.account.application.authorized"
    type: Literal["v1.account.application.authorized"]

    @override
    def fetch_event(self) -> "V1AccountApplicationAuthorizedEvent":
        return cast(
            "V1AccountApplicationAuthorizedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V1AccountApplicationAuthorizedEvent":
        return cast(
            "V1AccountApplicationAuthorizedEvent",
            await super().fetch_event_async(),
        )


class V1AccountApplicationAuthorizedEvent(Event):
    LOOKUP_TYPE = "v1.account.application.authorized"
    type: Literal["v1.account.application.authorized"]
