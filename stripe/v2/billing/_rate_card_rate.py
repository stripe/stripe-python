# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._custom_pricing_unit import CustomPricingUnit
    from stripe.v2.billing._metered_item import MeteredItem


class RateCardRate(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.rate_card_rate"]] = (
        "v2.billing.rate_card_rate"
    )

    class CustomPricingUnitAmount(StripeObject):
        custom_pricing_unit_details: Optional["CustomPricingUnit"]
        """
        The Custom Pricing Unit object.
        """
        id: str
        """
        The id of the custom pricing unit.
        """
        value: str
        """
        The unit value for the custom pricing unit, as a string.
        """

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
    custom_pricing_unit_amount: Optional[CustomPricingUnitAmount]
    """
    The custom pricing unit that this rate binds to.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    metered_item: "MeteredItem"
    """
    A Metered Item represents a billable item whose pricing is based on usage, measured by a meter. You can use rate cards
    to specify the pricing and create subscriptions to these items.
    """
    object: Literal["v2.billing.rate_card_rate"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    rate_card: str
    """
    The ID of the Rate Card it belongs to.
    """
    rate_card_version: str
    """
    The ID of the Rate Card Version it was created on.
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
        "custom_pricing_unit_amount": CustomPricingUnitAmount,
        "tiers": Tier,
        "transform_quantity": TransformQuantity,
    }
