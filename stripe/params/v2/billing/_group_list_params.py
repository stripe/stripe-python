# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class GroupListParams(TypedDict):
    customer: NotRequired[str]
    """
    Filter billing groups by Customer ID. Mutually exclusive with test_clock.
    """
    limit: NotRequired[int]
    """
    The maximum number of results per page. Defaults to 10.
    """
    lookup_keys: NotRequired[List[str]]
    """
    Filter billing groups by lookup keys. You can specify up to 10 lookup keys.
    """
    test_clock: NotRequired[str]
    """
    Filter billing groups by TestClock ID. Mutually exclusive with customer.
    """
