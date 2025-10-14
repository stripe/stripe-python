# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.core._event_destination_service import EventDestinationService
from stripe.v2.core._event_service import EventService
from importlib import import_module

_subservices = {
    "events": ["stripe._account_service", "AccountService"],
    "event_destinations": ["stripe._account_service", "AccountService"],
}


class CoreService(StripeService):
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
