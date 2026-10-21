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
        Union[
            Literal[
                "account_takeover",
                "fraudulent_website",
                "user_account_sharing",
                "user_merchant_fit",
                "user_multi_accounting",
            ],
            str,
        ]
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
    account_takeover_confirmation: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataAccountTakeoverConfirmation"
    ]
    """
    Required when type is account_takeover_confirmation. Requires an existing customer or account with a customer configuration.
    """
    account_takeover_report: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataAccountTakeoverReport"
    ]
    """
    Required when type is account_takeover_report. Requires an existing customer or account with a customer configuration.
    """
    credential_change: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataCredentialChange"
    ]
    """
    Required when type is credential_change. Requires an existing customer or account with a customer configuration.
    """
    login_attempt: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt"
    ]
    """
    Details for the login attempt. Provide only when type is login_attempt.
    """
    mfa_addition: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataMfaAddition"
    ]
    """
    Required when type is mfa_addition. Requires an existing customer or account with a customer configuration.
    """
    mfa_removal: NotRequired[
        "AccountEvaluationCreateParamsAccountActivityDetailsDataMfaRemoval"
    ]
    """
    Required when type is mfa_removal. Requires an existing customer or account with a customer configuration.
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
            "account_restricted",
            "account_reviewed",
            "account_suspended",
            "account_takeover_confirmation",
            "account_takeover_mitigation",
            "account_takeover_report",
            "credential_change",
            "login_attempt",
            "login_decision",
            "mfa_addition",
            "mfa_removal",
            "registration_attempt",
            "registration_decision",
        ],
        str,
    ]
    """
    The type of activity. Supports registration_attempt, login_attempt, mfa_addition, mfa_removal,
    credential_change, account_takeover_report, account_takeover_confirmation, or account_takeover_mitigation.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataAccountTakeoverConfirmation(
    TypedDict,
):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential involved in the confirmed takeover.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataAccountTakeoverReport(
    TypedDict,
):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential involved in the reported takeover.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataCredentialChange(
    TypedDict,
):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential that changed.
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


class AccountEvaluationCreateParamsAccountActivityDetailsDataMfaAddition(
    TypedDict,
):
    mfa_type: Union[
        Literal["authenticator_app", "email", "hardware_key", "other", "sms"],
        str,
    ]
    """
    The authentication method added to the account.
    """


class AccountEvaluationCreateParamsAccountActivityDetailsDataMfaRemoval(
    TypedDict,
):
    mfa_type: Union[
        Literal["authenticator_app", "email", "hardware_key", "other", "sms"],
        str,
    ]
    """
    The authentication method removed from the account.
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
    The v1 customer ID of the account, for users not yet migrated to v2 accounts.
    """
    data: NotRequired["AccountEvaluationCreateParamsAccountDetailsData"]
    """
    Inline account data to evaluate without creating a v2 account.
    """


class AccountEvaluationCreateParamsAccountDetailsData(TypedDict):
    contact_email: NotRequired[str]
    """
    The account's contact email.
    """
    defaults: NotRequired[
        "AccountEvaluationCreateParamsAccountDetailsDataDefaults"
    ]
    """
    Default account settings.
    """
    identity: NotRequired[
        "AccountEvaluationCreateParamsAccountDetailsDataIdentity"
    ]
    """
    Identity data.
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


class AccountEvaluationCreateParamsAccountDetailsDataIdentity(TypedDict):
    business_details: "AccountEvaluationCreateParamsAccountDetailsDataIdentityBusinessDetails"
    """
    Business details for identity data.
    """


class AccountEvaluationCreateParamsAccountDetailsDataIdentityBusinessDetails(
    TypedDict,
):
    registered_name: NotRequired[str]
    """
    Registered business name.
    """
