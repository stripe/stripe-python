# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.issuing._authorization import Authorization as Authorization
    from stripe.issuing._authorization_service import (
        AuthorizationService as AuthorizationService,
    )
    from stripe.issuing._card import Card as Card
    from stripe.issuing._card_service import CardService as CardService
    from stripe.issuing._cardholder import Cardholder as Cardholder
    from stripe.issuing._cardholder_service import (
        CardholderService as CardholderService,
    )
    from stripe.issuing._credit_underwriting_record import (
        CreditUnderwritingRecord as CreditUnderwritingRecord,
    )
    from stripe.issuing._credit_underwriting_record_service import (
        CreditUnderwritingRecordService as CreditUnderwritingRecordService,
    )
    from stripe.issuing._dispute import Dispute as Dispute
    from stripe.issuing._dispute_service import (
        DisputeService as DisputeService,
    )
    from stripe.issuing._dispute_settlement_detail import (
        DisputeSettlementDetail as DisputeSettlementDetail,
    )
    from stripe.issuing._dispute_settlement_detail_service import (
        DisputeSettlementDetailService as DisputeSettlementDetailService,
    )
    from stripe.issuing._fraud_liability_debit import (
        FraudLiabilityDebit as FraudLiabilityDebit,
    )
    from stripe.issuing._fraud_liability_debit_service import (
        FraudLiabilityDebitService as FraudLiabilityDebitService,
    )
    from stripe.issuing._personalization_design import (
        PersonalizationDesign as PersonalizationDesign,
    )
    from stripe.issuing._personalization_design_service import (
        PersonalizationDesignService as PersonalizationDesignService,
    )
    from stripe.issuing._physical_bundle import (
        PhysicalBundle as PhysicalBundle,
    )
    from stripe.issuing._physical_bundle_service import (
        PhysicalBundleService as PhysicalBundleService,
    )
    from stripe.issuing._program import Program as Program
    from stripe.issuing._program_service import (
        ProgramService as ProgramService,
    )
    from stripe.issuing._settlement import Settlement as Settlement
    from stripe.issuing._token import Token as Token
    from stripe.issuing._token_service import TokenService as TokenService
    from stripe.issuing._transaction import Transaction as Transaction
    from stripe.issuing._transaction_service import (
        TransactionService as TransactionService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Authorization": ("stripe.issuing._authorization", False),
    "AuthorizationService": ("stripe.issuing._authorization_service", False),
    "Card": ("stripe.issuing._card", False),
    "CardService": ("stripe.issuing._card_service", False),
    "Cardholder": ("stripe.issuing._cardholder", False),
    "CardholderService": ("stripe.issuing._cardholder_service", False),
    "CreditUnderwritingRecord": (
        "stripe.issuing._credit_underwriting_record",
        False,
    ),
    "CreditUnderwritingRecordService": (
        "stripe.issuing._credit_underwriting_record_service",
        False,
    ),
    "Dispute": ("stripe.issuing._dispute", False),
    "DisputeService": ("stripe.issuing._dispute_service", False),
    "DisputeSettlementDetail": (
        "stripe.issuing._dispute_settlement_detail",
        False,
    ),
    "DisputeSettlementDetailService": (
        "stripe.issuing._dispute_settlement_detail_service",
        False,
    ),
    "FraudLiabilityDebit": ("stripe.issuing._fraud_liability_debit", False),
    "FraudLiabilityDebitService": (
        "stripe.issuing._fraud_liability_debit_service",
        False,
    ),
    "PersonalizationDesign": ("stripe.issuing._personalization_design", False),
    "PersonalizationDesignService": (
        "stripe.issuing._personalization_design_service",
        False,
    ),
    "PhysicalBundle": ("stripe.issuing._physical_bundle", False),
    "PhysicalBundleService": (
        "stripe.issuing._physical_bundle_service",
        False,
    ),
    "Program": ("stripe.issuing._program", False),
    "ProgramService": ("stripe.issuing._program_service", False),
    "Settlement": ("stripe.issuing._settlement", False),
    "Token": ("stripe.issuing._token", False),
    "TokenService": ("stripe.issuing._token_service", False),
    "Transaction": ("stripe.issuing._transaction", False),
    "TransactionService": ("stripe.issuing._transaction_service", False),
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
