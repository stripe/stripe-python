# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from typing import Dict, List, Optional
from typing_extensions import Literal


class WebhookEndpoint(
    CreateableAPIResource["WebhookEndpoint"],
    DeletableAPIResource["WebhookEndpoint"],
    ListableAPIResource["WebhookEndpoint"],
    UpdateableAPIResource["WebhookEndpoint"],
):
    """
    You can configure [webhook endpoints](https://stripe.com/docs/webhooks/) via the API to be
    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up webhooks](https://stripe.com/docs/webhooks/configure)
    """

    OBJECT_NAME = "webhook_endpoint"
    api_version: Optional[str]
    application: Optional[str]
    created: str
    description: Optional[str]
    enabled_events: List[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["webhook_endpoint"]
    secret: str
    status: str
    url: str
