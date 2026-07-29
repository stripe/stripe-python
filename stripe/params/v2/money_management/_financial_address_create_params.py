# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, TypedDict


class FinancialAddressCreateParams(TypedDict):
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    type: Union[Literal["gb_bank_account", "us_bank_account"], str]
    """
    The type of FinancialAddress details to provision.
    """
