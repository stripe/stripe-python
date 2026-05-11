# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerEvaluationModifyParams(RequestOptions):
    customer: NotRequired[str]
    """
    The ID of a Customer to attach to an entity-less registration evaluation.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_failed: NotRequired["CustomerEvaluationModifyParamsLoginFailed"]
    """
    Data for a failed login event.
    """
    registration_failed: NotRequired[
        "CustomerEvaluationModifyParamsRegistrationFailed"
    ]
    """
    Data for a failed registration event.
    """
    registration_success: NotRequired[
        "CustomerEvaluationModifyParamsRegistrationSuccess"
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


class CustomerEvaluationModifyParamsLoginFailed(TypedDict):
    reason: Literal["other", "suspected_account_sharing"]
    """
    The reason why this login failed.
    """


class CustomerEvaluationModifyParamsRegistrationFailed(TypedDict):
    reason: Literal["other", "suspected_multi_accounting"]
    """
    The reason why this registration failed.
    """


class CustomerEvaluationModifyParamsRegistrationSuccess(TypedDict):
    customer: NotRequired[str]
    """
    The ID of a Customer to attach to an entity-less registration evaluation.
    """
