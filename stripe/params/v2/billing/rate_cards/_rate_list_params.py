# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class RateListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    metered_item: NotRequired[str]
    """
    Optionally filter by a Metered Item.
    """
    rate_card_version: NotRequired[str]
    """
    Optionally filter by a RateCard version. If not specified, defaults to the latest version.
    """
