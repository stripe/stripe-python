# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class Cardholder(
    CreateableAPIResource["Cardholder"],
    ListableAPIResource["Cardholder"],
    UpdateableAPIResource["Cardholder"],
):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

    Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards#create-cardholder)
    """

    OBJECT_NAME = "issuing.cardholder"
    billing: StripeObject
    company: Optional[StripeObject]
    created: int
    email: Optional[str]
    id: str
    individual: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["issuing.cardholder"]
    phone_number: Optional[str]
    preferred_locales: Optional[List[Literal["de", "en", "es", "fr", "it"]]]
    requirements: StripeObject
    spending_controls: Optional[StripeObject]
    status: Literal["active", "blocked", "inactive"]
    type: Literal["company", "individual"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Cardholder":
        return cast(
            "Cardholder",
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
    ) -> ListObject["Cardholder"]:
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
    def modify(cls, id, **params: Any) -> "Cardholder":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Cardholder",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Cardholder":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
