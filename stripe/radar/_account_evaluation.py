# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.radar._account_evaluation_create_params import (
        AccountEvaluationCreateParams,
    )
    from stripe.params.radar._account_evaluation_modify_params import (
        AccountEvaluationModifyParams,
    )
    from stripe.params.radar._account_evaluation_retrieve_params import (
        AccountEvaluationRetrieveParams,
    )


class AccountEvaluation(
    CreateableAPIResource["AccountEvaluation"],
    UpdateableAPIResource["AccountEvaluation"],
):
    """
    Account Evaluation resource returned by the Radar Account Evaluations API.
    """

    OBJECT_NAME: ClassVar[Literal["radar.account_evaluation"]] = (
        "radar.account_evaluation"
    )

    class Event(StripeObject):
        occurred_at: int
        """
        Time at which the event occurred. Measured in seconds since the Unix epoch.
        """
        type: str
        """
        The type of event that occurred.
        """

    class Signals(StripeObject):
        class AccountSharing(StripeObject):
            score: float
            """
            Score for this signal (float between 0.0-100.0).
            """

        class MultiAccounting(StripeObject):
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
    customer: str
    """
    The ID of the Stripe customer the account evaluation is associated with.
    """
    events: Optional[List[Event]]
    """
    The list of events that were reported for this Account Evaluation object via the report API.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["radar.account_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    signals: Optional[Signals]
    """
    A hash of signal objects providing Radar's evaluation for the lifecycle event.
    """
    type: str
    """
    The type of evaluation returned, based on the user's request.
    """

    @classmethod
    def create(
        cls, **params: Unpack["AccountEvaluationCreateParams"]
    ) -> "AccountEvaluation":
        """
        Creates a new AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["AccountEvaluationCreateParams"]
    ) -> "AccountEvaluation":
        """
        Creates a new AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["AccountEvaluationModifyParams"]
    ) -> "AccountEvaluation":
        """
        Reports an event on an AccountEvaluation object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "AccountEvaluation",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["AccountEvaluationModifyParams"]
    ) -> "AccountEvaluation":
        """
        Reports an event on an AccountEvaluation object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "AccountEvaluation",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["AccountEvaluationRetrieveParams"]
    ) -> "AccountEvaluation":
        """
        Retrieves an AccountEvaluation object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["AccountEvaluationRetrieveParams"]
    ) -> "AccountEvaluation":
        """
        Retrieves an AccountEvaluation object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"events": Event, "signals": Signals}
