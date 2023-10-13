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
from typing import Dict, List, Optional, cast
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

    OBJECT_NAME = "issuing.personalization_design"

    class CarrierText(StripeObject):
        footer_body: Optional[str]
        footer_title: Optional[str]
        header_body: Optional[str]
        header_title: Optional[str]

    class Preferences(StripeObject):
        account_default: bool
        platform_default: Optional[bool]

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

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            card_logo: NotRequired["str|None"]
            carrier_text: NotRequired[
                "PersonalizationDesign.CreateParamsCarrierText|None"
            ]
            expand: NotRequired["List[str]|None"]
            lookup_key: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: NotRequired["str|None"]
            physical_bundle: str
            preferences: NotRequired[
                "PersonalizationDesign.CreateParamsPreferences|None"
            ]
            transfer_lookup_key: NotRequired["bool|None"]

        class CreateParamsPreferences(TypedDict):
            account_default: bool

        class CreateParamsCarrierText(TypedDict):
            footer_body: NotRequired["Literal['']|str|None"]
            footer_title: NotRequired["Literal['']|str|None"]
            header_body: NotRequired["Literal['']|str|None"]
            header_title: NotRequired["Literal['']|str|None"]

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            lookup_keys: NotRequired["List[str]|None"]
            preferences: NotRequired[
                "PersonalizationDesign.ListParamsPreferences|None"
            ]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['active', 'inactive', 'rejected', 'review']|None"
            ]

        class ListParamsPreferences(TypedDict):
            account_default: NotRequired["bool|None"]
            platform_default: NotRequired["bool|None"]

        class ModifyParams(RequestOptions):
            card_logo: NotRequired["Literal['']|str|None"]
            carrier_text: NotRequired[
                "Literal['']|PersonalizationDesign.ModifyParamsCarrierText|None"
            ]
            expand: NotRequired["List[str]|None"]
            lookup_key: NotRequired["Literal['']|str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: NotRequired["Literal['']|str|None"]
            physical_bundle: NotRequired["str|None"]
            preferences: NotRequired[
                "PersonalizationDesign.ModifyParamsPreferences|None"
            ]
            transfer_lookup_key: NotRequired["bool|None"]

        class ModifyParamsPreferences(TypedDict):
            account_default: bool

        class ModifyParamsCarrierText(TypedDict):
            footer_body: NotRequired["Literal['']|str|None"]
            footer_title: NotRequired["Literal['']|str|None"]
            header_body: NotRequired["Literal['']|str|None"]
            header_title: NotRequired["Literal['']|str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ActivateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class DeactivateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RejectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            rejection_reasons: "PersonalizationDesign.RejectParamsRejectionReasons"

        class RejectParamsRejectionReasons(TypedDict):
            card_logo: NotRequired[
                "List[Literal['geographic_location', 'inappropriate', 'network_name', 'non_binary_image', 'non_fiat_currency', 'other', 'other_entity', 'promotional_material']]|None"
            ]
            carrier_text: NotRequired[
                "List[Literal['geographic_location', 'inappropriate', 'network_name', 'non_fiat_currency', 'other', 'other_entity', 'promotional_material']]|None"
            ]

    card_logo: Optional[ExpandableField["File"]]
    carrier_text: Optional[CarrierText]
    id: str
    lookup_key: Optional[str]
    metadata: Dict[str, str]
    name: Optional[str]
    object: Literal["issuing.personalization_design"]
    physical_bundle: ExpandableField["PhysicalBundle"]
    preferences: Preferences
    rejection_reasons: RejectionReasons
    status: Literal["active", "inactive", "rejected", "review"]

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
        cls, id, **params: Unpack["PersonalizationDesign.ModifyParams"]
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
        ):
            return cls._static_request(
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
            )

        @util.class_method_variant("_cls_activate")
        def activate(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.ActivateParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate".format(
                    personalization_design=util.sanitize_id(
                        self.resource.get("id")
                    )
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_deactivate(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ):
            return cls._static_request(
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
            )

        @util.class_method_variant("_cls_deactivate")
        def deactivate(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.DeactivateParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate".format(
                    personalization_design=util.sanitize_id(
                        self.resource.get("id")
                    )
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_reject(
            cls,
            personalization_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ):
            return cls._static_request(
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
            )

        @util.class_method_variant("_cls_reject")
        def reject(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["PersonalizationDesign.RejectParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject".format(
                    personalization_design=util.sanitize_id(
                        self.resource.get("id")
                    )
                ),
                idempotency_key=idempotency_key,
                params=params,
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
