# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.capital._financing_offer_service import FinancingOfferService
    from stripe.capital._financing_summary_service import (
        FinancingSummaryService,
    )
    from stripe.capital._financing_transaction_service import (
        FinancingTransactionService,
    )

_subservices = {
    "financing_offers": [
        "stripe.capital._financing_offer_service",
        "FinancingOfferService",
    ],
    "financing_summary": [
        "stripe.capital._financing_summary_service",
        "FinancingSummaryService",
    ],
    "financing_transactions": [
        "stripe.capital._financing_transaction_service",
        "FinancingTransactionService",
    ],
}


class CapitalService(StripeService):
    financing_offers: "FinancingOfferService"
    financing_summary: "FinancingSummaryService"
    financing_transactions: "FinancingTransactionService"

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
