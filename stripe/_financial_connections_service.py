# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.financial_connections._account_service import AccountService
from stripe.financial_connections._session_service import SessionService
from stripe.financial_connections._transaction_service import (
    TransactionService,
)
from importlib import import_module

_subservices = {
    "accounts": ["stripe._account_service", "AccountService"],
    "sessions": ["stripe._account_service", "AccountService"],
    "transactions": ["stripe._account_service", "AccountService"],
}


class FinancialConnectionsService(StripeService):
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
