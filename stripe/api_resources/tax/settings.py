# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    SingletonAPIResource,
    UpdateableAPIResource,
)
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class ModifyParams(RequestOptions):
        defaults: NotRequired[Optional["Settings.ModifyDefaultsParams"]]
        expand: NotRequired[Optional[List[str]]]
        head_office: NotRequired[Optional["Settings.ModifyHeadOfficeParams"]]

    class ModifyHeadOfficeParams(TypedDict):
        address: "Settings.ModifyHeadOfficeAddressParams"

    class ModifyHeadOfficeAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyDefaultsParams(TypedDict):
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "inferred_by_currency"]]
        ]
        tax_code: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    defaults: StripeObject
    head_office: Optional[StripeObject]
    livemode: bool
    object: Literal["tax.settings"]
    status: Literal["active", "pending"]
    status_details: StripeObject

    @classmethod
    def modify(
        cls, id, **params: Unpack["Settings.ModifyParams"]
    ) -> "Settings":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Settings",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, **params: Unpack["Settings.RetrieveParams"]
    ) -> "Settings":
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/tax/settings"
