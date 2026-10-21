# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class OperationSearchParams(TypedDict):
    catalogs: NotRequired[
        List[Union[Literal["metrics", "reports", "schemas"], str]]
    ]
    """
    Restrict results to public resource catalogs. Defaults to all catalogs
    available to the caller.
    """
    limit: NotRequired[int]
    """
    Maximum results. Default: 5, Max: 20.
    """
    page: NotRequired[str]
    """
    The page token for pagination.
    """
    query: str
    """
    Natural-language question. Required.
    """
