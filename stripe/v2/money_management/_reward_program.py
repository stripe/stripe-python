# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Union
from typing_extensions import Literal


class RewardProgram(StripeObject):
    """
    A RewardProgram represents shared card-spend cashback reward configuration for Issuing Card-Spend
    Rewards. It is not scoped to a single Issuer Program or connected account.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.reward_program"]] = (
        "v2.money_management.reward_program"
    )
    created: str
    """
    Time at which the RewardProgram was created.
    """
    fulfilled_by: Union[Literal["application"], str]
    """
    Determines who performs reward money movement after rule evaluation. Immutable after creation.
    """
    id: str
    """
    Unique identifier for the RewardProgram.
    """
    livemode: bool
    """
    Whether this object exists in livemode or testmode.
    """
    name: str
    """
    Display name for the RewardProgram.
    """
    object: Literal["v2.money_management.reward_program"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[Literal["active", "inactive"], str]
    """
    The status of the RewardProgram. Inactive by default on creation; use activate/deactivate to change.
    """
