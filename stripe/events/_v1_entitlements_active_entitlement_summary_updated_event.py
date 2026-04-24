# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v1.entitlements.active_entitlement_summary.updated"
    type: Literal["v1.entitlements.active_entitlement_summary.updated"]

    @override
    def fetch_event(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryUpdatedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryUpdatedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryUpdatedEvent",
            await super().fetch_event_async(),
        )


class V1EntitlementsActiveEntitlementSummaryUpdatedEvent(Event):
    LOOKUP_TYPE = "v1.entitlements.active_entitlement_summary.updated"
    type: Literal["v1.entitlements.active_entitlement_summary.updated"]
