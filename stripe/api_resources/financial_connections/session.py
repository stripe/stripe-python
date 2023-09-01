# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.stripe_object import StripeObject
from typing import Any
from typing import List
from typing import Optional
from typing_extensions import Literal


class Session(CreateableAPIResource["Session"]):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    OBJECT_NAME = "financial_connections.session"
    account_holder: Optional[StripeObject]
    accounts: Any
    client_secret: str
    filters: StripeObject
    id: str
    livemode: bool
    object: Literal["financial_connections.session"]
    permissions: List[str]
    prefetch: Optional[List[str]]
    return_url: str
