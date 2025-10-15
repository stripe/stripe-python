# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from importlib import import_module

if TYPE_CHECKING:
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

# hardcode lookups
V2_EVENT_CLASS_LOOKUP = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
}


def get_v2_event_class(type_):
    if type_ not in V2_EVENT_CLASS_LOOKUP:
        return UnknownEventNotification

    import_path, class_name = V2_EVENT_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    V1BillingMeterErrorReportTriggeredEventNotification.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterNoMeterFoundEventNotification.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEventNotification,
    V2CoreEventDestinationPingEventNotification.LOOKUP_TYPE: V2CoreEventDestinationPingEventNotification,
}


def get_v2_event_notification_class(type_):
    if type_ not in V2_EVENT_NOTIFICATION_CLASS_LOOKUP:
        return UnknownEventNotification

    import_path, class_name = V2_EVENT_NOTIFICATION_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


ALL_EVENT_NOTIFICATIONS = Union[
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V2CoreEventDestinationPingEventNotification",
]
