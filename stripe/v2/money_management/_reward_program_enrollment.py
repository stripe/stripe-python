# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Union
from typing_extensions import Literal


class RewardProgramEnrollment(StripeObject):
    """
    A RewardProgramEnrollment represents the binding of a connected account / Issuer Program to a shared
    RewardProgram. RewardProgramEnrollments are platform-owned canonical objects and are active by default
    on creation. At most one RewardProgramEnrollment may be active per Issuer Program globally, across all
    RewardPrograms.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.reward_program_enrollment"]
    ] = "v2.money_management.reward_program_enrollment"

    class CardSpend(StripeObject):
        issuer_program: str
        """
        The Issuer Program for this connected account. Immutable after creation.
        """

    account: str
    """
    The connected account enrolled in this RewardProgram. Immutable after creation.
    """
    card_spend: CardSpend
    """
    Issuing-specific per-enrollment configuration. Immutable after creation.
    """
    created: str
    """
    Time at which the RewardProgramEnrollment was created.
    """
    id: str
    """
    Unique identifier for the RewardProgramEnrollment.
    """
    livemode: bool
    """
    Whether this object exists in livemode or testmode.
    """
    object: Literal["v2.money_management.reward_program_enrollment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reward_program: str
    """
    The ID of the RewardProgram this enrollment belongs to. Immutable after creation.
    """
    status: Union[Literal["active", "inactive"], str]
    """
    The status of the RewardProgramEnrollment. Active by default on creation; use activate/deactivate to
    change.
    """
    _inner_class_types = {"card_spend": CardSpend}
