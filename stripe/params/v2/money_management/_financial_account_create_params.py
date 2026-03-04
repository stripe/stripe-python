# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountCreateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Metadata associated with the FinancialAccount.
    """
    storage: NotRequired["FinancialAccountCreateParamsStorage"]
    """
    Parameters specific to creating `storage` type FinancialAccounts.
    """
    type: Literal["storage"]
    """
    The type of FinancialAccount to create.
    """


class FinancialAccountCreateParamsStorage(TypedDict):
    funds_usage_type: NotRequired[Literal["business", "consumer"]]
    """
    The usage type for funds in this FinancialAccount. Can be used to specify that the funds are for Consumer activity.
    """
    holds_currencies: List[str]
    """
    The currencies that this FinancialAccount can hold.
    """
