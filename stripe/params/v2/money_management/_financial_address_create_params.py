# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreateParams(TypedDict):
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    sepa_bank_account: NotRequired[
        "FinancialAddressCreateParamsSepaBankAccount"
    ]
    """
    Optional SEPA Bank account options, used to configure the type of SEPA Bank account to create, such as the originating country.
    """
    type: Literal["gb_bank_account", "sepa_bank_account", "us_bank_account"]
    """
    The type of FinancialAddress details to provision.
    """


class FinancialAddressCreateParamsSepaBankAccount(TypedDict):
    country: str
    """
    The originating country of the SEPA Bank account.
    """
