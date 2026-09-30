# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.data._analytics_service import AnalyticsService
    from stripe.v2.data._query_run_service import QueryRunService
    from stripe.v2.data._report_run_service import ReportRunService
    from stripe.v2.data._report_service import ReportService
    from stripe.v2.data._reporting_service import ReportingService
    from stripe.v2.data._schema_service import SchemaService

_subservices = {
    "analytics": ["stripe.v2.data._analytics_service", "AnalyticsService"],
    "query_runs": ["stripe.v2.data._query_run_service", "QueryRunService"],
    "reports": ["stripe.v2.data._report_service", "ReportService"],
    "report_runs": ["stripe.v2.data._report_run_service", "ReportRunService"],
    "reporting": ["stripe.v2.data._reporting_service", "ReportingService"],
    "schemas": ["stripe.v2.data._schema_service", "SchemaService"],
}


class DataService(StripeService):
    analytics: "AnalyticsService"
    query_runs: "QueryRunService"
    reports: "ReportService"
    report_runs: "ReportRunService"
    reporting: "ReportingService"
    schemas: "SchemaService"

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
