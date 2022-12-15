# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource


class AccountSession(CreateableAPIResource):
    """
    An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded UIs.

    We recommend that you create an AccountSession each time you need to display an embedded UI
    to your user. Do not save AccountSessions to your database as they expire relatively
    quickly, and cannot be used more than once.

    Related guide: [Connect embedded UIs](https://stripe.com/docs/connect/get-started-connect-embedded-uis).
    """

    OBJECT_NAME = "account_session"
