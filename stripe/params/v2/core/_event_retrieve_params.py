# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class EventRetrieveParams(TypedDict):
    include: NotRequired[List[Union[Literal["reason.request.client"], str]]]
    """
    Additional fields to include in the response.
    """
