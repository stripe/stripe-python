# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class WorkflowRunListParams(TypedDict):
    limit: NotRequired[int]
    """
    Restrict page size to no more than this number.
    """
    status: NotRequired[List[Literal["failed", "started", "succeeded"]]]
    """
    When retrieving Workflow Runs, include only those with the specified status values. If not specified, all Runs are returned.
    """
    workflow: NotRequired[List[str]]
    """
    When retrieving Workflow Runs, include only those associated with the Workflows specified. If not specified, all Runs are returned.
    """
