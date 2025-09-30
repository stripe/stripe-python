# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ComponentUpdateParams(TypedDict):
    lookup_key: NotRequired[str]
    """
    An identifier that can be used to find this component. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object.
    """
