# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReportListParams(TypedDict):
    include: NotRequired[
        List[Union[Literal["default_sql", "parameters"], str]]
    ]
    """
    Any optional includes (see [include-dependent response values](https://docs.stripe.com/api-includable-response-values)).
    """
    limit: NotRequired[int]
    """
    The maximum number of results per page. Defaults to 10. Maximum is 1,000.
    """
    name: NotRequired[str]
    """
    If supplied, only return reports with this exact, case-sensitive name.
    """
