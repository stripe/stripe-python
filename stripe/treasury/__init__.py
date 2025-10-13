# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.treasury._credit_reversal import (
        CreditReversal as CreditReversal,
    )
    from stripe.treasury._credit_reversal_service import (
        CreditReversalService as CreditReversalService,
    )
    from stripe.treasury._debit_reversal import DebitReversal as DebitReversal
    from stripe.treasury._debit_reversal_service import (
        DebitReversalService as DebitReversalService,
    )
    from stripe.treasury._financial_account import (
        FinancialAccount as FinancialAccount,
    )
    from stripe.treasury._financial_account_features import (
        FinancialAccountFeatures as FinancialAccountFeatures,
    )
    from stripe.treasury._financial_account_features_service import (
        FinancialAccountFeaturesService as FinancialAccountFeaturesService,
    )
    from stripe.treasury._financial_account_service import (
        FinancialAccountService as FinancialAccountService,
    )
    from stripe.treasury._inbound_transfer import (
        InboundTransfer as InboundTransfer,
    )
    from stripe.treasury._inbound_transfer_service import (
        InboundTransferService as InboundTransferService,
    )
    from stripe.treasury._outbound_payment import (
        OutboundPayment as OutboundPayment,
    )
    from stripe.treasury._outbound_payment_service import (
        OutboundPaymentService as OutboundPaymentService,
    )
    from stripe.treasury._outbound_transfer import (
        OutboundTransfer as OutboundTransfer,
    )
    from stripe.treasury._outbound_transfer_service import (
        OutboundTransferService as OutboundTransferService,
    )
    from stripe.treasury._received_credit import (
        ReceivedCredit as ReceivedCredit,
    )
    from stripe.treasury._received_credit_service import (
        ReceivedCreditService as ReceivedCreditService,
    )
    from stripe.treasury._received_debit import ReceivedDebit as ReceivedDebit
    from stripe.treasury._received_debit_service import (
        ReceivedDebitService as ReceivedDebitService,
    )
    from stripe.treasury._transaction import Transaction as Transaction
    from stripe.treasury._transaction_entry import (
        TransactionEntry as TransactionEntry,
    )
    from stripe.treasury._transaction_entry_service import (
        TransactionEntryService as TransactionEntryService,
    )
    from stripe.treasury._transaction_service import (
        TransactionService as TransactionService,
    )

_submodules = {
    "CreditReversal": "stripe.treasury._credit_reversal",
    "CreditReversalService": "stripe.treasury._credit_reversal_service",
    "DebitReversal": "stripe.treasury._debit_reversal",
    "DebitReversalService": "stripe.treasury._debit_reversal_service",
    "FinancialAccount": "stripe.treasury._financial_account",
    "FinancialAccountFeatures": "stripe.treasury._financial_account_features",
    "FinancialAccountFeaturesService": "stripe.treasury._financial_account_features_service",
    "FinancialAccountService": "stripe.treasury._financial_account_service",
    "InboundTransfer": "stripe.treasury._inbound_transfer",
    "InboundTransferService": "stripe.treasury._inbound_transfer_service",
    "OutboundPayment": "stripe.treasury._outbound_payment",
    "OutboundPaymentService": "stripe.treasury._outbound_payment_service",
    "OutboundTransfer": "stripe.treasury._outbound_transfer",
    "OutboundTransferService": "stripe.treasury._outbound_transfer_service",
    "ReceivedCredit": "stripe.treasury._received_credit",
    "ReceivedCreditService": "stripe.treasury._received_credit_service",
    "ReceivedDebit": "stripe.treasury._received_debit",
    "ReceivedDebitService": "stripe.treasury._received_debit_service",
    "Transaction": "stripe.treasury._transaction",
    "TransactionEntry": "stripe.treasury._transaction_entry",
    "TransactionEntryService": "stripe.treasury._transaction_entry_service",
    "TransactionService": "stripe.treasury._transaction_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
