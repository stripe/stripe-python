# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2PaymentsSettlementAllocationIntentNotFoundEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.payments.settlement_allocation_intent.not_found"
    type: Literal["v2.payments.settlement_allocation_intent.not_found"]

    @override
    def fetch_event(
        self,
    ) -> "V2PaymentsSettlementAllocationIntentNotFoundEvent":
        return cast(
            "V2PaymentsSettlementAllocationIntentNotFoundEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2PaymentsSettlementAllocationIntentNotFoundEvent":
        return cast(
            "V2PaymentsSettlementAllocationIntentNotFoundEvent",
            await super().fetch_event_async(),
        )


class V2PaymentsSettlementAllocationIntentNotFoundEvent(Event):
    LOOKUP_TYPE = "v2.payments.settlement_allocation_intent.not_found"
    type: Literal["v2.payments.settlement_allocation_intent.not_found"]

    class V2PaymentsSettlementAllocationIntentNotFoundEventData(StripeObject):
        received_credit_id: str
        """
        The ID of the ReceivedCredit.
        """

    data: V2PaymentsSettlementAllocationIntentNotFoundEventData
    """
    Data for the v2.payments.settlement_allocation_intent.not_found event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2PaymentsSettlementAllocationIntentNotFoundEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2PaymentsSettlementAllocationIntentNotFoundEvent.V2PaymentsSettlementAllocationIntentNotFoundEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
