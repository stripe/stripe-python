# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import get_api_mode
from stripe.v2._amount import Amount
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_client import StripeClient
    from stripe.v2.money_management._reward_program import RewardProgram


class V2MoneyManagementRewardProgramRewardEarnedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.money_management.reward_program.reward_earned"
    type: Literal["v2.money_management.reward_program.reward_earned"]
    related_object: RelatedObject

    def __init__(
        self, parsed_body: Dict[str, Any], client: "StripeClient"
    ) -> None:
        super().__init__(
            parsed_body,
            client,
        )
        self.related_object = RelatedObject(parsed_body["related_object"])

    @override
    def fetch_event(self) -> "V2MoneyManagementRewardProgramRewardEarnedEvent":
        return cast(
            "V2MoneyManagementRewardProgramRewardEarnedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "RewardProgram":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "RewardProgram",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2MoneyManagementRewardProgramRewardEarnedEvent":
        return cast(
            "V2MoneyManagementRewardProgramRewardEarnedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "RewardProgram":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "RewardProgram",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2MoneyManagementRewardProgramRewardEarnedEvent(Event):
    LOOKUP_TYPE = "v2.money_management.reward_program.reward_earned"
    type: Literal["v2.money_management.reward_program.reward_earned"]

    class V2MoneyManagementRewardProgramRewardEarnedEventData(StripeObject):
        class CardSpend(StripeObject):
            cardholder: Optional[str]
            """
            The Issuing cardholder whose spend earned the reward.
            """
            issuing_transaction: Optional[str]
            """
            The Issuing transaction that earned the reward. Present when the reward is calculated from a
            single Issuing transaction.
            """

        class Reward(StripeObject):
            class EarningPeriod(StripeObject):
                end: str
                """
                End of the earning period, exclusive.
                """
                start: str
                """
                Start of the earning period, inclusive.
                """

            amount: Amount
            """
            The reward amount. Always positive; the event type determines whether to credit or debit the
            connected account.
            """
            earning_period: Optional[EarningPeriod]
            """
            The period over which the reward was earned. Present when the reward is calculated over an
            earning period rather than from a single Issuing transaction.
            """
            _inner_class_types = {"earning_period": EarningPeriod}

        account: str
        """
        The connected account that earned the reward.
        """
        card_spend: Optional[CardSpend]
        """
        Issuing card spend details for the reward.
        """
        reward: Reward
        """
        The reward to credit to the connected account.
        """
        _inner_class_types = {"card_spend": CardSpend, "reward": Reward}

    data: V2MoneyManagementRewardProgramRewardEarnedEventData
    """
    Data for the v2.money_management.reward_program.reward_earned event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2MoneyManagementRewardProgramRewardEarnedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2MoneyManagementRewardProgramRewardEarnedEvent.V2MoneyManagementRewardProgramRewardEarnedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> "RewardProgram":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "RewardProgram",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={
                    "stripe_context": self.context,
                    "headers": {"Stripe-Request-Trigger": f"event={self.id}"},
                },
            ),
        )
