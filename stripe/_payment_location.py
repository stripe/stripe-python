# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._payment_location_create_params import (
        PaymentLocationCreateParams,
    )


class PaymentLocation(CreateableAPIResource["PaymentLocation"]):
    """
    A Payment Location represents a physical location where payments take place.
    """

    OBJECT_NAME: ClassVar[Literal["payment_location"]] = "payment_location"

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
        Address line 1, such as the street, PO Box, or company name.
        """
        line2: Optional[str]
        """
        Address line 2, such as the apartment, suite, unit, or building.
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
        """

    class BusinessRegistration(StripeObject):
        siret: Optional[str]
        """
        14-digit SIRET (Système d'identification du répertoire des établissements) number for the location.
        """

    class CapabilitySettings(StripeObject):
        class FrMealVouchersConecsPayments(StripeObject):
            class SupportedIssuers(StripeObject):
                card: Optional[
                    List[Literal["bimpli", "edenred", "pluxee", "up"]]
                ]
                """
                Supported meal voucher issuers for card payments.
                """
                card_present: Optional[
                    List[Literal["bimpli", "edenred", "pluxee", "up"]]
                ]
                """
                Supported meal voucher issuers for card present payments.
                """

            supported_issuers: Optional[SupportedIssuers]
            """
            Supported meal voucher issuers.
            """
            _inner_class_types = {"supported_issuers": SupportedIssuers}

        fr_meal_vouchers_conecs_payments: Optional[
            FrMealVouchersConecsPayments
        ]
        """
        Settings for Conecs French meal voucher capability.
        """
        _inner_class_types = {
            "fr_meal_vouchers_conecs_payments": FrMealVouchersConecsPayments,
        }

    address: Address
    business_registration: Optional[BusinessRegistration]
    """
    Identification numbers associated with the location.
    """
    capability_settings: Optional[CapabilitySettings]
    """
    The capability settings for the location. Only applicable for locations with requested Payment Location Capabilities.
    """
    display_name: str
    """
    The display name of the location.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["payment_location"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def create(
        cls, **params: Unpack["PaymentLocationCreateParams"]
    ) -> "PaymentLocation":
        """
        Create a Payment Location.
        """
        return cast(
            "PaymentLocation",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["PaymentLocationCreateParams"]
    ) -> "PaymentLocation":
        """
        Create a Payment Location.
        """
        return cast(
            "PaymentLocation",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {
        "address": Address,
        "business_registration": BusinessRegistration,
        "capability_settings": CapabilitySettings,
    }
