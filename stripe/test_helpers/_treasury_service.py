# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.test_helpers.treasury._inbound_transfer_service import (
    InboundTransferService,
)
from stripe.test_helpers.treasury._outbound_payment_service import (
    OutboundPaymentService,
)
from stripe.test_helpers.treasury._outbound_transfer_service import (
    OutboundTransferService,
)
from stripe.test_helpers.treasury._received_credit_service import (
    ReceivedCreditService,
)
from stripe.test_helpers.treasury._received_debit_service import (
    ReceivedDebitService,
)
from importlib import import_module

_subservices = {
    "inbound_transfers": ["stripe._account_service", "AccountService"],
    "outbound_payments": ["stripe._account_service", "AccountService"],
    "outbound_transfers": ["stripe._account_service", "AccountService"],
    "received_credits": ["stripe._account_service", "AccountService"],
    "received_debits": ["stripe._account_service", "AccountService"],
}


class TreasuryService(StripeService):
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
