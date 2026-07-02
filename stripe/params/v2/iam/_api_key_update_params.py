# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class ApiKeyUpdateParams(TypedDict):
    connect_permissions: NotRequired[List[str]]
    """
    List of connect permissions for this API key.
    """
    name: NotRequired[str]
    """
    Name to set for the API key. If blank, the field is left unchanged.
    """
    note: NotRequired[str]
    """
    Note or description to set for the API key. If blank, the field is left unchanged.
    """
    permissions: NotRequired[List[str]]
    """
    List of permissions for this API key.
    """
