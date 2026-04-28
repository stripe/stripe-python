# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.data.analytics._metric_query_result import (
        MetricQueryResult as MetricQueryResult,
    )
    from stripe.v2.data.analytics._metric_query_service import (
        MetricQueryService as MetricQueryService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "MetricQueryResult": (
        "stripe.v2.data.analytics._metric_query_result",
        False,
    ),
    "MetricQueryService": (
        "stripe.v2.data.analytics._metric_query_service",
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
