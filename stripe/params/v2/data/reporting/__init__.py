# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.data.reporting._query_run_create_params import (
        QueryRunCreateParams as QueryRunCreateParams,
        QueryRunCreateParamsResultOptions as QueryRunCreateParamsResultOptions,
    )
    from stripe.params.v2.data.reporting._query_run_retrieve_params import (
        QueryRunRetrieveParams as QueryRunRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "QueryRunCreateParams": (
        "stripe.params.v2.data.reporting._query_run_create_params",
        False,
    ),
    "QueryRunCreateParamsResultOptions": (
        "stripe.params.v2.data.reporting._query_run_create_params",
        False,
    ),
    "QueryRunRetrieveParams": (
        "stripe.params.v2.data.reporting._query_run_retrieve_params",
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
