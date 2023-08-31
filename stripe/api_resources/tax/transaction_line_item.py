# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
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
    tax_behavior: str
    tax_code: str
    type: str
