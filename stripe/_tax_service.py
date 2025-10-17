# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.tax._association_service import AssociationService
from stripe.tax._calculation_service import CalculationService
from stripe.tax._form_service import FormService
from stripe.tax._registration_service import RegistrationService
from stripe.tax._settings_service import SettingsService
from stripe.tax._transaction_service import TransactionService


class TaxService(StripeService):
    calculations: "CalculationService"
    registrations: "RegistrationService"
    settings: "SettingsService"
    transactions: "TransactionService"

    def __init__(self, requestor):
        super().__init__(requestor)
        self.associations = AssociationService(self._requestor)
        self.calculations = CalculationService(self._requestor)
        self.forms = FormService(self._requestor)
        self.registrations = RegistrationService(self._requestor)
        self.settings = SettingsService(self._requestor)
        self.transactions = TransactionService(self._requestor)
