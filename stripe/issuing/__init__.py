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
    from stripe.issuing._dispute import Dispute as Dispute
    from stripe.issuing._dispute_service import (
        DisputeService as DisputeService,
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
    from stripe.issuing._token import Token as Token
    from stripe.issuing._token_service import TokenService as TokenService
    from stripe.issuing._transaction import Transaction as Transaction
    from stripe.issuing._transaction_service import (
        TransactionService as TransactionService,
    )

_submodules = {
    "Authorization": "stripe.issuing._authorization",
    "AuthorizationService": "stripe.issuing._authorization_service",
    "Card": "stripe.issuing._card",
    "CardService": "stripe.issuing._card_service",
    "Cardholder": "stripe.issuing._cardholder",
    "CardholderService": "stripe.issuing._cardholder_service",
    "Dispute": "stripe.issuing._dispute",
    "DisputeService": "stripe.issuing._dispute_service",
    "PersonalizationDesign": "stripe.issuing._personalization_design",
    "PersonalizationDesignService": "stripe.issuing._personalization_design_service",
    "PhysicalBundle": "stripe.issuing._physical_bundle",
    "PhysicalBundleService": "stripe.issuing._physical_bundle_service",
    "Token": "stripe.issuing._token",
    "TokenService": "stripe.issuing._token_service",
    "Transaction": "stripe.issuing._transaction",
    "TransactionService": "stripe.issuing._transaction_service",
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
