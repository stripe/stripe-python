# -*- coding: utf-8 -*-

from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import (
    EventNotification as EventNotification,
    RelatedObject as RelatedObject,
    Reason as Reason,
    ReasonRequest as ReasonRequest,
)

# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.v2.core._event import Event as Event
    from stripe.v2.core._event_destination import (
        EventDestination as EventDestination,
    )
    from stripe.v2.core._event_destination_service import (
        EventDestinationService as EventDestinationService,
    )
    from stripe.v2.core._event_service import EventService as EventService

_submodules = {
    "Event": "stripe.v2.core._event",
    "EventDestination": "stripe.v2.core._event_destination",
    "EventDestinationService": "stripe.v2.core._event_destination_service",
    "EventService": "stripe.v2.core._event_service",
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

# The end of the section generated from our OpenAPI spec
