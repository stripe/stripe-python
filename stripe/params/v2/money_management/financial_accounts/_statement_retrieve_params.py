# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class StatementRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["files_by_currency"]]]
    """
    Additional fields to include in the response.
    """
