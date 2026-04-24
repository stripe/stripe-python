# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ApprovalRequest(StripeObject):
    """
    An approval request represents a pending action that requires review before execution.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.approval_request"]] = (
        "v2.core.approval_request"
    )

    class RequestedBy(StripeObject):
        id: str
        """
        Stripe-defined identifier for the requester (e.g. a restricted API key token).
        """
        name: Optional[str]
        """
        Merchant-defined name for the requester.
        """

    class Review(StripeObject):
        class ReviewedBy(StripeObject):
            id: str
            """
            Stripe-defined identifier for the reviewer (e.g. a restricted API key token).
            """
            name: str
            """
            Merchant-defined name for the reviewer.
            """

        reason: Optional[str]
        """
        The reason provided by the reviewer.
        """
        result: Literal["approved", "rejected"]
        """
        The result of the review.
        """
        reviewed_at: str
        """
        Timestamp when the review was performed.
        """
        reviewed_by: ReviewedBy
        """
        The reviewer who performed the review.
        """
        _inner_class_types = {"reviewed_by": ReviewedBy}

    class Rule(StripeObject):
        name: str
        """
        The name of the rule.
        """

    class StatusDetails(StripeObject):
        class Approved(StripeObject):
            reason: Optional[str]
            """
            The reason provided when approving the request.
            """

        class Canceled(StripeObject):
            pass

        class ExecutionFailed(StripeObject):
            code: str
            """
            The error code for the failed execution.
            """
            message: str
            """
            The error message for the failed execution.
            """
            type: str
            """
            The error type for the failed execution.
            """

        class ExecutionStarted(StripeObject):
            pass

        class ExecutionSucceeded(StripeObject):
            class Result(StripeObject):
                id: str
                """
                The unique identifier of the executed object.
                """
                object: str
                """
                The object type of the executed resource.
                """

            result: Result
            """
            The result of the successful execution.
            """
            _inner_class_types = {"result": Result}

        class Expired(StripeObject):
            pass

        class Failed(StripeObject):
            error_code: str
            """
            The error code for the failed execution.
            """
            error_message: str
            """
            The error message for the failed execution.
            """
            error_type: str
            """
            The error type for the failed execution.
            """

        class Pending(StripeObject):
            pass

        class Rejected(StripeObject):
            reason: Optional[str]
            """
            The reason provided when rejecting the request.
            """

        class Succeeded(StripeObject):
            class Result(StripeObject):
                id: str
                """
                The unique identifier of the executed object.
                """
                object: str
                """
                The object type of the executed resource.
                """

            result: Result
            """
            The result of the successful execution.
            """
            _inner_class_types = {"result": Result}

        approved: Optional[Approved]
        """
        Deprecated: use requires_execution status instead.
        """
        canceled: Optional[Canceled]
        """
        Deprecated: use canceled status instead.
        """
        execution_failed: Optional[ExecutionFailed]
        """
        Deprecated: use failed status instead.
        """
        execution_started: Optional[ExecutionStarted]
        """
        Deprecated: use requires_execution status instead.
        """
        execution_succeeded: Optional[ExecutionSucceeded]
        """
        Deprecated: use succeeded status instead.
        """
        expired: Optional[Expired]
        """
        Deprecated: use expired status instead.
        """
        failed: Optional[Failed]
        """
        Details when the approval request failed.
        """
        pending: Optional[Pending]
        """
        Deprecated: use requires_review status instead.
        """
        rejected: Optional[Rejected]
        """
        Deprecated: use rejected status instead.
        """
        succeeded: Optional[Succeeded]
        """
        Details when the approval request succeeded.
        """
        _inner_class_types = {
            "approved": Approved,
            "canceled": Canceled,
            "execution_failed": ExecutionFailed,
            "execution_started": ExecutionStarted,
            "execution_succeeded": ExecutionSucceeded,
            "expired": Expired,
            "failed": Failed,
            "pending": Pending,
            "rejected": Rejected,
            "succeeded": Succeeded,
        }

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Timestamp when the approval request was canceled.
        """
        expired_at: Optional[str]
        """
        Timestamp when the approval request expired.
        """
        failed_at: Optional[str]
        """
        Timestamp when the approval request failed.
        """
        rejected_at: Optional[str]
        """
        Timestamp when the approval request was rejected.
        """
        requires_execution_at: Optional[str]
        """
        Timestamp when the approval request moved to requires_execution status.
        """
        succeeded_at: Optional[str]
        """
        Timestamp when the approval request succeeded.
        """

    action: Literal[
        "charge.create",
        "dispute.close",
        "inbound_transfers.money_management.create",
        "invoice.create",
        "outbound_payments.money_management.create",
        "outbound_transfers.money_management.create",
        "payment_intent.create",
        "payment_intent.update",
        "payout.create",
        "price.update",
        "refund.create",
        "setup_intent.create",
        "subscription.create",
        "subscription.update",
        "topup.create",
        "transfer.create",
    ]
    """
    The action that was requested.
    """
    created: str
    """
    Time this ApprovalRequest was created.
    """
    dashboard_url: Optional[str]
    """
    The URL to the dashboard for this ApprovalRequest.
    """
    description: Optional[str]
    """
    A description of the approval request.
    """
    expires_at: str
    """
    The timestamp at which this ApprovalRequest will expire.
    """
    id: str
    """
    The unique identifier for this ApprovalRequest.
    """
    livemode: bool
    """
    Whether this ApprovalRequest is livemode.
    """
    object: Literal["v2.core.approval_request"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    requested_by: RequestedBy
    """
    The requester of this ApprovalRequest.
    """
    review: Optional[Review]
    """
    The review of this ApprovalRequest if it has been reviewed.
    """
    rule: Optional[Rule]
    """
    The rule associated with this ApprovalRequest.
    """
    status: Literal[
        "approved",
        "canceled",
        "execution_failed",
        "execution_started",
        "execution_succeeded",
        "expired",
        "failed",
        "pending",
        "rejected",
        "requires_execution",
        "requires_review",
        "succeeded",
    ]
    """
    The status of this ApprovalRequest.
    """
    status_details: Optional[StatusDetails]
    """
    The details of the status of this ApprovalRequest.
    """
    status_transitions: Optional[StatusTransitions]
    """
    The transitions of the status of this ApprovalRequest.
    """
    _inner_class_types = {
        "requested_by": RequestedBy,
        "review": Review,
        "rule": Rule,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
    }
