# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.treasury._credit_reversal_service import CreditReversalService
from stripe.treasury._debit_reversal_service import DebitReversalService
from stripe.treasury._financial_account_service import FinancialAccountService
from stripe.treasury._inbound_transfer_service import InboundTransferService
from stripe.treasury._outbound_payment_service import OutboundPaymentService
from stripe.treasury._outbound_transfer_service import OutboundTransferService
from stripe.treasury._received_credit_service import ReceivedCreditService
from stripe.treasury._received_debit_service import ReceivedDebitService
from stripe.treasury._transaction_entry_service import TransactionEntryService
from stripe.treasury._transaction_service import TransactionService
from importlib import import_module

_subservices = {
    "credit_reversals": ["stripe._account_service", "AccountService"],
    "debit_reversals": ["stripe._account_service", "AccountService"],
    "financial_accounts": ["stripe._account_service", "AccountService"],
    "inbound_transfers": ["stripe._account_service", "AccountService"],
    "outbound_payments": ["stripe._account_service", "AccountService"],
    "outbound_transfers": ["stripe._account_service", "AccountService"],
    "received_credits": ["stripe._account_service", "AccountService"],
    "received_debits": ["stripe._account_service", "AccountService"],
    "transactions": ["stripe._account_service", "AccountService"],
    "transaction_entries": ["stripe._account_service", "AccountService"],
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
