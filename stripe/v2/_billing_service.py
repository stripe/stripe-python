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


class BillingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.meter_event_adjustments = MeterEventAdjustmentService(
            self._requestor,
        )
        self.meter_event_session = MeterEventSessionService(self._requestor)
        self.meter_event_stream = MeterEventStreamService(self._requestor)
        self.meter_events = MeterEventService(self._requestor)
