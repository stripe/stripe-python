# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.tax._calculation import Calculation as Calculation
    from stripe.tax._calculation_line_item import (
        CalculationLineItem as CalculationLineItem,
    )
    from stripe.tax._calculation_line_item_service import (
        CalculationLineItemService as CalculationLineItemService,
    )
    from stripe.tax._calculation_service import (
        CalculationService as CalculationService,
    )
    from stripe.tax._registration import Registration as Registration
    from stripe.tax._registration_service import (
        RegistrationService as RegistrationService,
    )
    from stripe.tax._settings import Settings as Settings
    from stripe.tax._settings_service import SettingsService as SettingsService
    from stripe.tax._transaction import Transaction as Transaction
    from stripe.tax._transaction_line_item import (
        TransactionLineItem as TransactionLineItem,
    )
    from stripe.tax._transaction_line_item_service import (
        TransactionLineItemService as TransactionLineItemService,
    )
    from stripe.tax._transaction_service import (
        TransactionService as TransactionService,
    )

_submodules = {
    "Calculation": "stripe.tax._calculation",
    "CalculationLineItem": "stripe.tax._calculation_line_item",
    "CalculationLineItemService": "stripe.tax._calculation_line_item_service",
    "CalculationService": "stripe.tax._calculation_service",
    "Registration": "stripe.tax._registration",
    "RegistrationService": "stripe.tax._registration_service",
    "Settings": "stripe.tax._settings",
    "SettingsService": "stripe.tax._settings_service",
    "Transaction": "stripe.tax._transaction",
    "TransactionLineItem": "stripe.tax._transaction_line_item",
    "TransactionLineItemService": "stripe.tax._transaction_line_item_service",
    "TransactionService": "stripe.tax._transaction_service",
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
