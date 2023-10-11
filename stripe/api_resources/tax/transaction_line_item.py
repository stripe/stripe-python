# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Dict, Optional
from typing_extensions import Literal


class TransactionLineItem(StripeObject):
    OBJECT_NAME = "tax.transaction_line_item"
    amount: int
    amount_tax: int
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax.transaction_line_item"]
    product: Optional[str]
    quantity: int
    reference: str
    reversal: Optional[StripeObject]
    tax_behavior: Literal["exclusive", "inclusive"]
    tax_code: str
    type: Literal["reversal", "transaction"]
