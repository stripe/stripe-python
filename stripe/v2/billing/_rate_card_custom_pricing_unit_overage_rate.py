# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._one_time_item import OneTimeItem


class RateCardCustomPricingUnitOverageRate(StripeObject):
    """
    A rate card custom pricing unit overage rate defines the conversion rate from a custom pricing unit
    to fiat currency when credits are exhausted. This enables automatic overage charges
    at a configurable per-unit rate.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.billing.rate_card_custom_pricing_unit_overage_rate"]
    ] = "v2.billing.rate_card_custom_pricing_unit_overage_rate"
    created: str
    """
    Timestamp of when the object was created.
    """
    custom_pricing_unit: str
    """
    The ID of the custom pricing unit this overage rate applies to.
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
    object: Literal["v2.billing.rate_card_custom_pricing_unit_overage_rate"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    one_time_item: "OneTimeItem"
    """
    A one-time item represents a product that can be charged as a one-time line item,
    used for overage charges when custom pricing unit credits are exhausted.
    """
    rate_card: str
    """
    The ID of the Rate Card this overage rate belongs to.
    """
    rate_card_version: str
    """
    The ID of the Rate Card Version this overage rate was created on.
    """
    unit_amount: str
    """
    The per-unit amount to charge for overages, represented as a decimal string in minor currency units with at most 12 decimal places.
    """
