# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class TrialOfferUpdateParams(TypedDict):
    active: NotRequired[bool]
    """
    Whether the trial offer can be used for new purchases.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
