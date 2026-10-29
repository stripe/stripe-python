# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = (
        "v1.entitlements.active_entitlement_summary.entitlement_removed"
    )
    type: Literal[
        "v1.entitlements.active_entitlement_summary.entitlement_removed"
    ]

    @override
    def fetch_event(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent",
            await super().fetch_event_async(),
        )


class V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent(Event):
    LOOKUP_TYPE = (
        "v1.entitlements.active_entitlement_summary.entitlement_removed"
    )
    type: Literal[
        "v1.entitlements.active_entitlement_summary.entitlement_removed"
    ]
