# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import get_api_mode
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_client import StripeClient
    from stripe.v2.extend._workflow_run import WorkflowRun


class V2ExtendWorkflowRunFailedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.extend.workflow_run.failed"
    type: Literal["v2.extend.workflow_run.failed"]
    related_object: RelatedObject

    def __init__(
        self, parsed_body: Dict[str, Any], client: "StripeClient"
    ) -> None:
        super().__init__(
            parsed_body,
            client,
        )
        self.related_object = RelatedObject(parsed_body["related_object"])

    @override
    def fetch_event(self) -> "V2ExtendWorkflowRunFailedEvent":
        return cast(
            "V2ExtendWorkflowRunFailedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "WorkflowRun":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "WorkflowRun",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(self) -> "V2ExtendWorkflowRunFailedEvent":
        return cast(
            "V2ExtendWorkflowRunFailedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "WorkflowRun":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "WorkflowRun",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2ExtendWorkflowRunFailedEvent(Event):
    LOOKUP_TYPE = "v2.extend.workflow_run.failed"
    type: Literal["v2.extend.workflow_run.failed"]

    class V2ExtendWorkflowRunFailedEventData(StripeObject):
        class FailureDetails(StripeObject):
            error_message: Optional[str]
            """
            Optional details about the failure result.
            """

        dashboard_url: str
        """
        A Stripe dashboard URL with more information about the Workflow Run failure.
        """
        failure_details: FailureDetails
        """
        Details about the Workflow Run's transition into the FAILED state.
        """
        _inner_class_types = {"failure_details": FailureDetails}

    data: V2ExtendWorkflowRunFailedEventData
    """
    Data for the v2.extend.workflow_run.failed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2ExtendWorkflowRunFailedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2ExtendWorkflowRunFailedEvent.V2ExtendWorkflowRunFailedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> "WorkflowRun":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "WorkflowRun",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={
                    "stripe_context": self.context,
                    "headers": {"Stripe-Request-Trigger": f"event={self.id}"},
                },
            ),
        )
