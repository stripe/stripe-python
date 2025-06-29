# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.money_management._adjustment_service import AdjustmentService
from stripe.v2.money_management._financial_account_service import (
    FinancialAccountService,
)
from stripe.v2.money_management._financial_address_service import (
    FinancialAddressService,
)
from stripe.v2.money_management._inbound_transfer_service import (
    InboundTransferService,
)
from stripe.v2.money_management._outbound_payment_quote_service import (
    OutboundPaymentQuoteService,
)
from stripe.v2.money_management._outbound_payment_service import (
    OutboundPaymentService,
)
from stripe.v2.money_management._outbound_setup_intent_service import (
    OutboundSetupIntentService,
)
from stripe.v2.money_management._outbound_transfer_service import (
    OutboundTransferService,
)
from stripe.v2.money_management._payout_method_service import (
    PayoutMethodService,
)
from stripe.v2.money_management._payout_methods_bank_account_spec_service import (
    PayoutMethodsBankAccountSpecService,
)
from stripe.v2.money_management._received_credit_service import (
    ReceivedCreditService,
)
from stripe.v2.money_management._received_debit_service import (
    ReceivedDebitService,
)
from stripe.v2.money_management._transaction_entry_service import (
    TransactionEntryService,
)
from stripe.v2.money_management._transaction_service import TransactionService


class MoneyManagementService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.adjustments = AdjustmentService(self._requestor)
        self.financial_accounts = FinancialAccountService(self._requestor)
        self.financial_addresses = FinancialAddressService(self._requestor)
        self.inbound_transfers = InboundTransferService(self._requestor)
        self.outbound_payment_quotes = OutboundPaymentQuoteService(
            self._requestor,
        )
        self.outbound_payments = OutboundPaymentService(self._requestor)
        self.outbound_setup_intents = OutboundSetupIntentService(
            self._requestor,
        )
        self.outbound_transfers = OutboundTransferService(self._requestor)
        self.payout_methods = PayoutMethodService(self._requestor)
        self.payout_methods_bank_account_spec = (
            PayoutMethodsBankAccountSpecService(
                self._requestor,
            )
        )
        self.received_credits = ReceivedCreditService(self._requestor)
        self.received_debits = ReceivedDebitService(self._requestor)
        self.transaction_entries = TransactionEntryService(self._requestor)
        self.transactions = TransactionService(self._requestor)
