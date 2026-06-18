# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ContractPricingLineQuantityChange(StripeObject):
    """
    A quantity change object for a pricing line, returned by ListContractPricingLineQuantityChanges.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.billing.contract_pricing_line_quantity_change"]
    ] = "v2.billing.contract_pricing_line_quantity_change"

    class Pricing(StripeObject):
        price: Optional[str]
        """
        The ID of the V1 price. Present when `type` is `price`.
        """
        type: Literal["price"]
        """
        The type of pricing.
        """

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
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.contract_pricing_line_quantity_change"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing: Pricing
    """
    The pricing configuration for the associated pricing line.
    """
    pricing_line: str
    """
    The ID of the pricing line associated with this quantity change.
    """
    quantity: Decimal
    """
    The quantity at the effective time.
    """
    _inner_class_types = {"pricing": Pricing}
    _field_encodings = {"quantity": "decimal_string"}
