# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterErrorReportTriggeredEventNotification,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
    V1BillingMeterNoMeterFoundEventNotification,
)
from stripe.events._v2_core_event_destination_ping_event import (
    V2CoreEventDestinationPingEvent,
    V2CoreEventDestinationPingEventNotification,
)


V2_EVENT_CLASS_LOOKUP = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
}

V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    V1BillingMeterErrorReportTriggeredEventNotification.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterNoMeterFoundEventNotification.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEventNotification,
    V2CoreEventDestinationPingEventNotification.LOOKUP_TYPE: V2CoreEventDestinationPingEventNotification,
}

ALL_EVENT_NOTIFICATIONS = Union[
    V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterNoMeterFoundEventNotification,
    V2CoreEventDestinationPingEventNotification,
]
