# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.data import (
        analytics as analytics,
        reporting as reporting,
    )
    from stripe.params.v2.data._query_run_create_params import (
        QueryRunCreateParams as QueryRunCreateParams,
        QueryRunCreateParamsQuery as QueryRunCreateParamsQuery,
        QueryRunCreateParamsResultOptions as QueryRunCreateParamsResultOptions,
    )
    from stripe.params.v2.data._query_run_retrieve_params import (
        QueryRunRetrieveParams as QueryRunRetrieveParams,
    )
    from stripe.params.v2.data._report_list_params import (
        ReportListParams as ReportListParams,
    )
    from stripe.params.v2.data._report_retrieve_params import (
        ReportRetrieveParams as ReportRetrieveParams,
    )
    from stripe.params.v2.data._report_run_create_params import (
        ReportRunCreateParams as ReportRunCreateParams,
        ReportRunCreateParamsReport as ReportRunCreateParamsReport,
        ReportRunCreateParamsResultOptions as ReportRunCreateParamsResultOptions,
    )
    from stripe.params.v2.data._report_run_retrieve_params import (
        ReportRunRetrieveParams as ReportRunRetrieveParams,
    )
    from stripe.params.v2.data._schema_list_params import (
        SchemaListParams as SchemaListParams,
    )
    from stripe.params.v2.data._schema_retrieve_params import (
        SchemaRetrieveParams as SchemaRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "analytics": ("stripe.params.v2.data.analytics", True),
    "reporting": ("stripe.params.v2.data.reporting", True),
    "QueryRunCreateParams": (
        "stripe.params.v2.data._query_run_create_params",
        False,
    ),
    "QueryRunCreateParamsQuery": (
        "stripe.params.v2.data._query_run_create_params",
        False,
    ),
    "QueryRunCreateParamsResultOptions": (
        "stripe.params.v2.data._query_run_create_params",
        False,
    ),
    "QueryRunRetrieveParams": (
        "stripe.params.v2.data._query_run_retrieve_params",
        False,
    ),
    "ReportListParams": ("stripe.params.v2.data._report_list_params", False),
    "ReportRetrieveParams": (
        "stripe.params.v2.data._report_retrieve_params",
        False,
    ),
    "ReportRunCreateParams": (
        "stripe.params.v2.data._report_run_create_params",
        False,
    ),
    "ReportRunCreateParamsReport": (
        "stripe.params.v2.data._report_run_create_params",
        False,
    ),
    "ReportRunCreateParamsResultOptions": (
        "stripe.params.v2.data._report_run_create_params",
        False,
    ),
    "ReportRunRetrieveParams": (
        "stripe.params.v2.data._report_run_retrieve_params",
        False,
    ),
    "SchemaListParams": ("stripe.params.v2.data._schema_list_params", False),
    "SchemaRetrieveParams": (
        "stripe.params.v2.data._schema_retrieve_params",
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
