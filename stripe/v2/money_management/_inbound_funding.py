# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class InboundFunding(StripeObject):
    """
    An InboundFunding represents an other-to-me pull movement into a FinancialAccount.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.inbound_funding"]] = (
        "v2.money_management.inbound_funding"
    )

    class From(StripeObject):
        class PaymentMethod(StripeObject):
            type: str
            """
            The type of this object.
            """
            us_paper_check: Optional[str]
            """
            The ID of the paper check.
            """

        debited: Amount
        """
        The amount debited from the source.
        """
        payment_method: PaymentMethod
        """
        The payment method that funds the InboundFunding.
        """
        _inner_class_types = {"payment_method": PaymentMethod}

    class History(StripeObject):
        class CheckFailed(StripeObject):
            failure_code: Optional[str]
            """
            The raw banking-partner failure code, when available.
            """
            failure_reason: Optional[str]
            """
            The reason the check failed.
            """

        class CheckProcessing(StripeObject):
            pass

        class CheckQueued(StripeObject):
            pass

        class CheckReturned(StripeObject):
            return_code: Optional[str]
            """
            The raw banking-partner return code, when available.
            """
            return_reason: Optional[str]
            """
            The reason the check was returned.
            """
            reversal_transaction: Optional[str]
            """
            The ID of the reversal Transaction.
            """

        class CheckSucceeded(StripeObject):
            pass

        check_failed: Optional[CheckFailed]
        """
        Details of the transition to failed.
        """
        check_processing: Optional[CheckProcessing]
        """
        Details of the transition to processing.
        """
        check_queued: Optional[CheckQueued]
        """
        Details of the transition to queued.
        """
        check_returned: Optional[CheckReturned]
        """
        Details of the transition to returned.
        """
        check_succeeded: Optional[CheckSucceeded]
        """
        Details of the transition to succeeded.
        """
        created: str
        """
        Time at which the object was created.
        """
        effective_at: str
        """
        Time at which the history entry took effect.
        """
        id: str
        """
        Unique identifier for the object.
        """
        type: Union[
            Literal[
                "check_failed",
                "check_processing",
                "check_queued",
                "check_returned",
                "check_succeeded",
            ],
            str,
        ]
        """
        The type of this object.
        """
        _inner_class_types = {
            "check_failed": CheckFailed,
            "check_processing": CheckProcessing,
            "check_queued": CheckQueued,
            "check_returned": CheckReturned,
            "check_succeeded": CheckSucceeded,
        }

    class To(StripeObject):
        credited: Amount
        """
        The amount credited to the destination.
        """
        financial_account: str
        """
        The ID of the destination FinancialAccount.
        """

    amount: Amount
    """
    The amount of the InboundFunding.
    """
    created: str
    """
    Time at which the object was created.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the InboundFunding.
    """
    from_: From
    """
    The source of the funds.
    """
    history: List[History]
    """
    The check lifecycle history.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Whether the InboundFunding exists in live mode.
    """
    object: Literal["v2.money_management.inbound_funding"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[
        Literal["failed", "processing", "queued", "returned", "succeeded"], str
    ]
    """
    The current status of the InboundFunding.
    """
    to: To
    """
    The destination for the funds.
    """
    _inner_class_types = {"from": From, "history": History, "to": To}
    _field_remappings = {"from_": "from"}
