# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.test_helpers._confirmation_token_service import (
    ConfirmationTokenService,
)
from stripe.test_helpers._customer_service import CustomerService
from stripe.test_helpers._issuing_service import IssuingService
from stripe.test_helpers._refund_service import RefundService
from stripe.test_helpers._terminal_service import TerminalService
from stripe.test_helpers._test_clock_service import TestClockService
from stripe.test_helpers._treasury_service import TreasuryService
from importlib import import_module

_subservices = {
    "confirmation_tokens": ["stripe._account_service", "AccountService"],
    "customers": ["stripe._account_service", "AccountService"],
    "issuing": ["stripe._account_service", "AccountService"],
    "refunds": ["stripe._account_service", "AccountService"],
    "terminal": ["stripe._account_service", "AccountService"],
    "test_clocks": ["stripe._account_service", "AccountService"],
    "treasury": ["stripe._account_service", "AccountService"],
}


class TestHelpersService(StripeService):
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
