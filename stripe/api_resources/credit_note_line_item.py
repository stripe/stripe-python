# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax_rate import TaxRate


class CreditNoteLineItem(ListableAPIResource["CreditNoteLineItem"]):
    """
    The credit note line item object
    """

    OBJECT_NAME = "credit_note_line_item"
    amount: int
    amount_excluding_tax: Optional[int]
    description: Optional[str]
    discount_amount: int
    discount_amounts: List[StripeObject]
    id: str
    invoice_line_item: str
    livemode: bool
    object: Literal["credit_note_line_item"]
    quantity: Optional[int]
    tax_amounts: List[StripeObject]
    tax_rates: List["TaxRate"]
    type: str
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[float]
    unit_amount_excluding_tax: Optional[float]
