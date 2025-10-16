# -*- coding: utf-8 -*-

from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import (
    UnknownEventNotification as UnknownEventNotification,
)


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.events._event_classes import (
        ALL_EVENT_NOTIFICATIONS as ALL_EVENT_NOTIFICATIONS,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEvent as V1BillingMeterErrorReportTriggeredEvent,
        V1BillingMeterErrorReportTriggeredEventNotification as V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEvent as V1BillingMeterNoMeterFoundEvent,
        V1BillingMeterNoMeterFoundEventNotification as V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEvent as V2CoreEventDestinationPingEvent,
        V2CoreEventDestinationPingEventNotification as V2CoreEventDestinationPingEventNotification,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ALL_EVENT_NOTIFICATIONS": ("stripe.events._event_classes", False),
    "V1BillingMeterErrorReportTriggeredEvent": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterErrorReportTriggeredEventNotification": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEvent": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEventNotification": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V2CoreEventDestinationPingEvent": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
    "V2CoreEventDestinationPingEventNotification": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()

# The end of the section generated from our OpenAPI spec
