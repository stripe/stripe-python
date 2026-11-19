# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class SpendModifierRuleListParams(TypedDict):
    effective_at: NotRequired[str]
    """
    Return only spend modifiers that are effective at the specified timestamp.
    """
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
