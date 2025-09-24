# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class RateCardSubscription(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.rate_card_subscription"]] = (
        "v2.billing.rate_card_subscription"
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
        will_activate_at: Optional[str]
        """
        When the servicing is scheduled to transition to activate.
        """
        will_cancel_at: Optional[str]
        """
        When the servicing is scheduled to cancel.
        """

    billing_cadence: str
    """
    The ID of the Billing Cadence.
    """
    collection_status: Optional[
        Literal[
            "awaiting_customer_action",
            "current",
            "past_due",
            "paused",
            "unpaid",
        ]
    ]
    """
    The payment status of a Rate Card Subscription.
    """
    collection_status_transitions: Optional[CollectionStatusTransitions]
    """
    The collection status transitions of the Rate Card Subscription.
    """
    created: str
    """
    Timestamp of when the object was created.
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
    object: Literal["v2.billing.rate_card_subscription"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    rate_card: str
    """
    The ID of the Rate Card.
    """
    rate_card_version: str
    """
    The ID of the Rate Card Version.
    """
    servicing_status: Optional[
        Literal["active", "canceled", "paused", "pending"]
    ]
    """
    The servicing status of a Rate Card Subscription.
    """
    servicing_status_transitions: Optional[ServicingStatusTransitions]
    """
    The servicing status transitions of the Rate Card Subscription.
    """
    test_clock: Optional[str]
    """
    The ID of the Test Clock, if any.
    """
    _inner_class_types = {
        "collection_status_transitions": CollectionStatusTransitions,
        "servicing_status_transitions": ServicingStatusTransitions,
    }
