# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1AccountApplicationDeauthorizedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.account.application.deauthorized"
    type: Literal["v1.account.application.deauthorized"]

    @override
    def fetch_event(self) -> "V1AccountApplicationDeauthorizedEvent":
        return cast(
            "V1AccountApplicationDeauthorizedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1AccountApplicationDeauthorizedEvent":
        return cast(
            "V1AccountApplicationDeauthorizedEvent",
            await super().fetch_event_async(),
        )


class V1AccountApplicationDeauthorizedEvent(Event):
    LOOKUP_TYPE = "v1.account.application.deauthorized"
    type: Literal["v1.account.application.deauthorized"]
