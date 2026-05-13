# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerEvaluationUpdateParams(TypedDict):
    customer: NotRequired[str]
    """
    The ID of a Customer to attach to an entity-less registration evaluation.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_failed: NotRequired["CustomerEvaluationUpdateParamsLoginFailed"]
    """
    Data for a failed login event.
    """
    registration_failed: NotRequired[
        "CustomerEvaluationUpdateParamsRegistrationFailed"
    ]
    """
    Data for a failed registration event.
    """
    registration_success: NotRequired[
        "CustomerEvaluationUpdateParamsRegistrationSuccess"
    ]
    """
    Data for a successful registration event.
    """
    status: NotRequired[Literal["allowed", "blocked", "restricted"]]
    """
    The outcome status of the evaluation: allowed, restricted, or blocked.
    """
    type: NotRequired[
        Literal[
            "login_failed",
            "login_success",
            "registration_failed",
            "registration_success",
        ]
    ]
    """
    The type of event to report on the customer evaluation.
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
