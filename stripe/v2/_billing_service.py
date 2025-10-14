# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.billing._meter_event_adjustment_service import (
    MeterEventAdjustmentService,
)
from stripe.v2.billing._meter_event_service import MeterEventService
from stripe.v2.billing._meter_event_session_service import (
    MeterEventSessionService,
)
from stripe.v2.billing._meter_event_stream_service import (
    MeterEventStreamService,
)
from importlib import import_module

_subservices = {
    "meter_events": ["stripe._account_service", "AccountService"],
    "meter_event_adjustments": ["stripe._account_service", "AccountService"],
    "meter_event_session": ["stripe._account_service", "AccountService"],
    "meter_event_stream": ["stripe._account_service", "AccountService"],
}


class BillingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
