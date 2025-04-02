# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, List, Optional
from typing_extensions import Literal


class V2CoreAccountLinkCompletedEvent(Event):
    LOOKUP_TYPE = "v2.core.account_link.completed"
    type: Literal["v2.core.account_link.completed"]

    class V2CoreAccountLinkCompletedEventData(StripeObject):
        account_id: str
        """
        The ID of the v2 account.
        """
        configurations: List[Literal["recipient"]]
        """
        Configurations on the Account that was onboarded via the account link.
        """
        use_case: Literal["account_onboarding", "account_update"]
        """
        Open Enum. The use case type of the account link that has been completed.
        """

    data: V2CoreAccountLinkCompletedEventData
    """
    Data for the v2.core.account_link.completed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreAccountLinkCompletedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountLinkCompletedEvent.V2CoreAccountLinkCompletedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
