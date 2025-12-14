# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ApiKeyListParams(TypedDict):
    include_expired: NotRequired[bool]
    """
    Whether to include expired API keys in the response.
    """
    limit: NotRequired[int]
    """
    Limit of items to return per page.
    """
