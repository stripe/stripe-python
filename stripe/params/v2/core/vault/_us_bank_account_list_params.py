# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class UsBankAccountListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 10.
    """
    verification_status: NotRequired[
        Literal[
            "awaiting_verification",
            "unverified",
            "verification_failed",
            "verified",
        ]
    ]
    """
    Closed Enum. Optionally filter by verification status.
    """
