# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    SingletonAPIResource,
    UpdateableAPIResource,
)
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
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

    OBJECT_NAME: ClassVar[Literal["tax.settings"]] = "tax.settings"

    class Defaults(StripeObject):
        tax_behavior: Optional[
            Literal["exclusive", "inclusive", "inferred_by_currency"]
        ]
        """
        Default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) used to specify whether the price is considered inclusive of taxes or exclusive of taxes. If the item's price has a tax behavior set, it will take precedence over the default tax behavior.
        """
        tax_code: Optional[str]
        """
        Default [tax code](https://stripe.com/docs/tax/tax-categories) used to classify your products and prices.
        """

    class HeadOffice(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Address
        _inner_class_types = {"address": Address}

    class StatusDetails(StripeObject):
        class Active(StripeObject):
            pass

        class Pending(StripeObject):
            missing_fields: Optional[List[str]]
            """
            The list of missing fields that are required to perform calculations. It includes the entry `head_office` when the status is `pending`. It is recommended to set the optional values even if they aren't listed as required for calculating taxes. Calculations can fail if missing fields aren't explicitly provided on every call.
            """

        active: Optional[Active]
        pending: Optional[Pending]
        _inner_class_types = {"active": Active, "pending": Pending}

    if TYPE_CHECKING:

        class ModifyParams(RequestOptions):
            defaults: NotRequired["Settings.ModifyParamsDefaults|None"]
            """
            Default configuration to be used on Stripe Tax calculations.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            head_office: NotRequired["Settings.ModifyParamsHeadOffice|None"]
            """
            The place where your business is located.
            """

        class ModifyParamsHeadOffice(TypedDict):
            address: "Settings.ModifyParamsHeadOfficeAddress"
            """
            The location of the business for tax purposes.
            """

        class ModifyParamsHeadOfficeAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
            """

        class ModifyParamsDefaults(TypedDict):
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'inferred_by_currency']|None"
            ]
            """
            Specifies the default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) to be used when the item's price has unspecified tax behavior. One of inclusive, exclusive, or inferred_by_currency. Once specified, it cannot be changed back to null.
            """
            tax_code: NotRequired["str|None"]
            """
            A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    defaults: Defaults
    head_office: Optional[HeadOffice]
    """
    The place where your business is located.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax.settings"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "pending"]
    """
    The `active` status indicates you have all required settings to calculate tax. A status can transition out of `active` when new required settings are introduced.
    """
    status_details: StatusDetails

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Settings.ModifyParams"]
    ) -> "Settings":
        """
        Updates Tax Settings parameters used in tax calculations. All parameters are editable but none can be removed once set.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Settings",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, **params: Unpack["Settings.RetrieveParams"]
    ) -> "Settings":
        """
        Retrieves Tax Settings for a merchant.
        """
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
