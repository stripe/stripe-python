# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ReceivedDebitListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page limit.
    """
    received_debit_mandate: NotRequired[str]
    """
    Filter by the received debit mandate ID.
    """
