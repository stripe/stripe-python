# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal


class PhysicalBundle(ListableAPIResource["PhysicalBundle"]):
    """
    A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.
    """

    OBJECT_NAME = "issuing.physical_bundle"
    features: Optional[StripeObject]
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
        **params: Any
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PhysicalBundle":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
