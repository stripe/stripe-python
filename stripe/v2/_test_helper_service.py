# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.test_helpers._financial_address_service import (
    FinancialAddressService,
)
from stripe.v2.test_helpers._money_management_service import (
    MoneyManagementService,
)


class TestHelperService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.financial_addresses = FinancialAddressService(self._requestor)
        self.money_management = MoneyManagementService(self._requestor)
