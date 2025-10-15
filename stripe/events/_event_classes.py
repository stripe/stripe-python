# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )


_V2_EVENT_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEvent",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEvent",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEvent",
    ),
}


def get_v2_event_class(type_: str):
    if type_ not in _V2_EVENT_CLASS_LOOKUP:
        return StripeObject

    import_path, class_name = _V2_EVENT_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


_V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEventNotification",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEventNotification",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEventNotification",
    ),
}


def get_v2_event_notification_class(type_: str):
    if type_ not in _V2_EVENT_NOTIFICATION_CLASS_LOOKUP:
        return UnknownEventNotification

    import_path, class_name = _V2_EVENT_NOTIFICATION_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


ALL_EVENT_NOTIFICATIONS = Union[
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V2CoreEventDestinationPingEventNotification",
]
