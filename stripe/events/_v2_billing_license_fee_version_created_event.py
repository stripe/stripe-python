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
    from stripe.v2.billing._license_fee_version import LicenseFeeVersion


class V2BillingLicenseFeeVersionCreatedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.billing.license_fee_version.created"
    type: Literal["v2.billing.license_fee_version.created"]
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
    def fetch_event(self) -> "V2BillingLicenseFeeVersionCreatedEvent":
        return cast(
            "V2BillingLicenseFeeVersionCreatedEvent",
            super().fetch_event(),
        )

    def fetch_related_object(self) -> "LicenseFeeVersion":
        response = self._client.raw_request(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "LicenseFeeVersion",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2BillingLicenseFeeVersionCreatedEvent":
        return cast(
            "V2BillingLicenseFeeVersionCreatedEvent",
            await super().fetch_event_async(),
        )

    async def fetch_related_object_async(self) -> "LicenseFeeVersion":
        response = await self._client.raw_request_async(
            "get",
            self.related_object.url,
            stripe_context=self.context,
            usage=["fetch_related_object"],
        )
        return cast(
            "LicenseFeeVersion",
            self._client.deserialize(
                response,
                api_mode=get_api_mode(self.related_object.url),
            ),
        )


class V2BillingLicenseFeeVersionCreatedEvent(Event):
    LOOKUP_TYPE = "v2.billing.license_fee_version.created"
    type: Literal["v2.billing.license_fee_version.created"]

    class V2BillingLicenseFeeVersionCreatedEventData(StripeObject):
        license_fee_id: str
        """
        The ID of the LicenseFee that the LicenseFeeVersion belongs to.
        """

    data: V2BillingLicenseFeeVersionCreatedEventData
    """
    Data for the v2.billing.license_fee_version.created event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2BillingLicenseFeeVersionCreatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2BillingLicenseFeeVersionCreatedEvent.V2BillingLicenseFeeVersionCreatedEventData._construct_from(
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

    def fetch_related_object(self) -> "LicenseFeeVersion":
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            "LicenseFeeVersion",
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_context": self.context},
            ),
        )
