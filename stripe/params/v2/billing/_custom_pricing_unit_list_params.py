# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitListParams(TypedDict):
    active: NotRequired[bool]
    """
    Filter for active/inactive custom pricing units. Mutually exclusive with `lookup_keys`.
    """
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    lookup_keys: NotRequired[List[str]]
    """
    Filter by lookup keys. Mutually exclusive with `active`.
    You can specify up to 10 lookup keys.
    """
