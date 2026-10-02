# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FinancialAddressListParams(TypedDict):
    account: NotRequired[str]
    """
    The ID of the Account that owns the FinancialAddresses.
    """
    financial_account: NotRequired[str]
    """
    The ID of the FinancialAccount for which FinancialAddresses are to be returned.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
