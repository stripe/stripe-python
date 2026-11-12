# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class OffSessionPaymentUpdateParams(TypedDict):
    description: NotRequired[str]
    """
    An arbitrary string attached to the payment. Set to null to clear the description.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs attached to the payment. Existing keys are preserved unless
    explicitly changed. Set an individual key to null to remove it.
    """
