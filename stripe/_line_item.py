# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._discount import Discount as DiscountResource
    from stripe._price import Price
    from stripe._product import Product
    from stripe._tax_rate import TaxRate


class LineItem(StripeObject):
    """
    A line item.
    """

    OBJECT_NAME: ClassVar[Literal["item"]] = "item"

    class AdjustableQuantity(StripeObject):
        enabled: bool
        maximum: Optional[int]
        minimum: Optional[int]

    class Discount(StripeObject):
        amount: int
        """
        The amount discounted.
        """
        discount: "DiscountResource"
        """
        A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
        It contains information about when the discount began, when it will end, and what it is applied to.

        Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
        """

    class Display(StripeObject):
        description: Optional[str]
        images: List[str]
        name: str

    class TaxCalculationReference(StripeObject):
        calculation_id: Optional[str]
        """
        The calculation identifier for tax calculation response.
        """
        calculation_item_id: Optional[str]
        """
        The calculation identifier for tax calculation response line item.
        """

    class Tax(StripeObject):
        amount: int
        """
        Amount of tax applied for this rate.
        """
        rate: "TaxRate"
        """
        Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

        Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
        """
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
        """
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
        """
        taxable_amount: Optional[int]
        """
        The amount on which tax is calculated, in cents (or local equivalent).
        """

    adjustable_quantity: Optional[AdjustableQuantity]
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
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.
    """
    discounts: Optional[List[Discount]]
    """
    The discounts applied to the line item.
    """
    display: Optional[Display]
    id: str
    """
    Unique identifier for the object.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: Optional["Price"]
    """
    The price used to generate the line item.
    """
    product: Optional[ExpandableField["Product"]]
    """
    The ID of the product for this line item.

    This will always be the same as `price.product`.
    """
    quantity: Optional[int]
    """
    The quantity of products being purchased.
    """
    tax_calculation_reference: Optional[TaxCalculationReference]
    """
    The tax calculation identifiers of the line item.
    """
    taxes: Optional[List[Tax]]
    """
    The taxes applied to the line item.
    """
    _inner_class_types = {
        "adjustable_quantity": AdjustableQuantity,
        "discounts": Discount,
        "display": Display,
        "tax_calculation_reference": TaxCalculationReference,
        "taxes": Tax,
    }
