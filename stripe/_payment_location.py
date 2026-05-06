# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._payment_location_create_params import (
        PaymentLocationCreateParams,
    )
    from stripe.params._payment_location_delete_params import (
        PaymentLocationDeleteParams,
    )
    from stripe.params._payment_location_modify_params import (
        PaymentLocationModifyParams,
    )
    from stripe.params._payment_location_retrieve_params import (
        PaymentLocationRetrieveParams,
    )


class PaymentLocation(
    CreateableAPIResource["PaymentLocation"],
    DeletableAPIResource["PaymentLocation"],
    UpdateableAPIResource["PaymentLocation"],
):
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
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
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

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "PaymentLocation",
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "PaymentLocation",
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentLocationDeleteParams"]
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["PaymentLocationModifyParams"]
    ) -> "PaymentLocation":
        """
        Update a Payment Location.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentLocation",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["PaymentLocationModifyParams"]
    ) -> "PaymentLocation":
        """
        Update a Payment Location.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentLocation",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentLocationRetrieveParams"]
    ) -> "PaymentLocation":
        """
        Retrieve a Payment Location.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentLocationRetrieveParams"]
    ) -> "PaymentLocation":
        """
        Retrieve a Payment Location.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "address": Address,
        "business_registration": BusinessRegistration,
        "capability_settings": CapabilitySettings,
    }
