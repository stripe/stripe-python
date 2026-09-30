# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Union
from typing_extensions import Literal, TypedDict


class TestHelperEarnedCreditsParams(TypedDict):
    amount: AmountParam
    """
    The amount and currency of the EarnedCredit.
    """
    financial_account: str
    """
    The FinancialAccount to simulate the EarnedCredit for.
    """
    type: Union[Literal["interest"], str]
    """
    The type of EarnedCredit to create. Currently only interest is supported.
    """
