# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountEvaluationUpdateParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_failed: NotRequired["AccountEvaluationUpdateParamsLoginFailed"]
    """
    Event payload for login_failed.
    """
    registration_failed: NotRequired[
        "AccountEvaluationUpdateParamsRegistrationFailed"
    ]
    """
    Event payload for registration_failed.
    """
    type: Literal[
        "login_failed",
        "login_succeeded",
        "registration_failed",
        "registration_succeeded",
    ]
    """
    The type of event to report.
    """


class AccountEvaluationUpdateParamsLoginFailed(TypedDict):
    reason: Literal["other", "suspected_account_sharing"]
    """
    The reason why this login failed.
    """


class AccountEvaluationUpdateParamsRegistrationFailed(TypedDict):
    reason: Literal["other", "suspected_multi_accounting"]
    """
    The reason why this registration failed.
    """
