# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentDecrementAuthorizationParams(RequestOptions):
    amount: int
    """
    The updated total amount that you intend to collect from the cardholder. This amount must be smaller than the currently authorized amount and greater than the already captured amount.
    """
    amount_details: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetails"
    ]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    hooks: NotRequired["PaymentIntentDecrementAuthorizationParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the charge.
    """
    transfer_data: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsTransferData"
    ]
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetails(TypedDict):
    discount_amount: NotRequired["Literal['']|int"]
    """
    The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[line_items][#][discount_amount]` field.
    """
    enforce_arithmetic_validation: NotRequired[bool]
    """
    Set to `false` to return arithmetic validation errors in the response without failing the request. Use this when you want the operation to proceed regardless of arithmetic errors in the line item data.

    Omit or set to `true` to immediately return a 400 error when arithmetic validation fails. Use this for strict validation that prevents processing with line item data that has arithmetic inconsistencies.

    For card payments, Stripe doesn't send line item data to card networks if there's an arithmetic validation error.
    """
    line_items: NotRequired[
        "Literal['']|List[PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 200 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    surcharge: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsSurcharge"
    ]
    """
    Contains information about the surcharge portion of the amount.
    """
    tax: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsTax"
    ]
    """
    Contains information about the tax portion of the amount.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItem(
    TypedDict
):
    discount_amount: NotRequired[int]
    """
    The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]` field.
    """
    payment_method_options: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions"
    ]
    """
    Payment method-specific information for line items.
    """
    product_code: NotRequired[str]
    """
    The product code of the line item, such as an SKU. Required for L3 rates. At most 12 characters long.
    """
    product_name: str
    """
    The product name of the line item. Required for L3 rates. At most 1024 characters long.

    For Cards, this field is truncated to 26 alphanumeric characters before being sent to the card networks. For PayPal, this field is truncated to 127 characters.
    """
    quantity: int
    """
    The quantity of items. Required for L3 rates. An integer greater than 0.
    """
    tax: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemTax"
    ]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    The unit cost of the line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.
    """
    unit_of_measure: NotRequired[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to the `card` payment method.
    """
    card_present: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to the `card_present` payment method.
    """
    klarna: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to the `klarna` payment method.
    """
    paypal: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to the `paypal` payment method.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
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


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
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


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemTax(
    TypedDict,
):
    total_tax_amount: int
    """
    The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsShipping(
    TypedDict
):
    amount: NotRequired["Literal['']|int"]
    """
    If a physical good is being shipped, the cost of shipping represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than or equal to 0.
    """
    from_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped from. At most 10 alphanumeric characters long, hyphens are allowed.
    """
    to_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped to. At most 10 alphanumeric characters long, hyphens are allowed.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsSurcharge(
    TypedDict,
):
    amount: NotRequired["Literal['']|int"]
    """
    Portion of the amount that corresponds to a surcharge.
    """
    enforce_validation: NotRequired[
        "Literal['']|Literal['automatic', 'disabled', 'enabled']"
    ]
    """
    Indicate whether to enforce validations on the surcharge amount.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class PaymentIntentDecrementAuthorizationParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentDecrementAuthorizationParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentDecrementAuthorizationParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentDecrementAuthorizationParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentDecrementAuthorizationParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id
    """


class PaymentIntentDecrementAuthorizationParamsPaymentDetails(TypedDict):
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    Required when the Payment Method Types array contains `card`, including when [automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled) is set to `true`.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.
    """


class PaymentIntentDecrementAuthorizationParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    """
