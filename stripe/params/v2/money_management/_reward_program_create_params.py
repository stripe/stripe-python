# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, TypedDict


class RewardProgramCreateParams(TypedDict):
    fulfilled_by: Union[Literal["application"], str]
    """
    Determines who performs reward money movement after rule evaluation. Only `application` is currently
    supported.
    """
    name: str
    """
    Display name for the RewardProgram.
    """
