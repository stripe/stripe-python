# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe._util import get_api_mode
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._stripe_client import StripeClient
    from stripe.v2.money_management._funding_intent import FundingIntent


class V2MoneyManagementFundingIntentCanceledEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.money_management.funding_intent.canceled"
    type: Literal["v2.money_management.funding_intent.canceled"]
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
    def fetch_event(self) -> "V2MoneyManagementFundingIntentCanceledEvent":
        return cast(
            "V2MoneyManagementFundingIntentCanceledEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "FundingIntent":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "FundingIntent",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2MoneyManagementFundingIntentCanceledEvent":
        return cast(
            "V2MoneyManagementFundingIntentCanceledEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "FundingIntent":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "FundingIntent",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2MoneyManagementFundingIntentCanceledEvent(Event):
    LOOKUP_TYPE = "v2.money_management.funding_intent.canceled"
    type: Literal["v2.money_management.funding_intent.canceled"]

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

    def fetch_related_object(self) -> "FundingIntent":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "FundingIntent",
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
