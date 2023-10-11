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
from typing import Any, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class PaymentMethodDomain(
    CreateableAPIResource["PaymentMethodDomain"],
    ListableAPIResource["PaymentMethodDomain"],
    UpdateableAPIResource["PaymentMethodDomain"],
):
    """
    A payment method domain represents a web domain that you have registered with Stripe.
    Stripe Elements use registered payment method domains to control where certain payment methods are shown.

    Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
    """

    OBJECT_NAME = "payment_method_domain"
    apple_pay: StripeObject
    created: int
    domain_name: str
    enabled: bool
    google_pay: StripeObject
    id: str
    link: StripeObject
    livemode: bool
    object: Literal["payment_method_domain"]
    paypal: StripeObject

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "PaymentMethodDomain":
        return cast(
            "PaymentMethodDomain",
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
    ) -> ListObject["PaymentMethodDomain"]:
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
    def modify(cls, id, **params: Any) -> "PaymentMethodDomain":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodDomain",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentMethodDomain":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_validate(
        cls,
        payment_method_domain: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                payment_method_domain=util.sanitize_id(payment_method_domain)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_validate")
    def validate(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                payment_method_domain=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
