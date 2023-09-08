# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal


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
    created: str
    email: Optional[str]
    id: str
    individual: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["issuing.cardholder"]
    phone_number: Optional[str]
    preferred_locales: Optional[List[str]]
    requirements: StripeObject
    spending_controls: Optional[StripeObject]
    status: str
    type: str

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
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
    def _cls_modify(
        cls,
        cardholder,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/cardholders/{cardholder}".format(
                cardholder=util.sanitize_id(cardholder)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_modify")
    def modify(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/cardholders/{cardholder}".format(
                cardholder=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "Cardholder":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
