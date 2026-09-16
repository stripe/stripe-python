# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class NetworkTokenGenerateCryptogramParams(TypedDict):
    type: NotRequired[Literal["token_cryptogram"]]
    """
    The cryptogram type. When omitted, token_cryptogram is used.
    """
