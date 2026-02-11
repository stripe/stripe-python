# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitOverageRateListParams(TypedDict):
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    rate_card_version: NotRequired[str]
    """
    Optionally filter by a RateCard version. If not specified, defaults to the latest version.
    """
