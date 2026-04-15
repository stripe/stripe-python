# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class Workflow(StripeObject):
    """
    A Stripe Workflow is a sequence of actions, like Stripe API calls, that are taken in response to an initiating trigger.
    A trigger can be a Stripe API event, or a manual invocation.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.workflow"]] = "v2.core.workflow"

    class Trigger(StripeObject):
        class EventTrigger(StripeObject):
            type: str
            """
            The Stripe event type that will trigger this Workflow.
            """

        class Manual(StripeObject):
            raw_schema: str
            """
            An unprocessed version of the trigger's input parameter schema.
            """

        event_trigger: Optional[EventTrigger]
        """
        The Workflow can be launched when Stripe emits a certain event.
        """
        manual: Optional[Manual]
        """
        The Workflow can be launched through a direct call, using either the Dashboard or the Stripe API.
        """
        type: Literal["event_trigger", "manual"]
        """
        Which type of trigger this is.
        """
        _inner_class_types = {"event_trigger": EventTrigger, "manual": Manual}

    created: str
    """
    When the Workflow was created.
    """
    description: str
    """
    Workflow description.
    """
    id: str
    """
    The unique ID of the Workflow.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.workflow"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["active", "archived", "draft", "inactive"]
    """
    Whether this Workflow is active, inactive, or in some other state. Only active Workflows may be invoked.
    """
    triggers: List[Trigger]
    """
    Under what conditions will this Workflow launch.
    """
    _inner_class_types = {"triggers": Trigger}
