# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1AccountExternalAccountDeletedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.account.external_account.deleted"
    type: Literal["v1.account.external_account.deleted"]

    @override
    def fetch_event(self) -> "V1AccountExternalAccountDeletedEvent":
        return cast(
            "V1AccountExternalAccountDeletedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1AccountExternalAccountDeletedEvent":
        return cast(
            "V1AccountExternalAccountDeletedEvent",
            await super().fetch_event_async(),
        )


class V1AccountExternalAccountDeletedEvent(Event):
    LOOKUP_TYPE = "v1.account.external_account.deleted"
    type: Literal["v1.account.external_account.deleted"]
