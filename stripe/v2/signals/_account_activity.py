# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
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

            defaults: Optional[Defaults]
            """
            Default account settings.
            """
            _inner_class_types = {"defaults": Defaults}

        account: Optional[str]
        """
        The v2 account ID of the account.
        """
        customer: Optional[str]
        """
        The v1 customer ID of the account, for users not yet migrated to v2/accounts.
        """
        data: Optional[Data]
        """
        Inline account data to evaluate without creating a v2 account.
        """
        _inner_class_types = {"data": Data}

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
    created: str
    """
    Timestamp at which the account activity was created.
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
    _inner_class_types = {
        "account_details": AccountDetails,
        "login_attempt": LoginAttempt,
        "login_decision": LoginDecision,
        "registration_attempt": RegistrationAttempt,
        "registration_decision": RegistrationDecision,
    }
