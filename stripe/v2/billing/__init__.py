# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._meter_event import MeterEvent as MeterEvent
    from stripe.v2.billing._meter_event_adjustment import (
        MeterEventAdjustment as MeterEventAdjustment,
    )
    from stripe.v2.billing._meter_event_adjustment_service import (
        MeterEventAdjustmentService as MeterEventAdjustmentService,
    )
    from stripe.v2.billing._meter_event_service import (
        MeterEventService as MeterEventService,
    )
    from stripe.v2.billing._meter_event_session import (
        MeterEventSession as MeterEventSession,
    )
    from stripe.v2.billing._meter_event_session_service import (
        MeterEventSessionService as MeterEventSessionService,
    )
    from stripe.v2.billing._meter_event_stream_service import (
        MeterEventStreamService as MeterEventStreamService,
    )

_submodules = {
    "MeterEvent": "stripe.v2.billing._meter_event",
    "MeterEventAdjustment": "stripe.v2.billing._meter_event_adjustment",
    "MeterEventAdjustmentService": "stripe.v2.billing._meter_event_adjustment_service",
    "MeterEventService": "stripe.v2.billing._meter_event_service",
    "MeterEventSession": "stripe.v2.billing._meter_event_session",
    "MeterEventSessionService": "stripe.v2.billing._meter_event_session_service",
    "MeterEventStreamService": "stripe.v2.billing._meter_event_stream_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
