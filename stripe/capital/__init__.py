# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.capital._financing_offer import (
        FinancingOffer as FinancingOffer,
    )
    from stripe.capital._financing_offer_service import (
        FinancingOfferService as FinancingOfferService,
    )
    from stripe.capital._financing_summary import (
        FinancingSummary as FinancingSummary,
    )
    from stripe.capital._financing_summary_service import (
        FinancingSummaryService as FinancingSummaryService,
    )
    from stripe.capital._financing_transaction import (
        FinancingTransaction as FinancingTransaction,
    )
    from stripe.capital._financing_transaction_service import (
        FinancingTransactionService as FinancingTransactionService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FinancingOffer": ("stripe.capital._financing_offer", False),
    "FinancingOfferService": (
        "stripe.capital._financing_offer_service",
        False,
    ),
    "FinancingSummary": ("stripe.capital._financing_summary", False),
    "FinancingSummaryService": (
        "stripe.capital._financing_summary_service",
        False,
    ),
    "FinancingTransaction": ("stripe.capital._financing_transaction", False),
    "FinancingTransactionService": (
        "stripe.capital._financing_transaction_service",
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
