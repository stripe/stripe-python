# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class PaymentIntentAmountDetailsLineItem(StripeObject):
    OBJECT_NAME: ClassVar[
        Literal["payment_intent_amount_details_line_item"]
    ] = "payment_intent_amount_details_line_item"

    class PaymentMethodOptions(StripeObject):
        class Card(StripeObject):
            commodity_code: Optional[str]

        class CardPresent(StripeObject):
            commodity_code: Optional[str]

        class Klarna(StripeObject):
            image_url: Optional[str]
            product_url: Optional[str]

        class Paypal(StripeObject):
            category: Optional[
                Literal["digital_goods", "donation", "physical_goods"]
            ]
            """
            Type of the line item.
            """
            description: Optional[str]
            """
            Description of the line item.
            """
            sold_by: Optional[str]
            """
            The Stripe account ID of the connected account that sells the item. This is only needed when using [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).
            """

        card: Optional[Card]
        card_present: Optional[CardPresent]
        klarna: Optional[Klarna]
        paypal: Optional[Paypal]
        _inner_class_types = {
            "card": Card,
            "card_present": CardPresent,
            "klarna": Klarna,
            "paypal": Paypal,
        }

    class Tax(StripeObject):
        total_tax_amount: int
        """
        Total portion of the amount that is for tax.
        """

    discount_amount: Optional[int]
    """
    The amount an item was discounted for. Positive integer.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["payment_intent_amount_details_line_item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method_options: Optional[PaymentMethodOptions]
    """
    Payment method-specific information for line items.
    """
    product_code: Optional[str]
    """
    Unique identifier of the product. At most 12 characters long.
    """
    product_name: str
    """
    Name of the product. At most 100 characters long.
    """
    quantity: int
    """
    Number of items of the product. Positive integer.
    """
    tax: Optional[Tax]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    Cost of the product. Non-negative integer.
    """
    unit_of_measure: Optional[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    """
    _inner_class_types = {
        "payment_method_options": PaymentMethodOptions,
        "tax": Tax,
    }
