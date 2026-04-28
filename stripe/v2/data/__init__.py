# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.data import analytics as analytics, reporting as reporting
    from stripe.v2.data._analytics_service import (
        AnalyticsService as AnalyticsService,
    )
    from stripe.v2.data._reporting_service import (
        ReportingService as ReportingService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "analytics": ("stripe.v2.data.analytics", True),
    "reporting": ("stripe.v2.data.reporting", True),
    "AnalyticsService": ("stripe.v2.data._analytics_service", False),
    "ReportingService": ("stripe.v2.data._reporting_service", False),
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
