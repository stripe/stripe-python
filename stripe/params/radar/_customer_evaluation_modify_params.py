# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class CustomerEvaluationModifyParams(RequestOptions):
    customer: NotRequired[str]
    """
    The ID of a Customer to attach to an entity-less registration evaluation.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    status: NotRequired[Literal["allowed", "blocked", "restricted"]]
    """
    The outcome status of the evaluation: allowed, restricted, or blocked.
    """
