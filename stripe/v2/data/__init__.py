# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.data import analytics as analytics, reporting as reporting
    from stripe.v2.data._analytics_service import (
        AnalyticsService as AnalyticsService,
    )
    from stripe.v2.data._query_run import QueryRun as QueryRun
    from stripe.v2.data._query_run_service import (
        QueryRunService as QueryRunService,
    )
    from stripe.v2.data._report import Report as Report
    from stripe.v2.data._report_run import ReportRun as ReportRun
    from stripe.v2.data._report_run_service import (
        ReportRunService as ReportRunService,
    )
    from stripe.v2.data._report_service import ReportService as ReportService
    from stripe.v2.data._reporting_service import (
        ReportingService as ReportingService,
    )
    from stripe.v2.data._schema import Schema as Schema
    from stripe.v2.data._schema_service import SchemaService as SchemaService

# name -> (import_target, is_submodule)
_import_map = {
    "analytics": ("stripe.v2.data.analytics", True),
    "reporting": ("stripe.v2.data.reporting", True),
    "AnalyticsService": ("stripe.v2.data._analytics_service", False),
    "QueryRun": ("stripe.v2.data._query_run", False),
    "QueryRunService": ("stripe.v2.data._query_run_service", False),
    "Report": ("stripe.v2.data._report", False),
    "ReportRun": ("stripe.v2.data._report_run", False),
    "ReportRunService": ("stripe.v2.data._report_run_service", False),
    "ReportService": ("stripe.v2.data._report_service", False),
    "ReportingService": ("stripe.v2.data._reporting_service", False),
    "Schema": ("stripe.v2.data._schema", False),
    "SchemaService": ("stripe.v2.data._schema_service", False),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
