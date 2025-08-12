# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
)
from stripe.events._v2_core_event_destination_ping_event import (
    V2CoreEventDestinationPingEvent,
)


THIN_EVENT_CLASSES = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
}
