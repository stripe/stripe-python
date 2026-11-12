# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class OffSessionPaymentCreateParams(TypedDict):
    application_fee_amount: NotRequired[AmountParam]
    """
    The amount of the application fee (if any) that will be requested to be applied to the
    payment and transferred to the application owner's Stripe account.
    """
    automatic_tax: NotRequired["OffSessionPaymentCreateParamsAutomaticTax"]
    """
    Settings for automatic tax calculation.
    """
    currency: NotRequired[str]
    """
    Three-letter ISO currency code, in lowercase.
    """
    customer: NotRequired[str]
    """
    ID of the Customer to which this OffSessionPayment belongs.
    Provide exactly one of customer or customer_account.
    """
    customer_account: NotRequired[str]
    """
    ID of the Account representing the customer to which this OffSessionPayment belongs.
    Provide exactly one of customer or customer_account.
    Payment methods attached to other Accounts cannot be used with this OffSessionPayment.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    items: NotRequired[List["OffSessionPaymentCreateParamsItem"]]
    """
    A list of items the customer will purchase.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata).
    """
    on_behalf_of: NotRequired[str]
    """
    The account (if any) for which the funds of the OffSessionPayment are intended.
    """
    payment_method: NotRequired[str]
    """
    ID of the payment method used in this OffSessionPayment.
    """
    payment_method_data: NotRequired[
        "OffSessionPaymentCreateParamsPaymentMethodData"
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear in the payment_method property on the OffSessionPayment.
    """
    payment_method_options: NotRequired[
        "OffSessionPaymentCreateParamsPaymentMethodOptions"
    ]
    """
    Payment method options for the off-session payment.
    """
    raw_amount: NotRequired["OffSessionPaymentCreateParamsRawAmount"]
    """
    The amount to collect without itemization.
    """
    retries: "OffSessionPaymentCreateParamsRetries"
    """
    Retry configuration for this OffSessionPayment.
    """
    statement_descriptor: NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a
    non-card charge. This value overrides the account's default statement descriptor.
    For information about requirements, including the 22-character limit, see the
    [Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """
    statement_descriptor_suffix: NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's
    [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
    to form the complete statement descriptor that appears on the customer's statement.
    """
    target_date: NotRequired[str]
    """
    Provides a way to schedule deferred payments for cards and debits, in YYYY-MM-DD format.
    """
    test_clock: NotRequired[str]
    """
    Test clock that can be used to advance the retry attempts in a sandbox.
    """
    transfer_data: NotRequired["OffSessionPaymentCreateParamsTransferData"]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class OffSessionPaymentCreateParamsAutomaticTax(TypedDict):
    enabled: bool
    """
    Whether to automatically calculate taxes for this OffSessionPayment.
    """


class OffSessionPaymentCreateParamsItem(TypedDict):
    one_time_price: "OffSessionPaymentCreateParamsItemOneTimePrice"
    """
    Configuration for the one-time price item.
    """
    type: Union[Literal["one_time_price"], str]
    """
    The type of item. Currently, only `one_time_price` is supported.
    """


class OffSessionPaymentCreateParamsItemOneTimePrice(TypedDict):
    items: List["OffSessionPaymentCreateParamsItemOneTimePriceItem"]
    """
    The list of one-time prices and quantities the customer will purchase. Contains 1 to 10 items.
    """


class OffSessionPaymentCreateParamsItemOneTimePriceItem(TypedDict):
    price: NotRequired[str]
    """
    The ID of an existing one-time [Price](https://docs.stripe.com/api/prices).
    Provide exactly one of `price` or `price_data`.
    """
    price_data: NotRequired[
        "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceData"
    ]
    """
    Data used to generate a new one-time [Price](https://docs.stripe.com/api/prices) object inline.
    Provide exactly one of `price` or `price_data`.
    """
    quantity: int
    """
    Quantity for this item.
    """


class OffSessionPaymentCreateParamsItemOneTimePriceItemPriceData(TypedDict):
    product: NotRequired[str]
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this
    [Price](https://docs.stripe.com/api/prices) will belong to.
    Provide exactly one of `product` or `product_data`.
    """
    product_data: NotRequired[
        "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductData"
    ]
    """
    Data used to generate a new [Product](https://docs.stripe.com/api/products) object inline.
    Provide exactly one of `product` or `product_data`.
    """
    tax_behavior: NotRequired[
        "Literal['exclusive', 'inclusive', 'unspecified']|str"
    ]
    """
    Specifies whether the price is considered inclusive of taxes or exclusive of taxes.
    One of `inclusive`, `exclusive`, or `unspecified`.
    """
    unit_amount: AmountParam
    """
    The amount to charge per unit and its currency. Specify `value` as a non-negative integer in
    the currency's minor unit (for example, `100` for USD 1.00).
    """


class OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductData(
    TypedDict,
):
    description: NotRequired[str]
    """
    The product's description, meant to be displayable to the customer.
    Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """
    images: NotRequired[List[str]]
    """
    A list of URLs of images for this product, meant to be displayable to the customer.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to the product.
    This can be useful for storing additional information about the product in a structured format.
    """
    name: str
    """
    The product's name, meant to be displayable to the customer.
    """
    tax_details: NotRequired[
        "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductDataTaxDetails"
    ]
    """
    Tax details for this product, including the [tax code](https://docs.stripe.com/tax/tax-codes)
    and an optional performance location.
    """
    unit_label: NotRequired[str]
    """
    A label that represents units of this product, such as seats or licenses.
    """


class OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductDataTaxDetails(
    TypedDict,
):
    performance_location: NotRequired[str]
    """
    A tax location ID. Depending on the [tax code](https://docs.stripe.com/tax/tax-for-tickets/reference/tax-location-performance),
    this is required, optional, or not supported.
    """
    tax_code: NotRequired[str]
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID.
    """


class OffSessionPaymentCreateParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails"
    ]
    """
    Billing information associated with the payment method.
    """
    card: NotRequired["OffSessionPaymentCreateParamsPaymentMethodDataCard"]
    """
    Contains card details that can be used to create a card PaymentMethod for PCI compliant users.
    """
    type: Union[Literal["card"], str]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """


class OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress"
    ]
    """
    Billing address.
    """
    email: NotRequired[str]
    """
    Email address.
    """
    name: NotRequired[str]
    """
    Full name.
    """
    phone: NotRequired[str]
    """
    Billing phone number (including extension).
    """


class OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code (ISO 3166-1 alpha-2).
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
    State, county, province, or region (ISO 3166-2).
    """


class OffSessionPaymentCreateParamsPaymentMethodDataCard(TypedDict):
    exp_month: str
    """
    The card expiration month.
    """
    exp_year: str
    """
    The card expiration year.
    """
    last4: NotRequired[str]
    """
    The last four digits of the underlying card number.
    """
    network_token: NotRequired[
        "OffSessionPaymentCreateParamsPaymentMethodDataCardNetworkToken"
    ]
    """
    The network token credential to use with the card.
    """
    number: NotRequired[str]
    """
    The card number.
    """


class OffSessionPaymentCreateParamsPaymentMethodDataCardNetworkToken(
    TypedDict
):
    exp_month: str
    """
    Two-digit number representing the network token's expiration month.
    """
    exp_year: str
    """
    Four-digit number representing the network token's expiration year.
    """
    number: str
    """
    The full network token number.
    """
    tokenization_method: Literal[
        "apple_pay", "google_pay_dpan", "google_pay_ecommerce_token"
    ]
    """
    The tokenization method used to generate the network token.
    """


class OffSessionPaymentCreateParamsPaymentMethodOptions(TypedDict):
    card: NotRequired["OffSessionPaymentCreateParamsPaymentMethodOptionsCard"]
    """
    Payment method options for the card payment type.
    """


class OffSessionPaymentCreateParamsPaymentMethodOptionsCard(TypedDict):
    stored_credential_usage: Union[Literal["recurring", "unscheduled"], str]
    """
    Indicates whether the saved card is used for a recurring or unscheduled payment.
    """


class OffSessionPaymentCreateParamsRawAmount(TypedDict):
    amount: AmountParam
    """
    The amount to collect and its currency.
    """


class OffSessionPaymentCreateParamsRetries(TypedDict):
    enabled: bool
    """
    Whether Stripe should retry failed payment attempts.
    """


class OffSessionPaymentCreateParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount transferred to the destination account. This transfer will occur
    automatically after the payment succeeds. If no amount is specified, by default
    the entire payment amount is transferred to the destination account. The amount
    must be less than or equal to the
    [amount_requested](https://docs.stripe.com/api/v2/off-session-payments/object?api-version=2025-05-28.preview#v2_off_session_payment_object-amount_requested),
    and must be a positive integer representing how much to transfer in the smallest
    currency unit (e.g., 100 cents to charge $1.00).
    """
    destination: str
    """
    The account (if any) that the payment is attributed to for tax reporting, and
    where funds from the payment are transferred to after payment success.
    """
