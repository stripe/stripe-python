# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    SingletonAPIResource,
    UpdateableAPIResource,
)
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
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
    if TYPE_CHECKING:

        class ModifyParams(RequestOptions):
            defaults: NotRequired["Settings.ModifyParamsDefaults|None"]
            expand: NotRequired["List[str]|None"]
            head_office: NotRequired["Settings.ModifyParamsHeadOffice|None"]

        class ModifyParamsHeadOffice(TypedDict):
            address: "Settings.ModifyParamsHeadOfficeAddress"

        class ModifyParamsHeadOfficeAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsDefaults(TypedDict):
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'inferred_by_currency']|None"
            ]
            tax_code: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
