# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class PricingPlanSubscriptionComponents(StripeObject):
    """
    A set of component subscriptions for a Pricing Plan Subscription.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.billing.pricing_plan_subscription_components"]
    ] = "v2.billing.pricing_plan_subscription_components"

    class Component(StripeObject):
        license_fee_subscription: Optional[str]
        """
        The ID of the License Fee Subscription.
        """
        pricing_plan_component: str
        """
        The Pricing Plan Component associated with this component subscription.
        """
        rate_card_subscription: Optional[str]
        """
        The ID of the Rate Card Subscription.
        """
        type: Literal["license_fee_subscription", "rate_card_subscription"]
        """
        The type of subscription.
        """

    components: List[Component]
    """
    The component subscriptions of the Pricing Plan Subscription.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.pricing_plan_subscription_components"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"components": Component}
