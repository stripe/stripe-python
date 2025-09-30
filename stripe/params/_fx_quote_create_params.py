# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FxQuoteCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    from_currencies: List[str]
    """
    A list of three letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be [supported currencies](https://stripe.com/docs/currencies).
    """
    lock_duration: Literal["day", "five_minutes", "hour", "none"]
    """
    The duration that you wish the quote to be locked for. The quote will be usable for the duration specified. The default is `none`. The maximum is 1 day.
    """
    to_currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    usage: NotRequired["FxQuoteCreateParamsUsage"]
    """
    The usage specific information for the quote.
    """


class FxQuoteCreateParamsUsage(TypedDict):
    payment: NotRequired["FxQuoteCreateParamsUsagePayment"]
    """
    The payment transaction details that are intended for the FX Quote.
    """
    transfer: NotRequired["FxQuoteCreateParamsUsageTransfer"]
    """
    The transfer transaction details that are intended for the FX Quote.
    """
    type: Literal["payment", "transfer"]
    """
    Which transaction the FX Quote will be used for

    Can be “payment” | “transfer”
    """


class FxQuoteCreateParamsUsagePayment(TypedDict):
    destination: NotRequired[str]
    """
    The Stripe account ID that the funds will be transferred to.

    This field should match the account ID that would be used in the PaymentIntent's transfer_data[destination] field.
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID that these funds are intended for.

    This field should match the account ID that would be used in the PaymentIntent's on_behalf_of field.
    """


class FxQuoteCreateParamsUsageTransfer(TypedDict):
    destination: str
    """
    The Stripe account ID that the funds will be transferred to.

    This field should match the account ID that would be used in the Transfer's destination field.
    """
