# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class ProgramCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    is_default: NotRequired[bool]
    """
    If true, makes the specified program the default for the given account.
    """
    platform_program: str
    """
    The program to use as the parent for the new program to create.
    """
