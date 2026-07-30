# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class InquiryListParams(TypedDict):
    account: str
    """
    The account to list inquiries for.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return. Default: 10. Valid range: 1-100.
    """
