# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class Location(
    CreateableAPIResource["Location"],
    DeletableAPIResource["Location"],
    ListableAPIResource["Location"],
    UpdateableAPIResource["Location"],
):
    """
    A Location represents a grouping of readers.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    OBJECT_NAME: ClassVar[Literal["terminal.location"]] = "terminal.location"

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
        State, county, province, or region.
        """

    class AddressKana(StripeObject):
        city: Optional[str]
        """
        City/Ward.
        """
        country: Optional[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: Optional[str]
        """
        Block/Building number.
        """
        line2: Optional[str]
        """
        Building details.
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        Prefecture.
        """
        town: Optional[str]
        """
        Town/cho-me.
        """

    class AddressKanji(StripeObject):
        city: Optional[str]
        """
        City/Ward.
        """
        country: Optional[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: Optional[str]
        """
        Block/Building number.
        """
        line2: Optional[str]
        """
        Building details.
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        Prefecture.
        """
        town: Optional[str]
        """
        Town/cho-me.
        """

    class CreateParams(RequestOptions):
        address: NotRequired["Location.CreateParamsAddress"]
        """
        The full address of the location.
        """
        address_kana: NotRequired["Location.CreateParamsAddressKana"]
        """
        The Kana variation of the full address of the location (Japan only).
        """
        address_kanji: NotRequired["Location.CreateParamsAddressKanji"]
        """
        The Kanji variation of the full address of the location (Japan only).
        """
        configuration_overrides: NotRequired[str]
        """
        The ID of a configuration that will be used to customize all readers in this location.
        """
        display_name: NotRequired[str]
        """
        A name for the location. Maximum length is 1000 characters.
        """
        display_name_kana: NotRequired[str]
        """
        The Kana variation of the name for the location (Japan only). Maximum length is 1000 characters.
        """
        display_name_kanji: NotRequired[str]
        """
        The Kanji variation of the name for the location (Japan only). Maximum length is 1000 characters.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        phone: NotRequired[str]
        """
        The phone number for the location.
        """

    class CreateParamsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: str
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1, such as the street, PO Box, or company name.
        """
        line2: NotRequired[str]
        """
        Address line 2, such as the apartment, suite, unit, or building.
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class CreateParamsAddressKana(TypedDict):
        city: NotRequired[str]
        """
        City or ward.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Block or building number.
        """
        line2: NotRequired[str]
        """
        Building details.
        """
        postal_code: NotRequired[str]
        """
        Postal code.
        """
        state: NotRequired[str]
        """
        Prefecture.
        """
        town: NotRequired[str]
        """
        Town or cho-me.
        """

    class CreateParamsAddressKanji(TypedDict):
        city: NotRequired[str]
        """
        City or ward.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Block or building number.
        """
        line2: NotRequired[str]
        """
        Building details.
        """
        postal_code: NotRequired[str]
        """
        Postal code.
        """
        state: NotRequired[str]
        """
        Prefecture.
        """
        town: NotRequired[str]
        """
        Town or cho-me.
        """

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        address: NotRequired["Location.ModifyParamsAddress"]
        """
        The full address of the location. You can't change the location's `country`. If you need to modify the `country` field, create a new `Location` object and re-register any existing readers to that location.
        """
        address_kana: NotRequired["Location.ModifyParamsAddressKana"]
        """
        The Kana variation of the full address of the location (Japan only).
        """
        address_kanji: NotRequired["Location.ModifyParamsAddressKanji"]
        """
        The Kanji variation of the full address of the location (Japan only).
        """
        configuration_overrides: NotRequired["Literal['']|str"]
        """
        The ID of a configuration that will be used to customize all readers in this location.
        """
        display_name: NotRequired["Literal['']|str"]
        """
        A name for the location.
        """
        display_name_kana: NotRequired["Literal['']|str"]
        """
        The Kana variation of the name for the location (Japan only).
        """
        display_name_kanji: NotRequired["Literal['']|str"]
        """
        The Kanji variation of the name for the location (Japan only).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        phone: NotRequired["Literal['']|str"]
        """
        The phone number for the location.
        """

    class ModifyParamsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1, such as the street, PO Box, or company name.
        """
        line2: NotRequired[str]
        """
        Address line 2, such as the apartment, suite, unit, or building.
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ModifyParamsAddressKana(TypedDict):
        city: NotRequired[str]
        """
        City or ward.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Block or building number.
        """
        line2: NotRequired[str]
        """
        Building details.
        """
        postal_code: NotRequired[str]
        """
        Postal code.
        """
        state: NotRequired[str]
        """
        Prefecture.
        """
        town: NotRequired[str]
        """
        Town or cho-me.
        """

    class ModifyParamsAddressKanji(TypedDict):
        city: NotRequired[str]
        """
        City or ward.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Block or building number.
        """
        line2: NotRequired[str]
        """
        Building details.
        """
        postal_code: NotRequired[str]
        """
        Postal code.
        """
        state: NotRequired[str]
        """
        Prefecture.
        """
        town: NotRequired[str]
        """
        Town or cho-me.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    address: Address
    address_kana: Optional[AddressKana]
    address_kanji: Optional[AddressKanji]
    configuration_overrides: Optional[str]
    """
    The ID of a configuration that will be used to customize all readers in this location.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """
    display_name: str
    """
    The display name of the location.
    """
    display_name_kana: Optional[str]
    """
    The Kana variation of the display name of the location.
    """
    display_name_kanji: Optional[str]
    """
    The Kanji variation of the display name of the location.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["terminal.location"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone: Optional[str]
    """
    The phone number of the location.
    """

    @classmethod
    def create(cls, **params: Unpack["Location.CreateParams"]) -> "Location":
        """
        Creates a new Location object.
        For further details, including which address fields are required in each country, see the [Manage locations](https://docs.stripe.com/docs/terminal/fleet/locations) guide.
        """
        return cast(
            "Location",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Location.CreateParams"]
    ) -> "Location":
        """
        Creates a new Location object.
        For further details, including which address fields are required in each country, see the [Manage locations](https://docs.stripe.com/docs/terminal/fleet/locations) guide.
        """
        return cast(
            "Location",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Location",
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Location.DeleteParams"]) -> "Location":
        """
        Deletes a Location object.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Location",
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        """
        Deletes a Location object.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls, **params: Unpack["Location.ListParams"]
    ) -> ListObject["Location"]:
        """
        Returns a list of Location objects.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Location.ListParams"]
    ) -> ListObject["Location"]:
        """
        Returns a list of Location objects.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Location.ModifyParams"]
    ) -> "Location":
        """
        Updates a Location object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Location",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Location.ModifyParams"]
    ) -> "Location":
        """
        Updates a Location object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Location",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Location.RetrieveParams"]
    ) -> "Location":
        """
        Retrieves a Location object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Location.RetrieveParams"]
    ) -> "Location":
        """
        Retrieves a Location object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "address": Address,
        "address_kana": AddressKana,
        "address_kanji": AddressKanji,
    }
