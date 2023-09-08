# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from typing_extensions import Literal


class ConnectionToken(CreateableAPIResource["ConnectionToken"]):
    """
    A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    OBJECT_NAME = "terminal.connection_token"
    location: str
    object: Literal["terminal.connection_token"]
    secret: str
