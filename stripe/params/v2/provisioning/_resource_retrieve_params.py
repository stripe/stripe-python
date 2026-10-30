# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ResourceRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["configuration"]]]
    """
    Additional fields to include in the response. Requesting configuration only populates names
    for a complete Resource with an available, unexpired configuration. Missing configuration is
    returned as null; authorization, dependency, malformed-data, and limit failures remain errors.
    """
