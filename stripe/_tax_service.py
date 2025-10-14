# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.tax._calculation_service import CalculationService
from stripe.tax._registration_service import RegistrationService
from stripe.tax._settings_service import SettingsService
from stripe.tax._transaction_service import TransactionService
from importlib import import_module

_subservices = {
    "calculations": ["stripe._account_service", "AccountService"],
    "registrations": ["stripe._account_service", "AccountService"],
    "settings": ["stripe._account_service", "AccountService"],
    "transactions": ["stripe._account_service", "AccountService"],
}


class TaxService(StripeService):
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
