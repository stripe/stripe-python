# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class PhysicalBundle(ListableAPIResource["PhysicalBundle"]):
    """
    A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.
    """

    OBJECT_NAME = "issuing.physical_bundle"

    class Features(StripeObject):
        card_logo: Literal["optional", "required", "unsupported"]
        carrier_text: Literal["optional", "required", "unsupported"]

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired["Literal['active', 'inactive', 'review']|None"]
            type: NotRequired["Literal['custom', 'standard']|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    features: Optional[Features]
    id: str
    livemode: bool
    name: str
    object: Literal["issuing.physical_bundle"]
    status: Literal["active", "inactive", "review"]
    type: Literal["custom", "standard"]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PhysicalBundle.ListParams"]
    ) -> ListObject["PhysicalBundle"]:
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
    def retrieve(
        cls, id: str, **params: Unpack["PhysicalBundle.RetrieveParams"]
    ) -> "PhysicalBundle":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"features": Features}
