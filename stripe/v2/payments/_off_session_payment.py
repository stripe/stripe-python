# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class OffSessionPayment(StripeObject):
    """
    An OffSessionPayment allows you to create your own payment flow for recurring and unscheduled payments. In a single API request, you can
    initiate a payment and leverage Stripe's AI-powered [Smart Retries](https://docs.stripe.com/payments/off-session-payments/smart-retries)
    to choose the best times to retry failures to increase the chance of a successful payment.
    To properly interface with OffSessionPayments, we recommend setting up an event destination to listen to webhook notifications, as the
    OffSessionPayment will transition through its lifecycle asynchronously.
    Related guide: [Off-Session Payments API](https://docs.stripe.com/payments/off-session-payments).
    """

    OBJECT_NAME: ClassVar[Literal["v2.payments.off_session_payment"]] = (
        "v2.payments.off_session_payment"
    )

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            type: Union[Literal["self"], str]
            """
            The type of account liable for tax.
            """

        enabled: bool
        """
        Whether automatic tax calculation is enabled for this OffSessionPayment.
        """
        liability: Optional[Liability]
        """
        The account liable for tax. Null when automatic tax is disabled; otherwise,
        an object with type set to `self`, indicating the account making the API request.
        """
        _inner_class_types = {"liability": Liability}

    class Item(StripeObject):
        class OneTimePrice(StripeObject):
            class Item(StripeObject):
                price: str
                """
                The ID of the resolved one-time Price.
                """
                quantity: int
                """
                Quantity of this price in the item group.
                """

            description: Optional[str]
            """
            A description of this item group. Currently always null.
            """
            items: List[Item]
            """
            The resolved price IDs and quantities in their original order.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Additional information about this item group. Currently always null.
            """
            _inner_class_types = {"items": Item}

        one_time_price: OneTimePrice
        """
        The persisted one-time prices in this item group.
        """
        type: Union[Literal["one_time_price"], str]
        """
        The type of item. Currently, only `one_time_price` is supported.
        """
        _inner_class_types = {"one_time_price": OneTimePrice}

    class PaymentsOrchestration(StripeObject):
        enabled: bool
        """
        True when you want to enable payments orchestration for this off-session payment. False otherwise.
        """

    class Retries(StripeObject):
        attempts: int
        """
        Number of authorization attempts so far.
        """
        enabled: bool
        """
        Whether retries are enabled for this OffSessionPayment.
        """

    class TotalDetails(StripeObject):
        amount_subtotal: Amount
        """
        The subtotal of the items, including any inclusive tax and excluding exclusive tax.
        """
        amount_tax: Optional[Amount]
        """
        The calculated tax amount, including zero. Null when automatic tax was disabled.
        """

    class TransferData(StripeObject):
        amount: Optional[int]
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

    amount_requested: Amount
    """
    Amount intended to be collected by this payment.
    """
    amount_total: Amount
    """
    The total amount to collect, including tax when applicable.
    """
    application: Optional[str]
    """
    The application associated with this OffSessionPayment.
    """
    application_fee_amount_requested: Optional[Amount]
    """
    The amount of the application fee requested to be applied to the payment.
    """
    automatic_tax: Optional[AutomaticTax]
    """
    Details about automatic tax calculation.
    """
    created: str
    """
    Creation time of the OffSessionPayment. Represented as a RFC 3339 date & time UTC
    value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase.
    """
    customer: Optional[str]
    """
    ID of the Customer to which this OffSessionPayment belongs, if one exists.
    """
    customer_account: Optional[str]
    """
    ID of the Account representing the customer to which this OffSessionPayment belongs, if one exists.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    failure_reason: Optional[
        Union[
            Literal[
                "authorization_expired",
                "exceeded_retry_window",
                "no_valid_payment_method",
                "rejected_by_partner",
                "retries_exhausted",
            ],
            str,
        ]
    ]
    """
    The reason why the OffSessionPayment failed.
    """
    id: str
    """
    Unique identifier for the object.
    """
    items: Optional[List[Item]]
    """
    The persisted item groups for this OffSessionPayment, in their original order. Null for raw-amount payments.
    """
    last_authorization_attempt_error: Optional[str]
    """
    The payment error encountered in the previous attempt to authorize the payment.
    """
    latest_payment_attempt_record: Optional[str]
    """
    Payment attempt record for the latest attempt, if one exists.
    """
    livemode: bool
    """
    Has the value true if the object exists in live mode or the value false if the object exists in test mode.
    """
    metadata: UntypedStripeObject[str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata).
    """
    object: Literal["v2.payments.off_session_payment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    on_behalf_of: Optional[str]
    """
    The account (if any) for which the funds of the OffSessionPayment are intended.
    """
    payment_method: str
    """
    ID of the payment method used in this OffSessionPayment.
    """
    payment_record: Optional[str]
    """
    Payment record associated with the OffSessionPayment.
    """
    payments_orchestration: PaymentsOrchestration
    """
    Details about the payments orchestration configuration.
    """
    retries: Retries
    """
    Retry configuration and attempts for this OffSessionPayment.
    """
    statement_descriptor: Optional[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a
    non-card charge. This value overrides the account's default statement descriptor.
    For information about requirements, including the 22-character limit, see the
    [Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """
    statement_descriptor_suffix: Optional[str]
    """
    Provides information about a card charge. Concatenated to the account's
    [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
    to form the complete statement descriptor that appears on the customer's statement.
    """
    status: Union[
        Literal[
            "canceled",
            "failed",
            "paused",
            "pending",
            "pending_retry",
            "processing",
            "succeeded",
        ],
        str,
    ]
    """
    Status of this OffSessionPayment, one of `pending`, `pending_retry`, `processing`,
    `failed`, `canceled`, or `succeeded`.
    """
    target_date: Optional[str]
    """
    Provides a way to schedule deferred payments for cards and debits, in YYYY-MM-DD format.
    """
    test_clock: Optional[str]
    """
    Test clock that can be used to advance the retry attempts in a sandbox.
    """
    total_details: Optional[TotalDetails]
    """
    Subtotal and tax for an itemized OffSessionPayment. Null for raw-amount payments.
    """
    transfer_data: Optional[TransferData]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "items": Item,
        "payments_orchestration": PaymentsOrchestration,
        "retries": Retries,
        "total_details": TotalDetails,
        "transfer_data": TransferData,
    }
