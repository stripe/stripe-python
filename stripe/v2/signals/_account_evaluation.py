# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class AccountEvaluation(StripeObject):
    """
    Account Evaluation resource for the Signals API.
    """

    OBJECT_NAME: ClassVar[Literal["v2.signals.account_evaluation"]] = (
        "v2.signals.account_evaluation"
    )

    class AccountActivityDetails(StripeObject):
        account_activity: Optional[str]
        """
        The ID of the account activity created or associated with the evaluation.
        """

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
        The v1 customer ID of the account, for users not yet migrated to v2/accounts.
        """
        data: Optional[Data]
        """
        Inline account data to evaluate without creating a v2 account.
        """
        _inner_class_types = {"data": Data}

    class EvaluatedSignals(StripeObject):
        class FraudulentWebsite(StripeObject):
            details: Optional[str]
            """
            Human-readable details about the fraudulent website evaluation, when available.
            """
            evaluated_at: Optional[str]
            """
            Timestamp at which the signal was evaluated.
            """
            risk_level: Literal[
                "elevated", "highest", "low", "normal", "unknown"
            ]
            """
            Categorical assessment of the fraudulent website risk.
            """
            signal: Optional[str]
            """
            The account signal ID containing the full fraudulent website signal result.
            """

        class UserAccountSharing(StripeObject):
            evaluated_at: Optional[str]
            """
            Timestamp at which the signal was evaluated.
            """
            risk_level: Literal[
                "elevated", "highest", "low", "normal", "unknown"
            ]
            """
            Categorical assessment of the account-sharing risk.
            """
            score: Optional[Decimal]
            """
            The specific risk score for the account, between 0.00 and 100.00, when available.
            """
            signal: Optional[str]
            """
            The account signal ID containing the full user account-sharing signal result.
            """
            _field_encodings = {"score": "decimal_string"}

        class UserMultiAccounting(StripeObject):
            evaluated_at: Optional[str]
            """
            Timestamp at which the signal was evaluated.
            """
            risk_level: Literal[
                "elevated", "highest", "low", "normal", "unknown"
            ]
            """
            Categorical assessment of the multi-accounting risk.
            """
            score: Optional[Decimal]
            """
            The specific risk score for the account, between 0.00 and 100.00, when available.
            """
            signal: Optional[str]
            """
            The account signal ID containing the full user multi-accounting signal result.
            """
            _field_encodings = {"score": "decimal_string"}

        fraudulent_website: Optional[FraudulentWebsite]
        """
        Fraudulent website result for the evaluation, when available.
        """
        user_account_sharing: Optional[UserAccountSharing]
        """
        User account-sharing result for the evaluation, when available.
        """
        user_multi_accounting: Optional[UserMultiAccounting]
        """
        User multi-accounting result for the evaluation, when available.
        """
        _inner_class_types = {
            "fraudulent_website": FraudulentWebsite,
            "user_account_sharing": UserAccountSharing,
            "user_multi_accounting": UserMultiAccounting,
        }

    account_activity_details: Optional[AccountActivityDetails]
    """
    Account activity recorded alongside this evaluation, when applicable.
    """
    account_details: AccountDetails
    """
    The account, customer, or inline account data being evaluated.
    """
    created: str
    """
    Timestamp at which the evaluation was created.
    """
    evaluated_signals: Optional[EvaluatedSignals]
    """
    Signal results that are available for the evaluation.
    """
    id: str
    """
    Unique identifier for the account evaluation.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.signals.account_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pending_signals: List[
        Union[
            Literal[
                "fraudulent_website",
                "user_account_sharing",
                "user_multi_accounting",
            ],
            str,
        ]
    ]
    """
    List of signals still pending evaluation.
    """
    requested_signals: List[
        Union[
            Literal[
                "fraudulent_website",
                "user_account_sharing",
                "user_multi_accounting",
            ],
            str,
        ]
    ]
    """
    List of signals requested for evaluation.
    """
    _inner_class_types = {
        "account_activity_details": AccountActivityDetails,
        "account_details": AccountDetails,
        "evaluated_signals": EvaluatedSignals,
    }
