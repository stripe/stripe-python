# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import get_api_mode
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_client import StripeClient
    from stripe.v2.money_management._inbound_transfer import InboundTransfer


class V2MoneyManagementInboundTransferAvailableEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.money_management.inbound_transfer.available"
    type: Literal["v2.money_management.inbound_transfer.available"]
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
    def fetch_event(self) -> "V2MoneyManagementInboundTransferAvailableEvent":
        return cast(
            "V2MoneyManagementInboundTransferAvailableEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "InboundTransfer":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "InboundTransfer",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2MoneyManagementInboundTransferAvailableEvent":
        return cast(
            "V2MoneyManagementInboundTransferAvailableEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "InboundTransfer":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "InboundTransfer",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2MoneyManagementInboundTransferAvailableEvent(Event):
    LOOKUP_TYPE = "v2.money_management.inbound_transfer.available"
    type: Literal["v2.money_management.inbound_transfer.available"]

    class V2MoneyManagementInboundTransferAvailableEventData(StripeObject):
        transaction_id: str
        """
        The transaction ID of the received credit.
        """

    data: V2MoneyManagementInboundTransferAvailableEventData
    """
    Data for the v2.money_management.inbound_transfer.available event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2MoneyManagementInboundTransferAvailableEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2MoneyManagementInboundTransferAvailableEvent.V2MoneyManagementInboundTransferAvailableEventData._construct_from(
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

    def fetch_related_object(self) -> "InboundTransfer":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "InboundTransfer",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_context": self.context},
            ),
        )
