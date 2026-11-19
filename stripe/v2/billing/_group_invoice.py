# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class GroupInvoice(StripeObject):
    """
    A Billing Group Invoice references an empty invoice created with the billing group's settings.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.group_invoice"]] = (
        "v2.billing.group_invoice"
    )
    created: str
    """
    Timestamp of when the BillingGroupInvoice object was created.
    """
    id: str
    """
    The ID of the BillingGroupInvoice object.
    """
    invoice_id: str
    """
    The ID of the created Invoice object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.group_invoice"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
