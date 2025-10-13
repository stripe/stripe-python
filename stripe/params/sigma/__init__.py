# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.sigma._scheduled_query_run_list_params import (
        ScheduledQueryRunListParams as ScheduledQueryRunListParams,
    )
    from stripe.params.sigma._scheduled_query_run_retrieve_params import (
        ScheduledQueryRunRetrieveParams as ScheduledQueryRunRetrieveParams,
    )

_submodules = {
    "ScheduledQueryRunListParams": "stripe.params.sigma._scheduled_query_run_list_params",
    "ScheduledQueryRunRetrieveParams": "stripe.params.sigma._scheduled_query_run_retrieve_params",
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
