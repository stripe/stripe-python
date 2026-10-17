# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class AccountActivity(StripeObject):
    """
    Account Activity resource for the Signals API.
    """

    OBJECT_NAME: ClassVar[Literal["v2.signals.account_activity"]] = (
        "v2.signals.account_activity"
    )

    class AccountDetails(StripeObject):
        class Data(StripeObject):
            class Defaults(StripeObject):
                class Profile(StripeObject):
                    business_url: str
                    """
                    The business URL.
                    """
                    doing_business_as: Optional[str]
                    """
                    Doing business as (DBA) name.
                    """
                    product_description: Optional[str]
                    """
                    Description of the account's product or service.
                    """

                profile: Profile
                """
                Account profile data.
                """
                _inner_class_types = {"profile": Profile}

            class Identity(StripeObject):
                class BusinessDetails(StripeObject):
                    registered_name: Optional[str]
                    """
                    Registered business name.
                    """

                business_details: BusinessDetails
                """
                Business details for identity data.
                """
                _inner_class_types = {"business_details": BusinessDetails}

            contact_email: Optional[str]
            """
            The account's contact email.
            """
            defaults: Optional[Defaults]
            """
            Default account settings.
            """
            identity: Optional[Identity]
            """
            Identity data.
            """
            _inner_class_types = {"defaults": Defaults, "identity": Identity}

        account: Optional[str]
        """
        The v2 account ID of the account.
        """
        customer: Optional[str]
        """
        The v1 customer ID of the account, for users not yet migrated to v2 accounts.
        """
        data: Optional[Data]
        """
        Inline account data to evaluate without creating a v2 account.
        """
        _inner_class_types = {"data": Data}

    class AccountRestricted(StripeObject):
        reason: Union[Literal["abuse", "other"], str]
        """
        The reason the account or customer was restricted.
        """

    class AccountReviewed(StripeObject):
        outcome: Union[Literal["trusted"], str]
        """
        The outcome of the merchant review.
        """

    class AccountSuspended(StripeObject):
        reason: Union[Literal["abuse", "other"], str]
        """
        The reason the customer was suspended.
        """

    class AccountTakeoverConfirmation(StripeObject):
        credential_type: Union[
            Literal["api_key", "login_password", "other"], str
        ]
        """
        The type of credential involved in the confirmed takeover.
        """

    class AccountTakeoverReport(StripeObject):
        credential_type: Union[
            Literal["api_key", "login_password", "other"], str
        ]
        """
        The type of credential involved in the reported takeover.
        """

    class CredentialChange(StripeObject):
        credential_type: Union[
            Literal["api_key", "login_password", "other"], str
        ]
        """
        The type of credential that changed.
        """

    class LoginAttempt(StripeObject):
        class ClientDetails(StripeObject):
            class Data(StripeObject):
                ip: str
                """
                The IP address associated with the activity.
                """
                referrer: Optional[str]
                """
                The referrer associated with the activity.
                """
                user_agent: Optional[str]
                """
                The user agent associated with the activity.
                """

            data: Optional[Data]
            """
            Raw client details for the activity, when a Radar session is not available.
            """
            radar_session: Optional[str]
            """
            The Radar session ID capturing client details for the activity.
            """
            _inner_class_types = {"data": Data}

        client_details: ClientDetails
        """
        Client details captured for the attempt.
        """
        _inner_class_types = {"client_details": ClientDetails}

    class LoginDecision(StripeObject):
        status: Literal["allowed", "blocked", "restricted"]
        """
        The action the merchant took following the evaluation.
        """

    class MfaAddition(StripeObject):
        mfa_type: Union[
            Literal[
                "authenticator_app", "email", "hardware_key", "other", "sms"
            ],
            str,
        ]
        """
        The authentication method added to the account.
        """

    class MfaRemoval(StripeObject):
        mfa_type: Union[
            Literal[
                "authenticator_app", "email", "hardware_key", "other", "sms"
            ],
            str,
        ]
        """
        The authentication method removed from the account.
        """

    class RegistrationAttempt(StripeObject):
        class ClientDetails(StripeObject):
            class Data(StripeObject):
                ip: str
                """
                The IP address associated with the activity.
                """
                referrer: Optional[str]
                """
                The referrer associated with the activity.
                """
                user_agent: Optional[str]
                """
                The user agent associated with the activity.
                """

            data: Optional[Data]
            """
            Raw client details for the activity, when a Radar session is not available.
            """
            radar_session: Optional[str]
            """
            The Radar session ID capturing client details for the activity.
            """
            _inner_class_types = {"data": Data}

        client_details: ClientDetails
        """
        Client details captured for the attempt.
        """
        _inner_class_types = {"client_details": ClientDetails}

    class RegistrationDecision(StripeObject):
        status: Literal["allowed", "blocked", "restricted"]
        """
        The action the merchant took following the evaluation.
        """

    account_details: Optional[AccountDetails]
    """
    The account, customer, or inline account data associated with the activity.
    """
    account_evaluation: Optional[str]
    """
    The account evaluation this activity is associated with, when applicable.
    """
    account_restricted: Optional[AccountRestricted]
    """
    Details for the account restriction. Present only when type is account_restricted. The activity
    requires an existing account_details.account or account_details.customer; inline data is unsupported.
    """
    account_reviewed: Optional[AccountReviewed]
    """
    Details for the account review. Present only when type is account_reviewed. The activity
    requires an existing account_details.account or account_details.customer; inline data is unsupported.
    """
    account_suspended: Optional[AccountSuspended]
    """
    Details for the account suspension. Present only when type is account_suspended. The activity
    requires an existing account_details.customer; account_details.account and inline data are unsupported.
    """
    account_takeover_confirmation: Optional[AccountTakeoverConfirmation]
    """
    Details for the merchant's takeover confirmation. Present only when type is account_takeover_confirmation.
    """
    account_takeover_report: Optional[AccountTakeoverReport]
    """
    Details for the account holder's takeover report. Present only when type is account_takeover_report.
    """
    created: str
    """
    Timestamp at which the account activity was created.
    """
    credential_change: Optional[CredentialChange]
    """
    Details for the credential change. Present only when type is credential_change.
    """
    id: str
    """
    Unique identifier for the account activity.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    login_attempt: Optional[LoginAttempt]
    """
    Details for the login attempt. Present only when type is login_attempt.
    """
    login_decision: Optional[LoginDecision]
    """
    Details for the login decision. Present only when type is login_decision.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Additional information about the activity.
    """
    mfa_addition: Optional[MfaAddition]
    """
    Details for the MFA addition. Present only when type is mfa_addition.
    """
    mfa_removal: Optional[MfaRemoval]
    """
    Details for the MFA removal. Present only when type is mfa_removal.
    """
    object: Literal["v2.signals.account_activity"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    occurred_at: str
    """
    Timestamp at which the activity occurred. Defaults to the created time if not provided.
    """
    registration_attempt: Optional[RegistrationAttempt]
    """
    Details for the registration attempt. Present only when type is registration_attempt.
    """
    registration_decision: Optional[RegistrationDecision]
    """
    Details for the registration decision. Present only when type is registration_decision.
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
    _inner_class_types = {
        "account_details": AccountDetails,
        "account_restricted": AccountRestricted,
        "account_reviewed": AccountReviewed,
        "account_suspended": AccountSuspended,
        "account_takeover_confirmation": AccountTakeoverConfirmation,
        "account_takeover_report": AccountTakeoverReport,
        "credential_change": CredentialChange,
        "login_attempt": LoginAttempt,
        "login_decision": LoginDecision,
        "mfa_addition": MfaAddition,
        "mfa_removal": MfaRemoval,
        "registration_attempt": RegistrationAttempt,
        "registration_decision": RegistrationDecision,
    }
