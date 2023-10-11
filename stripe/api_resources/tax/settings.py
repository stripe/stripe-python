# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    SingletonAPIResource,
    UpdateableAPIResource,
)
from stripe.stripe_object import StripeObject
from typing import Any, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


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
    status: Literal["active", "pending"]
    status_details: StripeObject

    @classmethod
    def modify(cls, id, **params: Any) -> "Settings":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Settings",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(cls, **params: Any) -> "Settings":
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/tax/settings"
