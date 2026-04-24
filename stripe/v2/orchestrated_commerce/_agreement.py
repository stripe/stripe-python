# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Agreement(StripeObject):
    """
    An Orchestrated Commerce Agreement represents a mutual agreement between a seller and an orchestrator/agent on the Stripe network.
    """

    OBJECT_NAME: ClassVar[Literal["v2.orchestrated_commerce.agreement"]] = (
        "v2.orchestrated_commerce.agreement"
    )

    class OrchestratorDetails(StripeObject):
        name: str
        """
        The name of the orchestrator. This can be the name of the agent or the name of the business.
        """
        network_business_profile: str
        """
        The Network ID of the orchestrator.
        """

    class SellerDetails(StripeObject):
        network_business_profile: str
        """
        The Network ID of the seller.
        """

    class StatusTransitions(StripeObject):
        orchestrator_confirmed_at: Optional[str]
        """
        The time at which the orchestrator confirmed the agreement.
        """
        seller_confirmed_at: Optional[str]
        """
        The time at which the seller confirmed the agreement.
        """
        terminated_at: Optional[str]
        """
        The time at which the agreement was terminated.
        """

    created: str
    """
    The time at which the agreement was created.
    """
    id: str
    """
    The unique identifier for the agreement.
    """
    initiated_by: Literal["orchestrator", "seller"]
    """
    The party that initiated the agreement.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.orchestrated_commerce.agreement"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    orchestrator_details: OrchestratorDetails
    """
    Details about the orchestrator.
    """
    seller_details: SellerDetails
    """
    Details about the seller.
    """
    status: Literal[
        "confirmed", "initiated", "partially_confirmed", "terminated"
    ]
    """
    The current status of the agreement.
    """
    status_transitions: StatusTransitions
    """
    Timestamps of key status transitions for the agreement.
    """
    terminated_by: Optional[Literal["orchestrator", "seller"]]
    """
    The party that terminated the agreement, if applicable.
    """
    _inner_class_types = {
        "orchestrator_details": OrchestratorDetails,
        "seller_details": SellerDetails,
        "status_transitions": StatusTransitions,
    }
