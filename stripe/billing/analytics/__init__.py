# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.billing.analytics._meter_usage import MeterUsage as MeterUsage
    from stripe.billing.analytics._meter_usage_row import (
        MeterUsageRow as MeterUsageRow,
    )
    from stripe.billing.analytics._meter_usage_service import (
        MeterUsageService as MeterUsageService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "MeterUsage": ("stripe.billing.analytics._meter_usage", False),
    "MeterUsageRow": ("stripe.billing.analytics._meter_usage_row", False),
    "MeterUsageService": (
        "stripe.billing.analytics._meter_usage_service",
        False,
    ),
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
