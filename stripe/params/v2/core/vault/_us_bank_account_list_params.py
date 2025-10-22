# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class UsBankAccountListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 10.
    """
    verification_status: NotRequired[str]
    """
    Optionally filter by verification status. Mutually exclusive with `unverified`, `verified`, `awaiting_verification`, and `verification_failed`.
    """
