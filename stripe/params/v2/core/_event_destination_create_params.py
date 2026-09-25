# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationCreateParams(TypedDict):
    amazon_eventbridge: NotRequired[
        "EventDestinationCreateParamsAmazonEventbridge"
    ]
    """
    AWS account and region where Stripe creates the EventBridge partner event source.
    """
    azure_event_grid: NotRequired["EventDestinationCreateParamsAzureEventGrid"]
    """
    Azure subscription, resource group, and region where Stripe creates the partner topic.
    """
    description: NotRequired[str]
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
    events_from: NotRequired[List[str]]
    """
    The account or organization scopes that can supply events. Use this with `enabled_events` to define the subscription.
    `@self`: Receive events from the account that owns the event destination.
    `@accounts`: Receive events emitted from other accounts you manage, including your v1 and v2 accounts.
    `@organization_members`: Receive events from accounts directly linked to the organization.
    `@organization_members/@accounts`: Receive events from all accounts connected to any platform accounts in the organization.
    """
    include: NotRequired[
        List[
            Union[
                Literal[
                    "webhook_endpoint.signing_secret", "webhook_endpoint.url"
                ],
                str,
            ]
        ]
    ]
    """
    Include normally redacted webhook fields in the create response. Public API clients must include `webhook_endpoint.signing_secret` to receive the signing secret.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    User-defined key/value data for the destination.
    """
    name: str
    """
    A user-defined label for identifying the destination.
    """
    snapshot_api_version: NotRequired[str]
    """
    For snapshot events only, the Stripe API version used to render event objects; do not provide this for thin events.
    """
    type: Union[
        Literal["amazon_eventbridge", "azure_event_grid", "webhook_endpoint"],
        str,
    ]
    """
    The delivery transport. Chosen when the destination is created and cannot be changed by update.
    """
    webhook_endpoint: NotRequired[
        "EventDestinationCreateParamsWebhookEndpoint"
    ]
    """
    Delivery target for the webhook endpoint. Live mode requires HTTPS; sandbox mode also supports HTTP.
    """


class EventDestinationCreateParamsAmazonEventbridge(TypedDict):
    aws_account_id: str
    """
    Your AWS account where Stripe creates the partner event source.
    """
    aws_region: str
    """
    The AWS region where Stripe creates the partner event source.
    """


class EventDestinationCreateParamsAzureEventGrid(TypedDict):
    azure_region: str
    """
    The Azure region where Stripe creates the partner topic.
    """
    azure_resource_group_name: str
    """
    The Azure resource group where Stripe creates the partner topic.
    """
    azure_subscription_id: str
    """
    The Azure subscription where Stripe creates the partner topic.
    """


class EventDestinationCreateParamsWebhookEndpoint(TypedDict):
    url: str
    """
    The URL where Stripe sends matching events. Live mode requires HTTPS; sandbox mode also supports HTTP.
    """
