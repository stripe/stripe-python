# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class SchemaListParams(TypedDict):
    dataset: NotRequired["Literal['analytical']|str"]
    """
    If supplied, only return schemas belonging to this dataset.
    """
    include: NotRequired[List[Union[Literal["columns"], str]]]
    """
    Any optional includes (see https://docs.stripe.com/api-includable-response-values).
    """
    limit: NotRequired[int]
    """
    The maximum number of results per page. Defaults to 10. Maximum is 100.
    """
    name: NotRequired[str]
    """
    If supplied, only return schemas with this name.
    """
