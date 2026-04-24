# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountEvaluationModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_failed: NotRequired["AccountEvaluationModifyParamsLoginFailed"]
    """
    Event payload for login_failed.
    """
    login_succeeded: NotRequired["AccountEvaluationModifyParamsLoginSucceeded"]
    """
    Event payload for login_succeeded.
    """
    registration_failed: NotRequired[
        "AccountEvaluationModifyParamsRegistrationFailed"
    ]
    """
    Event payload for registration_failed.
    """
    registration_succeeded: NotRequired[
        "AccountEvaluationModifyParamsRegistrationSucceeded"
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


class AccountEvaluationModifyParamsLoginFailed(TypedDict):
    reason: Literal["other", "suspected_account_sharing"]
    """
    The reason why this login failed.
    """


class AccountEvaluationModifyParamsLoginSucceeded(TypedDict):
    qualification: NotRequired[Literal["suspected_account_sharing"]]
    """
    An optional qualification for a login success.
    """


class AccountEvaluationModifyParamsRegistrationFailed(TypedDict):
    reason: Literal["other", "suspected_multi_accounting"]
    """
    The reason why this registration failed.
    """


class AccountEvaluationModifyParamsRegistrationSucceeded(TypedDict):
    qualification: NotRequired[Literal["suspected_multi_accounting"]]
    """
    An optional qualification for a registration success.
    """
