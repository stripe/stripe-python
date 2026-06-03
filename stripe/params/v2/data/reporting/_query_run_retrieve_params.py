# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class QueryRunRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["result.file.schema"]]]
    """
    Any optional includes (see https://docs.stripe.com/api-includable-response-values).
    """
