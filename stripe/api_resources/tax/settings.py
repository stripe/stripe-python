# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import SingletonAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class Settings(
    SingletonAPIResource["Settings"],
    UpdateableAPIResource["Settings"],
):
    """
    You can use Tax `Settings` to manage configurations used by Stripe Tax calculations.

    Related guide: [Using the Settings API](https://stripe.com/docs/tax/settings-api)
    """

    OBJECT_NAME = "tax.settings"
    defaults: StripeObject
    head_office: Optional[StripeObject]
    livemode: bool
    object: Literal["tax.settings"]
    status: str
    status_details: StripeObject

    @classmethod
    def class_url(cls):
        return "/v1/tax/settings"
