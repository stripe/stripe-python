# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountRetrieveParams(TypedDict):
    include: NotRequired[
        List[Literal["storage.deposit_insurance_eligibility"]]
    ]
    """
    Additional fields to include in the response.
    """
