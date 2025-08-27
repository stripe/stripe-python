# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class LicensedItem(StripeObject):
    """
    A Licensed Item represents a billable item whose pricing is based on license fees. You can use license fees
    to specify the pricing and create subscriptions to these items.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.licensed_item"]] = (
        "v2.billing.licensed_item"
    )

    class TaxDetails(StripeObject):
        tax_code: str
        """
        Product tax code (PTC).
        """

    created: str
    """
    Timestamp of when the object was created.
    """
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular billable item.
    Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.licensed_item"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    tax_details: Optional[TaxDetails]
    """
    Stripe Tax details.
    """
    unit_label: Optional[str]
    """
    The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
    to "seat" for Checkout to display "(price) per seat", or "environment" to display "(price) per environment".
    Maximum length of 100 characters.
    """
    _inner_class_types = {"tax_details": TaxDetails}
