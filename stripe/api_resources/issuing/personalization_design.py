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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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
        **params: Any
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "PersonalizationDesign":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PersonalizationDesign",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PersonalizationDesign":
        instance = cls(id, api_key, **params)
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
            **params: Any
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
            self, idempotency_key: Optional[str] = None, **params: Any
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
            **params: Any
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
            self, idempotency_key: Optional[str] = None, **params: Any
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
            **params: Any
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
        def reject(self, idempotency_key: Optional[str] = None, **params: Any):
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
