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
        The ID of the License Fee.
        """
        version: Optional[str]
        """
        The version of the LicenseFee. Defaults to 'latest', if not specified.
        """

    class RateCard(StripeObject):
        id: str
        """
        The ID of the Rate Card.
        """
        version: Optional[str]
        """
        The version of the RateCard. Defaults to 'latest', if not specified.
        """

    class ServiceAction(StripeObject):
        id: str
        """
        The ID of the service action.
        """

    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    license_fee: Optional[LicenseFee]
    """
    Details if this component is a License Fee.
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
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.pricing_plan_component"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_plan: str
    """
    The ID of the Pricing Plan this component belongs to.
    """
    pricing_plan_version: str
    """
    The ID of the Pricing Plan Version this component belongs to.
    """
    rate_card: Optional[RateCard]
    """
    Details if this component is a Rate Card.
    """
    service_action: Optional[ServiceAction]
    """
    Details if this component is a Service Action.
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
