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
            A description of this item group.
            """
            items: List[Item]
            """
            The resolved price IDs and quantities in their original order.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Additional information about this item group.
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

    amount_total: Amount
    """
    The total amount to collect, including tax when applicable.
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
                "customer_invalid",
                "exceeded_retry_window",
                "no_valid_payment_method",
                "payment_method_currency_invalid",
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
    payment_method: str
    """
    ID of the payment method used in this OffSessionPayment.
    """
    payment_record: Optional[str]
    """
    Payment record associated with the OffSessionPayment.
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
            "pending_initial_attempt",
            "pending_retry",
            "processing",
            "succeeded",
        ],
        str,
    ]
    """
    Status of this OffSessionPayment, one of `pending_initial_attempt`, `pending_retry`,
    `processing`, `failed`, `canceled`, `succeeded`, or `paused`.
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
    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "items": Item,
        "retries": Retries,
        "total_details": TotalDetails,
    }
