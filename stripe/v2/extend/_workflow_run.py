# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, Optional
from typing_extensions import Literal


class WorkflowRun(StripeObject):
    """
    An execution of a Workflow in response to a triggering event.
    """

    OBJECT_NAME: ClassVar[Literal["v2.extend.workflow_run"]] = (
        "v2.extend.workflow_run"
    )

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            error_message: Optional[str]
            """
            Optional details about the failure result.
            """

        class Started(StripeObject):
            pass

        class Succeeded(StripeObject):
            pass

        failed: Optional[Failed]
        """
        Details about the Workflow Run's transition into the FAILED state.
        """
        started: Optional[Started]
        """
        Details about the Workflow Run's transition in to the STARTED state.
        """
        succeeded: Optional[Succeeded]
        """
        Details about the Workflow Run's transition into the SUCCEEDED state.
        """
        _inner_class_types = {
            "failed": Failed,
            "started": Started,
            "succeeded": Succeeded,
        }

    class StatusTransitions(StripeObject):
        failed_at: Optional[str]
        """
        When the Workflow Run failed.
        """
        started_at: Optional[str]
        """
        When the Workflow Run was started.
        """
        succeeded_at: Optional[str]
        """
        When the Workflow Run succeeded.
        """

    class Trigger(StripeObject):
        class EventTrigger(StripeObject):
            context: str
            """
            The account that generated the triggering event.
            """
            id: str
            """
            The Stripe event that triggered this Run.
            """
            type: str
            """
            The Stripe event type triggered this Run.
            """

        class Manual(StripeObject):
            input_parameters: UntypedStripeObject[Any]
            """
            The input parameters used when launching the Run.
            """

        event_trigger: Optional[EventTrigger]
        """
        The Workflow Run was launched when Stripe emitted a certain event.
        """
        manual: Optional[Manual]
        """
        The Workflow Run was launched through a direct call, using either the Dashboard or the Stripe API.
        """
        type: Literal["event_trigger", "manual"]
        """
        Which type of trigger this is.
        """
        _inner_class_types = {"event_trigger": EventTrigger, "manual": Manual}

    created: str
    """
    When the Workflow Run was created.
    """
    id: str
    """
    The unique ID of the Workflow Run.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.extend.workflow_run"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["failed", "started", "succeeded"]
    """
    The current Workflow Run execution status.
    """
    status_details: Optional[StatusDetails]
    """
    Details about the Workflow Run's status transitions.
    """
    status_transitions: StatusTransitions
    """
    Summary information about the Workflow Run's status transitions.
    """
    trigger: Trigger
    """
    A record of the trigger that launched this Workflow Run.
    """
    workflow: str
    """
    The Workflow this Run belongs to.
    """
    _inner_class_types = {
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "trigger": Trigger,
    }
