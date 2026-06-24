# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.core.health import alerts as alerts
    from stripe.v2.core.health._alert import Alert as Alert
    from stripe.v2.core.health._alert_history_entry import (
        AlertHistoryEntry as AlertHistoryEntry,
    )
    from stripe.v2.core.health._alert_service import (
        AlertService as AlertService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "alerts": ("stripe.v2.core.health.alerts", True),
    "Alert": ("stripe.v2.core.health._alert", False),
    "AlertHistoryEntry": ("stripe.v2.core.health._alert_history_entry", False),
    "AlertService": ("stripe.v2.core.health._alert_service", False),
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
