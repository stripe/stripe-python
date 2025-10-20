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
    from stripe.v2.core._account import Account


class V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = (
        "v2.core.account[configuration.storer].capability_status_updated"
    )
    type: Literal[
        "v2.core.account[configuration.storer].capability_status_updated"
    ]
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
    def fetch_event(
        self,
    ) -> (
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent"
    ):
        return cast(
            "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "Account":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "Account",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> (
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent"
    ):
        return cast(
            "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "Account":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "Account",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent(
    Event,
):
    LOOKUP_TYPE = (
        "v2.core.account[configuration.storer].capability_status_updated"
    )
    type: Literal[
        "v2.core.account[configuration.storer].capability_status_updated"
    ]

    class V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventData(
        StripeObject,
    ):
        updated_capability: Literal[
            "financial_addressses.bank_accounts",
            "financial_addressses.crypto_wallets",
            "holds_currencies.eur",
            "holds_currencies.gbp",
            "holds_currencies.usd",
            "holds_currencies.usdc",
            "inbound_transfers.bank_accounts",
            "outbound_payments.bank_accounts",
            "outbound_payments.cards",
            "outbound_payments.crypto_wallets",
            "outbound_payments.financial_accounts",
            "outbound_transfers.bank_accounts",
            "outbound_transfers.crypto_wallets",
            "outbound_transfers.financial_accounts",
        ]
        """
        Open Enum. The capability which had its status updated.
        """

    data: V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventData
    """
    Data for the v2.core.account[configuration.storer].capability_status_updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> (
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent"
    ):
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventData._construct_from(
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

    def fetch_related_object(self) -> "Account":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "Account",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_context": self.context},
            ),
        )
