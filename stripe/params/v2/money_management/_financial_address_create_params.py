# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, TypedDict


class FinancialAddressCreateParams(TypedDict):
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    type: Literal["gb_bank_account", "us_bank_account"]
    """
    The type of FinancialAddress details to provision.
    """
