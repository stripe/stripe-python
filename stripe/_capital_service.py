# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.capital._financing_offer_service import FinancingOfferService
from stripe.capital._financing_summary_service import FinancingSummaryService
from stripe.capital._financing_transaction_service import (
    FinancingTransactionService,
)


class CapitalService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.financing_offers = FinancingOfferService(self._requestor)
        self.financing_summary = FinancingSummaryService(self._requestor)
        self.financing_transactions = FinancingTransactionService(
            self._requestor,
        )
