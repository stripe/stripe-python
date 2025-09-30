# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class SourceModifyParams(RequestOptions):
    amount: NotRequired[int]
    """
    Amount associated with the source.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    mandate: NotRequired["SourceModifyParamsMandate"]
    """
    Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    owner: NotRequired["SourceModifyParamsOwner"]
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """
    source_order: NotRequired["SourceModifyParamsSourceOrder"]
    """
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    """


class SourceModifyParamsMandate(TypedDict):
    acceptance: NotRequired["SourceModifyParamsMandateAcceptance"]
    """
    The parameters required to notify Stripe of a mandate acceptance or refusal by the customer.
    """
    amount: NotRequired["Literal['']|int"]
    """
    The amount specified by the mandate. (Leave null for a mandate covering all amounts)
    """
    currency: NotRequired[str]
    """
    The currency specified by the mandate. (Must match `currency` of the source)
    """
    interval: NotRequired[Literal["one_time", "scheduled", "variable"]]
    """
    The interval of debits permitted by the mandate. Either `one_time` (just permitting a single debit), `scheduled` (with debits on an agreed schedule or for clearly-defined events), or `variable`(for debits with any frequency)
    """
    notification_method: NotRequired[
        Literal["deprecated_none", "email", "manual", "none", "stripe_email"]
    ]
    """
    The method Stripe should use to notify the customer of upcoming debit instructions and/or mandate confirmation as required by the underlying debit network. Either `email` (an email is sent directly to the customer), `manual` (a `source.mandate_notification` event is sent to your webhooks endpoint and you should handle the notification) or `none` (the underlying debit network does not require any notification).
    """


class SourceModifyParamsMandateAcceptance(TypedDict):
    date: NotRequired[int]
    """
    The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
    """
    ip: NotRequired[str]
    """
    The IP address from which the mandate was accepted or refused by the customer.
    """
    offline: NotRequired["SourceModifyParamsMandateAcceptanceOffline"]
    """
    The parameters required to store a mandate accepted offline. Should only be set if `mandate[type]` is `offline`
    """
    online: NotRequired["SourceModifyParamsMandateAcceptanceOnline"]
    """
    The parameters required to store a mandate accepted online. Should only be set if `mandate[type]` is `online`
    """
    status: Literal["accepted", "pending", "refused", "revoked"]
    """
    The status of the mandate acceptance. Either `accepted` (the mandate was accepted) or `refused` (the mandate was refused).
    """
    type: NotRequired[Literal["offline", "online"]]
    """
    The type of acceptance information included with the mandate. Either `online` or `offline`
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the mandate was accepted or refused by the customer.
    """


class SourceModifyParamsMandateAcceptanceOffline(TypedDict):
    contact_email: str
    """
    An email to contact you with if a copy of the mandate is requested, required if `type` is `offline`.
    """


class SourceModifyParamsMandateAcceptanceOnline(TypedDict):
    date: NotRequired[int]
    """
    The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.
    """
    ip: NotRequired[str]
    """
    The IP address from which the mandate was accepted or refused by the customer.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the mandate was accepted or refused by the customer.
    """


class SourceModifyParamsOwner(TypedDict):
    address: NotRequired["SourceModifyParamsOwnerAddress"]
    """
    Owner's address.
    """
    email: NotRequired[str]
    """
    Owner's email address.
    """
    name: NotRequired[str]
    """
    Owner's full name.
    """
    phone: NotRequired[str]
    """
    Owner's phone number.
    """


class SourceModifyParamsOwnerAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """


class SourceModifyParamsSourceOrder(TypedDict):
    items: NotRequired[List["SourceModifyParamsSourceOrderItem"]]
    """
    List of items constituting the order.
    """
    shipping: NotRequired["SourceModifyParamsSourceOrderShipping"]
    """
    Shipping address for the order. Required if any of the SKUs are for products that have `shippable` set to true.
    """


class SourceModifyParamsSourceOrderItem(TypedDict):
    amount: NotRequired[int]
    currency: NotRequired[str]
    description: NotRequired[str]
    parent: NotRequired[str]
    """
    The ID of the SKU being ordered.
    """
    quantity: NotRequired[int]
    """
    The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.
    """
    type: NotRequired[Literal["discount", "shipping", "sku", "tax"]]


class SourceModifyParamsSourceOrderShipping(TypedDict):
    address: "SourceModifyParamsSourceOrderShippingAddress"
    """
    Shipping address.
    """
    carrier: NotRequired[str]
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
    """
    name: NotRequired[str]
    """
    Recipient name.
    """
    phone: NotRequired[str]
    """
    Recipient phone (including extension).
    """
    tracking_number: NotRequired[str]
    """
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
    """


class SourceModifyParamsSourceOrderShippingAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: str
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
