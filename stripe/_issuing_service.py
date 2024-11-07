# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.issuing._authorization_service import AuthorizationService
from stripe.issuing._card_service import CardService
from stripe.issuing._cardholder_service import CardholderService
from stripe.issuing._credit_underwriting_record_service import (
    CreditUnderwritingRecordService,
)
from stripe.issuing._dispute_service import DisputeService
from stripe.issuing._dispute_settlement_detail_service import (
    DisputeSettlementDetailService,
)
from stripe.issuing._fraud_liability_debit_service import (
    FraudLiabilityDebitService,
)
from stripe.issuing._personalization_design_service import (
    PersonalizationDesignService,
)
from stripe.issuing._physical_bundle_service import PhysicalBundleService
from stripe.issuing._token_service import TokenService
from stripe.issuing._transaction_service import TransactionService


class IssuingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.authorizations = AuthorizationService(self._requestor)
        self.cards = CardService(self._requestor)
        self.cardholders = CardholderService(self._requestor)
        self.credit_underwriting_records = CreditUnderwritingRecordService(
            self._requestor,
        )
        self.disputes = DisputeService(self._requestor)
        self.dispute_settlement_details = DisputeSettlementDetailService(
            self._requestor,
        )
        self.fraud_liability_debits = FraudLiabilityDebitService(
            self._requestor,
        )
        self.personalization_designs = PersonalizationDesignService(
            self._requestor,
        )
        self.physical_bundles = PhysicalBundleService(self._requestor)
        self.tokens = TokenService(self._requestor)
        self.transactions = TransactionService(self._requestor)
