# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import List
from typing import Optional
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
    amount: int
    amount_excluding_tax: Optional[int]
    currency: str
    description: Optional[str]
    discount_amounts: Optional[List[StripeObject]]
    discountable: bool
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    invoice_item: ExpandableField["InvoiceItem"]
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
    subscription_item: ExpandableField["SubscriptionItem"]
    tax_amounts: List[StripeObject]
    tax_rates: List["TaxRate"]
    type: str
    unit_amount_excluding_tax: Optional[float]
