# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class TransactionLineItem(StripeObject):
    OBJECT_NAME: ClassVar[Literal["tax.transaction_line_item"]] = (
        "tax.transaction_line_item"
    )

    class PerformanceLocationDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1, such as the street, PO Box, or company name.
            """
            line2: Optional[str]
            """
            Address line 2, such as the apartment, suite, unit, or building.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as "NY" or "TX".
            """

        address: Address
        _inner_class_types = {"address": Address}

    class Reversal(StripeObject):
        original_line_item: str
        """
        The `id` of the line item to reverse in the original transaction.
        """

    amount: int
    """
    The line item amount in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
    """
    amount_tax: int
    """
    The amount of tax calculated for this line item, in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["tax.transaction_line_item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    performance_location_details: Optional[PerformanceLocationDetails]
    """
    The address of the location where this line item's event or service takes place. Depending on the [tax code](https://docs.stripe.com/tax/tax-codes), providing a performance location is required, optional, or not supported. Use this to provide the address inline without pre-creating a [TaxLocation](https://docs.stripe.com/api/tax/location) object. Can't be used with `performance_location`.
    """
    product: Optional[str]
    """
    The ID of an existing [Product](https://docs.stripe.com/api/products/object).
    """
    quantity: int
    """
    The number of units of the item being purchased. For reversals, this is the quantity reversed.
    """
    reference: str
    """
    A custom identifier for this line item in the transaction.
    """
    reversal: Optional[Reversal]
    """
    If `type=reversal`, contains information about what was reversed.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
    """
    tax_code: str
    """
    The [tax code](https://docs.stripe.com/tax/tax-categories) ID used for this resource.
    """
    type: Literal["reversal", "transaction"]
    """
    If `reversal`, this line item reverses an earlier transaction.
    """
    _inner_class_types = {
        "performance_location_details": PerformanceLocationDetails,
        "reversal": Reversal,
    }
