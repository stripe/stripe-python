# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class AccountSignals(StripeObject):
    """
    The Account Signals API provides risk related signals that can be used to better manage risks.
    """

    OBJECT_NAME: ClassVar[Literal["account_signals"]] = "account_signals"

    class Delinquency(StripeObject):
        class Indicator(StripeObject):
            description: str
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
                "dispute_window",
                "disputes",
                "duplicates",
                "exposure",
                "firmographic",
                "lifetime_metrics",
                "payment_processing",
                "payment_volume",
                "payouts",
                "refunds",
                "tenure",
                "transfers",
            ]
            """
            The name of the specific indicator used in the risk assessment.
            """

        evaluated_at: Optional[int]
        """
        Time at which the signal was evaluated, measured in seconds since the Unix epoch.
        """
        indicators: Optional[List[Indicator]]
        """
        Array of objects representing individual factors that contributed to the calculated probability of delinquency.
        """
        probability: Optional[float]
        """
        The probability of delinquency. Can be between 0.00 and 100.00
        """
        risk_level: Literal[
            "elevated", "highest", "low", "normal", "not_assessed", "unknown"
        ]
        """
        Categorical assessment of the delinquency risk based on probability.
        """
        signal_id: Optional[str]
        """
        Unique identifier for the delinquency signal.
        """
        _inner_class_types = {"indicators": Indicator}

    account: str
    """
    The account for which the signals belong to.
    """
    delinquency: Optional[Delinquency]
    """
    The delinquency signal of the account.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["account_signals"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    _inner_class_types = {"delinquency": Delinquency}
