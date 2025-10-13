# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.reporting._report_run_create_params import (
        ReportRunCreateParams as ReportRunCreateParams,
        ReportRunCreateParamsParameters as ReportRunCreateParamsParameters,
    )
    from stripe.params.reporting._report_run_list_params import (
        ReportRunListParams as ReportRunListParams,
        ReportRunListParamsCreated as ReportRunListParamsCreated,
    )
    from stripe.params.reporting._report_run_retrieve_params import (
        ReportRunRetrieveParams as ReportRunRetrieveParams,
    )
    from stripe.params.reporting._report_type_list_params import (
        ReportTypeListParams as ReportTypeListParams,
    )
    from stripe.params.reporting._report_type_retrieve_params import (
        ReportTypeRetrieveParams as ReportTypeRetrieveParams,
    )

_submodules = {
    "ReportRunCreateParams": "stripe.params.reporting._report_run_create_params",
    "ReportRunCreateParamsParameters": "stripe.params.reporting._report_run_create_params",
    "ReportRunListParams": "stripe.params.reporting._report_run_list_params",
    "ReportRunListParamsCreated": "stripe.params.reporting._report_run_list_params",
    "ReportRunRetrieveParams": "stripe.params.reporting._report_run_retrieve_params",
    "ReportTypeListParams": "stripe.params.reporting._report_type_list_params",
    "ReportTypeRetrieveParams": "stripe.params.reporting._report_type_retrieve_params",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
