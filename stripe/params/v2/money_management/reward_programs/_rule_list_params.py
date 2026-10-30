# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class RuleListParams(TypedDict):
    limit: NotRequired[int]
    """
    Maximum number of results to return. Default: 10. Valid range: 1-100.
    """
    status: NotRequired["Literal['active', 'inactive']|str"]
    """
    Filter by RewardProgramRule status.
    """
