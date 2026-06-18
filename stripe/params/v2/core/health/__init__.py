# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core.health import alerts as alerts
    from stripe.params.v2.core.health._alert_list_params import (
        AlertListParams as AlertListParams,
    )
    from stripe.params.v2.core.health._alert_retrieve_params import (
        AlertRetrieveParams as AlertRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "alerts": ("stripe.params.v2.core.health.alerts", True),
    "AlertListParams": (
        "stripe.params.v2.core.health._alert_list_params",
        False,
    ),
    "AlertRetrieveParams": (
        "stripe.params.v2.core.health._alert_retrieve_params",
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
