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


class V2IamStripeAccessGrantRequestedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.requested"
    type: Literal["v2.iam.stripe_access_grant.requested"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantRequestedEvent":
        return cast(
            "V2IamStripeAccessGrantRequestedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2IamStripeAccessGrantRequestedEvent":
        return cast(
            "V2IamStripeAccessGrantRequestedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantRequestedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.requested"
    type: Literal["v2.iam.stripe_access_grant.requested"]

    class V2IamStripeAccessGrantRequestedEventData(StripeObject):
        stripe_access_grant: str
        """
        ID of requested Stripe Access Grant.
        """

    data: V2IamStripeAccessGrantRequestedEventData
    """
    Data for the v2.iam.stripe_access_grant.requested event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamStripeAccessGrantRequestedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamStripeAccessGrantRequestedEvent.V2IamStripeAccessGrantRequestedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
