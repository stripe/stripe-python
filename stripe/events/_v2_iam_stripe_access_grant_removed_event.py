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


class V2IamStripeAccessGrantRemovedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.removed"
    type: Literal["v2.iam.stripe_access_grant.removed"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantRemovedEvent":
        return cast(
            "V2IamStripeAccessGrantRemovedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantRemovedEvent":
        return cast(
            "V2IamStripeAccessGrantRemovedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantRemovedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.removed"
    type: Literal["v2.iam.stripe_access_grant.removed"]

    class V2IamStripeAccessGrantRemovedEventData(StripeObject):
        stripe_access_grant: str
        """
        ID of removed Stripe Access Grant.
        """

    data: V2IamStripeAccessGrantRemovedEventData
    """
    Data for the v2.iam.stripe_access_grant.removed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamStripeAccessGrantRemovedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamStripeAccessGrantRemovedEvent.V2IamStripeAccessGrantRemovedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
