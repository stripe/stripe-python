# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._discount import Discount
    from stripe._invoice_item import InvoiceItem
    from stripe._plan import Plan
    from stripe._price import Price
    from stripe._subscription import Subscription
    from stripe._subscription_item import SubscriptionItem
    from stripe._tax_rate import TaxRate


class InvoiceLineItem(StripeObject):
    OBJECT_NAME: ClassVar[Literal["line_item"]] = "line_item"

    class DiscountAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the discount.
        """
        discount: ExpandableField["Discount"]
        """
        The discount that was applied to get this discount amount.
        """

    class Period(StripeObject):
        end: int
        """
        The end of the period, which must be greater than or equal to the start. This value is inclusive.
        """
        start: int
        """
        The start of the period. This value is inclusive.
        """

    class ProrationDetails(StripeObject):
        class CreditedItems(StripeObject):
            invoice: str
            """
            Invoice containing the credited invoice line items
            """
            invoice_line_items: List[str]
            """
            Credited invoice line items
            """

        credited_items: Optional[CreditedItems]
        """
        For a credit proration `line_item`, the original debit line_items to which the credit proration applies.
        """
        _inner_class_types = {"credited_items": CreditedItems}

    class TaxAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the tax.
        """
        inclusive: bool
        """
        Whether this tax amount is inclusive or exclusive.
        """
        tax_rate: ExpandableField["TaxRate"]
        """
        The tax rate that was applied to get this tax amount.
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

    amount: int
    """
    The amount, in cents (or local equivalent).
    """
    amount_excluding_tax: Optional[int]
    """
    The integer amount in cents (or local equivalent) representing the amount for this line item, excluding all tax and discounts.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discount_amounts: Optional[List[DiscountAmount]]
    """
    The amount of discount calculated per discount for this line item.
    """
    discountable: bool
    """
    If true, discounts will apply to this line item. Always false for prorations.
    """
    discounts: Optional[List[ExpandableField["Discount"]]]
    """
    The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_item: Optional[ExpandableField["InvoiceItem"]]
    """
    The ID of the [invoice item](https://stripe.com/docs/api/invoiceitems) associated with this line item if any.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription` this will reflect the metadata of the subscription that caused the line item to be created.
    """
    object: Literal["line_item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    period: Period
    plan: Optional["Plan"]
    """
    The plan of the subscription, if the line item is a subscription or a proration.
    """
    price: Optional["Price"]
    """
    The price of the line item.
    """
    proration: bool
    """
    Whether this is a proration.
    """
    proration_details: Optional[ProrationDetails]
    """
    Additional details for proration line items
    """
    quantity: Optional[int]
    """
    The quantity of the subscription, if the line item is a subscription or a proration.
    """
    subscription: Optional[ExpandableField["Subscription"]]
    """
    The subscription that the invoice item pertains to, if any.
    """
    subscription_item: Optional[ExpandableField["SubscriptionItem"]]
    """
    The subscription item that generated this line item. Left empty if the line item is not an explicit result of a subscription.
    """
    tax_amounts: Optional[List[TaxAmount]]
    """
    The amount of tax calculated per tax rate for this line item
    """
    tax_rates: Optional[List["TaxRate"]]
    """
    The tax rates which apply to the line item.
    """
    type: Literal["invoiceitem", "subscription"]
    """
    A string identifying the type of the source of this line item, either an `invoiceitem` or a `subscription`.
    """
    unit_amount_excluding_tax: Optional[str]
    """
    The amount in cents (or local equivalent) representing the unit amount for this line item, excluding all tax and discounts.
    """
    _inner_class_types = {
        "discount_amounts": DiscountAmount,
        "period": Period,
        "proration_details": ProrationDetails,
        "tax_amounts": TaxAmount,
    }
