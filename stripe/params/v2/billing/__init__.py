# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing._meter_event_adjustment_create_params import (
        MeterEventAdjustmentCreateParams as MeterEventAdjustmentCreateParams,
        MeterEventAdjustmentCreateParamsCancel as MeterEventAdjustmentCreateParamsCancel,
    )
    from stripe.params.v2.billing._meter_event_create_params import (
        MeterEventCreateParams as MeterEventCreateParams,
    )
    from stripe.params.v2.billing._meter_event_session_create_params import (
        MeterEventSessionCreateParams as MeterEventSessionCreateParams,
    )
    from stripe.params.v2.billing._meter_event_stream_create_params import (
        MeterEventStreamCreateParams as MeterEventStreamCreateParams,
        MeterEventStreamCreateParamsEvent as MeterEventStreamCreateParamsEvent,
    )

_submodules = {
    "MeterEventAdjustmentCreateParams": "stripe.params.v2.billing._meter_event_adjustment_create_params",
    "MeterEventAdjustmentCreateParamsCancel": "stripe.params.v2.billing._meter_event_adjustment_create_params",
    "MeterEventCreateParams": "stripe.params.v2.billing._meter_event_create_params",
    "MeterEventSessionCreateParams": "stripe.params.v2.billing._meter_event_session_create_params",
    "MeterEventStreamCreateParams": "stripe.params.v2.billing._meter_event_stream_create_params",
    "MeterEventStreamCreateParamsEvent": "stripe.params.v2.billing._meter_event_stream_create_params",
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
