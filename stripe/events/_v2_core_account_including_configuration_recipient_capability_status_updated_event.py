# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from stripe.v2.core._account import Account
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal


class V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent(
    Event,
):
    LOOKUP_TYPE = (
        "v2.core.account[configuration.recipient].capability_status_updated"
    )
    type: Literal[
        "v2.core.account[configuration.recipient].capability_status_updated"
    ]

    class V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventData(
        StripeObject,
    ):
        updated_capability: Literal[
            "bank_accounts.local",
            "bank_accounts.local_uk",
            "bank_accounts.wire",
            "bank_accounts.wire_uk",
            "cards",
            "cards_uk",
            "crypto_wallets_v2",
            "stripe_balance.stripe_transfers",
            "stripe.transfers",
        ]
        """
        Open Enum. The capability which had its status updated.
        """

    data: V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventData
    """
    Data for the v2.core.account[configuration.recipient].capability_status_updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> Account:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            Account,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
