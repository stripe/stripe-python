# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class OffSessionPaymentListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page size limit. If not provided, the default is 20.
    """
