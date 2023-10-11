# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice_item import InvoiceItem
    from stripe.api_resources.plan import Plan
    from stripe.api_resources.price import Price
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.subscription_item import SubscriptionItem
    from stripe.api_resources.tax_rate import TaxRate


class InvoiceLineItem(StripeObject):
    OBJECT_NAME = "line_item"

    class DiscountAmount(StripeObject):
        amount: int
        discount: ExpandableField["Discount"]

    class Period(StripeObject):
        end: int
        start: int

    class ProrationDetails(StripeObject):
        class CreditedItems(StripeObject):
            invoice: str
            invoice_line_items: List[str]

        credited_items: Optional[CreditedItems]
        _inner_class_types = {"credited_items": CreditedItems}

    class TaxAmount(StripeObject):
        amount: int
        inclusive: bool
        tax_rate: ExpandableField["TaxRate"]
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

    amount: int
    amount_excluding_tax: Optional[int]
    currency: str
    description: Optional[str]
    discount_amounts: Optional[List[DiscountAmount]]
    discountable: bool
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    invoice_item: Optional[ExpandableField["InvoiceItem"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["line_item"]
    period: Period
    plan: Optional["Plan"]
    price: Optional["Price"]
    proration: bool
    proration_details: Optional[ProrationDetails]
    quantity: Optional[int]
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_item: Optional[ExpandableField["SubscriptionItem"]]
    tax_amounts: Optional[List[TaxAmount]]
    tax_rates: Optional[List["TaxRate"]]
    type: Literal["invoiceitem", "subscription"]
    unit_amount_excluding_tax: Optional[float]

    _inner_class_types = {
        "discount_amounts": DiscountAmount,
        "period": Period,
        "proration_details": ProrationDetails,
        "tax_amounts": TaxAmount,
    }
