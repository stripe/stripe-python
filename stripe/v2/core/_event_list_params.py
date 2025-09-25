# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class EventListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page size.
    """
    object_id: str
    """
    Primary object ID used to retrieve related events.
    """
