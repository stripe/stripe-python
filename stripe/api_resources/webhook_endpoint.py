# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class WebhookEndpoint(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    You can configure [webhook endpoints](https://stripe.com/docs/webhooks/) via the API to be
    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up Webhooks](https://stripe.com/docs/webhooks/configure).
    """

    OBJECT_NAME = "webhook_endpoint"
