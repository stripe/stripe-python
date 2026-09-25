# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class EarnedCredit(StripeObject):
    """
    The EarnedCredit object.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.earned_credit"]] = (
        "v2.money_management.earned_credit"
    )

    class Period(StripeObject):
        end_date: str
        """
        The end date of the period during which the credit was earned, inclusive.
        """
        start_date: str
        """
        The start date of the period during which the credit was earned, inclusive.
        """

    class RevenueShare(StripeObject):
        type: Union[
            Literal["administrative_facilitation_fee", "savings_referral"], str
        ]
        """
        The type of revenue share that caused the EarnedCredit.
        """

    class Reward(StripeObject):
        earned_from: Union[Literal["platform_cash_rewards"], str]
        """
        The program from which the reward was earned.
        """
        from_account: str
        """
        The Account that funded the reward.
        """
        outbound_payment: str
        """
        The OutboundPayment that delivered the reward.
        """

    class StatusTransitions(StripeObject):
        succeeded_at: Optional[str]
        """
        The time at which the EarnedCredit succeeded.
        """

    amount: Amount
    """
    The amount and currency of the EarnedCredit.
    """
    created: str
    """
    Time at which the EarnedCredit was created.
    """
    description: str
    """
    Description of the EarnedCredit.
    """
    financial_account: str
    """
    The FinancialAccount that earned the credit.
    """
    id: str
    """
    Unique identifier for the EarnedCredit.
    """
    livemode: bool
    """
    Has the value true if the object exists in live mode.
    """
    object: Literal["v2.money_management.earned_credit"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    period: Optional[Period]
    """
    The period during which the credit was earned.
    """
    revenue_share: Optional[RevenueShare]
    """
    Details about the revenue share that caused the EarnedCredit.
    """
    reward: Optional[Reward]
    """
    Details about the reward that caused the EarnedCredit.
    """
    status: Union[Literal["succeeded"], str]
    """
    The status of the EarnedCredit.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for EarnedCredit status transitions.
    """
    type: Union[Literal["interest", "revenue_share", "reward"], str]
    """
    The type of flow that caused the EarnedCredit.
    """
    _inner_class_types = {
        "period": Period,
        "revenue_share": RevenueShare,
        "reward": Reward,
        "status_transitions": StatusTransitions,
    }
