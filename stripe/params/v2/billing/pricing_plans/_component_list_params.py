# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class ComponentListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    lookup_keys: NotRequired[List[str]]
    """
    Filter by lookup keys. Mutually exclusive with `pricing_plan_version`.
    You can specify up to 10 lookup keys.
    """
    pricing_plan_version: NotRequired[str]
    """
    The ID of the Pricing Plan Version to list components for. Will use the latest version if not provided.
    Mutually exclusive with `lookup_keys`.
    """
