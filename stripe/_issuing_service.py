# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.issuing._authorization_service import AuthorizationService
from stripe.issuing._card_service import CardService
from stripe.issuing._cardholder_service import CardholderService
from stripe.issuing._dispute_service import DisputeService
from stripe.issuing._personalization_design_service import (
    PersonalizationDesignService,
)
from stripe.issuing._physical_bundle_service import PhysicalBundleService
from stripe.issuing._token_service import TokenService
from stripe.issuing._transaction_service import TransactionService
from importlib import import_module

_subservices = {
    "authorizations": ["stripe._account_service", "AccountService"],
    "cards": ["stripe._account_service", "AccountService"],
    "cardholders": ["stripe._account_service", "AccountService"],
    "disputes": ["stripe._account_service", "AccountService"],
    "personalization_designs": ["stripe._account_service", "AccountService"],
    "physical_bundles": ["stripe._account_service", "AccountService"],
    "tokens": ["stripe._account_service", "AccountService"],
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
