# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class AutomaticRule(StripeObject):
    """
    An AutomaticRule holds automatic Tax configuration for a BillableItem.
    """

    OBJECT_NAME: ClassVar[Literal["v2.tax.automatic_rule"]] = (
        "v2.tax.automatic_rule"
    )
    billable_item: str
    """
    The ID of the BillableItem.
    """
    created: str
    """
    The time at which the AutomaticRule object was created.
    """
    id: str
    """
    The ID of the AutomaticRule object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.tax.automatic_rule"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["active", "inactive"]
    """
    The status of the AutomaticRule object.
    """
    tax_code: str
    """
    A TaxCode object that will be used for automatic tax calculations.
    """
