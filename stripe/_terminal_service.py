# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.terminal._configuration_service import ConfigurationService
from stripe.terminal._connection_token_service import ConnectionTokenService
from stripe.terminal._location_service import LocationService
from stripe.terminal._reader_service import ReaderService
from importlib import import_module

_subservices = {
    "configurations": ["stripe._account_service", "AccountService"],
    "connection_tokens": ["stripe._account_service", "AccountService"],
    "locations": ["stripe._account_service", "AccountService"],
    "readers": ["stripe._account_service", "AccountService"],
}


class TerminalService(StripeService):
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
