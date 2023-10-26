# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.source_transaction import SourceTransaction


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

    OBJECT_NAME: ClassVar[Literal["source"]] = "source"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. Not supported for `receiver` type sources, where charge amount may not be specified until funds land.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready.
            """
            customer: NotRequired["str|None"]
            """
            The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`).
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            flow: NotRequired[
                "Literal['code_verification', 'none', 'receiver', 'redirect']|None"
            ]
            """
            The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows.
            """
            mandate: NotRequired["Source.CreateParamsMandate|None"]
            """
            Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            original_source: NotRequired["str|None"]
            """
            The source to share.
            """
            owner: NotRequired["Source.CreateParamsOwner|None"]
            """
            Information about the owner of the payment instrument that may be used or required by particular source types.
            """
            receiver: NotRequired["Source.CreateParamsReceiver|None"]
            """
            Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`).
            """
            redirect: NotRequired["Source.CreateParamsRedirect|None"]
            """
            Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`).
            """
            source_order: NotRequired["Source.CreateParamsSourceOrder|None"]
            """
            Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all.
            """
            token: NotRequired["str|None"]
            """
            An optional token used to create the source. When passed, token properties will override source parameters.
            """
            type: NotRequired["str|None"]
            """
            The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Cloning card Sources](https://stripe.com/docs/sources/connect#cloning-card-sources) guide)
            """
            usage: NotRequired["Literal['reusable', 'single_use']|None"]

        class CreateParamsSourceOrder(TypedDict):
            items: NotRequired["List[Source.CreateParamsSourceOrderItem]|None"]
            """
            List of items constituting the order.
            """
            shipping: NotRequired[
                "Source.CreateParamsSourceOrderShipping|None"
            ]
            """
            Shipping address for the order. Required if any of the SKUs are for products that have `shippable` set to true.
            """

        class CreateParamsSourceOrderShipping(TypedDict):
            address: "Source.CreateParamsSourceOrderShippingAddress"
            """
            Shipping address.
            """
            carrier: NotRequired["str|None"]
            """
            The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
            """
            name: NotRequired["str|None"]
            """
            Recipient name.
            """
            phone: NotRequired["str|None"]
            """
            Recipient phone (including extension).
            """
            tracking_number: NotRequired["str|None"]
            """
            The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
            """

        class CreateParamsSourceOrderShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: str
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsSourceOrderItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            parent: NotRequired["str|None"]
            """
            The ID of the SKU being ordered.
            """
            quantity: NotRequired["int|None"]
            """
            The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.
            """
            type: NotRequired[
                "Literal['discount', 'shipping', 'sku', 'tax']|None"
            ]

        class CreateParamsRedirect(TypedDict):
            return_url: str
            """
            The URL you provide to redirect the customer back to you after they authenticated their payment. It can use your application URI scheme in the context of a mobile application.
            """

        class CreateParamsReceiver(TypedDict):
            refund_attributes_method: NotRequired[
                "Literal['email', 'manual', 'none']|None"
            ]
            """
            The method Stripe should use to request information needed to process a refund or mispayment. Either `email` (an email is sent directly to the customer) or `manual` (a `source.refund_attributes_required` event is sent to your webhooks endpoint). Refer to each payment method's documentation to learn which refund attributes may be required.
            """

        class CreateParamsOwner(TypedDict):
            address: NotRequired["Source.CreateParamsOwnerAddress|None"]
            """
            Owner's address.
            """
            email: NotRequired["str|None"]
            """
            Owner's email address.
            """
            name: NotRequired["str|None"]
            """
            Owner's full name.
            """
            phone: NotRequired["str|None"]
            """
            Owner's phone number.
            """

        class CreateParamsOwnerAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsMandate(TypedDict):
            acceptance: NotRequired[
                "Source.CreateParamsMandateAcceptance|None"
            ]
            """
            The parameters required to notify Stripe of a mandate acceptance or refusal by the customer.
            """
            amount: NotRequired["Literal['']|int|None"]
            """
            The amount specified by the mandate. (Leave null for a mandate covering all amounts)
            """
            currency: NotRequired["str|None"]
            """
            The currency specified by the mandate. (Must match `currency` of the source)
            """
            interval: NotRequired[
                "Literal['one_time', 'scheduled', 'variable']|None"
            ]
            """
            The interval of debits permitted by the mandate. Either `one_time` (just permitting a single debit), `scheduled` (with debits on an agreed schedule or for clearly-defined events), or `variable`(for debits with any frequency)
            """
            notification_method: NotRequired[
                "Literal['deprecated_none', 'email', 'manual', 'none', 'stripe_email']|None"
            ]
            """
            The method Stripe should use to notify the customer of upcoming debit instructions and/or mandate confirmation as required by the underlying debit network. Either `email` (an email is sent directly to the customer), `manual` (a `source.mandate_notification` event is sent to your webhooks endpoint and you should handle the notification) or `none` (the underlying debit network does not require any notification).
            """

        class CreateParamsMandateAcceptance(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the mandate was accepted or refused by the customer.
            """
            offline: NotRequired[
                "Source.CreateParamsMandateAcceptanceOffline|None"
            ]
            """
            The parameters required to store a mandate accepted offline. Should only be set if `mandate[type]` is `offline`
            """
            online: NotRequired[
                "Source.CreateParamsMandateAcceptanceOnline|None"
            ]
            """
            The parameters required to store a mandate accepted online. Should only be set if `mandate[type]` is `online`
            """
            status: Literal["accepted", "pending", "refused", "revoked"]
            """
            The status of the mandate acceptance. Either `accepted` (the mandate was accepted) or `refused` (the mandate was refused).
            """
            type: NotRequired["Literal['offline', 'online']|None"]
            """
            The type of acceptance information included with the mandate. Either `online` or `offline`
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the mandate was accepted or refused by the customer.
            """

        class CreateParamsMandateAcceptanceOnline(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the mandate was accepted or refused by the customer.
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the mandate was accepted or refused by the customer.
            """

        class CreateParamsMandateAcceptanceOffline(TypedDict):
            contact_email: str
            """
            An email to contact you with if a copy of the mandate is requested, required if `type` is `offline`.
            """

        class ListSourceTransactionsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            Amount associated with the source.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            mandate: NotRequired["Source.ModifyParamsMandate|None"]
            """
            Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            owner: NotRequired["Source.ModifyParamsOwner|None"]
            """
            Information about the owner of the payment instrument that may be used or required by particular source types.
            """
            source_order: NotRequired["Source.ModifyParamsSourceOrder|None"]
            """
            Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
            """

        class ModifyParamsSourceOrder(TypedDict):
            items: NotRequired["List[Source.ModifyParamsSourceOrderItem]|None"]
            """
            List of items constituting the order.
            """
            shipping: NotRequired[
                "Source.ModifyParamsSourceOrderShipping|None"
            ]
            """
            Shipping address for the order. Required if any of the SKUs are for products that have `shippable` set to true.
            """

        class ModifyParamsSourceOrderShipping(TypedDict):
            address: "Source.ModifyParamsSourceOrderShippingAddress"
            """
            Shipping address.
            """
            carrier: NotRequired["str|None"]
            """
            The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
            """
            name: NotRequired["str|None"]
            """
            Recipient name.
            """
            phone: NotRequired["str|None"]
            """
            Recipient phone (including extension).
            """
            tracking_number: NotRequired["str|None"]
            """
            The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
            """

        class ModifyParamsSourceOrderShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: str
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyParamsSourceOrderItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            parent: NotRequired["str|None"]
            """
            The ID of the SKU being ordered.
            """
            quantity: NotRequired["int|None"]
            """
            The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.
            """
            type: NotRequired[
                "Literal['discount', 'shipping', 'sku', 'tax']|None"
            ]

        class ModifyParamsOwner(TypedDict):
            address: NotRequired["Source.ModifyParamsOwnerAddress|None"]
            """
            Owner's address.
            """
            email: NotRequired["str|None"]
            """
            Owner's email address.
            """
            name: NotRequired["str|None"]
            """
            Owner's full name.
            """
            phone: NotRequired["str|None"]
            """
            Owner's phone number.
            """

        class ModifyParamsOwnerAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyParamsMandate(TypedDict):
            acceptance: NotRequired[
                "Source.ModifyParamsMandateAcceptance|None"
            ]
            """
            The parameters required to notify Stripe of a mandate acceptance or refusal by the customer.
            """
            amount: NotRequired["Literal['']|int|None"]
            """
            The amount specified by the mandate. (Leave null for a mandate covering all amounts)
            """
            currency: NotRequired["str|None"]
            """
            The currency specified by the mandate. (Must match `currency` of the source)
            """
            interval: NotRequired[
                "Literal['one_time', 'scheduled', 'variable']|None"
            ]
            """
            The interval of debits permitted by the mandate. Either `one_time` (just permitting a single debit), `scheduled` (with debits on an agreed schedule or for clearly-defined events), or `variable`(for debits with any frequency)
            """
            notification_method: NotRequired[
                "Literal['deprecated_none', 'email', 'manual', 'none', 'stripe_email']|None"
            ]
            """
            The method Stripe should use to notify the customer of upcoming debit instructions and/or mandate confirmation as required by the underlying debit network. Either `email` (an email is sent directly to the customer), `manual` (a `source.mandate_notification` event is sent to your webhooks endpoint and you should handle the notification) or `none` (the underlying debit network does not require any notification).
            """

        class ModifyParamsMandateAcceptance(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the mandate was accepted or refused by the customer.
            """
            offline: NotRequired[
                "Source.ModifyParamsMandateAcceptanceOffline|None"
            ]
            """
            The parameters required to store a mandate accepted offline. Should only be set if `mandate[type]` is `offline`
            """
            online: NotRequired[
                "Source.ModifyParamsMandateAcceptanceOnline|None"
            ]
            """
            The parameters required to store a mandate accepted online. Should only be set if `mandate[type]` is `online`
            """
            status: Literal["accepted", "pending", "refused", "revoked"]
            """
            The status of the mandate acceptance. Either `accepted` (the mandate was accepted) or `refused` (the mandate was refused).
            """
            type: NotRequired["Literal['offline', 'online']|None"]
            """
            The type of acceptance information included with the mandate. Either `online` or `offline`
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the mandate was accepted or refused by the customer.
            """

        class ModifyParamsMandateAcceptanceOnline(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the mandate was accepted or refused by the customer.
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the mandate was accepted or refused by the customer.
            """

        class ModifyParamsMandateAcceptanceOffline(TypedDict):
            contact_email: str
            """
            An email to contact you with if a copy of the mandate is requested, required if `type` is `offline`.
            """

        class RetrieveParams(RequestOptions):
            client_secret: NotRequired["str|None"]
            """
            The client secret of the source. Required if a publishable key is used to retrieve the source.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class VerifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            values: List[str]
            """
            The values needed to verify the source.
            """

    ach_credit_transfer: Optional[StripeObject]
    ach_debit: Optional[StripeObject]
    acss_debit: Optional[StripeObject]
    alipay: Optional[StripeObject]
    amount: Optional[int]
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.
    """
    au_becs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    card: Optional[StripeObject]
    card_present: Optional[StripeObject]
    client_secret: str
    """
    The client secret of the source. Used for client-side retrieval using a publishable key.
    """
    code_verification: Optional[StripeObject]
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources.
    """
    customer: Optional[str]
    """
    The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.
    """
    eps: Optional[StripeObject]
    flow: str
    """
    The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.
    """
    giropay: Optional[StripeObject]
    id: str
    """
    Unique identifier for the object.
    """
    ideal: Optional[StripeObject]
    klarna: Optional[StripeObject]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    multibanco: Optional[StripeObject]
    object: Literal["source"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    owner: Optional[StripeObject]
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """
    p24: Optional[StripeObject]
    receiver: Optional[StripeObject]
    redirect: Optional[StripeObject]
    sepa_credit_transfer: Optional[StripeObject]
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
    source_order: Optional[StripeObject]
    statement_descriptor: Optional[str]
    """
    Extra information about a source. This will appear on your customer's statement every time you charge the source.
    """
    status: str
    """
    The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge.
    """
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
    """
    The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used.
    """
    usage: Optional[str]
    """
    Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned.
    """
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
    ) -> ListObject["SourceTransaction"]:
        return cast(
            ListObject["SourceTransaction"],
            cls._static_request(
                "get",
                "/v1/sources/{source}/source_transactions".format(
                    source=util.sanitize_id(source)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_source_transactions(
        cls,
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Source.ListSourceTransactionsParams"]
    ) -> ListObject["SourceTransaction"]:
        ...

    @overload
    def list_source_transactions(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.ListSourceTransactionsParams"]
    ) -> ListObject["SourceTransaction"]:
        ...

    @class_method_variant("_cls_list_source_transactions")
    def list_source_transactions(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.ListSourceTransactionsParams"]
    ) -> ListObject["SourceTransaction"]:
        return cast(
            ListObject["SourceTransaction"],
            self._request(
                "get",
                "/v1/sources/{source}/source_transactions".format(
                    source=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Source.ModifyParams"]
    ) -> "Source":
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
    ) -> "Source":
        return cast(
            "Source",
            cls._static_request(
                "post",
                "/v1/sources/{source}/verify".format(
                    source=util.sanitize_id(source)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def verify(
        cls,
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Source.VerifyParams"]
    ) -> "Source":
        ...

    @overload
    def verify(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.VerifyParams"]
    ) -> "Source":
        ...

    @class_method_variant("_cls_verify")
    def verify(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Source.VerifyParams"]
    ) -> "Source":
        return cast(
            "Source",
            self._request(
                "post",
                "/v1/sources/{source}/verify".format(
                    source=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
