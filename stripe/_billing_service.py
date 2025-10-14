# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.billing._alert_service import AlertService
from stripe.billing._credit_balance_summary_service import (
    CreditBalanceSummaryService,
)
from stripe.billing._credit_balance_transaction_service import (
    CreditBalanceTransactionService,
)
from stripe.billing._credit_grant_service import CreditGrantService
from stripe.billing._meter_event_adjustment_service import (
    MeterEventAdjustmentService,
)
from stripe.billing._meter_event_service import MeterEventService
from stripe.billing._meter_service import MeterService
from importlib import import_module

_subservices = {
    "alerts": ["stripe._account_service", "AccountService"],
    "credit_balance_summary": ["stripe._account_service", "AccountService"],
    "credit_balance_transactions": [
        "stripe._account_service",
        "AccountService",
    ],
    "credit_grants": ["stripe._account_service", "AccountService"],
    "meters": ["stripe._account_service", "AccountService"],
    "meter_events": ["stripe._account_service", "AccountService"],
    "meter_event_adjustments": ["stripe._account_service", "AccountService"],
}


class BillingService(StripeService):
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
