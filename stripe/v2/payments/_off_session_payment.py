# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class OffSessionPayment(StripeObject):
    """
    OffSessionPayment resource.
    """

    OBJECT_NAME: ClassVar[Literal["v2.payments.off_session_payment"]] = (
        "v2.payments.off_session_payment"
    )

    class RetryDetails(StripeObject):
        attempts: int
        """
        Number of authorization attempts so far.
        """
        retry_strategy: Literal["none", "smart"]
        """
        Indicates the strategy for how you want Stripe to retry the payment.
        """

    class TransferData(StripeObject):
        amount: Optional[int]
        """
        The amount transferred to the destination account. This transfer will occur
        automatically after the payment succeeds. If no amount is specified, by default
        the entire payment amount is transferred to the destination account. The amount
        must be less than or equal to the
        [amount_requested](https://docs.corp.stripe.com/api/v2/off-session-payments/object?api-version=2025-05-28.preview#v2_off_session_payment_object-amount_requested),
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
    The “presentment amount” to be collected from the customer.
    """
    cadence: Literal["recurring", "unscheduled"]
    """
    The frequency of the underlying payment.
    """
    compartment_id: str
    """
    ID of the owning compartment.
    """
    created: str
    """
    Creation time of the OffSessionPayment. Represented as a RFC 3339 date & time UTC
    value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    customer: str
    """
    ID of the Customer to which this OffSessionPayment belongs.
    """
    failure_reason: Optional[
        Literal["rejected_by_partner", "retries_exhausted"]
    ]
    """
    The reason why the OffSessionPayment failed.
    """
    id: str
    """
    Unique identifier for the object..
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
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.corp.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.corp.stripe.com/payments/payment-intents#storing-information-in-metadata).
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
    retry_details: RetryDetails
    """
    Details about the OffSessionPayment retries.
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
    status: Literal[
        "canceled",
        "failed",
        "pending",
        "pending_retry",
        "processing",
        "requires_capture",
        "succeeded",
    ]
    """
    Status of this OffSessionPayment, one of `pending`, `pending_retry`, `processing`,
    `failed`, `canceled`, `requires_capture`, or `succeeded`.
    """
    test_clock: Optional[str]
    """
    Test clock that can be used to advance the retry attempts in a sandbox.
    """
    transfer_data: Optional[TransferData]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.corp.stripe.com/payments/connected-accounts).
    """
    _inner_class_types = {
        "retry_details": RetryDetails,
        "transfer_data": TransferData,
    }
