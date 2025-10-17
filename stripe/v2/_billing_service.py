# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.billing._bill_setting_service import BillSettingService
from stripe.v2.billing._cadence_service import CadenceService
from stripe.v2.billing._collection_setting_service import (
    CollectionSettingService,
)
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
from stripe.v2.billing._profile_service import ProfileService


class BillingService(StripeService):
    meter_events: "MeterEventService"
    meter_event_adjustments: "MeterEventAdjustmentService"
    meter_event_session: "MeterEventSessionService"
    meter_event_stream: "MeterEventStreamService"

    def __init__(self, requestor):
        super().__init__(requestor)
        self.bill_settings = BillSettingService(self._requestor)
        self.cadences = CadenceService(self._requestor)
        self.collection_settings = CollectionSettingService(self._requestor)
        self.meter_events = MeterEventService(self._requestor)
        self.meter_event_adjustments = MeterEventAdjustmentService(
            self._requestor,
        )
        self.meter_event_session = MeterEventSessionService(self._requestor)
        self.meter_event_stream = MeterEventStreamService(self._requestor)
        self.profiles = ProfileService(self._requestor)
