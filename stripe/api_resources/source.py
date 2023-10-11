# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error, util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        customer: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        flow: NotRequired[
            Optional[
                Literal["code_verification", "none", "receiver", "redirect"]
            ]
        ]
        mandate: NotRequired[Optional["Source.CreateMandateParams"]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        original_source: NotRequired[Optional[str]]
        owner: NotRequired[Optional["Source.CreateOwnerParams"]]
        receiver: NotRequired[Optional["Source.CreateReceiverParams"]]
        redirect: NotRequired[Optional["Source.CreateRedirectParams"]]
        source_order: NotRequired[Optional["Source.CreateSourceOrderParams"]]
        statement_descriptor: NotRequired[Optional[str]]
        token: NotRequired[Optional[str]]
        type: NotRequired[Optional[str]]
        usage: NotRequired[Optional[Literal["reusable", "single_use"]]]

    class CreateSourceOrderParams(TypedDict):
        items: NotRequired[
            Optional[List["Source.CreateSourceOrderItemParams"]]
        ]
        shipping: NotRequired[
            Optional["Source.CreateSourceOrderShippingParams"]
        ]

    class CreateSourceOrderShippingParams(TypedDict):
        address: "Source.CreateSourceOrderShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class CreateSourceOrderShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: str
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateSourceOrderItemParams(TypedDict):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        parent: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        type: NotRequired[
            Optional[Literal["discount", "shipping", "sku", "tax"]]
        ]

    class CreateRedirectParams(TypedDict):
        return_url: str

    class CreateReceiverParams(TypedDict):
        refund_attributes_method: NotRequired[
            Optional[Literal["email", "manual", "none"]]
        ]

    class CreateOwnerParams(TypedDict):
        address: NotRequired[Optional["Source.CreateOwnerAddressParams"]]
        email: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]

    class CreateOwnerAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateMandateParams(TypedDict):
        acceptance: NotRequired[
            Optional["Source.CreateMandateAcceptanceParams"]
        ]
        amount: NotRequired[Optional[Union[Literal[""], int]]]
        currency: NotRequired[Optional[str]]
        interval: NotRequired[
            Optional[Literal["one_time", "scheduled", "variable"]]
        ]
        notification_method: NotRequired[
            Optional[
                Literal[
                    "deprecated_none",
                    "email",
                    "manual",
                    "none",
                    "stripe_email",
                ]
            ]
        ]

    class CreateMandateAcceptanceParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        offline: NotRequired[
            Optional["Source.CreateMandateAcceptanceOfflineParams"]
        ]
        online: NotRequired[
            Optional["Source.CreateMandateAcceptanceOnlineParams"]
        ]
        status: Literal["accepted", "pending", "refused", "revoked"]
        type: NotRequired[Optional[Literal["offline", "online"]]]
        user_agent: NotRequired[Optional[str]]

    class CreateMandateAcceptanceOnlineParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateMandateAcceptanceOfflineParams(TypedDict):
        contact_email: str

    class ListSourceTransactionsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        mandate: NotRequired[Optional["Source.ModifyMandateParams"]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        owner: NotRequired[Optional["Source.ModifyOwnerParams"]]
        source_order: NotRequired[Optional["Source.ModifySourceOrderParams"]]

    class ModifySourceOrderParams(TypedDict):
        items: NotRequired[
            Optional[List["Source.ModifySourceOrderItemParams"]]
        ]
        shipping: NotRequired[
            Optional["Source.ModifySourceOrderShippingParams"]
        ]

    class ModifySourceOrderShippingParams(TypedDict):
        address: "Source.ModifySourceOrderShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class ModifySourceOrderShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: str
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifySourceOrderItemParams(TypedDict):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        parent: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        type: NotRequired[
            Optional[Literal["discount", "shipping", "sku", "tax"]]
        ]

    class ModifyOwnerParams(TypedDict):
        address: NotRequired[Optional["Source.ModifyOwnerAddressParams"]]
        email: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]

    class ModifyOwnerAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyMandateParams(TypedDict):
        acceptance: NotRequired[
            Optional["Source.ModifyMandateAcceptanceParams"]
        ]
        amount: NotRequired[Optional[Union[Literal[""], int]]]
        currency: NotRequired[Optional[str]]
        interval: NotRequired[
            Optional[Literal["one_time", "scheduled", "variable"]]
        ]
        notification_method: NotRequired[
            Optional[
                Literal[
                    "deprecated_none",
                    "email",
                    "manual",
                    "none",
                    "stripe_email",
                ]
            ]
        ]

    class ModifyMandateAcceptanceParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        offline: NotRequired[
            Optional["Source.ModifyMandateAcceptanceOfflineParams"]
        ]
        online: NotRequired[
            Optional["Source.ModifyMandateAcceptanceOnlineParams"]
        ]
        status: Literal["accepted", "pending", "refused", "revoked"]
        type: NotRequired[Optional[Literal["offline", "online"]]]
        user_agent: NotRequired[Optional[str]]

    class ModifyMandateAcceptanceOnlineParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class ModifyMandateAcceptanceOfflineParams(TypedDict):
        contact_email: str

    class RetrieveParams(RequestOptions):
        client_secret: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    class VerifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        values: List[str]

    ach_credit_transfer: Optional[StripeObject]
    ach_debit: Optional[StripeObject]
    acss_debit: Optional[StripeObject]
    alipay: Optional[StripeObject]
    amount: Optional[int]
    au_becs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    card: Optional[StripeObject]
    card_present: Optional[StripeObject]
    client_secret: str
    code_verification: Optional[StripeObject]
    created: int
    currency: Optional[str]
    customer: Optional[str]
    eps: Optional[StripeObject]
    flow: str
    giropay: Optional[StripeObject]
    id: str
    ideal: Optional[StripeObject]
    klarna: Optional[StripeObject]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    multibanco: Optional[StripeObject]
    object: Literal["source"]
    owner: Optional[StripeObject]
    p24: Optional[StripeObject]
    receiver: Optional[StripeObject]
    redirect: Optional[StripeObject]
    sepa_credit_transfer: Optional[StripeObject]
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
    source_order: Optional[StripeObject]
    statement_descriptor: Optional[str]
    status: str
    three_d_secure: Optional[StripeObject]
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
    wechat: Optional[StripeObject]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Source.CreateParams"]
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
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Source.ListSourceTransactionsParams"]
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
    def list_source_transactions(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.ListSourceTransactionsParams"]
    ):
        return self._request(
            "get",
            "/v1/sources/{source}/source_transactions".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Unpack["Source.ModifyParams"]) -> "Source":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Source",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Source.RetrieveParams"]
    ) -> "Source":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify(
        cls,
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Source.VerifyParams"]
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
    def verify(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.VerifyParams"]
    ):
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
