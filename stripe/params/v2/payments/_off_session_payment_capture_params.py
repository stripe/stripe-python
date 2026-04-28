# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List
from typing_extensions import NotRequired, TypedDict


class OffSessionPaymentCaptureParams(TypedDict):
    amount_details: NotRequired["OffSessionPaymentCaptureParamsAmountDetails"]
    """
    Provides industry-specific information about the amount.
    """
    amount_to_capture: NotRequired[int]
    """
    The amount to capture.
    """
    application_fee_amount: NotRequired[AmountParam]
    """
    The amount of the application fee for this capture.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata).
    """
    payment_details: NotRequired[
        "OffSessionPaymentCaptureParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the payment.
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
    transfer_data: NotRequired["OffSessionPaymentCaptureParamsTransferData"]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class OffSessionPaymentCaptureParamsAmountDetails(TypedDict):
    discount_amount: NotRequired[int]
    """
    The amount the total transaction was discounted for.
    """
    enforce_arithmetic_validation: NotRequired[bool]
    """
    Set to `false` to return arithmetic validation errors in the response without failing the request. Use this when you want the operation to proceed regardless of arithmetic errors in the line item data.
    Omit or set to `true` to immediately return a 400 error when arithmetic validation fails. Use this for strict validation that prevents processing with line item data that has arithmetic inconsistencies.
    For card payments, Stripe doesn't send line item data to card networks if there's an arithmetic validation error.
    """
    line_items: NotRequired[
        List["OffSessionPaymentCaptureParamsAmountDetailsLineItem"]
    ]
    """
    A list of line items, each containing information about a product in the OffSessionPayment. There is a maximum of 10 line items.
    """
    shipping: NotRequired[
        "OffSessionPaymentCaptureParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired["OffSessionPaymentCaptureParamsAmountDetailsTax"]
    """
    Contains information about the tax portion of the amount.
    """


class OffSessionPaymentCaptureParamsAmountDetailsLineItem(TypedDict):
    discount_amount: NotRequired[int]
    """
    The amount an item was discounted for. Positive integer.
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
    tax: NotRequired["OffSessionPaymentCaptureParamsAmountDetailsLineItemTax"]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    Cost of the product. Positive integer.
    """
    unit_of_measure: NotRequired[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    The maximum length is 12 characters.
    """


class OffSessionPaymentCaptureParamsAmountDetailsLineItemTax(TypedDict):
    total_tax_amount: int
    """
    Total portion of the amount that is for tax.
    """


class OffSessionPaymentCaptureParamsAmountDetailsShipping(TypedDict):
    amount: NotRequired[int]
    """
    Portion of the amount that is for shipping.
    """
    from_postal_code: NotRequired[str]
    """
    The postal code that represents the shipping source.
    """
    to_postal_code: NotRequired[str]
    """
    The postal code that represents the shipping destination.
    """


class OffSessionPaymentCaptureParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    Total portion of the amount that is for tax.
    """


class OffSessionPaymentCaptureParamsPaymentDetails(TypedDict):
    customer_reference: NotRequired[str]
    """
    A unique value to identify the customer. This field is applicable only for card payments. For card payments, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    order_reference: NotRequired[str]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.
    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """


class OffSessionPaymentCaptureParamsTransferData(TypedDict):
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
