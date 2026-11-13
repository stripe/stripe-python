# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationRetrieveParams(TypedDict):
    include: NotRequired[List[Union[Literal["webhook_endpoint.url"], str]]]
    """
    Additional fields to include in the response.
    """
