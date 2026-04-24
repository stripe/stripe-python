# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class OffSessionPaymentCreateParams(TypedDict):
    amount: AmountParam
    """
    The “presentment amount” to be collected from the customer.
    """
    amount_details: NotRequired["OffSessionPaymentCreateParamsAmountDetails"]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired[AmountParam]
    """
    The amount of the application fee (if any) that will be requested to be applied to the
    payment and transferred to the application owner's Stripe account.
    """
    cadence: Literal["recurring", "unscheduled"]
    """
    The frequency of the underlying payment.
    """
    capture: NotRequired["OffSessionPaymentCreateParamsCapture"]
    """
    Details about the capture configuration for the OffSessionPayment.
    """
    customer: str
    """
    ID of the Customer to which this OffSessionPayment belongs.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    metadata: "Dict[str, str]|UntypedStripeObject[str]"
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
    payment_details: NotRequired["OffSessionPaymentCreateParamsPaymentDetails"]
    """
    Provides industry-specific information about the payment.
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
    payments_orchestration: NotRequired[
        "OffSessionPaymentCreateParamsPaymentsOrchestration"
    ]
    """
    Details about the payments orchestration configuration.
    """
    retry_details: NotRequired["OffSessionPaymentCreateParamsRetryDetails"]
    """
    Details about the OffSessionPayment retries.
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
    test_clock: NotRequired[str]
    """
    Test clock that can be used to advance the retry attempts in a sandbox.
    """
    transfer_data: NotRequired["OffSessionPaymentCreateParamsTransferData"]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class OffSessionPaymentCreateParamsAmountDetails(TypedDict):
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
        List["OffSessionPaymentCreateParamsAmountDetailsLineItem"]
    ]
    """
    A list of line items, each containing information about a product in the OffSessionPayment. There is a maximum of 10 line items.
    """
    shipping: NotRequired["OffSessionPaymentCreateParamsAmountDetailsShipping"]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired["OffSessionPaymentCreateParamsAmountDetailsTax"]
    """
    Contains information about the tax portion of the amount.
    """


class OffSessionPaymentCreateParamsAmountDetailsLineItem(TypedDict):
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
    tax: NotRequired["OffSessionPaymentCreateParamsAmountDetailsLineItemTax"]
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


class OffSessionPaymentCreateParamsAmountDetailsLineItemTax(TypedDict):
    total_tax_amount: int
    """
    Total portion of the amount that is for tax.
    """


class OffSessionPaymentCreateParamsAmountDetailsShipping(TypedDict):
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


class OffSessionPaymentCreateParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    Total portion of the amount that is for tax.
    """


class OffSessionPaymentCreateParamsCapture(TypedDict):
    capture_method: Literal["automatic", "manual"]
    """
    The method to use to capture the payment.
    """


class OffSessionPaymentCreateParamsPaymentDetails(TypedDict):
    customer_reference: NotRequired[str]
    """
    A unique value to identify the customer. This field is applicable only for card payments. For card payments, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    order_reference: NotRequired[str]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.
    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
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
    type: Literal["card"]
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
    cvc: NotRequired[str]
    """
    The card CVC.
    """
    exp_month: str
    """
    The card expiration month.
    """
    exp_year: str
    """
    The card expiration year.
    """
    number: NotRequired[str]
    """
    The card number.
    """


class OffSessionPaymentCreateParamsPaymentMethodOptions(TypedDict):
    card: NotRequired["OffSessionPaymentCreateParamsPaymentMethodOptionsCard"]
    """
    Payment method options for the card payment type.
    """


class OffSessionPaymentCreateParamsPaymentMethodOptionsCard(TypedDict):
    mcc: NotRequired[str]
    """
    The merchant category code for this transaction. Used in interchange and authorization to improve auth rates.
    """
    network_transaction_id: NotRequired[str]
    """
    If you are making a Credential On File transaction with a previously saved card, you should pass the Network Transaction ID
    from a prior initial authorization on Stripe (from a successful SetupIntent or a PaymentIntent with `setup_future_usage` set),
    or one that you have obtained from another payment processor. This is a token from the network which uniquely identifies the transaction.
    Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data.
    Note that you should pass in a Network Transaction ID if you have one, regardless of whether this is a
    Customer-Initiated Transaction (CIT) or a Merchant-Initiated Transaction (MIT).
    """


class OffSessionPaymentCreateParamsPaymentsOrchestration(TypedDict):
    enabled: bool
    """
    True when you want to enable payments orchestration for this off-session payment. False otherwise.
    """


class OffSessionPaymentCreateParamsRetryDetails(TypedDict):
    retry_policy: NotRequired[str]
    """
    The pre-configured retry policy to use for the payment.
    """
    retry_strategy: NotRequired[Literal["best_available", "none"]]
    """
    Indicates the strategy for how you want Stripe to retry the payment.
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
