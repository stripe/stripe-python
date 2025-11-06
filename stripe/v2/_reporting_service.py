# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.reporting._report_run_service import ReportRunService
    from stripe.v2.reporting._report_service import ReportService

_subservices = {
    "reports": ["stripe.v2.reporting._report_service", "ReportService"],
    "report_runs": [
        "stripe.v2.reporting._report_run_service",
        "ReportRunService",
    ],
}


class ReportingService(StripeService):
    reports: "ReportService"
    report_runs: "ReportRunService"

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
