# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class EventRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["reason.request.client"]]]
    """
    Additional fields to include in the response.
    """
