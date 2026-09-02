# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, Union
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
    account_suspended: NotRequired[
        "AccountActivityCreateParamsAccountSuspended"
    ]
    """
    Details for the account suspension. Provide only when type is account_suspended. The activity
    requires an existing account_details.customer; account_details.account and inline data are unsupported.
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
    type: Union[
        Literal[
            "account_restricted",
            "account_suspended",
            "login_attempt",
            "login_decision",
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
    The v1 customer ID of the account, for users not yet migrated to v2/accounts.
    """
    data: NotRequired["AccountActivityCreateParamsAccountDetailsData"]
    """
    Inline account data to evaluate without creating a v2 account.
    """


class AccountActivityCreateParamsAccountDetailsData(TypedDict):
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


class AccountActivityCreateParamsAccountSuspended(TypedDict):
    reason: Union[Literal["abuse", "other"], str]
    """
    The reason the customer was suspended.
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
    status: Literal["allowed", "blocked", "restricted"]
    """
    The action the merchant took following the evaluation.
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
