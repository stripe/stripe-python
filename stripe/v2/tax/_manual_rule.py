# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ManualRule(StripeObject):
    """
    A ManualRule holds tax rates for a BillableItem. It can hold at most 5 distinct tax rates.
    """

    OBJECT_NAME: ClassVar[Literal["v2.tax.manual_rule"]] = "v2.tax.manual_rule"

    class Location(StripeObject):
        country: str
        """
        Country ISO-3166.
        """
        state: Optional[str]
        """
        State ISO-3166.
        """

    class Product(StripeObject):
        licensed_item: Optional[str]
        """
        The licensed item identifier.
        """
        metered_item: Optional[str]
        """
        The metered item identifier.
        """
        tax_code: Optional[str]
        """
        The tax code for the product.
        """
        type: Literal["licensed_item", "metered_item", "tax_code"]
        """
        The type of the product.
        """

    class ScheduledTaxRate(StripeObject):
        class Rate(StripeObject):
            country: Optional[str]
            """
            Country of the tax rate.
            """
            description: Optional[str]
            """
            Description of the tax rate.
            """
            display_name: str
            """
            Display name of the tax rate as it will be shown on the invoice.
            """
            jurisdiction: Optional[str]
            """
            Jurisdiction of the tax rate should apply as it will be shown on the invoice.
            """
            percentage: str
            """
            Percentage of the tax rate. Must be positive and maximum of 4 decimal points.
            """
            state: Optional[str]
            """
            State of the tax rate.
            """

        rates: List[Rate]
        """
        The tax rates to be applied.
        """
        starts_at: Optional[str]
        """
        The start time for the tax rate.
        """
        _inner_class_types = {"rates": Rate}

    created: str
    """
    The time at which the ManualRule object was created.
    """
    id: str
    """
    The ID of the ManualRule object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    location: Optional[Location]
    """
    Location where the rule applies.
    """
    object: Literal["v2.tax.manual_rule"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    products: List[Product]
    """
    Products associated with the rule.
    """
    scheduled_tax_rates: List[ScheduledTaxRate]
    """
    Tax rates to be applied.
    """
    status: Literal["active", "inactive"]
    """
    The status of the ManualRule object.
    """
    _inner_class_types = {
        "location": Location,
        "products": Product,
        "scheduled_tax_rates": ScheduledTaxRate,
    }
