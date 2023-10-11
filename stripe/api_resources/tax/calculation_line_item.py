# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal


class CalculationLineItem(StripeObject):
    OBJECT_NAME = "tax.calculation_line_item"
    amount: int
    amount_tax: int
    id: str
    livemode: bool
    object: Literal["tax.calculation_line_item"]
    product: Optional[str]
    quantity: int
    reference: Optional[str]
    tax_behavior: Literal["exclusive", "inclusive"]
    tax_breakdown: Optional[List[StripeObject]]
    tax_code: str
