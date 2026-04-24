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
    login_succeeded: NotRequired["AccountEvaluationUpdateParamsLoginSucceeded"]
    """
    Event payload for login_succeeded.
    """
    registration_failed: NotRequired[
        "AccountEvaluationUpdateParamsRegistrationFailed"
    ]
    """
    Event payload for registration_failed.
    """
    registration_succeeded: NotRequired[
        "AccountEvaluationUpdateParamsRegistrationSucceeded"
    ]
    """
    Event payload for registration_succeeded.
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


class AccountEvaluationUpdateParamsLoginSucceeded(TypedDict):
    qualification: NotRequired[Literal["suspected_account_sharing"]]
    """
    An optional qualification for a login success.
    """


class AccountEvaluationUpdateParamsRegistrationFailed(TypedDict):
    reason: Literal["other", "suspected_multi_accounting"]
    """
    The reason why this registration failed.
    """


class AccountEvaluationUpdateParamsRegistrationSucceeded(TypedDict):
    qualification: NotRequired[Literal["suspected_multi_accounting"]]
    """
    An optional qualification for a registration success.
    """
