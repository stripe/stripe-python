# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
    PushedV1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
    PushedV1BillingMeterNoMeterFoundEvent,
)
from stripe.events._v2_core_event_destination_ping_event import (
    V2CoreEventDestinationPingEvent,
    PushedV2CoreEventDestinationPingEvent,
)


THIN_EVENT_CLASSES = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
}

PUSHED_THIN_EVENT_CLASSES = {
    PushedV1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: PushedV1BillingMeterErrorReportTriggeredEvent,
    PushedV1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: PushedV1BillingMeterNoMeterFoundEvent,
    PushedV2CoreEventDestinationPingEvent.LOOKUP_TYPE: PushedV2CoreEventDestinationPingEvent,
}

All_PUSHED_THIN_EVENTS = Union[
    PushedV1BillingMeterErrorReportTriggeredEvent,
    PushedV1BillingMeterNoMeterFoundEvent,
    PushedV2CoreEventDestinationPingEvent,
]
