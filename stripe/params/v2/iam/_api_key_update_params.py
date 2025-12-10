# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ApiKeyUpdateParams(TypedDict):
    name: NotRequired[str]
    """
    Name to set for the API key. If blank, the field is left unchanged.
    """
    note: NotRequired[str]
    """
    Note or description to set for the API key. If blank, the field is left unchanged.
    """
