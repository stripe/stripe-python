# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountActivityCreateParams(TypedDict):
    account_details: NotRequired["AccountActivityCreateParamsAccountDetails"]
    """
    The account, customer, or inline account data associated with the activity.
    """
    account_evaluation: NotRequired[str]
    """
    The account evaluation this activity is associated with, when applicable.
    """
    account_restricted: NotRequired[
        "AccountActivityCreateParamsAccountRestricted"
    ]
    """
    Details for the account restriction. Provide only when type is account_restricted. The activity
    requires an existing account_details.account or account_details.customer; inline data is unsupported.
    """
    account_reviewed: NotRequired["AccountActivityCreateParamsAccountReviewed"]
    """
    Details for the account review. Provide only when type is account_reviewed. The activity
    requires an existing account_details.account or account_details.customer; inline data is unsupported.
    """
    account_suspended: NotRequired[
        "AccountActivityCreateParamsAccountSuspended"
    ]
    """
    Details for the account suspension. Provide only when type is account_suspended. The activity
    requires an existing account_details.customer; account_details.account and inline data are unsupported.
    """
    account_takeover_confirmation: NotRequired[
        "AccountActivityCreateParamsAccountTakeoverConfirmation"
    ]
    """
    Required when type is account_takeover_confirmation. Requires an existing customer or account with a customer configuration.
    """
    account_takeover_report: NotRequired[
        "AccountActivityCreateParamsAccountTakeoverReport"
    ]
    """
    Required when type is account_takeover_report. Requires an existing customer or account with a customer configuration.
    """
    credential_change: NotRequired[
        "AccountActivityCreateParamsCredentialChange"
    ]
    """
    Required when type is credential_change. Requires an existing customer or account with a customer configuration.
    """
    login_attempt: NotRequired["AccountActivityCreateParamsLoginAttempt"]
    """
    Details for the login attempt. Provide only when type is login_attempt.
    """
    login_decision: NotRequired["AccountActivityCreateParamsLoginDecision"]
    """
    Details for the login decision. Provide only when type is login_decision.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Additional information about the activity.
    """
    mfa_addition: NotRequired["AccountActivityCreateParamsMfaAddition"]
    """
    Required when type is mfa_addition. Requires an existing customer or account with a customer configuration.
    """
    mfa_removal: NotRequired["AccountActivityCreateParamsMfaRemoval"]
    """
    Required when type is mfa_removal. Requires an existing customer or account with a customer configuration.
    """
    occurred_at: NotRequired[str]
    """
    Timestamp at which the activity occurred. Defaults to the created time if not provided.
    """
    registration_attempt: NotRequired[
        "AccountActivityCreateParamsRegistrationAttempt"
    ]
    """
    Details for the registration attempt. Provide only when type is registration_attempt.
    """
    registration_decision: NotRequired[
        "AccountActivityCreateParamsRegistrationDecision"
    ]
    """
    Details for the registration decision. Provide only when type is registration_decision.
    """
    triggering_signal: NotRequired[str]
    """
    An accessible AccountSignal that prompted this activity. The signal must be within its
    90-day retrieval window and match the existing account or customer in account_details.
    Inline data is unsupported. May be supplied together with account_evaluation.
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
    The type of activity.
    """


class AccountActivityCreateParamsAccountDetails(TypedDict):
    account: NotRequired[str]
    """
    The v2 account ID of the account.
    """
    customer: NotRequired[str]
    """
    The v1 customer ID of the account, for users not yet migrated to v2 accounts.
    """
    data: NotRequired["AccountActivityCreateParamsAccountDetailsData"]
    """
    Inline account data to evaluate without creating a v2 account.
    """


class AccountActivityCreateParamsAccountDetailsData(TypedDict):
    contact_email: NotRequired[str]
    """
    The account's contact email.
    """
    defaults: NotRequired[
        "AccountActivityCreateParamsAccountDetailsDataDefaults"
    ]
    """
    Default account settings.
    """
    identity: NotRequired[
        "AccountActivityCreateParamsAccountDetailsDataIdentity"
    ]
    """
    Identity data.
    """


class AccountActivityCreateParamsAccountDetailsDataDefaults(TypedDict):
    profile: "AccountActivityCreateParamsAccountDetailsDataDefaultsProfile"
    """
    Account profile data.
    """


