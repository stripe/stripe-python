# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class OffSessionPayment(StripeObject):
    """
    Off-session payment resource.
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
        How you want Stripe to retry the payment.
        """

    class TransferData(StripeObject):
        amount: Optional[int]
        """
        Amount in minor units that you want to transfer.
        """
        destination: str
        """
        ID of the connected account where you want money to go.
        """

    amount_requested: Amount
    """
    The amount you requested to be collected on the OSP upon creation.
    """
    cadence: Literal["recurring", "unscheduled"]
    """
    The frequency of the underlying payment that this OSP represents.
    """
    compartment_id: str
    """
    ID of owning compartment.
    """
    created: str
    """
    Timestamp of creation.
    """
    customer: str
    """
    Customer owning the supplied payment method.
    """
    failure_reason: Optional[
        Literal["rejected_by_partner", "retries_exhausted"]
    ]
    """
    Reason why the OSP failed.
    """
    id: str
    """
    ID of the OSP.
    """
    last_authorization_attempt_error: Optional[str]
    """
    Last error returned by the financial partner for a failed authorization.
    """
    latest_payment_attempt_record: Optional[str]
    """
    Payment attempt record for the latest attempt, if one exists.
    """
    livemode: bool
    """
    True if the txn is livemode, false otherwise.
    """
    metadata: Dict[str, str]
    """
    Metadata you provided.
    """
    object: Literal["v2.payments.off_session_payment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    on_behalf_of: Optional[str]
    """
    OBO, same as on the PI.
    """
    payment_method: str
    """
    ID of payment method.
    """
    payment_record: Optional[str]
    """
    Payment record associated with the OSP. consistent across attempts.
    """
    retry_details: RetryDetails
    """
    Details about the OSP retries.
    """
    statement_descriptor: Optional[str]
    """
    Statement descriptor you provided.
    """
    statement_descriptor_suffix: Optional[str]
    """
    Statement descriptor suffix you provided, similar to that on the PI.
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
    Status of the OSP.
    """
    test_clock: Optional[str]
    """
    Test clock to be used to advance the retry attempts.
    """
    transfer_data: Optional[TransferData]
    """
    Instructions for the transfer to be made with this OSP after successful money movement.
    """
    _inner_class_types = {
        "retry_details": RetryDetails,
        "transfer_data": TransferData,
    }
