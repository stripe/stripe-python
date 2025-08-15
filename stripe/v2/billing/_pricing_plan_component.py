# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class PricingPlanComponent(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.pricing_plan_component"]] = (
        "v2.billing.pricing_plan_component"
    )

    class LicenseFee(StripeObject):
        id: str
        """
        The ID of the LicenseFee.
        """
        version: str
        """
        The version of the LicenseFee.
        """

    class RateCard(StripeObject):
        id: str
        """
        The ID of the RateCard.
        """
        version: str
        """
        The version of the RateCard.
        """

    class ServiceAction(StripeObject):
        id: str
        """
        The ID of the ServiceAction.
        """
        version: str
        """
        The version of the ServiceAction.
        """

    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the PricingPlanComponent.
    """
    license_fee: Optional[LicenseFee]
    """
    Details if this component is a LicenseFee.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular PricingPlanComponent.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object.
    """
    object: Literal["v2.billing.pricing_plan_component"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_plan: str
    """
    The ID of the PricingPlan this component belongs to.
    """
    pricing_plan_version: str
    """
    The ID of the PricingPlanVersion this component belongs to.
    """
    rate_card: Optional[RateCard]
    """
    Details if this component is a RateCard.
    """
    service_action: Optional[ServiceAction]
    """
    Details if this component is a ServiceAction.
    """
    type: Literal["license_fee", "rate_card", "service_action"]
    """
    The type of the PricingPlanComponent.
    """
    _inner_class_types = {
        "license_fee": LicenseFee,
        "rate_card": RateCard,
        "service_action": ServiceAction,
    }
