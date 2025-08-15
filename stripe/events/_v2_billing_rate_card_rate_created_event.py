# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from stripe.v2.billing._rate_card_rate import RateCardRate
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal


class V2BillingRateCardRateCreatedEvent(Event):
    LOOKUP_TYPE = "v2.billing.rate_card_rate.created"
    type: Literal["v2.billing.rate_card_rate.created"]

    class V2BillingRateCardRateCreatedEventData(StripeObject):
        billable_item: str
        """
        The ID of the BillableItem which this Rate is associated with.
        """
        created: str
        """
        Timestamp of when the object was created.
        """
        rate_card: str
        """
        The ID of the RateCard which this Rate belongs to.
        """
        rate_card_version: str
        """
        The ID of the latest RateCard Version when the Rate was created.
        """

    data: V2BillingRateCardRateCreatedEventData
    """
    Data for the v2.billing.rate_card_rate.created event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2BillingRateCardRateCreatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2BillingRateCardRateCreatedEvent.V2BillingRateCardRateCreatedEventData._construct_from(
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

    def fetch_related_object(self) -> RateCardRate:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            RateCardRate,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
