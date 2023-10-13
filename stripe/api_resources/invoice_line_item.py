# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

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
    amount: int
    amount_excluding_tax: Optional[int]
    currency: str
    description: Optional[str]
    discount_amounts: Optional[List[StripeObject]]
    discountable: bool
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    invoice_item: Optional[ExpandableField["InvoiceItem"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["line_item"]
    period: StripeObject
    plan: Optional["Plan"]
    price: Optional["Price"]
    proration: bool
    proration_details: Optional[StripeObject]
    quantity: Optional[int]
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_item: Optional[ExpandableField["SubscriptionItem"]]
    tax_amounts: Optional[List[StripeObject]]
    tax_rates: Optional[List["TaxRate"]]
    type: Literal["invoiceitem", "subscription"]
    unit_amount_excluding_tax: Optional[float]
