# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.billing.analytics._meter_usage_service import MeterUsageService


class AnalyticsService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.meter_usage = MeterUsageService(self._requestor)
