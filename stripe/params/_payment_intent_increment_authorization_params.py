# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentIncrementAuthorizationParams(RequestOptions):
    amount: int
    """
    The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
    """
    amount_details: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetails"
    ]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    hooks: NotRequired["PaymentIntentIncrementAuthorizationParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the charge.
    """
    payment_method_options: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsPaymentMethodOptions"
    ]
    """
    Payment method-specific configuration for this PaymentIntent.
    """
    statement_descriptor: NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """
    transfer_data: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsTransferData"
    ]
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetails(TypedDict):
    discount_amount: NotRequired["Literal['']|int"]
    """
    The total discount applied on the transaction.
    """
    line_items: NotRequired[
        "Literal['']|List[PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 100 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentIncrementAuthorizationParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired[
        "Literal['']|PaymentIntentIncrementAuthorizationParamsAmountDetailsTax"
    ]
    """
    Contains information about the tax portion of the amount.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItem(
    TypedDict
):
    discount_amount: NotRequired[int]
    """
    The amount an item was discounted for. Positive integer.
    """
    payment_method_options: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions"
    ]
    """
    Payment method-specific information for line items.
    """
    product_code: NotRequired[str]
    """
    Unique identifier of the product. At most 12 characters long.
    """
    product_name: str
    """
    Name of the product. At most 100 characters long.
    """
    quantity: int
    """
    Number of items of the product. Positive integer.
    """
    tax: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemTax"
    ]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    Cost of the product. Non-negative integer.
    """
    unit_of_measure: NotRequired[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to `card` payment method."
    """
    card_present: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to `card_present` payment method."
    """
    klarna: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to `klarna` payment method."
    """
    paypal: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to `paypal` payment method."
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
    TypedDict,
):
    image_url: NotRequired[str]
    """
    URL to an image for the product. Max length, 4096 characters.
    """
    product_url: NotRequired[str]
    """
    URL to the product page. Max length, 4096 characters.
    """
    reference: NotRequired[str]
    """
    Unique reference for this line item to correlate it with your system's internal records. The field is displayed in the Klarna Consumer App if passed.
    """
    subscription_reference: NotRequired[str]
    """
    Reference for the subscription this line item is for.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
    TypedDict,
):
    category: NotRequired[
        Literal["digital_goods", "donation", "physical_goods"]
    ]
    """
    Type of the line item.
    """
    description: NotRequired[str]
    """
    Description of the line item.
    """
    sold_by: NotRequired[str]
    """
    The Stripe account ID of the connected account that sells the item.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsLineItemTax(
    TypedDict,
):
    total_tax_amount: int
    """
    The total tax on an item. Non-negative integer.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsShipping(
    TypedDict
):
    amount: NotRequired["Literal['']|int"]
    """
    Portion of the amount that is for shipping.
    """
    from_postal_code: NotRequired["Literal['']|str"]
    """
    The postal code that represents the shipping source.
    """
    to_postal_code: NotRequired["Literal['']|str"]
    """
    The postal code that represents the shipping destination.
    """


class PaymentIntentIncrementAuthorizationParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    Total portion of the amount that is for tax.
    """


class PaymentIntentIncrementAuthorizationParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentIncrementAuthorizationParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentIncrementAuthorizationParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentIncrementAuthorizationParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentIncrementAuthorizationParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://stripe.com/docs/api/tax/calculations) id
    """


class PaymentIntentIncrementAuthorizationParamsPaymentDetails(TypedDict):
    customer_reference: NotRequired["Literal['']|str"]
    """
    Some customers might be required by their company or organization to provide this information. If so, provide this value. Otherwise you can ignore this field.
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction.
    """


class PaymentIntentIncrementAuthorizationParamsPaymentMethodOptions(TypedDict):
    card: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsPaymentMethodOptionsCard"
    ]
    """
    Configuration for any card payments attempted on this PaymentIntent.
    """


class PaymentIntentIncrementAuthorizationParamsPaymentMethodOptionsCard(
    TypedDict,
):
    request_partial_authorization: NotRequired[
        Literal["if_available", "never"]
    ]
    """
    Request partial authorization on this PaymentIntent.
    """


class PaymentIntentIncrementAuthorizationParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    """
