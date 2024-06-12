# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class PlatformTaxFee(StripeObject):
    OBJECT_NAME: ClassVar[Literal["platform_tax_fee"]] = "platform_tax_fee"
    account: str
    """
    The Connected account that incurred this charge.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["platform_tax_fee"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    source_transaction: str
    """
    The payment object that caused this tax to be inflicted.
    """
    type: str
    """
    The type of tax (VAT).
    """
