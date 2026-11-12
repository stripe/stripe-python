# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreateParams(TypedDict):
    bank_account: NotRequired["FinancialAddressCreateParamsBankAccount"]
    """
    Properties for creating a bank account FinancialAddress.
    """
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    type: Union[Literal["bank_account"], str]
    """
    The type of FinancialAddress to create. Must agree with which branch of financial_address_type_properties is set.
    """


class FinancialAddressCreateParamsBankAccount(TypedDict):
    country: NotRequired[str]
    """
    The country where Stripe provisions the bank account. Each currency supports the country listed in its description. If omitted, Stripe selects that country.
    """
    currency: Union[Literal["eur", "gbp", "usd"], str]
    """
    The currency of the bank account to provision. Some currencies require preview or rollout access, as configured for your account.
    """
