# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.reporting._report_run import ReportRun as ReportRun
    from stripe.reporting._report_run_service import (
        ReportRunService as ReportRunService,
    )
    from stripe.reporting._report_type import ReportType as ReportType
    from stripe.reporting._report_type_service import (
        ReportTypeService as ReportTypeService,
    )

_submodules = {
    "ReportRun": "stripe.reporting._report_run",
    "ReportRunService": "stripe.reporting._report_run_service",
    "ReportType": "stripe.reporting._report_type",
    "ReportTypeService": "stripe.reporting._report_type_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
