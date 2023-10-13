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

    class Defaults(StripeObject):
        tax_behavior: Optional[
            Literal["exclusive", "inclusive", "inferred_by_currency"]
        ]
        tax_code: Optional[str]

    class HeadOffice(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Address
        _inner_class_types = {"address": Address}

    class StatusDetails(StripeObject):
        class Active(StripeObject):
            pass

        class Pending(StripeObject):
            missing_fields: Optional[List[str]]

        active: Optional[Active]
        pending: Optional[Pending]
        _inner_class_types = {"active": Active, "pending": Pending}

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

    defaults: Defaults
    head_office: Optional[HeadOffice]
    livemode: bool
    object: Literal["tax.settings"]
    status: Literal["active", "pending"]
    status_details: StatusDetails

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

    _inner_class_types = {
        "defaults": Defaults,
        "head_office": HeadOffice,
        "status_details": StatusDetails,
    }
