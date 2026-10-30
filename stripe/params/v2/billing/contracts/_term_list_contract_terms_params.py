# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class TermListContractTermsParams(TypedDict):
    limit: NotRequired[int]
    """
    Maximum results per page.
    """
    type: NotRequired[
        "Literal['ad_hoc_product', 'pricing_override', 'recurring_price']|str"
    ]
    """
    Filter terms by type.
    """
