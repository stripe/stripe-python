# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.test_helpers.issuing._authorization_service import (
    AuthorizationService,
)
from stripe.test_helpers.issuing._card_service import CardService
from stripe.test_helpers.issuing._personalization_design_service import (
    PersonalizationDesignService,
)
from stripe.test_helpers.issuing._transaction_service import TransactionService
from importlib import import_module

_subservices = {
    "authorizations": ["stripe._account_service", "AccountService"],
    "cards": ["stripe._account_service", "AccountService"],
    "personalization_designs": ["stripe._account_service", "AccountService"],
    "transactions": ["stripe._account_service", "AccountService"],
}


class IssuingService(StripeService):
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
