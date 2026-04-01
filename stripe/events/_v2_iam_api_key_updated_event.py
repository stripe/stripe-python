# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2IamApiKeyUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.updated"
    type: Literal["v2.iam.api_key.updated"]

    @override
    def fetch_event(self) -> "V2IamApiKeyUpdatedEvent":
        return cast(
            "V2IamApiKeyUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyUpdatedEvent":
        return cast(
            "V2IamApiKeyUpdatedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.updated"
    type: Literal["v2.iam.api_key.updated"]

    class V2IamApiKeyUpdatedEventData(StripeObject):
        api_key: str
        """
        ID of the updated key.
        """

    data: V2IamApiKeyUpdatedEventData
    """
    Data for the v2.iam.api_key.updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamApiKeyUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamApiKeyUpdatedEvent.V2IamApiKeyUpdatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
