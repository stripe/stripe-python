# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class CalculationLineItem(StripeObject):
    OBJECT_NAME: ClassVar[
        Literal["tax.calculation_line_item"]
    ] = "tax.calculation_line_item"
    amount: int
    """
    The line item amount in integer cents. If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
    """
    amount_tax: int
    """
    The amount of tax calculated for this line item, in integer cents.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax.calculation_line_item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: Optional[str]
    """
    The ID of an existing [Product](https://stripe.com/docs/api/products/object).
    """
    quantity: int
    """
    The number of units of the item being purchased. For reversals, this is the quantity reversed.
    """
    reference: Optional[str]
    """
    A custom identifier for this line item.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
    """
    tax_breakdown: Optional[List[StripeObject]]
    """
    Detailed account of taxes relevant to this line item.
    """
    tax_code: str
    """
    The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for this resource.
    """
