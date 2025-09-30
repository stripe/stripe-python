# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class AccountListParams(TypedDict):
    applied_configurations: NotRequired[List[str]]
    """
    Filter only accounts that have all of the configurations specified. If omitted, returns all accounts regardless of which configurations they have.
    """
    limit: NotRequired[int]
    """
    The upper limit on the number of accounts returned by the List Account request.
    """
