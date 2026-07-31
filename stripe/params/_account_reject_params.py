# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class AccountRejectParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payouts_action: NotRequired[Literal["none", "pause"]]
    """
    Whether to pause payouts on the account as part of the rejection. Defaults to `pause`. Use `none` to leave payouts enabled.
    """
    reason: str
    """
    The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.
    """
