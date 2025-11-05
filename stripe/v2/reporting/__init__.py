# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.reporting._report import Report as Report
    from stripe.v2.reporting._report_run import ReportRun as ReportRun
    from stripe.v2.reporting._report_run_service import (
        ReportRunService as ReportRunService,
    )
    from stripe.v2.reporting._report_service import (
        ReportService as ReportService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Report": ("stripe.v2.reporting._report", False),
    "ReportRun": ("stripe.v2.reporting._report_run", False),
    "ReportRunService": ("stripe.v2.reporting._report_run_service", False),
    "ReportService": ("stripe.v2.reporting._report_service", False),
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
