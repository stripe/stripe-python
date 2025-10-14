# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.core._event_destination_service import (
        EventDestinationService,
    )
    from stripe.v2.core._event_service import EventService

_subservices = {
    "events": ["stripe.v2.core._event_service", "EventService"],
    "event_destinations": [
        "stripe.v2.core._event_destination_service",
        "EventDestinationService",
    ],
}


class CoreService(StripeService):
    events: "EventService"
    event_destinations: "EventDestinationService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
