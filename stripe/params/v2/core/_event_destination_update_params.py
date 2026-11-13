# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationUpdateParams(TypedDict):
    description: NotRequired[str]
    """
    An optional user-defined description of the destination's purpose; it does not control routing.
    """
    enabled_events: NotRequired[List[str]]
    """
    The list of event types enabled for delivery to this destination. Event scopes are configured when the destination is created.
    """
    include: NotRequired[List[Union[Literal["webhook_endpoint.url"], str]]]
    """
    Include the normally redacted `webhook_endpoint.url` in the response.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata.
    """
    name: NotRequired[str]
    """
    A user-defined label for identifying the destination; it does not control routing.
    """
    webhook_endpoint: NotRequired[
        "EventDestinationUpdateParamsWebhookEndpoint"
    ]
    """
    New delivery target for the webhook endpoint. Live mode requires HTTPS; sandbox mode also supports HTTP.
    """


class EventDestinationUpdateParamsWebhookEndpoint(TypedDict):
    url: str
    """
    The URL where Stripe sends matching events. Live mode requires HTTPS; sandbox mode also supports HTTP.
    """
