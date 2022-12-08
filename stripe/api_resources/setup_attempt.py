# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class SetupAttempt(ListableAPIResource):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,
    whether that confirmation was successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.
    """

    OBJECT_NAME = "setup_attempt"
