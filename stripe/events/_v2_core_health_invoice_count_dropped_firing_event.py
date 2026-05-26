# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthInvoiceCountDroppedFiringEventNotification(
    EventNotification
):
    LOOKUP_TYPE = "v2.core.health.invoice_count_dropped.firing"
    type: Literal["v2.core.health.invoice_count_dropped.firing"]

    @override
    def fetch_event(self) -> "V2CoreHealthInvoiceCountDroppedFiringEvent":
        return cast(
            "V2CoreHealthInvoiceCountDroppedFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthInvoiceCountDroppedFiringEvent":
        return cast(
            "V2CoreHealthInvoiceCountDroppedFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthInvoiceCountDroppedFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.invoice_count_dropped.firing"
    type: Literal["v2.core.health.invoice_count_dropped.firing"]

    class V2CoreHealthInvoiceCountDroppedFiringEventData(StripeObject):
        class Impact(StripeObject):
            observed_count: Decimal
            """
            The observed number of invoices within the time window.
            """
            threshold_count: Decimal
            """
            The expected threshold number of invoices within the time window.
            """
            time_window: str
            """
            The size of the observation time window.
            """
            _field_encodings = {
                "observed_count": "decimal_string",
                "threshold_count": "decimal_string",
            }

        alert_id: str
        """
        The alert ID.
        """
        grouping_key: str
        """
        The grouping key for the alert.
        """
        impact: Impact
        """
        The user impact.
        """
        started_at: str
        """
        The time when impact on the user experience was first detected.
        """
        summary: str
        """
        A short description of the alert.
        """
        _inner_class_types = {"impact": Impact}

    data: V2CoreHealthInvoiceCountDroppedFiringEventData
    """
    Data for the v2.core.health.invoice_count_dropped.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthInvoiceCountDroppedFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthInvoiceCountDroppedFiringEvent.V2CoreHealthInvoiceCountDroppedFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
