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

# name -> (import_target, is_submodule)
_import_map = {
    "Event": ("stripe.v2.core._event", False),
    "EventDestination": ("stripe.v2.core._event_destination", False),
    "EventDestinationService": (
        "stripe.v2.core._event_destination_service",
        False,
    ),
    "EventService": ("stripe.v2.core._event_service", False),
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
