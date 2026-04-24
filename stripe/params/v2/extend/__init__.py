# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.extend._workflow_invoke_params import (
        WorkflowInvokeParams as WorkflowInvokeParams,
    )
    from stripe.params.v2.extend._workflow_list_params import (
        WorkflowListParams as WorkflowListParams,
    )
    from stripe.params.v2.extend._workflow_retrieve_params import (
        WorkflowRetrieveParams as WorkflowRetrieveParams,
    )
    from stripe.params.v2.extend._workflow_run_list_params import (
        WorkflowRunListParams as WorkflowRunListParams,
    )
    from stripe.params.v2.extend._workflow_run_retrieve_params import (
        WorkflowRunRetrieveParams as WorkflowRunRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "WorkflowInvokeParams": (
        "stripe.params.v2.extend._workflow_invoke_params",
        False,
    ),
    "WorkflowListParams": (
        "stripe.params.v2.extend._workflow_list_params",
        False,
    ),
    "WorkflowRetrieveParams": (
        "stripe.params.v2.extend._workflow_retrieve_params",
        False,
    ),
    "WorkflowRunListParams": (
        "stripe.params.v2.extend._workflow_run_list_params",
        False,
    ),
    "WorkflowRunRetrieveParams": (
        "stripe.params.v2.extend._workflow_run_retrieve_params",
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
