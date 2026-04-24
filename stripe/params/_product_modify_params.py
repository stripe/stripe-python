# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class ProductModifyParams(RequestOptions):
    active: NotRequired[bool]
    """
    Whether the product is available for purchase.
    """
    default_price: NotRequired[str]
    """
    The ID of the [Price](https://docs.stripe.com/api/prices) object that is the default price for this product.
    """
    description: NotRequired["Literal['']|str"]
    """
    The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    identifiers: NotRequired["ProductModifyParamsIdentifiers"]
    """
    Other identifiers for this product.
    """
    images: NotRequired["Literal['']|List[str]"]
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    """
    marketing_features: NotRequired[
        "Literal['']|List[ProductModifyParamsMarketingFeature]"
    ]
    """
    A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://docs.stripe.com/payments/checkout/pricing-table).
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    name: NotRequired[str]
    """
    The product's name, meant to be displayable to the customer.
    """
    package_dimensions: NotRequired[
        "Literal['']|ProductModifyParamsPackageDimensions"
    ]
    """
    The dimensions of this product for shipping purposes.
    """
    shippable: NotRequired[bool]
    """
    Whether this product is shipped (i.e., physical goods).
    """
    statement_descriptor: NotRequired[str]
    """
    An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

    This may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
     It must contain at least one letter. May only be set if `type=service`. Only used for subscription payments.
    """
    tax_code: NotRequired["Literal['']|str"]
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID.
    """
    tax_details: NotRequired["Literal['']|ProductModifyParamsTaxDetails"]
    """
    Tax details for this product, including the [tax code](https://docs.stripe.com/tax/tax-codes) and an optional performance location.
    """
    unit_label: NotRequired["Literal['']|str"]
    """
    A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`.
    """
    url: NotRequired["Literal['']|str"]
    """
    A URL of a publicly-accessible webpage for this product.
    """


class ProductModifyParamsIdentifiers(TypedDict):
    ean: NotRequired["Literal['']|str"]
    """
    European Article Number (EAN) consisting of 8 or 13 digits and optional dashes. You may optionally provide a leading 0 for a total of 14 digits. The final digit is a validated check digit.
    """
    gtin: NotRequired["Literal['']|str"]
    """
    Global Trade Item Number (GTIN) consisting of 8, 12, 13, or 14 digits and optional dashes. The final digit is a validated check digit.
    """
    isbn: NotRequired["Literal['']|str"]
    """
    International Standard Book Number (ISBN) consisting of 10 or 13 digits and optional dashes. The final digit is a validated check digit. For ISBN-10, the final digit may be a `X`.
    """
    jan: NotRequired["Literal['']|str"]
    """
    Japanese Article Number (JAN) consisting of 13 digits and optional dashes. The first two digits must either be `45` or `49`. The final digit is a validated check digit.
    """
    mpn: NotRequired["Literal['']|str"]
    """
    Manufacturer Part Number (MPN). May include up to 70 alphanumeric characters and dashes.
    """
    nsn: NotRequired["Literal['']|str"]
    """
    National Stock Number (NSN) consisting of 13 digits and optional dashes. The seventh character may also be alphanumeric.
    """
    upc: NotRequired["Literal['']|str"]
    """
    Universal Product Code (UPC) consisting of 12 digits and optional dashes. The final digit is a validated check digit.
    """


class ProductModifyParamsMarketingFeature(TypedDict):
    name: str
    """
    The marketing feature name. Up to 80 characters long.
    """


class ProductModifyParamsPackageDimensions(TypedDict):
    height: float
    """
    Height, in inches. Maximum precision is 2 decimal places.
    """
    length: float
    """
    Length, in inches. Maximum precision is 2 decimal places.
    """
    weight: float
    """
    Weight, in ounces. Maximum precision is 2 decimal places.
    """
    width: float
    """
    Width, in inches. Maximum precision is 2 decimal places.
    """


class ProductModifyParamsTaxDetails(TypedDict):
    performance_location: NotRequired[str]
    """
    A tax location ID. Depending on the [tax code](https://docs.stripe.com/tax/tax-for-tickets/reference/tax-location-performance), this is required, optional, or not supported.
    """
    tax_code: NotRequired["Literal['']|str"]
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID.
    """
