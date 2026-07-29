# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class WorkflowListParams(TypedDict):
    limit: NotRequired[int]
    """
    Restrict page size to no more than this number.
    """
    status: NotRequired[
        List[Union[Literal["active", "archived", "draft", "inactive"], str]]
    ]
    """
    When retrieving Workflows, include only those with the specified status values.
    If not specified, all Workflows in active and inactive status are returned.
    """
