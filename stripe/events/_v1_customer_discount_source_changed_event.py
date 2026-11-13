# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1CustomerDiscountSourceChangedEventNotification(EventNotification):
    LOOKUP_TYPE = "v1.customer.discount.source_changed"
    type: Literal["v1.customer.discount.source_changed"]

    @override
    def fetch_event(self) -> "V1CustomerDiscountSourceChangedEvent":
        return cast(
            "V1CustomerDiscountSourceChangedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1CustomerDiscountSourceChangedEvent":
        return cast(
            "V1CustomerDiscountSourceChangedEvent",
            await super().fetch_event_async(),
        )


class V1CustomerDiscountSourceChangedEvent(Event):
    LOOKUP_TYPE = "v1.customer.discount.source_changed"
    type: Literal["v1.customer.discount.source_changed"]
