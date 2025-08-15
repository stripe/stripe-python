# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class PricingPlanSubscription(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.pricing_plan_subscription"]] = (
        "v2.billing.pricing_plan_subscription"
    )

    class CollectionStatusTransitions(StripeObject):
        awaiting_customer_action_at: Optional[str]
        """
        When the collection status transitioned to awaiting customer action.
        """
        current_at: Optional[str]
        """
        When the collection status transitioned to current.
        """
        past_due_at: Optional[str]
        """
        When the collection status transitioned to past due.
        """
        paused_at: Optional[str]
        """
        When the collection status transitioned to paused.
        """
        unpaid_at: Optional[str]
        """
        When the collection status transitioned to unpaid.
        """

    class ServicingStatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        When the servicing status transitioned to activated.
        """
        canceled_at: Optional[str]
        """
        When the servicing status transitioned to canceled.
        """
        paused_at: Optional[str]
        """
        When the servicing status transitioned to paused.
        """

    billing_cadence: str
    """
    The ID of the Cadence this subscription is billed on.
    """
    collection_status: Literal[
        "awaiting_customer_action", "current", "past_due", "paused", "unpaid"
    ]
    """
    Current collection status of this subscription.
    """
    collection_status_transitions: CollectionStatusTransitions
    """
    Timestamps for collection status transitions.
    """
    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the PricingPlanSubscription.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object.
    """
    object: Literal["v2.billing.pricing_plan_subscription"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_plan: str
    """
    The ID of the PricingPlan for this subscription.
    """
    pricing_plan_version: str
    """
    The ID of the PricingPlanVersion for this subscription.
    """
    servicing_status: Literal["active", "canceled", "paused", "pending"]
    """
    Current servicing status of this subscription.
    """
    servicing_status_transitions: ServicingStatusTransitions
    """
    Timestamps for servicing status transitions.
    """
    test_clock: Optional[str]
    """
    The ID of the TestClock of the associated Cadence, if any.
    """
    _inner_class_types = {
        "collection_status_transitions": CollectionStatusTransitions,
        "servicing_status_transitions": ServicingStatusTransitions,
    }
