# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class RewardProgramEnrollmentListParams(TypedDict):
    limit: NotRequired[int]
    """
    Maximum number of results to return. Default: 10. Valid range: 1-100.
    """
    reward_program: NotRequired[str]
    """
    Filter by RewardProgram. Omitting this field returns platform-wide enrollments across all
    RewardPrograms.
    """
    status: NotRequired["Literal['active', 'inactive']|str"]
    """
    Filter by RewardProgramEnrollment status.
    """
