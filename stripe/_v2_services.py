# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2._billing_service import BillingService
from stripe.v2._core_service import CoreService


class V2Services(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.billing = BillingService(self._requestor)
        self.core = CoreService(self._requestor)
