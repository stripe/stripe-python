# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import get_api_mode
from stripe.v2.core._event import Event, EventNotification, RelatedObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_client import StripeClient
    from stripe.v2.payments._off_session_payment import OffSessionPayment


class V2PaymentsOffSessionPaymentFailedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.payments.off_session_payment.failed"
    type: Literal["v2.payments.off_session_payment.failed"]
    related_object: RelatedObject

    def __init__(
        self, parsed_body: Dict[str, Any], client: "StripeClient"
    ) -> None:
        super().__init__(
            parsed_body,
            client,
        )
        self.related_object = RelatedObject(parsed_body["related_object"])

    @override
    def fetch_event(self) -> "V2PaymentsOffSessionPaymentFailedEvent":
        return cast(
            "V2PaymentsOffSessionPaymentFailedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "OffSessionPayment":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "OffSessionPayment",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2PaymentsOffSessionPaymentFailedEvent":
        return cast(
            "V2PaymentsOffSessionPaymentFailedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "OffSessionPayment":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            headers={"Stripe-Request-Trigger": f"event={self.id}"},
            usage=["fetch_related_object"],
        )
        return cast(
            "OffSessionPayment",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2PaymentsOffSessionPaymentFailedEvent(Event):
    LOOKUP_TYPE = "v2.payments.off_session_payment.failed"
    type: Literal["v2.payments.off_session_payment.failed"]

    class V2PaymentsOffSessionPaymentFailedEventData(StripeObject):
        payment_attempt_record: str
        """
        The ID of the payment attempt record associated with this terminal failure. Equal to the `latest_payment_attempt_record` on the Off-Session Payment object.
        """

    data: V2PaymentsOffSessionPaymentFailedEventData
    """
    Data for the v2.payments.off_session_payment.failed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2PaymentsOffSessionPaymentFailedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2PaymentsOffSessionPaymentFailedEvent.V2PaymentsOffSessionPaymentFailedEventData._construct_from(
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

    def fetch_related_object(self) -> "OffSessionPayment":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "OffSessionPayment",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={
                    "stripe_context": self.context,
                    "headers": {"Stripe-Request-Trigger": f"event={self.id}"},
                },
            ),
        )
