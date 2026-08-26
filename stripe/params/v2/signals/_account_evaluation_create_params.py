# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountEvaluationCreateParams(TypedDict):
    account_activity_details: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetails"
    ]
    """
    Account activity to record alongside this evaluation.
    """
    account_details: "AccountEvaluationCreateParamsAccountDetails"
    """
    The account, customer, or inline account data to evaluate.
    """
    requested_signals: List[
        Union[Literal["user_account_sharing", "user_multi_accounting"], str]
    ]
    """
    List of signals to evaluate.
    """


class AccountEvaluationCreateParamsAccountActivityDetails(TypedDict):
    account_activity: NotRequired[str]
    """
    The ID of an existing account activity to associate with the evaluation.
    """
    data: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsData"
    ]
    """
    Inline activity data used to create a new account activity for the evaluation.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsData(TypedDict):
    login_attempt: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt"
    ]
    """
    Details for the login attempt. Provide only when type is login_attempt.
    """
    occurred_at: NotRequired[str]
    """
    Timestamp at which the activity occurred. Defaults to the created time if not provided.
    """
    registration_attempt: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttempt"
    ]
    """
    Details for the registration attempt. Provide only when type is registration_attempt.
    """
    type: Union[
        Literal[
            "login_attempt",
            "login_decision",
            "registration_attempt",
            "registration_decision",
        ],
        str,
    ]
    """
    The type of activity. Must be registration_attempt or login_attempt.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt(
    TypedDict,
):
    client_details: "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetails"
    """
    Client details captured for the attempt.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetails(
    TypedDict,
):
    data: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetailsData"
    ]
    """
    Raw client details for the activity, when a Radar session is not available.
    """
    radar_session: NotRequired[str]
    """
    The Radar session ID capturing client details for the activity.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetailsData(
    TypedDict,
):
    ip: str
    """
    The IP address associated with the activity.
    """
    referrer: NotRequired[str]
    """
    The referrer associated with the activity.
    """
    user_agent: NotRequired[str]
    """
    The user agent associated with the activity.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttempt(
    TypedDict,
):
    client_details: "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetails"
    """
    Client details captured for the attempt.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetails(
    TypedDict,
):
    data: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetailsData"
    ]
    """
    Raw client details for the activity, when a Radar session is not available.
    """
    radar_session: NotRequired[str]
    """
    The Radar session ID capturing client details for the activity.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetailsData(
    TypedDict,
):
    ip: str
    """
    The IP address associated with the activity.
    """
    referrer: NotRequired[str]
    """
    The referrer associated with the activity.
    """
    user_agent: NotRequired[str]
    """
    The user agent associated with the activity.
    """


class AccountEvaluationCreateParamsAccountDetails(TypedDict):
    account: NotRequired[str]
    """
    The v2 account ID of the account.
    """
    customer: NotRequired[str]
    """
    The v1 customer ID of the account, for users not yet migrated to v2/accounts.
    """
    data: NotRequired["AccountEvaluationCreateParamsAccountDetailsData"]
    """
    Inline account data to evaluate without creating a v2 account.
    """


class AccountEvaluationCreateParamsAccountDetailsData(TypedDict):
    defaults: NotRequired[
        "AccountEvaluationCreateParamsAccountDetailsDataDefaults"
    ]
    """
    Default account settings.
    """


class AccountEvaluationCreateParamsAccountDetailsDataDefaults(TypedDict):
    profile: "AccountEvaluationCreateParamsAccountDetailsDataDefaultsProfile"
    """
    Account profile data.
    """


class AccountEvaluationCreateParamsAccountDetailsDataDefaultsProfile(
    TypedDict
):
    business_url: str
    """
    The business URL.
    """
    doing_business_as: NotRequired[str]
    """
    Doing business as (DBA) name.
    """
    product_description: NotRequired[str]
    """
    Description of the account's product or service.
    """
