# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class EventDestination(StripeObject):
    OBJECT_NAME: ClassVar[Literal["event_destination"]] = "event_destination"

    class StatusDetails(StripeObject):
        class Disabled(StripeObject):
            reason: Literal["no_aws_event_source_exists", "user"]
            """
            Closed Enum. Reason event destination has been disabled.
            """

        disabled: Optional[Disabled]
        """
        Details about why the event destination has been disabled.
        """
        _inner_class_types = {"disabled": Disabled}

    class AmazonEventbridge(StripeObject):
        aws_account_id: str
        """
        The AWS account ID.
        """
        aws_event_source_arn: str
        """
        The ARN of the AWS event source.
        """
        aws_event_source_status: Literal[
            "active", "deleted", "pending", "unknown"
        ]
        """
        Closed Enum. The state of the AWS event source.
        """

    class WebhookEndpoint(StripeObject):
        url: str
        """
        The URL of the webhook endpoint.
        """

    created: str
    """
    Time at which the object was created.
    """
    description: str
    """
    An optional description of what the event destination is used for.
    """
    enabled_events: List[str]
    """
    The list of events to enable for this endpoint.
    """
    event_namespace: Literal["v1", "v2"]
    """
    Closed Enum. Namespace of events being subscribed to.
    """
    events_from: Optional[List[Literal["accounts", "self"]]]
    """
    Open Enum. Where events should be routed from.
    """
    id: str
    """
    Unique identifier for the object.
    """
    metadata: Optional[Dict[str, str]]
    """
    Metadata.
    """
    name: str
    """
    Event destination name.
    """
    object: Literal["event_destination"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["disabled", "enabled"]
    """
    Closed Enum. Status. It can be set to either enabled or disabled.
    """
    status_details: Optional[StatusDetails]
    """
    Additional information about event destination status.
    """
    type: Literal["amazon_eventbridge", "webhook_endpoint"]
    """
    Closed Enum. Event destination type.
    """
    updated: str
    """
    Time at which the object was last updated.
    """
    v1_api_version: Optional[str]
    """
    If using the v1 event namespace, the API version events are rendered as.
    """
    amazon_eventbridge: Optional[AmazonEventbridge]
    """
    Amazon EventBridge configuration.
    """
    webhook_endpoint: Optional[WebhookEndpoint]
    """
    Webhook endpoint configuration.
    """
    _inner_class_types = {
        "status_details": StatusDetails,
        "amazon_eventbridge": AmazonEventbridge,
        "webhook_endpoint": WebhookEndpoint,
    }
