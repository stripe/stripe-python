# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class FinancialAccountUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata associated with the FinancialAccount.
    """
    storage: NotRequired["FinancialAccountUpdateParamsStorage"]
    """
    Parameters for updating storage-specific fields on the FinancialAccount.
    """


class FinancialAccountUpdateParamsStorage(TypedDict):
    holds_currencies: NotRequired[List[str]]
    """
    The currencies that this storage FinancialAccount can hold a balance in. Three-letter ISO currency code, in lowercase.
    Adding currencies requires the corresponding holds_currencies storer capabilities to be enabled.
    Removing currencies is not supported as of March 2026.
    """
