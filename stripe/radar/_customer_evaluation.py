# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.radar._customer_evaluation_create_params import (
        CustomerEvaluationCreateParams,
    )


class CustomerEvaluation(CreateableAPIResource["CustomerEvaluation"]):
    """
    Customer Evaluation resource returned by the Radar Customer Evaluations API.
    """

    OBJECT_NAME: ClassVar[Literal["radar.customer_evaluation"]] = (
        "radar.customer_evaluation"
    )

    class Signals(StripeObject):
        class AccountSharing(StripeObject):
            evaluated_at: int
            """
            Time at which the signal was evaluated. Measured in seconds since the Unix epoch.
            """
            risk_level: Optional[str]
            """
            The risk level for this signal.
            """
            score: float
            """
            Score for this signal (float between 0.0-100.0).
            """

        class MultiAccounting(StripeObject):
            evaluated_at: int
            """
            Time at which the signal was evaluated. Measured in seconds since the Unix epoch.
            """
            risk_level: Optional[str]
            """
            The risk level for this signal.
            """
            score: float
            """
            Score for this signal (float between 0.0-100.0).
            """

        account_sharing: Optional[AccountSharing]
        multi_accounting: Optional[MultiAccounting]
        _inner_class_types = {
            "account_sharing": AccountSharing,
            "multi_accounting": MultiAccounting,
        }

    created_at: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[str]
    """
    The ID of the Stripe customer the customer evaluation is associated with.
    """
    event_type: str
    """
    The type of evaluation event.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["radar.customer_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    signals: Optional[Signals]
    """
    A hash of signal objects providing Radar's evaluation for the lifecycle event.
    """

    @classmethod
    def create(
        cls, **params: Unpack["CustomerEvaluationCreateParams"]
    ) -> "CustomerEvaluation":
        """
        Creates a new CustomerEvaluation object.
        """
        return cast(
            "CustomerEvaluation",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["CustomerEvaluationCreateParams"]
    ) -> "CustomerEvaluation":
        """
        Creates a new CustomerEvaluation object.
        """
        return cast(
            "CustomerEvaluation",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"signals": Signals}
