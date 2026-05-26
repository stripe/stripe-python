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


class V2CoreHealthInvoiceCountDroppedResolvedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.core.health.invoice_count_dropped.resolved"
    type: Literal["v2.core.health.invoice_count_dropped.resolved"]

    @override
    def fetch_event(self) -> "V2CoreHealthInvoiceCountDroppedResolvedEvent":
        return cast(
            "V2CoreHealthInvoiceCountDroppedResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthInvoiceCountDroppedResolvedEvent":
        return cast(
            "V2CoreHealthInvoiceCountDroppedResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthInvoiceCountDroppedResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.invoice_count_dropped.resolved"
    type: Literal["v2.core.health.invoice_count_dropped.resolved"]

    class V2CoreHealthInvoiceCountDroppedResolvedEventData(StripeObject):
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
        resolved_at: str
        """
        The time when the user experience has returned to expected levels.
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

    data: V2CoreHealthInvoiceCountDroppedResolvedEventData
    """
    Data for the v2.core.health.invoice_count_dropped.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthInvoiceCountDroppedResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthInvoiceCountDroppedResolvedEvent.V2CoreHealthInvoiceCountDroppedResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
