# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ApiKeyExpireParams(TypedDict):
    expire_in_minutes: NotRequired[int]
    """
    Duration in minutes before the key expires (defaults to immediate).
    """
