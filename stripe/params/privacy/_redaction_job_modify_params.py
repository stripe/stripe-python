# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class RedactionJobModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    validation_behavior: NotRequired[Literal["error", "fix"]]
    """
    Determines the validation behavior of the job. Default is `error`.
    """
