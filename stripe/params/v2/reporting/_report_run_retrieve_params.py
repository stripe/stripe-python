# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReportRunRetrieveParams(TypedDict):
    include: NotRequired[List[Union[Literal["result.file.schema"], str]]]
    """
    Any optional includes (see https://docs.stripe.com/api-includable-response-values).
    """
