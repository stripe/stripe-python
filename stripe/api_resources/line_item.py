# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.price import Price
    from stripe.api_resources.product import Product
    from stripe.api_resources.tax_rate import TaxRate


class LineItem(StripeObject):
    """
    A line item.
    """

    OBJECT_NAME = "item"

    class Discount(StripeObject):
        amount: int
        discount: "DiscountResource"

    class Tax(StripeObject):
        amount: int
        rate: "TaxRate"
        taxability_reason: Optional[
            Literal[
                "customer_exempt",
                "not_collecting",
                "not_subject_to_tax",
                "not_supported",
                "portion_product_exempt",
                "portion_reduced_rated",
                "portion_standard_rated",
                "product_exempt",
                "product_exempt_holiday",
                "proportionally_rated",
                "reduced_rated",
                "reverse_charge",
                "standard_rated",
                "taxable_basis_reduced",
                "zero_rated",
            ]
        ]
        taxable_amount: Optional[int]

    amount_discount: int
    amount_subtotal: int
    amount_tax: int
    amount_total: int
    currency: str
    description: str
    discounts: Optional[List[Discount]]
    id: str
    object: Literal["item"]
    price: Optional["Price"]
    product: Optional[ExpandableField["Product"]]
    quantity: Optional[int]
    taxes: Optional[List[Tax]]

    _inner_class_types = {"discounts": Discount, "taxes": Tax}
