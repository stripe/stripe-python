# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ClaimableSandboxRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["sandbox_details.api_keys"]]]
    """
    Additional fields to include in the response.
    """
