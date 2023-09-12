# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error, util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)
from stripe.stripe_object import StripeObject
from typing import Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class Source(CreateableAPIResource["Source"], UpdateableAPIResource["Source"]):
    """
    `Source` objects allow you to accept a variety of payment methods. They
    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
    This newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).
    """

    OBJECT_NAME = "source"
    ach_credit_transfer: StripeObject
    ach_debit: StripeObject
    acss_debit: StripeObject
    alipay: StripeObject
    amount: Optional[int]
    au_becs_debit: StripeObject
    bancontact: StripeObject
    card: StripeObject
    card_present: StripeObject
    client_secret: str
    code_verification: StripeObject
    created: int
    currency: Optional[str]
    customer: str
    eps: StripeObject
    flow: str
    giropay: StripeObject
    id: str
    ideal: StripeObject
    klarna: StripeObject
    livemode: bool
    metadata: Optional[Dict[str, str]]
    multibanco: StripeObject
    object: Literal["source"]
    owner: Optional[StripeObject]
    p24: StripeObject
    receiver: StripeObject
    redirect: StripeObject
    sepa_credit_transfer: StripeObject
    sepa_debit: StripeObject
    sofort: StripeObject
    source_order: StripeObject
    statement_descriptor: Optional[str]
    status: str
    three_d_secure: StripeObject
    type: Literal[
        "ach_credit_transfer",
        "ach_debit",
        "acss_debit",
        "alipay",
        "au_becs_debit",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_credit_transfer",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ]
    usage: Optional[str]
    wechat: StripeObject

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> "Source":
        return cast(
            "Source",
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
    def _cls_list_source_transactions(
        cls,
        source,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/sources/{source}/source_transactions".format(
                source=util.sanitize_id(source)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_source_transactions")
    def list_source_transactions(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/sources/{source}/source_transactions".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params) -> "Source":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Source",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "Source":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify(
        cls,
        source,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(source)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify")
    def verify(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def detach(self, idempotency_key=None, **params):
        token = self.id

        if hasattr(self, "customer") and self.customer:
            extn = quote_plus(token)
            customer = self.customer
            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request("delete", url, params, headers))
            return self

        else:
            raise error.InvalidRequestError(
                "Source %s does not appear to be currently attached "
                "to a customer object." % token,
                "id",
            )
