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


class V2IamStripeAccessGrantCanceledEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.canceled"
    type: Literal["v2.iam.stripe_access_grant.canceled"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantCanceledEvent":
        return cast(
            "V2IamStripeAccessGrantCanceledEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantCanceledEvent":
        return cast(
            "V2IamStripeAccessGrantCanceledEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantCanceledEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.canceled"
    type: Literal["v2.iam.stripe_access_grant.canceled"]

    class V2IamStripeAccessGrantCanceledEventData(StripeObject):
        stripe_access_grant: str
        """
        ID of canceled Stripe Access Grant.
        """

    data: V2IamStripeAccessGrantCanceledEventData
    """
    Data for the v2.iam.stripe_access_grant.canceled event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamStripeAccessGrantCanceledEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamStripeAccessGrantCanceledEvent.V2IamStripeAccessGrantCanceledEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
