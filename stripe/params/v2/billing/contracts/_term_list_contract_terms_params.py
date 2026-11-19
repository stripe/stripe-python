# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class TermListContractTermsParams(TypedDict):
    limit: NotRequired[int]
    """
    Maximum results per page.
    """
    type: NotRequired[
        "Literal['pricing_override', 'recurring_price', 'scheduled_fee']|str"
    ]
    """
    Filter terms by type.
    """
