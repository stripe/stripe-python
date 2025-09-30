# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class CollectionSettingListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    lookup_keys: NotRequired[List[str]]
    """
    Only return the settings with these lookup_keys, if any exist.
    You can specify up to 10 lookup_keys.
    """
