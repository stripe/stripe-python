# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class TransactionUpdateParams(TypedDict):
    description: NotRequired[str]
    """
    A description of the Transaction, up to 100 characters. Pass `null` to clear the description,
    or omit this parameter to leave it unchanged.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs that you can attach to the Transaction. Individual keys can be unset by posting
    null to them.
    """
