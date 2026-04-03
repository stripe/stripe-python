# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerEvaluationUpdateParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_failed: NotRequired["CustomerEvaluationUpdateParamsLoginFailed"]
    """
    Event payload for login_failed.
    """
    registration_failed: NotRequired[
        "CustomerEvaluationUpdateParamsRegistrationFailed"
    ]
    """
    Event payload for registration_failed.
    """
    registration_success: NotRequired[
        "CustomerEvaluationUpdateParamsRegistrationSuccess"
    ]
    """
    Event payload for registration_success.
    """
    type: Literal[
        "login_failed",
        "login_success",
        "registration_failed",
        "registration_success",
    ]
    """
    The type of event to report.
    """


class CustomerEvaluationUpdateParamsLoginFailed(TypedDict):
    reason: Literal["other", "suspected_account_sharing"]
    """
    The reason why this login failed.
    """


class CustomerEvaluationUpdateParamsRegistrationFailed(TypedDict):
    reason: Literal["other", "suspected_multi_accounting"]
    """
    The reason why this registration failed.
    """


class CustomerEvaluationUpdateParamsRegistrationSuccess(TypedDict):
    customer: NotRequired[str]
    """
    The ID of a Customer to attach to an entity-less registration evaluation.
    """
