# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class EvaluationOutcome(StripeObject):
    """
    An immutable, point-in-time risk evaluation result that captures recommended controls and
    their expected impact. The type identifies the scenario evaluated and its corresponding details.
    Unavailable optional values are null.
    """

    OBJECT_NAME: ClassVar[Literal["v2.risk.evaluation_outcome"]] = (
        "v2.risk.evaluation_outcome"
    )

    class AccountDetails(StripeObject):
        class Data(StripeObject):
            contact_email: Optional[str]
            """
            Contact email supplied for the evaluation, or null when unavailable.
            """

        account: Optional[str]
        """
        Connected account evaluated.
        """
        customer: Optional[str]
        """
        Customer evaluated.
        """
        data: Optional[Data]
        """
        Inline subject data for an evaluation without a Stripe entity.
        """
        _inner_class_types = {"data": Data}

    class Delinquency(StripeObject):
        class BusinessObjective(StripeObject):
            class BaselineOutcome(StripeObject):
                loss: Amount
                """
                Expected financial loss from delinquency under this reserve configuration, expressed as a negative amount.
                """
                profitability: Amount
                """
                Expected financial result after accounting for revenue and losses. Can be negative.
                """
                revenue: Amount
                """
                Expected revenue under this reserve configuration.
                """

            class ProjectedOutcome(StripeObject):
                loss: Amount
                """
                Expected financial loss from delinquency under this reserve configuration, expressed as a negative amount.
                """
                profitability: Amount
                """
                Expected financial result after accounting for revenue and losses. Can be negative.
                """
                revenue: Amount
                """
                Expected revenue under this reserve configuration.
                """

            baseline_outcome: Optional[BaselineOutcome]
            """
            Expected profitability, revenue, and losses if the current reserve configuration remains unchanged.
            Provides a comparison for projected_outcome. Null when not reliably quantifiable.
            """
            projected_outcome: Optional[ProjectedOutcome]
            """
            Expected profitability, revenue, and losses if the recommended controls are applied. Equals
            baseline_outcome when the recommendation maintains the current state. Null when not reliably quantifiable.
            """
            type: Union[Literal["profitability"], str]
            """
            The financial objective the recommended controls are intended to improve.
            """
            _inner_class_types = {
                "baseline_outcome": BaselineOutcome,
                "projected_outcome": ProjectedOutcome,
            }

        class Control(StripeObject):
            class RiskReserve(StripeObject):
                class Target(StripeObject):
                    percent: int
                    """
                    Integer percentage of funds to reserve.
                    """
                    release_after_days: int
                    """
                    Integer number of days after which reserved funds are released.
                    """
                    release_type: Union[Literal["rolling"], str]
                    """
                    How reserved funds are released.
                    """
                    sweep_available_funds: bool
                    """
                    Whether to reserve already available funds as well as future funds.
                    """

                action: Union[
                    Literal[
                        "clear_reserve",
                        "maintain_current_state",
                        "update_reserve",
                    ],
                    str,
                ]
                """
                Whether to update, maintain, or clear reserves.
                """
                target: Optional[Target]
                """
                Recommended reserve configuration, specifying the percentage of funds to hold, when to release
                them, and whether to include available funds. Populated for update_reserve; null for
                maintain_current_state and clear_reserve.
                """
                _inner_class_types = {"target": Target}

            risk_reserve: Optional[RiskReserve]
            """
            The recommended action for funds held in reserve, including a target configuration when
            updating reserves. Populated when type is risk_reserve; null otherwise.
            """
            type: Union[Literal["risk_reserve"], str]
            """
            The kind of control recommended to manage risk.
            """
            _inner_class_types = {"risk_reserve": RiskReserve}

        class RiskAppetite(StripeObject):
            mode: Union[
                Literal["balanced", "maximize_protection", "maximize_revenue"],
                str,
            ]
            """
            How the recommendation prioritizes protection from losses relative to revenue.
            """

        class SupportingSignals(StripeObject):
            class MerchantDelinquency(StripeObject):
                evaluated_at: str
                """
                Time the signal was evaluated.
                """
                probability: Optional[Decimal]
                """
                Probability of delinquency, represented as a decimal string. Null when the risk level is
                unknown or the account signal does not include a numeric score.
                """
                risk_level: Literal[
                    "elevated", "highest", "low", "normal", "unknown"
                ]
                """
                Assessed risk level.
                """
                signal: str
                """
                ID of the supporting account signal.
                """
                _field_encodings = {"probability": "decimal_string"}

            class PaymentDelinquencyExposure(StripeObject):
                evaluated_at: str
                """
                Time the signal was evaluated.
                """
                exposure_amount: Amount
                """
                Exposure if the account becomes delinquent.
                """
                signal: str
                """
                ID of the supporting account signal.
                """

            merchant_delinquency: Optional[MerchantDelinquency]
            """
            The account's assessed probability and level of delinquency risk. Null when unavailable.
            """
            payment_delinquency_exposure: Optional[PaymentDelinquencyExposure]
            """
            The account's assessed financial exposure if it becomes delinquent. Null when unavailable.
            """
            _inner_class_types = {
                "merchant_delinquency": MerchantDelinquency,
                "payment_delinquency_exposure": PaymentDelinquencyExposure,
            }

        business_objective: BusinessObjective
        """
        The objective of the recommendation, with expected financial outcomes for the recommended
        controls and the current configuration when those outcomes can be quantified.
        """
        controls: List[Control]
        """
        Risk controls recommended to manage the account's delinquency risk.
        """
        risk_appetite: RiskAppetite
        """
        The balance between loss protection and revenue used to generate this recommendation.
        """
        supporting_signals: Optional[SupportingSignals]
        """
        Signals that informed this evaluation, with their values at evaluation time. Null when unavailable.
        """
        _inner_class_types = {
            "business_objective": BusinessObjective,
            "controls": Control,
            "risk_appetite": RiskAppetite,
            "supporting_signals": SupportingSignals,
        }

    account_details: AccountDetails
    """
    Subject of the evaluation. Exactly one of account, customer, or data is provided.
    """
    created: str
    """
    Timestamp when the evaluation was created.
    """
    delinquency: Optional[Delinquency]
    """
    Recommended controls, expected financial impact, and supporting signals for a delinquency
    evaluation. Populated when type is delinquency; null otherwise.
    """
    id: str
    """
    Unique identifier for the evaluation outcome, prefixed with evalout_.
    """
    livemode: bool
    """
    Whether the evaluation outcome is in live mode.
    """
    object: Literal["v2.risk.evaluation_outcome"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    origin: Union[Literal["rule_outcome", "stripe_recommendation"], str]
    """
    How the outcome was generated.
    """
    type: Union[Literal["delinquency"], str]
    """
    Scenario evaluated; determines which type-specific payload is provided.
    """
    _inner_class_types = {
        "account_details": AccountDetails,
        "delinquency": Delinquency,
    }
