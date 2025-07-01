# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2._billing_service import BillingService
from stripe.v2._core_service import CoreService
from stripe.v2._money_management_service import MoneyManagementService
from stripe.v2._payment_service import PaymentService
from stripe.v2._test_helper_service import TestHelperService


class V2Services(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.billing = BillingService(self._requestor)
        self.core = CoreService(self._requestor)
        self.money_management = MoneyManagementService(self._requestor)
        self.payments = PaymentService(self._requestor)
        self.test_helpers = TestHelperService(self._requestor)
