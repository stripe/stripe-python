# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class FinancialAccountUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name appears in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs that you can attach to the FinancialAccount. Individual keys can be unset by posting
    null to them.
    """
