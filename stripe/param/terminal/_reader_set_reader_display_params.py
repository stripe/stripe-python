# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ReaderSetReaderDisplayParams(RequestOptions):
    cart: NotRequired["ReaderSetReaderDisplayParamsCart"]
    """
    Cart
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    type: Literal["cart"]
    """
    Type
    """


class ReaderSetReaderDisplayParamsCart(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    line_items: List["ReaderSetReaderDisplayParamsCartLineItem"]
    """
    Array of line items that were purchased.
    """
    tax: NotRequired[int]
    """
    The amount of tax in cents.
    """
    total: int
    """
    Total balance of cart due in cents.
    """


class ReaderSetReaderDisplayParamsCartLineItem(TypedDict):
    amount: int
    """
    The price of the item in cents.
    """
    description: str
    """
    The description or name of the item.
    """
    quantity: int
    """
    The quantity of the line item being purchased.
    """
