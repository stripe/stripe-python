# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from stripe.v2.money_management._received_credit import ReceivedCredit
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal


class V2MoneyManagementReceivedCreditAvailableEvent(Event):
    LOOKUP_TYPE = "v2.money_management.received_credit.available"
    type: Literal["v2.money_management.received_credit.available"]

    class V2MoneyManagementReceivedCreditAvailableEventData(StripeObject):
        transaction_id: str
        """
        The transaction ID of the received credit.
        """

    data: V2MoneyManagementReceivedCreditAvailableEventData
    """
    Data for the v2.money_management.received_credit.available event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2MoneyManagementReceivedCreditAvailableEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2MoneyManagementReceivedCreditAvailableEvent.V2MoneyManagementReceivedCreditAvailableEventData._construct_from(
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

    def fetch_related_object(self) -> ReceivedCredit:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            ReceivedCredit,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
