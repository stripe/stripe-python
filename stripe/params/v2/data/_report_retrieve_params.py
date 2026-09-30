# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReportRetrieveParams(TypedDict):
    include: NotRequired[
        List[Union[Literal["default_sql", "parameters"], str]]
    ]
    """
    Any optional includes (see https://docs.stripe.com/api-includable-response-values).
    """
