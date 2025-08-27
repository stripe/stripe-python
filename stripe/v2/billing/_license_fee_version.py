# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class LicenseFeeVersion(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.license_fee_version"]] = (
        "v2.billing.license_fee_version"
    )

    class Tier(StripeObject):
        flat_amount: Optional[str]
        """
        Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
        """
        unit_amount: Optional[str]
        """
        Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
        most 12 decimal places.
        """
        up_to_decimal: Optional[str]
        """
        Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
        be set.
        """
        up_to_inf: Optional[Literal["inf"]]
        """
        No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
        """

    class TransformQuantity(StripeObject):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, round the result up or down.
        """

    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    license_fee_id: str
    """
    The ID of the parent License Fee.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.license_fee_version"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    tiering_mode: Optional[Literal["graduated", "volume"]]
    """
    Defines whether the tiering price should be graduated or volume-based. In volume-based tiering, the maximum
    quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
    grows into new tiers. Can only be set if `tiers` is set.
    """
    tiers: List[Tier]
    """
    Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
    """
    transform_quantity: Optional[TransformQuantity]
    """
    Apply a transformation to the reported usage or set quantity before computing the amount billed.
    """
    unit_amount: Optional[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
    places. Cannot be set if `tiers` is provided.
    """
    _inner_class_types = {
        "tiers": Tier,
        "transform_quantity": TransformQuantity,
    }
