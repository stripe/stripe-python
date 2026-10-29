# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


class V1EntitlementsActiveEntitlementSummaryEntitlementAddedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = (
        "v1.entitlements.active_entitlement_summary.entitlement_added"
    )
    type: Literal[
        "v1.entitlements.active_entitlement_summary.entitlement_added"
    ]

    @override
    def fetch_event(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent":
        return cast(
            "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent",
            await super().fetch_event_async(),
        )


class V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent(Event):
    LOOKUP_TYPE = (
        "v1.entitlements.active_entitlement_summary.entitlement_added"
    )
    type: Literal[
        "v1.entitlements.active_entitlement_summary.entitlement_added"
    ]
