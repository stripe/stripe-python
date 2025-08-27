# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.reporting._report_run_service import ReportRunService
from stripe.v2.reporting._report_service import ReportService


class ReportingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.reports = ReportService(self._requestor)
        self.report_runs = ReportRunService(self._requestor)
