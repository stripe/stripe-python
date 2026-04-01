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


class V2IamStripeAccessGrantApprovedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.approved"
    type: Literal["v2.iam.stripe_access_grant.approved"]

    @override
    def fetch_event(self) -> "V2IamStripeAccessGrantApprovedEvent":
        return cast(
            "V2IamStripeAccessGrantApprovedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2IamStripeAccessGrantApprovedEvent":
        return cast(
            "V2IamStripeAccessGrantApprovedEvent",
            await super().fetch_event_async(),
        )


class V2IamStripeAccessGrantApprovedEvent(Event):
    LOOKUP_TYPE = "v2.iam.stripe_access_grant.approved"
    type: Literal["v2.iam.stripe_access_grant.approved"]

    class V2IamStripeAccessGrantApprovedEventData(StripeObject):
        stripe_access_grant: str
        """
        ID of approved Stripe Access Grant.
        """

    data: V2IamStripeAccessGrantApprovedEventData
    """
    Data for the v2.iam.stripe_access_grant.approved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2IamStripeAccessGrantApprovedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2IamStripeAccessGrantApprovedEvent.V2IamStripeAccessGrantApprovedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
