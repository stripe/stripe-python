# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.money_management._adjustment_service import (
        AdjustmentService,
    )
    from stripe.v2.money_management._currency_conversion_service import (
        CurrencyConversionService,
    )
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
    from stripe.v2.money_management._recipient_verification_service import (
        RecipientVerificationService,
    )
    from stripe.v2.money_management._transaction_entry_service import (
        TransactionEntryService,
    )
    from stripe.v2.money_management._transaction_service import (
        TransactionService,
    )

_subservices = {
    "adjustments": [
        "stripe.v2.money_management._adjustment_service",
        "AdjustmentService",
    ],
    "currency_conversions": [
        "stripe.v2.money_management._currency_conversion_service",
        "CurrencyConversionService",
    ],
    "financial_accounts": [
        "stripe.v2.money_management._financial_account_service",
        "FinancialAccountService",
    ],
    "financial_addresses": [
        "stripe.v2.money_management._financial_address_service",
        "FinancialAddressService",
    ],
    "inbound_transfers": [
        "stripe.v2.money_management._inbound_transfer_service",
        "InboundTransferService",
    ],
    "outbound_payments": [
        "stripe.v2.money_management._outbound_payment_service",
        "OutboundPaymentService",
    ],
    "outbound_payment_quotes": [
        "stripe.v2.money_management._outbound_payment_quote_service",
        "OutboundPaymentQuoteService",
    ],
    "outbound_setup_intents": [
        "stripe.v2.money_management._outbound_setup_intent_service",
        "OutboundSetupIntentService",
    ],
    "outbound_transfers": [
        "stripe.v2.money_management._outbound_transfer_service",
        "OutboundTransferService",
    ],
    "payout_methods": [
        "stripe.v2.money_management._payout_method_service",
        "PayoutMethodService",
    ],
    "payout_methods_bank_account_spec": [
        "stripe.v2.money_management._payout_methods_bank_account_spec_service",
        "PayoutMethodsBankAccountSpecService",
    ],
    "received_credits": [
        "stripe.v2.money_management._received_credit_service",
        "ReceivedCreditService",
    ],
    "received_debits": [
        "stripe.v2.money_management._received_debit_service",
        "ReceivedDebitService",
    ],
    "recipient_verifications": [
        "stripe.v2.money_management._recipient_verification_service",
        "RecipientVerificationService",
    ],
    "transactions": [
        "stripe.v2.money_management._transaction_service",
        "TransactionService",
    ],
    "transaction_entries": [
        "stripe.v2.money_management._transaction_entry_service",
        "TransactionEntryService",
    ],
}


class MoneyManagementService(StripeService):
    adjustments: "AdjustmentService"
    currency_conversions: "CurrencyConversionService"
    financial_accounts: "FinancialAccountService"
    financial_addresses: "FinancialAddressService"
    inbound_transfers: "InboundTransferService"
    outbound_payments: "OutboundPaymentService"
    outbound_payment_quotes: "OutboundPaymentQuoteService"
    outbound_setup_intents: "OutboundSetupIntentService"
    outbound_transfers: "OutboundTransferService"
    payout_methods: "PayoutMethodService"
    payout_methods_bank_account_spec: "PayoutMethodsBankAccountSpecService"
    received_credits: "ReceivedCreditService"
    received_debits: "ReceivedDebitService"
    recipient_verifications: "RecipientVerificationService"
    transactions: "TransactionService"
    transaction_entries: "TransactionEntryService"

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
