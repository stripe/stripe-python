# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.signals._account_signal import (
        AccountSignal as AccountSignal,
    )
    from stripe.v2.signals._account_signal_service import (
        AccountSignalService as AccountSignalService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AccountSignal": ("stripe.v2.signals._account_signal", False),
    "AccountSignalService": (
        "stripe.v2.signals._account_signal_service",
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
