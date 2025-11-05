# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.reporting._report_retrieve_params import (
        ReportRetrieveParams as ReportRetrieveParams,
    )
    from stripe.params.v2.reporting._report_run_create_params import (
        ReportRunCreateParams as ReportRunCreateParams,
        ReportRunCreateParamsResultOptions as ReportRunCreateParamsResultOptions,
    )
    from stripe.params.v2.reporting._report_run_retrieve_params import (
        ReportRunRetrieveParams as ReportRunRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ReportRetrieveParams": (
        "stripe.params.v2.reporting._report_retrieve_params",
        False,
    ),
    "ReportRunCreateParams": (
        "stripe.params.v2.reporting._report_run_create_params",
        False,
    ),
    "ReportRunCreateParamsResultOptions": (
        "stripe.params.v2.reporting._report_run_create_params",
        False,
    ),
    "ReportRunRetrieveParams": (
        "stripe.params.v2.reporting._report_run_retrieve_params",
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
