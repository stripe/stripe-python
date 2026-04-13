# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationCreateParams(TypedDict):
    amazon_eventbridge: NotRequired[
        "EventDestinationCreateParamsAmazonEventbridge"
    ]
    """
    Amazon EventBridge configuration.
    """
    description: NotRequired[str]
    """
    An optional description of what the event destination is used for.
    """
    enabled_events: List[str]
    """
    The list of events to enable for this endpoint.
    """
    event_payload: Literal["snapshot", "thin"]
    """
    Payload type of events being subscribed to.
    """
    events_from: NotRequired[List[str]]
    """
    Specifies which accounts' events route to this destination.
    `@self`: Receive events from the account that owns the event destination.
    `@accounts`: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.
    `@organization_members`: Receive events from accounts directly linked to the organization.
    `@organization_members/@accounts`: Receive events from all accounts connected to any platform accounts in the organization.
    """
    include: NotRequired[
        List[
            Literal["webhook_endpoint.signing_secret", "webhook_endpoint.url"]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata.
    """
    name: str
    """
    Event destination name.
    """
    snapshot_api_version: NotRequired[str]
    """
    If using the snapshot event payload, the API version events are rendered as.
    """
    type: Literal["amazon_eventbridge", "webhook_endpoint"]
    """
    Event destination type.
    """
    webhook_endpoint: NotRequired[
        "EventDestinationCreateParamsWebhookEndpoint"
    ]
    """
    Webhook endpoint configuration.
    """


class EventDestinationCreateParamsAmazonEventbridge(TypedDict):
    aws_account_id: str
    """
    The AWS account ID.
    """
    aws_region: str
    """
    The region of the AWS event source.
    """


class EventDestinationCreateParamsWebhookEndpoint(TypedDict):
    url: str
    """
    The URL of the webhook endpoint.
    """
