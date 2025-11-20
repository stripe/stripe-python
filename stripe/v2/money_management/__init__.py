# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.money_management._adjustment import Adjustment as Adjustment
    from stripe.v2.money_management._adjustment_service import (
        AdjustmentService as AdjustmentService,
    )
    from stripe.v2.money_management._currency_conversion import (
        CurrencyConversion as CurrencyConversion,
    )
    from stripe.v2.money_management._currency_conversion_service import (
        CurrencyConversionService as CurrencyConversionService,
    )
    from stripe.v2.money_management._financial_account import (
        FinancialAccount as FinancialAccount,
    )
    from stripe.v2.money_management._financial_account_service import (
        FinancialAccountService as FinancialAccountService,
    )
    from stripe.v2.money_management._financial_address import (
        FinancialAddress as FinancialAddress,
    )
    from stripe.v2.money_management._financial_address_service import (
        FinancialAddressService as FinancialAddressService,
    )
    from stripe.v2.money_management._inbound_transfer import (
        InboundTransfer as InboundTransfer,
    )
    from stripe.v2.money_management._inbound_transfer_service import (
        InboundTransferService as InboundTransferService,
    )
    from stripe.v2.money_management._outbound_payment import (
        OutboundPayment as OutboundPayment,
    )
    from stripe.v2.money_management._outbound_payment_quote import (
        OutboundPaymentQuote as OutboundPaymentQuote,
    )
    from stripe.v2.money_management._outbound_payment_quote_service import (
        OutboundPaymentQuoteService as OutboundPaymentQuoteService,
    )
    from stripe.v2.money_management._outbound_payment_service import (
        OutboundPaymentService as OutboundPaymentService,
    )
    from stripe.v2.money_management._outbound_setup_intent import (
        OutboundSetupIntent as OutboundSetupIntent,
    )
    from stripe.v2.money_management._outbound_setup_intent_service import (
        OutboundSetupIntentService as OutboundSetupIntentService,
    )
    from stripe.v2.money_management._outbound_transfer import (
        OutboundTransfer as OutboundTransfer,
    )
    from stripe.v2.money_management._outbound_transfer_service import (
        OutboundTransferService as OutboundTransferService,
    )
    from stripe.v2.money_management._payout_method import (
        PayoutMethod as PayoutMethod,
    )
    from stripe.v2.money_management._payout_method_service import (
        PayoutMethodService as PayoutMethodService,
    )
    from stripe.v2.money_management._payout_methods_bank_account_spec import (
        PayoutMethodsBankAccountSpec as PayoutMethodsBankAccountSpec,
    )
    from stripe.v2.money_management._payout_methods_bank_account_spec_service import (
        PayoutMethodsBankAccountSpecService as PayoutMethodsBankAccountSpecService,
    )
    from stripe.v2.money_management._received_credit import (
        ReceivedCredit as ReceivedCredit,
    )
    from stripe.v2.money_management._received_credit_service import (
        ReceivedCreditService as ReceivedCreditService,
    )
    from stripe.v2.money_management._received_debit import (
        ReceivedDebit as ReceivedDebit,
    )
    from stripe.v2.money_management._received_debit_service import (
        ReceivedDebitService as ReceivedDebitService,
    )
    from stripe.v2.money_management._recipient_verification import (
        RecipientVerification as RecipientVerification,
    )
    from stripe.v2.money_management._recipient_verification_service import (
        RecipientVerificationService as RecipientVerificationService,
    )
    from stripe.v2.money_management._transaction import (
        Transaction as Transaction,
    )
    from stripe.v2.money_management._transaction_entry import (
        TransactionEntry as TransactionEntry,
    )
    from stripe.v2.money_management._transaction_entry_service import (
        TransactionEntryService as TransactionEntryService,
    )
    from stripe.v2.money_management._transaction_service import (
        TransactionService as TransactionService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Adjustment": ("stripe.v2.money_management._adjustment", False),
    "AdjustmentService": (
        "stripe.v2.money_management._adjustment_service",
        False,
    ),
    "CurrencyConversion": (
        "stripe.v2.money_management._currency_conversion",
        False,
    ),
    "CurrencyConversionService": (
        "stripe.v2.money_management._currency_conversion_service",
        False,
    ),
    "FinancialAccount": (
        "stripe.v2.money_management._financial_account",
        False,
    ),
    "FinancialAccountService": (
        "stripe.v2.money_management._financial_account_service",
        False,
    ),
    "FinancialAddress": (
        "stripe.v2.money_management._financial_address",
        False,
    ),
    "FinancialAddressService": (
        "stripe.v2.money_management._financial_address_service",
        False,
    ),
    "InboundTransfer": ("stripe.v2.money_management._inbound_transfer", False),
    "InboundTransferService": (
        "stripe.v2.money_management._inbound_transfer_service",
        False,
    ),
    "OutboundPayment": ("stripe.v2.money_management._outbound_payment", False),
    "OutboundPaymentQuote": (
        "stripe.v2.money_management._outbound_payment_quote",
        False,
    ),
    "OutboundPaymentQuoteService": (
        "stripe.v2.money_management._outbound_payment_quote_service",
        False,
    ),
    "OutboundPaymentService": (
        "stripe.v2.money_management._outbound_payment_service",
        False,
    ),
    "OutboundSetupIntent": (
        "stripe.v2.money_management._outbound_setup_intent",
        False,
    ),
    "OutboundSetupIntentService": (
        "stripe.v2.money_management._outbound_setup_intent_service",
        False,
    ),
    "OutboundTransfer": (
        "stripe.v2.money_management._outbound_transfer",
        False,
    ),
    "OutboundTransferService": (
        "stripe.v2.money_management._outbound_transfer_service",
        False,
    ),
    "PayoutMethod": ("stripe.v2.money_management._payout_method", False),
    "PayoutMethodService": (
        "stripe.v2.money_management._payout_method_service",
        False,
    ),
    "PayoutMethodsBankAccountSpec": (
        "stripe.v2.money_management._payout_methods_bank_account_spec",
        False,
    ),
    "PayoutMethodsBankAccountSpecService": (
        "stripe.v2.money_management._payout_methods_bank_account_spec_service",
        False,
    ),
    "ReceivedCredit": ("stripe.v2.money_management._received_credit", False),
    "ReceivedCreditService": (
        "stripe.v2.money_management._received_credit_service",
        False,
    ),
    "ReceivedDebit": ("stripe.v2.money_management._received_debit", False),
    "ReceivedDebitService": (
        "stripe.v2.money_management._received_debit_service",
        False,
    ),
    "RecipientVerification": (
        "stripe.v2.money_management._recipient_verification",
        False,
    ),
    "RecipientVerificationService": (
        "stripe.v2.money_management._recipient_verification_service",
        False,
    ),
    "Transaction": ("stripe.v2.money_management._transaction", False),
    "TransactionEntry": (
        "stripe.v2.money_management._transaction_entry",
        False,
    ),
    "TransactionEntryService": (
        "stripe.v2.money_management._transaction_entry_service",
        False,
    ),
    "TransactionService": (
        "stripe.v2.money_management._transaction_service",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
