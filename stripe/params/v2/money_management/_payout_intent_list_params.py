# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class PayoutIntentListParams(TypedDict):
    limit: NotRequired[int]
    """
    Maximum number of objects to return. Defaults to 10. Maximum is 100.
    """
