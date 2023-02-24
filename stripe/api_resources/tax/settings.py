# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import SingletonAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Settings(SingletonAPIResource, UpdateableAPIResource):
    """
    You can use Tax `Settings` to manage configurations used by Stripe Tax calculations.

    Related guide: [Account settings](https://stripe.com/docs/tax/connect/settings).
    """

    OBJECT_NAME = "tax.settings"

    @classmethod
    def class_url(cls):
        return "/v1/tax/settings"
