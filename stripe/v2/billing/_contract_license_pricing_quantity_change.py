# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class ContractLicensePricingQuantityChange(StripeObject):
    """
    A license pricing quantity change object returned by ListContractLicenseQuantityChanges.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.billing.contract_license_pricing_quantity_change"]
    ] = "v2.billing.contract_license_pricing_quantity_change"
    created: str
    """
    The timestamp when this quantity change object was created.
    """
    effective_at: str
    """
    The timestamp when this quantity change takes effect.
    """
    id: str
    """
    The ID of the quantity change object.
    """
    license_pricing_id: str
    """
    The ID of the license pricing.
    """
    license_pricing_type: Literal["license_fee", "price"]
    """
    The type of the license pricing.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.contract_license_pricing_quantity_change"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_line: str
    """
    The ID of the pricing line associated with this quantity change.
    """
    quantity: int
    """
    The quantity at the effective time.
    """