class AccountActivityCreateParamsAccountDetailsDataDefaultsProfile(TypedDict):
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


class AccountActivityCreateParamsAccountDetailsDataIdentity(TypedDict):
    business_details: (
        "AccountActivityCreateParamsAccountDetailsDataIdentityBusinessDetails"
    )
    """
    Business details for identity data.
    """


class AccountActivityCreateParamsAccountDetailsDataIdentityBusinessDetails(
    TypedDict,
):
    registered_name: NotRequired[str]
    """
    Registered business name.
    """


class AccountActivityCreateParamsAccountRestricted(TypedDict):
    reason: Union[Literal["abuse", "other"], str]
    """
    The reason the account or customer was restricted.
    """


class AccountActivityCreateParamsAccountReviewed(TypedDict):
    outcome: Union[Literal["trusted"], str]
    """
    The outcome of the merchant review.
    """


class AccountActivityCreateParamsAccountSuspended(TypedDict):
    reason: Union[Literal["abuse", "other"], str]
    """
    The reason the customer was suspended.
    """


class AccountActivityCreateParamsAccountTakeoverConfirmation(TypedDict):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential involved in the confirmed takeover.
    """


class AccountActivityCreateParamsAccountTakeoverReport(TypedDict):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential involved in the reported takeover.
    """


class AccountActivityCreateParamsCredentialChange(TypedDict):
    credential_type: Union[Literal["api_key", "login_password", "other"], str]
    """
    The type of credential that changed.
    """


class AccountActivityCreateParamsLoginAttempt(TypedDict):
    client_details: "AccountActivityCreateParamsLoginAttemptClientDetails"
    """
    Client details captured for the attempt.
    """


class AccountActivityCreateParamsLoginAttemptClientDetails(TypedDict):
    data: NotRequired[
        "AccountActivityCreateParamsLoginAttemptClientDetailsData"
    ]
    """
    Raw client details for the activity, when a Radar session is not available.
    """
    radar_session: NotRequired[str]
    """
    The Radar session ID capturing client details for the activity.
    """


class AccountActivityCreateParamsLoginAttemptClientDetailsData(TypedDict):
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


class AccountActivityCreateParamsLoginDecision(TypedDict):
    mfa_challenges: NotRequired[
        List["AccountActivityCreateParamsLoginDecisionMfaChallenge"]
    ]
    """
    Multi-factor authentication challenges performed during the login process.
    """
    status: Literal["allowed", "blocked", "restricted"]
    """
    The action the merchant took following the evaluation.
    """


class AccountActivityCreateParamsLoginDecisionMfaChallenge(TypedDict):
    mfa_type: Union[
        Literal["authenticator_app", "email", "hardware_key", "other", "sms"],
        str,
    ]
    """
    The authentication method used for the challenge.
    """
    status: Union[Literal["failed", "other", "succeeded"], str]
    """
    The outcome of the authentication challenge.
    """


class AccountActivityCreateParamsMfaAddition(TypedDict):
    mfa_type: Union[
        Literal["authenticator_app", "email", "hardware_key", "other", "sms"],
        str,
    ]
    """
    The authentication method added to the account.
    """


class AccountActivityCreateParamsMfaRemoval(TypedDict):
    mfa_type: Union[
        Literal["authenticator_app", "email", "hardware_key", "other", "sms"],
        str,
    ]
    """
    The authentication method removed from the account.
    """


class AccountActivityCreateParamsRegistrationAttempt(TypedDict):
    client_details: (
        "AccountActivityCreateParamsRegistrationAttemptClientDetails"
    )
    """
    Client details captured for the attempt.
    """


class AccountActivityCreateParamsRegistrationAttemptClientDetails(TypedDict):
    data: NotRequired[
        "AccountActivityCreateParamsRegistrationAttemptClientDetailsData"
    ]
    """
    Raw client details for the activity, when a Radar session is not available.
    """
    radar_session: NotRequired[str]
    """
    The Radar session ID capturing client details for the activity.
    """


class AccountActivityCreateParamsRegistrationAttemptClientDetailsData(
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


class AccountActivityCreateParamsRegistrationDecision(TypedDict):
    status: Literal["allowed", "blocked", "restricted"]
    """
    The action the merchant took following the evaluation.
    """
