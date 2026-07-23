# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class AccountSignal(StripeObject):
    """
    An automatically evaluated signal on an account. Each Account Signal object corresponds to
    exactly one signal type, indicated by type. Only the type-specific field is populated; other
    type-specific payload fields are null. If an account has multiple signals, Stripe creates
    separate account signal objects.
    """

    OBJECT_NAME: ClassVar[Literal["v2.signals.account_signal"]] = (
        "v2.signals.account_signal"
    )

    class AccountDetails(StripeObject):
        account: Optional[str]
        """
        The v2 account ID of the account.
        """
        customer: Optional[str]
        """
        The v1 customer ID of the account, for users not yet migrated to v2/accounts.
        """

    class FraudulentMerchant(StripeObject):
        class Indicator(StripeObject):
            explanation: str
            """
            A brief explanation of how this indicator contributed to the fraudulent merchant probability.
            """
            impact: Literal[
                "decrease", "neutral", "slight_increase", "strong_increase"
            ]
            """
            The effect this indicator had on the overall risk level.
            """
            indicator: Literal[
                "bank_account",
                "business_information_and_account_activity",
                "disputes",
                "failures",
                "geolocation",
                "other",
                "other_related_accounts",
                "other_transaction_activity",
                "owner_email",
            ]
            """
            The name of the specific indicator used in the risk assessment.
            """

        indicators: List[Indicator]
        """
        Array of objects representing individual factors that contributed to the calculated probability. Absent when risk level is not_assessed or unknown,
        or when the user is not on a product tier that includes indicators.
        """
        probability: Optional[Decimal]
        """
        The probability of the merchant being fraudulent. Can be between 0.00 and 100.00. Absent when risk level is not_assessed or unknown,
        or when the user is not on a product tier that includes numeric scores.
        """
        risk_level: Literal[
            "elevated", "highest", "low", "normal", "not_assessed", "unknown"
        ]
        """
        Categorical assessment of the fraudulent merchant risk based on probability.
        """
        _inner_class_types = {"indicators": Indicator}
        _field_encodings = {"probability": "decimal_string"}

    class MerchantDelinquency(StripeObject):
        class Indicator(StripeObject):
            explanation: str
            """
            A brief explanation of how this indicator contributed to the delinquency probability.
            """
            impact: Literal[
                "decrease", "neutral", "slight_increase", "strong_increase"
            ]
            """
            The effect this indicator had on the overall risk level.
            """
            indicator: Literal[
                "account_balance",
                "aov",
                "charge_concentration",
                "disputes",
                "dispute_window",
                "exposure",
                "firmographic",
                "lifetime_metrics",
                "other",
                "payment_processing",
                "payment_volume",
                "payouts",
                "refunds",
                "related_accounts",
                "tenure",
                "transfers",
            ]
            """
            The name of the specific indicator used in the risk assessment.
            """

        indicators: List[Indicator]
        """
        Array of objects representing individual factors that contributed to the calculated probability of delinquency. Absent when risk level is not_assessed or unknown,
        or when the user is not on a product tier that includes indicators.
        """
        probability: Optional[Decimal]
        """
        The probability of delinquency. Can be between 0.00 and 100.00. Absent when risk level is not_assessed or unknown,
        or when the user is not on a product tier that includes numeric scores.
        """
        risk_level: Literal[
            "elevated", "highest", "low", "normal", "not_assessed", "unknown"
        ]
        """
        Categorical assessment of the delinquency risk based on probability.
        """
        _inner_class_types = {"indicators": Indicator}
        _field_encodings = {"probability": "decimal_string"}

    account_details: Optional[AccountDetails]
    """
    The account or customer this signal is associated with.
    """
    created: str
    """
    Timestamp at which the signal was created.
    """
    fraudulent_merchant: Optional[FraudulentMerchant]
    """
    Data for the fraudulent merchant signal. Present only when type is fraudulent_merchant.
    """
    id: str
    """
    Unique identifier for the account signal.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    merchant_delinquency: Optional[MerchantDelinquency]
    """
    Data for the merchant delinquency signal. Present only when type is merchant_delinquency.
    """
    object: Literal["v2.signals.account_signal"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    type: Union[
        Literal[
            "fraudulent_merchant",
            "merchant_delinquency",
            "payment_delinquency_exposure",
        ],
        str,
    ]
    """
    The type of signal.
    """
    _inner_class_types = {
        "account_details": AccountDetails,
        "fraudulent_merchant": FraudulentMerchant,
        "merchant_delinquency": MerchantDelinquency,
    }
