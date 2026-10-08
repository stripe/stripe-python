# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class QueryRunRetrieveParams(TypedDict):
    include: NotRequired[List[Union[Literal["result.inline"], str]]]
    """
    Any optional includes (see [include-dependent response values](https://docs.stripe.com/api-includable-response-values)).
    """
    limit: NotRequired[int]
    """
    The maximum number of inline `QueryRun` result rows to return. Defaults to 10. Maximum is 1000.
    """
    page: NotRequired[str]
    """
    The page token for paginating the inline `QueryRun` result rows.
    """
