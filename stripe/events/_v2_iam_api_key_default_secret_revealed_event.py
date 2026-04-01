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


class V2IamApiKeyDefaultSecretRevealedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.api_key.default_secret_revealed"
    type: Literal["v2.iam.api_key.default_secret_revealed"]

    @override
    def fetch_event(self) -> "V2IamApiKeyDefaultSecretRevealedEvent":
        return cast(
            "V2IamApiKeyDefaultSecretRevealedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2IamApiKeyDefaultSecretRevealedEvent":
        return cast(
            "V2IamApiKeyDefaultSecretRevealedEvent",
            await super().fetch_event_async(),
        )


class V2IamApiKeyDefaultSecretRevealedEvent(Event):
    LOOKUP_TYPE = "v2.iam.api_key.default_secret_revealed"
    type: Literal["v2.iam.api_key.default_secret_revealed"]

    class V2IamApiKeyDefaultSecretRevealedEventData(StripeObject):
        api_key: str
        """
        ID of the default key whose secret was revealed.
        """

    data: V2IamApiKeyDefaultSecretRevealedEventData
    """
    Data for the v2.iam.api_key.default_secret_revealed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamApiKeyDefaultSecretRevealedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamApiKeyDefaultSecretRevealedEvent.V2IamApiKeyDefaultSecretRevealedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
