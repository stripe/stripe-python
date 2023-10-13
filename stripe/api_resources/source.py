# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            flow: NotRequired[
                "Literal['code_verification', 'none', 'receiver', 'redirect']|None"
            ]
            mandate: NotRequired["Source.CreateParamsMandate|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            original_source: NotRequired["str|None"]
            owner: NotRequired["Source.CreateParamsOwner|None"]
            receiver: NotRequired["Source.CreateParamsReceiver|None"]
            redirect: NotRequired["Source.CreateParamsRedirect|None"]
            source_order: NotRequired["Source.CreateParamsSourceOrder|None"]
            statement_descriptor: NotRequired["str|None"]
            token: NotRequired["str|None"]
            type: NotRequired["str|None"]
            usage: NotRequired["Literal['reusable', 'single_use']|None"]

        class CreateParamsSourceOrder(TypedDict):
            items: NotRequired["List[Source.CreateParamsSourceOrderItem]|None"]
            shipping: NotRequired[
                "Source.CreateParamsSourceOrderShipping|None"
            ]

        class CreateParamsSourceOrderShipping(TypedDict):
            address: "Source.CreateParamsSourceOrderShippingAddress"
            carrier: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class CreateParamsSourceOrderShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: str
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsSourceOrderItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            parent: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            type: NotRequired[
                "Literal['discount', 'shipping', 'sku', 'tax']|None"
            ]

        class CreateParamsRedirect(TypedDict):
            return_url: str

        class CreateParamsReceiver(TypedDict):
            refund_attributes_method: NotRequired[
                "Literal['email', 'manual', 'none']|None"
            ]

        class CreateParamsOwner(TypedDict):
            address: NotRequired["Source.CreateParamsOwnerAddress|None"]
            email: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]

        class CreateParamsOwnerAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsMandate(TypedDict):
            acceptance: NotRequired[
                "Source.CreateParamsMandateAcceptance|None"
            ]
            amount: NotRequired["Literal['']|int|None"]
            currency: NotRequired["str|None"]
            interval: NotRequired[
                "Literal['one_time', 'scheduled', 'variable']|None"
            ]
            notification_method: NotRequired[
                "Literal['deprecated_none', 'email', 'manual', 'none', 'stripe_email']|None"
            ]

        class CreateParamsMandateAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            offline: NotRequired[
                "Source.CreateParamsMandateAcceptanceOffline|None"
            ]
            online: NotRequired[
                "Source.CreateParamsMandateAcceptanceOnline|None"
            ]
            status: Literal["accepted", "pending", "refused", "revoked"]
            type: NotRequired["Literal['offline', 'online']|None"]
            user_agent: NotRequired["str|None"]

        class CreateParamsMandateAcceptanceOnline(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class CreateParamsMandateAcceptanceOffline(TypedDict):
            contact_email: str

        class ListSourceTransactionsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            mandate: NotRequired["Source.ModifyParamsMandate|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            owner: NotRequired["Source.ModifyParamsOwner|None"]
            source_order: NotRequired["Source.ModifyParamsSourceOrder|None"]

        class ModifyParamsSourceOrder(TypedDict):
            items: NotRequired["List[Source.ModifyParamsSourceOrderItem]|None"]
            shipping: NotRequired[
                "Source.ModifyParamsSourceOrderShipping|None"
            ]

        class ModifyParamsSourceOrderShipping(TypedDict):
            address: "Source.ModifyParamsSourceOrderShippingAddress"
            carrier: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class ModifyParamsSourceOrderShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: str
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsSourceOrderItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            parent: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            type: NotRequired[
                "Literal['discount', 'shipping', 'sku', 'tax']|None"
            ]

        class ModifyParamsOwner(TypedDict):
            address: NotRequired["Source.ModifyParamsOwnerAddress|None"]
            email: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]

        class ModifyParamsOwnerAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsMandate(TypedDict):
            acceptance: NotRequired[
                "Source.ModifyParamsMandateAcceptance|None"
            ]
            amount: NotRequired["Literal['']|int|None"]
            currency: NotRequired["str|None"]
            interval: NotRequired[
                "Literal['one_time', 'scheduled', 'variable']|None"
            ]
            notification_method: NotRequired[
                "Literal['deprecated_none', 'email', 'manual', 'none', 'stripe_email']|None"
            ]

        class ModifyParamsMandateAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            offline: NotRequired[
                "Source.ModifyParamsMandateAcceptanceOffline|None"
            ]
            online: NotRequired[
                "Source.ModifyParamsMandateAcceptanceOnline|None"
            ]
            status: Literal["accepted", "pending", "refused", "revoked"]
            type: NotRequired["Literal['offline', 'online']|None"]
            user_agent: NotRequired["str|None"]

        class ModifyParamsMandateAcceptanceOnline(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class ModifyParamsMandateAcceptanceOffline(TypedDict):
            contact_email: str

        class RetrieveParams(RequestOptions):
            client_secret: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

        class VerifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
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
