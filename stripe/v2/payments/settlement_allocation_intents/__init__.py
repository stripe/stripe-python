# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.payments.settlement_allocation_intents._split_service import (
        SplitService as SplitService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "SplitService": (
        "stripe.v2.payments.settlement_allocation_intents._split_service",
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
