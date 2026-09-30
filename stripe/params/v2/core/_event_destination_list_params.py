# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationListParams(TypedDict):
    include: NotRequired[List[Union[Literal["webhook_endpoint.url"], str]]]
    """
    Include the normally redacted `webhook_endpoint.url` in each returned destination.
    """
    limit: NotRequired[int]
    """
    The page size.
    """
