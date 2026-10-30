# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TypedDict


class RewardProgramEnrollmentCreateParams(TypedDict):
    account: str
    """
    The connected account to enroll into this RewardProgram.
    """
    card_spend: "RewardProgramEnrollmentCreateParamsCardSpend"
    """
    Issuing-specific per-enrollment configuration.
    """
    reward_program: str
    """
    The RewardProgram to enroll into.
    """


class RewardProgramEnrollmentCreateParamsCardSpend(TypedDict):
    issuer_program: str
    """
    The Issuer Program for this connected account. Immutable after creation.
    """
