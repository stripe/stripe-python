# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class FinancialAccountUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Metadata associated with the FinancialAccount.
    """
