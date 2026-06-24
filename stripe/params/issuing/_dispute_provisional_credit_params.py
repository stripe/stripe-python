# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class DisputeProvisionalCreditParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    grant_deadline: NotRequired[int]
    """
    Override the deadline by which the platform must grant a provisional credit to the consumer.
    """
    revocable_after: NotRequired[int]
    """
    Override the earliest time after which the platform may revoke the provisional credit.
    """
