# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountCreateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
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
    deposit_insurance_eligibility: NotRequired[
        List["FinancialAccountCreateParamsStorageDepositInsuranceEligibility"]
    ]
    """
    Array of eligibility objects, segmented by bank name and deposit insurance scheme.
    """
    holds_currencies: List[str]
    """
    The currencies that this FinancialAccount can hold.
    """


class FinancialAccountCreateParamsStorageDepositInsuranceEligibility(
    TypedDict
):
    bank_name: Union[Literal["fifth_third"], str]
    """
    The bank where funds are stored.
    """
    currencies: List[str]
    """
    Currencies eligible for deposit insurance at this bank under this scheme.
    """
    type: Union[Literal["fdic", "fdic_passthrough"], str]
    """
    The deposit insurance scheme.
    """
