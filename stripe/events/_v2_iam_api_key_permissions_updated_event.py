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


class V2IamApiKeyPermissionsUpdatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.permissions_updated"
    type: Literal["v2.iam.api_key.permissions_updated"]

    @override
    def fetch_event(self) -> "V2IamApiKeyPermissionsUpdatedEvent":
        return cast(
            "V2IamApiKeyPermissionsUpdatedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamApiKeyPermissionsUpdatedEvent":
        return cast(
            "V2IamApiKeyPermissionsUpdatedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyPermissionsUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.permissions_updated"
    type: Literal["v2.iam.api_key.permissions_updated"]

    class V2IamApiKeyPermissionsUpdatedEventData(StripeObject):
        api_key: str
        """
        ID of the key whose permissions were updated.
        """

    data: V2IamApiKeyPermissionsUpdatedEventData
    """
    Data for the v2.iam.api_key.permissions_updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamApiKeyPermissionsUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamApiKeyPermissionsUpdatedEvent.V2IamApiKeyPermissionsUpdatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
