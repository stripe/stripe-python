# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountRetrieveParams(TypedDict):
    include: NotRequired[List[Literal["payments.balance_by_funds_type"]]]
    """
    Additional fields to include in the response.
    """
