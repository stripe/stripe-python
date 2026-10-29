# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class EventDestination(StripeObject):
    """
    Set up an event destination to receive events from Stripe across multiple destination types, including [webhook endpoints](https://docs.stripe.com/webhooks), [Amazon EventBridge](https://docs.stripe.com/event-destinations/eventbridge), and [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid). Event destinations support receiving [thin events](https://docs.stripe.com/api/v2/events) and [snapshot events](https://docs.stripe.com/api/events).
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.event_destination"]] = (
        "v2.core.event_destination"
    )

    class AmazonEventbridge(StripeObject):
        aws_account_id: str
        """
        The AWS account ID that owns the event bus receiving events.
        """
        aws_event_source_arn: str
        """
        The ARN of the Stripe-created partner event source in your AWS account.
        """
        aws_event_source_status: Literal[
            "active", "deleted", "pending", "unknown"
        ]
        """
        The AWS-reported lifecycle state of the partner event source.
        """

    class AzureEventGrid(StripeObject):
        azure_partner_topic_name: str
        """
        The name of the Stripe-created partner topic that receives events.
        """
        azure_partner_topic_status: Union[
            Literal["activated", "deleted", "never_activated", "unknown"], str
        ]
        """
        The Azure-reported lifecycle state of the partner topic.
        """
        azure_region: str
        """
        The Azure region where the partner topic is located.
        """
        azure_resource_group_name: str
        """
        The Azure resource group containing the partner topic.
        """
        azure_subscription_id: str
        """
        The Azure subscription containing the resource group and partner topic.
        """

    class StatusDetails(StripeObject):
        class Disabled(StripeObject):
            reason: Union[
                Literal[
                    "no_aws_event_source_exists",
                    "no_azure_partner_topic_exists",
                    "user",
                ],
                str,
            ]
            """
            Reason event destination has been disabled.
            """

        disabled: Optional[Disabled]
        """
        Present when the destination was disabled; identifies the cause, time, and provider-side object involved when available.
        """
        _inner_class_types = {"disabled": Disabled}

    class WebhookEndpoint(StripeObject):
        signing_secret: Optional[str]
        """
        The secret used to verify Stripe signatures on delivered events. Returned only in the create response when explicitly included; public API clients cannot retrieve it later.
        """
        url: Optional[str]
        """
        The URL where Stripe sends matching events. Live mode requires HTTPS; sandbox mode also supports HTTP. Returned only when explicitly included.
        """

    amazon_eventbridge: Optional[AmazonEventbridge]
    """
    Configuration for delivering events through an Amazon EventBridge partner event source.
    """
    azure_event_grid: Optional[AzureEventGrid]
    """
    Configuration for delivering events through an Azure Event Grid partner topic.
    """
    created: str
    """
    The time when the destination was created.
    """
    description: str
    """
    An optional user-defined description of the destination's purpose.
    """
    enabled_events: List[str]
    """
    The list of event types enabled for delivery to this destination.
    """
    event_payload: Literal["snapshot", "thin"]
    """
    Whether to deliver as snapshot or thin events.
    """
    events_from: Optional[List[str]]
    """
    Specifies which accounts' events route to this destination.
    `@self`: Receive events from the account that owns the event destination.
    `@accounts`: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.
    `@organization_members`: Receive events from accounts directly linked to the organization.
    `@organization_members/@accounts`: Receive events from all accounts connected to any platform accounts in the organization.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    User-defined key/value data for the destination; it has no effect on event matching or delivery.
    """
    name: str
    """
    A user-defined label for identifying the destination in Stripe.
    """
    object: Literal["v2.core.event_destination"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    snapshot_api_version: Optional[str]
    """
    For snapshot events only, the Stripe API version used to render event objects. You can't change this value after you create the event destination. Thin events are not pinned to an API version.
    """
    status: Literal["disabled", "enabled"]
    """
    Whether Stripe currently attempts delivery. Stripe attempts delivery to enabled destinations when their provider configuration is active; disabled destinations do not receive delivery attempts.
    """
    status_details: Optional[StatusDetails]
    """
    Additional lifecycle context for the destination status, when available.
    """
    type: Union[
        Literal["amazon_eventbridge", "azure_event_grid", "webhook_endpoint"],
        str,
    ]
    """
    The delivery transport. Chosen when the destination is created and cannot be changed by update.
    """
    updated: str
    """
    The time when the destination object was last updated.
    """
    webhook_endpoint: Optional[WebhookEndpoint]
    """
    Configuration for delivering events to a webhook endpoint. Live mode requires HTTPS; sandbox mode also supports HTTP.
    """
    _inner_class_types = {
        "amazon_eventbridge": AmazonEventbridge,
        "azure_event_grid": AzureEventGrid,
        "status_details": StatusDetails,
        "webhook_endpoint": WebhookEndpoint,
    }
