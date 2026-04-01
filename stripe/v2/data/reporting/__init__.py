# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.data.reporting._query_run import QueryRun as QueryRun
    from stripe.v2.data.reporting._query_run_service import (
        QueryRunService as QueryRunService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "QueryRun": ("stripe.v2.data.reporting._query_run", False),
    "QueryRunService": ("stripe.v2.data.reporting._query_run_service", False),
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
