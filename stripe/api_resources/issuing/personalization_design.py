# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.file import File
    from stripe.api_resources.issuing.physical_bundle import PhysicalBundle


class PersonalizationDesign(
    CreateableAPIResource["PersonalizationDesign"],
    ListableAPIResource["PersonalizationDesign"],
    UpdateableAPIResource["PersonalizationDesign"],
):
    """
    A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.
    """

    OBJECT_NAME: ClassVar[
        Literal["issuing.personalization_design"]
    ] = "issuing.personalization_design"

    class CarrierText(StripeObject):
        footer_body: Optional[str]
        """
        The footer body text of the carrier letter.
        """
        footer_title: Optional[str]
        """
        The footer title text of the carrier letter.
        """
        header_body: Optional[str]
        """
        The header body text of the carrier letter.
        """
        header_title: Optional[str]
        """
        The header title text of the carrier letter.
        """

    class Preferences(StripeObject):
        is_default: bool
        """
        Whether this personalization design is used to create cards when one is not specified. A connected account will use the Connect platform's default if no personalization design is set as the account default.
        """
        is_platform_default: Optional[bool]
        """
        Whether this personalization design is used to create cards when one is not specified and a default for this connected account does not exist.
        """

    class RejectionReasons(StripeObject):
        card_logo: Optional[
            List[
                Literal[
                    "geographic_location",
                    "inappropriate",
                    "network_name",
                    "non_binary_image",
                    "non_fiat_currency",
                    "other",
                    "other_entity",
                    "promotional_material",
                ]
            ]
        ]
        """
        The reason(s) the card logo was rejected.
        """
        carrier_text: Optional[
            List[
                Literal[
                    "geographic_location",
                    "inappropriate",
                    "network_name",
                    "non_fiat_currency",
                    "other",
                    "other_entity",
                    "promotional_material",
                ]
            ]
        ]
        """
        The reason(s) the carrier text was rejected.
        """

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            card_logo: NotRequired["str|None"]
            """
            The file for the card logo, for use with physical bundles that support card logos. Must have `purpose` value of `issuing_logo`.
            """
            carrier_text: NotRequired[
                "PersonalizationDesign.CreateParamsCarrierText|None"
            ]
            """
            Hash containing carrier text, for use with physical bundles that support carrier text.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            lookup_key: NotRequired["str|None"]
            """
            A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["str|None"]
            """
            Friendly display name.
            """
            physical_bundle: str
            """
            The physical bundle object belonging to this personalization design.
            """
            preferences: NotRequired[
                "PersonalizationDesign.CreateParamsPreferences|None"
            ]
            """
            Information on whether this personalization design is used to create cards when one is not specified.
            """
            transfer_lookup_key: NotRequired["bool|None"]
            """
            If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.
            """

        class CreateParamsPreferences(TypedDict):
            is_default: bool
            """
            Whether this personalization design is used to create cards when one is not specified. A connected account will use the Connect platform's default if no personalization design is set as default.
            """

        class CreateParamsCarrierText(TypedDict):
            footer_body: NotRequired["Literal['']|str|None"]
            """
            The footer body text of the carrier letter.
            """
            footer_title: NotRequired["Literal['']|str|None"]
            """
            The footer title text of the carrier letter.
            """
            header_body: NotRequired["Literal['']|str|None"]
            """
            The header body text of the carrier letter.
            """
            header_title: NotRequired["Literal['']|str|None"]
            """
            The header title text of the carrier letter.
            """

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            lookup_keys: NotRequired["List[str]|None"]
            """
            Only return personalization designs with the given lookup keys.
            """
            preferences: NotRequired[
                "PersonalizationDesign.ListParamsPreferences|None"
            ]
            """
            Only return personalization designs with the given preferences.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['active', 'inactive', 'rejected', 'review']|None"
            ]
            """
            Only return personalization designs with the given status.
            """

        class ListParamsPreferences(TypedDict):
            is_default: NotRequired["bool|None"]
            """
            Only return the personalization design that is set as default. A connected account will use the Connect platform's default if no personalization design is set as default.
            """
            is_platform_default: NotRequired["bool|None"]
            """
            Only return the personalization design that is set as the Connect platform's default. This parameter is only applicable to connected accounts.
            """

        class ModifyParams(RequestOptions):
            card_logo: NotRequired["Literal['']|str|None"]
            """
            The file for the card logo, for use with physical bundles that support card logos. Must have `purpose` value of `issuing_logo`.
            """
            carrier_text: NotRequired[
                "Literal['']|PersonalizationDesign.ModifyParamsCarrierText|None"
            ]
            """
            Hash containing carrier text, for use with physical bundles that support carrier text.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            lookup_key: NotRequired["Literal['']|str|None"]
            """
            A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Friendly display name. Providing an empty string will set the field to null.
            """
            physical_bundle: NotRequired["str|None"]
            """
            The physical bundle object belonging to this personalization design.
            """
            preferences: NotRequired[
                "PersonalizationDesign.ModifyParamsPreferences|None"
            ]
            """
            Information on whether this personalization design is used to create cards when one is not specified.
            """
            transfer_lookup_key: NotRequired["bool|None"]
            """
            If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.
            """

        class ModifyParamsPreferences(TypedDict):
            is_default: bool
            """
            Whether this personalization design is used to create cards when one is not specified. A connected account will use the Connect platform's default if no personalization design is set as default.
            """

        class ModifyParamsCarrierText(TypedDict):
            footer_body: NotRequired["Literal['']|str|None"]
            """
            The footer body text of the carrier letter.
            """
            footer_title: NotRequired["Literal['']|str|None"]
            """
            The footer title text of the carrier letter.
            """
            header_body: NotRequired["Literal['']|str|None"]
            """
            The header body text of the carrier letter.
            """
            header_title: NotRequired["Literal['']|str|None"]
            """
            The header title text of the carrier letter.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ActivateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class DeactivateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RejectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            rejection_reasons: "PersonalizationDesign.RejectParamsRejectionReasons"
            """
            The reason(s) the personalization design was rejected.
            """

        class RejectParamsRejectionReasons(TypedDict):
            card_logo: NotRequired[
                "List[Literal['geographic_location', 'inappropriate', 'network_name', 'non_binary_image', 'non_fiat_currency', 'other', 'other_entity', 'promotional_material']]|None"
            ]
            """
            The reason(s) the card logo was rejected.
            """
            carrier_text: NotRequired[
                "List[Literal['geographic_location', 'inappropriate', 'network_name', 'non_fiat_currency', 'other', 'other_entity', 'promotional_material']]|None"
            ]
            """
            The reason(s) the carrier text was rejected.
            """

    card_logo: Optional[ExpandableField["File"]]
    """
    The file for the card logo, for use with physical bundles that support card logos.
    """
    carrier_text: Optional[CarrierText]
    """
    Hash containing carrier text, for use with physical bundles that support carrier text.
    """
    id: str
    """
    Unique identifier for the object.
    """
    lookup_key: Optional[str]
    """
    A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    Friendly display name.
    """
    object: Literal["issuing.personalization_design"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    physical_bundle: ExpandableField["PhysicalBundle"]
    """
    The physical bundle object belonging to this personalization design.
    """
    preferences: Preferences
    rejection_reasons: RejectionReasons
    status: Literal["active", "inactive", "rejected", "review"]
    """
    Whether this personalization design can be used to create cards.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PersonalizationDesign.CreateParams"]
    ) -> "PersonalizationDesign":
        return cast(
            "PersonalizationDesign",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PersonalizationDesign.ListParams"]
    ) -> ListObject["PersonalizationDesign"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
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
        cls, id: str, **params: Unpack["PersonalizationDesign.ModifyParams"]
    ) -> "PersonalizationDesign":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PersonalizationDesign",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PersonalizationDesign.RetrieveParams"]
    ) -> "PersonalizationDesign":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["PersonalizationDesign"]):
        _resource_cls: Type["PersonalizationDesign"]

        @classmethod
        def _cls_activate(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.ActivateParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate".format(
                        personalization_design=util.sanitize_id(
                            personalization_design
                        )
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @classmethod
        def activate(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.ActivateParams"]
        ) -> "PersonalizationDesign":
            ...

        @overload
        def activate(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.ActivateParams"]
        ) -> "PersonalizationDesign":
            ...

        @class_method_variant("_cls_activate")
        def activate(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.ActivateParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate".format(
                        personalization_design=util.sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_deactivate(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate".format(
                        personalization_design=util.sanitize_id(
                            personalization_design
                        )
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @classmethod
        def deactivate(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ) -> "PersonalizationDesign":
            ...

        @overload
        def deactivate(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ) -> "PersonalizationDesign":
            ...

        @class_method_variant("_cls_deactivate")
        def deactivate(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate".format(
                        personalization_design=util.sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_reject(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject".format(
                        personalization_design=util.sanitize_id(
                            personalization_design
                        )
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @classmethod
        def reject(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ) -> "PersonalizationDesign":
            ...

        @overload
        def reject(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ) -> "PersonalizationDesign":
            ...

        @class_method_variant("_cls_reject")
        def reject(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ) -> "PersonalizationDesign":
            return cast(
                "PersonalizationDesign",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject".format(
                        personalization_design=util.sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "carrier_text": CarrierText,
        "preferences": Preferences,
        "rejection_reasons": RejectionReasons,
    }


PersonalizationDesign.TestHelpers._resource_cls = PersonalizationDesign
