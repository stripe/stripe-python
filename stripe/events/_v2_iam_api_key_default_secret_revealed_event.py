# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2.core._event import Event, EventNotification
from typing import cast
from typing_extensions import Literal, override


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
