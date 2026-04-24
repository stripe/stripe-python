# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.extend._workflow import Workflow as Workflow
    from stripe.v2.extend._workflow_run import WorkflowRun as WorkflowRun
    from stripe.v2.extend._workflow_run_service import (
        WorkflowRunService as WorkflowRunService,
    )
    from stripe.v2.extend._workflow_service import (
        WorkflowService as WorkflowService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Workflow": ("stripe.v2.extend._workflow", False),
    "WorkflowRun": ("stripe.v2.extend._workflow_run", False),
    "WorkflowRunService": ("stripe.v2.extend._workflow_run_service", False),
    "WorkflowService": ("stripe.v2.extend._workflow_service", False),
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
