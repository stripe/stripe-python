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


class V2IamStripeAccessGrantDeniedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.denied"
    type: Literal["v2.iam.stripe_access_grant.denied"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantDeniedEvent":
        return cast(
            "V2IamStripeAccessGrantDeniedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantDeniedEvent":
        return cast(
            "V2IamStripeAccessGrantDeniedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantDeniedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.denied"
    type: Literal["v2.iam.stripe_access_grant.denied"]

    class V2IamStripeAccessGrantDeniedEventData(StripeObject):
        stripe_access_grant: str
        """
        ID of denied Stripe Access Grant.
        """

    data: V2IamStripeAccessGrantDeniedEventData
    """
    Data for the v2.iam.stripe_access_grant.denied event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamStripeAccessGrantDeniedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamStripeAccessGrantDeniedEvent.V2IamStripeAccessGrantDeniedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
