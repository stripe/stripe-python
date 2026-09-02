# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class FeedbackOptionUpdateParams(TypedDict):
    description: NotRequired[str]
    """
    The text of the feedback option, which customers see when canceling. Maximum 100 characters.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
