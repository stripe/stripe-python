# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.price import Price


class LineItem(StripeObject):
    """
    A line item.
    """

    OBJECT_NAME: ClassVar[Literal["item"]] = "item"
    amount_discount: int
    """
    Total discount amount applied. If no discounts were applied, defaults to 0.
    """
    amount_subtotal: int
    """
    Total before any discounts or taxes are applied.
    """
    amount_tax: int
    """
    Total tax amount applied. If no tax was applied, defaults to 0.
    """
    amount_total: int
    """
    Total after discounts and taxes.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: str
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.
    """
    discounts: Optional[List[StripeObject]]
    """
    The discounts applied to the line item.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: Optional["Price"]
    """
    The price used to generate the line item.
    """
    quantity: Optional[int]
    """
    The quantity of products being purchased.
    """
    taxes: Optional[List[StripeObject]]
    """
    The taxes applied to the line item.
    """
