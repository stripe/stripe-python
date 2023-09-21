# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.file import File
    from stripe.api_resources.issuing.card_bundle import CardBundle


class CardDesign(
    CreateableAPIResource["CardDesign"],
    ListableAPIResource["CardDesign"],
    UpdateableAPIResource["CardDesign"],
):
    """
    A Card Design is a logical grouping of a Card Bundle, card logo, and carrier text that represents a product line.
    """

    OBJECT_NAME = "issuing.card_design"
    card_bundle: ExpandableField["CardBundle"]
    card_logo: Optional[ExpandableField["File"]]
    carrier_text: Optional[StripeObject]
    id: str
    lookup_key: Optional[str]
    metadata: Dict[str, str]
    name: Optional[str]
    object: Literal["issuing.card_design"]
    preferences: StripeObject
    rejection_reasons: StripeObject
    status: Literal["active", "inactive", "rejected", "review"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "CardDesign":
        return cast(
            "CardDesign",
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
    ) -> ListObject["CardDesign"]:
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
    def modify(cls, id, **params: Any) -> "CardDesign":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "CardDesign",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "CardDesign":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["CardDesign"]):
        _resource_cls: Type["CardDesign"]

        @classmethod
        def _cls_activate_testmode(
            cls,
            card_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/activate".format(
                    card_design=util.sanitize_id(card_design)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_activate_testmode")
        def activate_testmode(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/activate".format(
                    card_design=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_deactivate_testmode(
            cls,
            card_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/deactivate".format(
                    card_design=util.sanitize_id(card_design)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_deactivate_testmode")
        def deactivate_testmode(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/deactivate".format(
                    card_design=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_reject_testmode(
            cls,
            card_design: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/reject".format(
                    card_design=util.sanitize_id(card_design)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_reject_testmode")
        def reject_testmode(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/reject".format(
                    card_design=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


CardDesign.TestHelpers._resource_cls = CardDesign
